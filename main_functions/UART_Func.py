'''
UART界面函数
    Chart_UART      : UART波形图    QWidgt
    com_Baud    : 波特率选择框  QComboBox
    com_Check_bit   : 校验位选择框  QComboBox
    com_Stop_bit   : 停止位选择框  QComboBox
    btn_UART_ctrl   : 开启串口      QPushButton
    btn_UART_auto   : 自动调整图表      QPushButton
    btn_UART_LED    : 状态控制      QPushButton

    cb_Rec_HEX      : 十六进制显示    QCheckBox
    btn_Rec_Clear   : 清空接收区      QPushButton
    te_UART_RecTerminal: 接收区      QTextEdit

    cb_Send_HEX     : 十六进制发送    QCheckBox
    btn_UART_Send   : 发送按钮       QPushButton
    te_UART_SendTerminal: 发送区      QTextEdit
'''
import binascii

from PySide6 import QtCore
from PySide6 import QtWidgets, QtCore, QtCharts, QtGui
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis, QSplineSeries
from PySide6.QtCore import QTimer, Qt,QObject,QPoint
from PySide6.QtGui import QPainter, QColor
import sys
import random


class UART_Manager(QtWidgets.QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.init_chart()
        self.ui.com_Baud.setCurrentIndex(6)
        self.buffer = ''
        self.buffer_str = ''
        self.cb_Send_HEX_Flag = False
        self.cb_Rec_HEX_Flag = False

    def init_chart(self):
        # 创建曲线对象
        self.seriesData1 = QtCharts.QLineSeries()
        self.seriesData2 = QtCharts.QLineSeries()
        self.seriesData3 = QtCharts.QLineSeries()
        self.seriesData4 = QtCharts.QLineSeries()

        # 创建图表和视图
        self.chart = QtCharts.QChart()
        self.chartView = QtCharts.QChartView(self.chart)
        self.chartView.setRenderHint(QtGui.QPainter.Antialiasing)   # 抗锯齿

        # 设置图表属性
        self.chart.legend().setVisible(False)
        self.chart.setBackgroundRoundness(0)
        self.chartView.setContentsMargins(0, 0, 0, 0)
        self.chart.setBackgroundVisible(False)


        # 设置坐标轴
        self.axisX = QtCharts.QValueAxis()
        self.axisY = QtCharts.QValueAxis()
        self.chart.addAxis(self.axisX, QtCore.Qt.AlignBottom)
        self.chart.addAxis(self.axisY, QtCore.Qt.AlignLeft)

        # X坐标轴设置
        self.axisX.setRange(0, 100)
        self.axisX.setLabelFormat("%g") # 设置刻度的格式
        self.axisX.setLabelsColor(QColor(177,177,177)); # 设置刻度的颜色
        self.axisX.setGridLineVisible(False)# 隐藏X轴网格线
        self.axisX.setTickCount(11)

        # Y坐标轴设置
        self.axisY.setRange(0, 200)
        self.axisY.setLabelFormat("%g")
        self.axisY.setLabelsColor(QColor(177,177,177))
        self.axisY.setGridLineVisible(False)
        self.axisY.setTickCount(11)

        # 添加曲线到图表
        self.chart.addSeries(self.seriesData1)
        self.chart.addSeries(self.seriesData2)
        self.chart.addSeries(self.seriesData3)
        self.chart.addSeries(self.seriesData4)

        # 绑定曲线到坐标轴
        self.seriesData1.attachAxis(self.axisX)
        self.seriesData1.attachAxis(self.axisY)
        self.seriesData2.attachAxis(self.axisX)
        self.seriesData2.attachAxis(self.axisY)
        self.seriesData3.attachAxis(self.axisX)
        self.seriesData3.attachAxis(self.axisY)
        self.seriesData4.attachAxis(self.axisX)
        self.seriesData4.attachAxis(self.axisY)

        # 设置曲线颜色
        self.seriesData1.setColor(QtGui.QColor(98, 222, 113))
        self.seriesData2.setColor(QtGui.QColor(233, 78, 112))
        self.seriesData3.setColor(QtGui.QColor(65, 140, 248))
        self.seriesData4.setColor(QtGui.QColor(162, 107, 234))

        self.ui.Chart_UART.setChart(self.chart)

    '''
    UART界面指令发送
    '''
    def UART_send(Baudrate, Check_bit, Stop_bit,server):
        senddata = []
        senddata.append(0x68)
        senddata.append(Baudrate & 0xff)
        senddata.append(Check_bit & 0xff)
        senddata.append(Stop_bit & 0xff)
        try:
            server.send_message_to_client_long(senddata)
        except Exception as e:
            print(e)

    '''
    UART波形数据更新
    '''
    def UART_seriesUpdate(self,data1,data2,data3,data4):
        xdata = self.seriesData1.pointsVector()[-1].x() + 1 if self.seriesData1.pointsVector() else 0

        # 向曲线添加新的数据点
        self.seriesData1.append(xdata, data1)
        self.seriesData2.append(xdata, data2)
        self.seriesData3.append(xdata, data3)
        self.seriesData4.append(xdata, data4)

        # 如果曲线上的点数超过一定数量，移除最早的点
        if self.seriesData1.count() > 100:
            self.seriesData1.remove(0)
            self.seriesData2.remove(0)
            self.seriesData3.remove(0)
            self.seriesData4.remove(0)

            # 后一个点前移
            for i in range(0, self.seriesData1.count()):
                self.seriesData1.replace(i, self.seriesData1.at(i).x() - 1, self.seriesData1.at(i).y())
                self.seriesData2.replace(i, self.seriesData2.at(i).x() - 1, self.seriesData2.at(i).y())
                self.seriesData3.replace(i, self.seriesData3.at(i).x() - 1, self.seriesData3.at(i).y())
                self.seriesData4.replace(i, self.seriesData4.at(i).x() - 1, self.seriesData4.at(i).y())

    #显示接收到的消息
    def UART_recRecTerminal(self,message):
        # message为bytearray类型，需要转为字符串
        message = message.decode('utf-8')
        #不换行追加
        # self.ui.te_UART_RecTerminal.insertPlainText(message)
        if self.cb_Rec_HEX_Flag:    #以HEX追加
            self.ui.te_UART_RecTerminal.insertPlainText(binascii.b2a_hex(message).decode('utf-8'))
        else:   #以字符串追加
            self.ui.te_UART_RecTerminal.insertPlainText(message)


    ############################################################################################################
    # UART 按钮事件
    ############################################################################################################
    def UART_ctrl(self,server):
        if self.ui.btn_UART_ctrl.text() == "Close COM":
            self.ui.btn_UART_ctrl.setText("Open COM")
            self.ui.btn_UART_LED.setStyleSheet("border-radius: 15px;background-color: rgb(220, 0, 0);border-color: rgb(173, 0, 0);")
            self.ui.com_Baud.setEnabled(True)
            self.ui.com_Check_bit.setEnabled(True)
            self.ui.com_Stop_bit.setEnabled(True)
            self.ui.btn_UART_Send.setEnabled(False)
        else:
            # 得到序列号
            Baudrate = self.ui.com_Baud.currentIndex()
            Check_bit = self.ui.com_Check_bit.currentIndex()
            Stop_bit = self.ui.com_Stop_bit.currentIndex()
            print(Baudrate,Check_bit,Stop_bit)
            UART_Manager.UART_send(Baudrate,Check_bit,Stop_bit,server)
            #将按钮文字改为Close COM
            self.ui.btn_UART_ctrl.setText("Close COM")
            #将按钮颜色改为绿色
            self.ui.btn_UART_LED.setStyleSheet("border-radius: 15px;background-color: rgb(0, 255, 0);border-color: rgb(0, 170, 127);")
            #失能comboBox
            self.ui.com_Baud.setEnabled(False)
            self.ui.com_Check_bit.setEnabled(False)
            self.ui.com_Stop_bit.setEnabled(False)
            #使能发送按钮
            self.ui.btn_UART_Send.setEnabled(True)

    def UART_auto(self):
        #自动调节chart到合适的y轴范围
        # 遍历所有的曲线寻找最大值和最小值
        min = 1000
        max = 0
        for i in range(0, self.seriesData1.count()):
            if self.seriesData1.at(i).y() > max:
                max = self.seriesData1.at(i).y()
            if self.seriesData1.at(i).y() < min:
                min = self.seriesData1.at(i).y()
        for i in range(0, self.seriesData2.count()):
            if self.seriesData2.at(i).y() > max:
                max = self.seriesData2.at(i).y()
            if self.seriesData2.at(i).y() < min:
                min = self.seriesData2.at(i).y()
        for i in range(0, self.seriesData3.count()):
            if self.seriesData3.at(i).y() > max:
                max = self.seriesData3.at(i).y()
            if self.seriesData3.at(i).y() < min:
                min = self.seriesData3.at(i).y()
        for i in range(0, self.seriesData4.count()):
            if self.seriesData4.at(i).y() > max:
                max = self.seriesData4.at(i).y()
            if self.seriesData4.at(i).y() < min:
                min = self.seriesData4.at(i).y()
        print(min,max)
        # 设置y轴范围
        self.axisY.setRange(min-abs(min) * 1, max + abs(max) * 0.2)

    def Rec_Clear(self):
        self.ui.te_UART_RecTerminal.clear()

    # cb_Send_HEX绑定事件
    def Rec_HEX(self):
        if self.ui.cb_Rec_HEX.isChecked():  #HEX显示
            data = self.ui.te_UART_RecTerminal.toPlainText()
            #将str转化为HEX，以空格分隔
            data = [hex(ord(i)) for i in data]
            data = " ".join(data)
            self.ui.te_UART_RecTerminal.setText(data)
            self.cb_Rec_HEX_Flag = True
        else:
            data = self.ui.te_UART_RecTerminal.toPlainText()
            data = data.split(" ")
            data = [int(i,16) for i in data]
            data = bytearray(data)
            data = data.decode('utf-8')
            self.ui.te_UART_RecTerminal.setText(data)
            self.cb_Rec_HEX_Flag = False

    # cb_Send_HEX绑定事件
    def Send_HEX(self):
        if self.ui.cb_Send_HEX.isChecked():
            data = self.ui.te_UART_SendTerminal.toPlainText()
            #将str转化为HEX，以空格分隔
            data = [hex(ord(i)) for i in data]
            data = " ".join(data)
            self.ui.te_UART_SendTerminal.setText(data)
            self.cb_Send_HEX_Flag = True
        else:
            data = self.ui.te_UART_SendTerminal.toPlainText()
            data = data.split(" ")
            data = [int(i,16) for i in data]
            data = bytearray(data)
            data = data.decode('utf-8')
            self.ui.te_UART_SendTerminal.setText(data)
            self.cb_Send_HEX_Flag = False


    def UART_Send(self,server):
        #得到发送的数据
        data = self.ui.te_UART_RecTerminal.toPlainText()
        if self.cb_Send_HEX_Flag:
            data = data.split(" ")
            data = [int(i,16) for i in data]
            data = bytearray(data)
        else:
            data = data.encode('utf-8')
        #发送数据
        server.send_message_to_client_long(data)




