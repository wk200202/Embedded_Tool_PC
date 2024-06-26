import math
import random
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Qt, QRect, QTimer, QThread, Signal, QPoint
from PySide6.QtGui import QPainter, QColor, QFont, QPen, QPixmap, QPolygon, QBrush
import sys
import numpy as np

# 垂直电压缩放，共10档,二维数组，第一维为显示字符，第二维为对应的波形缩放倍数,第三维为电压计算系数
osc_vol_scale = [["10mV/div",   10,     0.1,    "10"],
                 ["20mV/div",   5,      0.2,    "5"],
                 ["50mV/div",   2,      0.5,    "2"],
                 ["100mV/div",  1,      1,      "1"],
                 ["200mV/div",  0.5,    2,      "1/2"],
                 ["500mV/div",  0.2,    5,      "1/5"],
                 ["1V/div",     0.1,    10,     "1/10"],
                 ["2V/div",     0.05,   20,     "1/20"],
                 ["5V/div",     0.02,   50,     "1/50"],
                 ["10V/div",    0.01,   100,    "1/100"]]
'''
水平时间基准计算
水平像素点100每格
若10M采样率，则一格10us
若5M采样率，则一格20us
若2M采样率，则一格50us
若1M采样率，则一格100us
若500K采样率，则一格200us
若200K采样率，则一格500us
若100K采样率，则一格1ms
'''
# 水平时间基准，共7档,二维数组，第一维为显示字符，第二维为对应的采样率
osc_time_scale = [["10us/div",   10000000],
                    ["20us/div",   5000000],
                    ["50us/div",   2000000],
                    ["100us/div",  1000000],
                    ["200us/div",  500000],
                    ["500us/div",  200000],
                    ["1ms/div",    100000]]



class OscillographWidget(QWidget):
    def __init__(self, ui, parent=None, number=1, main=None):
        super().__init__(parent)
        self.parent = parent
        self.number = number
        self.main = main

        # UI相关设置
        self.setMinimumSize(self.parent.width(), self.parent.height())
        self.setAutoFillBackground(True)        # 设置背景自动填充
        self.setStyleSheet(
            "border-radius: 5px;border: 2px solid rgb(98, 98, 98);background-color: rgb(0, 0, 0);")
        self.ui = ui
        self.ui.Slider_WaveHorzontal.setValue(50)  # 滑块默认位置中间
        self.ui.dial_OSC_Offset_CH1.setValue(200)  # 通道1垂直偏移默认位置中间
        self.ui.dial_OSC_Offset_CH2.setValue(200)  # 通道2垂直偏移默认位置中间

        self.waveDataLength = 1024 * 20    # 波形数据长度
        # 分配波形数据缓冲区
        self.waveDataCH1 = [0] * self.waveDataLength
        self.waveDataCH2 = [0] * self.waveDataLength
        # 通道波形颜色
        self.channelColorCH1 = QColor(255, 255, 127)
        self.channelColorCH2 = QColor(0, 85, 255)
        # 通道显示状态
        self.channelDisplayCH1 = True
        self.channelDisplayCH2 = True
        # 记录屏幕显示区域的序列左右边界
        self.waveDataStartIndex = 0
        self.waveDataEndIndex = self.waveDataLength

        # FFT相关设置
        self.FFTLength = 2048                   # FFT长度
        self.FFTData = [0] * self.FFTLength     # 分配FFT数据缓冲区
        self.FFTData2 = [0] * self.FFTLength    # 分配FFT数据缓冲区2
        self.FFTColor = QColor(189, 147, 249)   # FFT波形颜色
        self.FFTflag = False                    # FFT模式标志
        self.FFTflag2 = False                   # FFT模式标志2,进程间互锁

        self.CH1_Freq = 0                       # 通道1频率
        self.CH2_Freq = 0                       # 通道2频率

        self.VerticalOffset_CH1 = self.ui.dial_OSC_Offset_CH1.value() - 200 # 通道1垂直偏移
        self.VerticalOffset_CH2 = self.ui.dial_OSC_Offset_CH2.value() - 200 # 通道2垂直偏移

        self.channelNumber = number                             # 通道个数
        self.trogglecnt = 1024 * 10                                 # 默认的触发点偏移量
        self.triggerIndex = 0                                   # 触发点索引
        self.triggerLevel = 5                                   # 触发电平
        self.triggerLevelflag = False                           # 触发电平显示标志
        self.triggerLocation = self.parent.width() // 2          # 触发位置,默认在屏幕中间
        self.triggerColor = QColor(213, 58, 44)                 # 触发线颜色
        self.shift = self.ui.Slider_WaveHorzontal.value() * 10 - 500  # 波形水平偏移，-500~500

        self.runflag = True                                     # 运行标志

        self.testflag = False                                   # 测试标志

        # 创建工作线程
        self.worker = WorkerThread(self)
        self.worker.trigger_repaint.connect(self.update_wave_data)
        self.worker.start()

    def start_worker_thread(self):
        # 确保工作线程已经启动
        if not self.worker.isRunning():
            self.worker.start()

    def stop_worker_thread(self):
        # 停止工作线程
        self.worker.stop()

    def update_wave_data(self):
        # 然后重绘窗口以显示新数据
        # if self.runflag == 1:       # 若运行则更新波形数据
            # self.TestSinWave()
            # self.findTrigger()
            # self.displayMeasure()

        self.repaint()
        # print("update_wave_data")

    def paintEvent(self, event):
        # super().paintEvent(event)
        self.drawFrame()
        self.drawWave()
        if self.runflag == 1:
            self.drawFFT()
            if self.triggerLevelflag == True:
                self.drawTriggerLine()

    '''
    绘制触发线
    '''

    def drawTriggerLine(self):
        TriggerWidth = self.parent.width()
        TriggerHeight = self.parent.height()
        painter = QPainter(self)
        painter.setPen(QPen(self.triggerColor, 1.5, Qt.DotLine))
        painter.drawLine(0, TriggerHeight / 2 - self.triggerLevel * 2,
                         TriggerWidth, TriggerHeight / 2 - self.triggerLevel * 2)
        # 末端显示箭头
        painter.drawLine(TriggerWidth - 10, TriggerHeight / 2 - self.triggerLevel *
                         2 - 5, TriggerWidth, TriggerHeight / 2 - self.triggerLevel * 2)
        painter.drawLine(TriggerWidth - 10, TriggerHeight / 2 - self.triggerLevel *
                         2 + 5, TriggerWidth, TriggerHeight / 2 - self.triggerLevel * 2)

    '''
    滚轮事件
    用于改变触发电平大小
    '''

    def wheelEvent(self, event):
        TriggerHeight = self.parent.height()
        if event.angleDelta().y() > 0:
            self.triggerLevel += 2
        else:
            self.triggerLevel -= 2

        if TriggerHeight / 2 - self.triggerLevel * 2 < 0:
            self.triggerLevel = TriggerHeight / 2 / 2
        if TriggerHeight / 2 - self.triggerLevel * 2 > TriggerHeight:
            self.triggerLevel = - TriggerHeight / 2 / 2

        # 滚动后使得triggerLevelflag = True，持续5秒后恢复
        self.triggerLevelflag = True
        self.triggerLevelTimer = QTimer()
        self.triggerLevelTimer.timeout.connect(self.triggerLevelTimeout)
        self.triggerLevelTimer.start(5000)

    def triggerLevelTimeout(self):
        self.triggerLevelflag = False
        self.triggerLevelTimer.stop()
    '''
    寻找触发点
    '''

    def findTrigger(self):
        # 通过com_Trigger_Channal判断触发通道
        if self.ui.com_Trigger_Channal.currentText() == "CH1":
            waveData = self.waveDataCH1
        elif self.ui.com_Trigger_Channal.currentText() == "CH2":
            waveData = self.waveDataCH2

        # 通过com_Trigger_Way判断触发方式
        if self.ui.com_Trigger_Way.currentText() == "上升沿":
            triggerWay = 1
        elif self.ui.com_Trigger_Way.currentText() == "下降沿":
            triggerWay = 0

        if triggerWay == 1:
            for i in range(self.trogglecnt, self.waveDataLength):
                if waveData[i] > self.triggerLevel and waveData[i - 3] < self.triggerLevel:
                    if i > self.waveDataLength - 1500:  # 防止触发点在波形末端
                        self.triggerIndex = self.waveDataLength - 1500
                    else:
                        self.triggerIndex = i
                    break
                else:   # 未找到触发点
                    self.triggerIndex = self.waveDataLength - 1500
        elif triggerWay == 0:
            for i in range(self.trogglecnt, self.waveDataLength):
                if waveData[i] < self.triggerLevel and waveData[i - 3] > self.triggerLevel:
                    if i > self.waveDataLength - 1500:  # 防止触发点在波形末端
                        self.triggerIndex = self.waveDataLength - 1500
                    else:
                        self.triggerIndex = i
                    break
                else:   # 未找到触发点
                    self.triggerIndex = self.waveDataLength - 1500

    '''
    绘制网格
    '''
    def drawFrame(self):

        # 获取窗口的宽度和高度
        width = self.parent.width()  # 使用父窗口的宽度
        height = self.parent.height()  # 使用父窗口的高度
        self.setMinimumSize(width, height)

        # 开始绘制
        painter = QPainter(self)

        # 设置绘制网格的间隔
        dx = 100
        dy = 100

        # 以窗口中心为原点绘制坐标轴
        pen = QPen(QColor(96, 96, 96), 4, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(0, int(height / 2), width, int(height / 2))
        painter.drawLine(int(width / 2), 0, int(width / 2), height)

        pen = QPen(QColor(96, 96, 96), 1.5, Qt.DotLine)
        painter.setPen(pen)

        # 绘制水平网格线
        # 从窗口中心向左绘制
        for x in range(int(width / 2), 0, -dx):
            painter.drawLine(x, 0, x, height)
        # 从窗口中心向右绘制
        for x in range(int(width / 2), width, dx):
            painter.drawLine(x, 0, x, height)

        # 绘制垂直网格线
        # 从窗口中心向上绘制
        for y in range(int(height / 2), 0, -dy):
            painter.drawLine(0, y, width, y)
        # 从窗口中心向下绘制
        for y in range(int(height / 2), height, dy):
            painter.drawLine(0, y, width, y)

    '''
    波形数据更新API
    '''

    def UpdateWaveData(self, data, chn):
        # 更新波形数据
        if chn == 1:
            self.waveDataCH1 = data
        elif chn == 2:
            self.waveDataCH2 = data

    def drawWave(self):
        dispWidth = self.parent.width()
        dispHeight = self.parent.height()
        self.shift = self.ui.Slider_WaveHorzontal.value() * 10 - 500  # 波形水平偏移
        self.triggerLocation = self.parent.width() // 2

        # 判断self.triggerLocation + self.shift是否超出显示范围
        if self.triggerLocation + self.shift < 0:
            start = 0
        elif self.triggerLocation + self.shift > dispWidth:
            start = dispWidth
        else:
            start = self.triggerLocation + self.shift

        painter = QPainter(self)

        # 绘制触发位置
        pen = QPen(self.triggerColor, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(start, 0, start, dispHeight)
        # 末端绘制实心三角形
        painter.setBrush(QBrush(self.triggerColor, Qt.SolidPattern))
        painter.drawPolygon(
            QPolygon([QPoint(start - 5, 5), QPoint(start + 5, 5), QPoint(start, 0)]))

        if self.channelDisplayCH1:
            # 绘制通道1波形
            pen = QPen(self.channelColorCH1, 1.5, Qt.SolidLine)
            painter.setPen(pen)
            # 以triggerLocation为中心，向左绘制triggerIndex前的波形，向右绘制triggerIndex后的波形，需要考虑self.shift的影响

            # 向左绘制
            for i in range(0, start, 1):
                x1 = i
                y1 = int(dispHeight / 2 - self.waveDataCH1[self.triggerIndex - start + i] * 2) + self.VerticalOffset_CH1
                x2 = i + 1
                y2 = int(dispHeight / 2 - self.waveDataCH1[self.triggerIndex - start + i + 1] * 2) + self.VerticalOffset_CH1
                painter.drawLine(x1, y1, x2, y2)
            # 向右绘制
            for i in range(start, dispWidth, 1):
                x1 = i
                y1 = int(dispHeight / 2 - self.waveDataCH1[self.triggerIndex - start + i] * 2) + self.VerticalOffset_CH1
                x2 = i + 1
                y2 = int(dispHeight / 2 - self.waveDataCH1[self.triggerIndex - start + i + 1] * 2) + self.VerticalOffset_CH1
                painter.drawLine(x1, y1, x2, y2)

        if self.channelDisplayCH2:
            # 绘制通道2波形
            pen = QPen(self.channelColorCH2, 1.5, Qt.SolidLine)
            painter.setPen(pen)
            # 以triggerLocation为中心，向左绘制triggerIndex前的波形，向右绘制triggerIndex后的波形，需要考虑self.shift的影响

            # 向左绘制
            for i in range(0, start, 1):
                x1 = i
                y1 = int(dispHeight / 2 - self.waveDataCH2[self.triggerIndex - start + i] * 2) + self.VerticalOffset_CH2
                x2 = i + 1
                y2 = int(dispHeight / 2 - self.waveDataCH2[self.triggerIndex - start + i + 1] * 2) + self.VerticalOffset_CH2
                painter.drawLine(x1, y1, x2, y2)
            # 向右绘制
            for i in range(start, dispWidth, 1):
                x1 = i
                y1 = int(dispHeight / 2 - self.waveDataCH2[self.triggerIndex - start + i] * 2) + self.VerticalOffset_CH2
                x2 = i + 1
                y2 = int(dispHeight / 2 - self.waveDataCH2[self.triggerIndex - start + i + 1] * 2) + self.VerticalOffset_CH2
                painter.drawLine(x1, y1, x2, y2)

        self.waveDataStartIndex = self.triggerIndex - start
        self.waveDataEndIndex = self.triggerIndex + dispWidth - start
        # painter.end()

    def CalcFFT(self):
        # 用于更新FFT数据，减少主线程负担
        if (self.FFTflag == 1):
            self.FFTData = np.fft.rfft(self.waveDataCH1)
            self.FFTflag2 = 1
        else:
            self.FFTflag2 = 0

    def drawFFT(self):
        if (self.FFTflag2 == 1):
            # self.FFTData = np.fft.rfft(self.waveDataCH1)
            FFTWidth = self.parent.width()
            FFTHeight = self.parent.height()

            painter = QPainter(self)

            # 绘制通道2FFT波形
            pen = QPen(self.channelColorCH2, 1.5, Qt.SolidLine)
            pen.setColor(QColor(189, 147, 249))
            painter.setPen(pen)
            num_points = len(self.FFTData)
            num_display_points = min(num_points, FFTWidth)

            # Scale the FFT data to fit within the height of the widget
            max_fft_value = max(abs(self.FFTData))
            if max_fft_value == 0:
                max_fft_value = 1  # Avoid division by zero
            scale_factor = FFTHeight / max_fft_value

            # Draw the FFT waveform
            for i in range(num_display_points - 1):
                x1 = int(i * FFTWidth / num_display_points)
                y1 = int(FFTHeight - abs(self.FFTData[i]) * scale_factor)
                x2 = int((i + 1) * FFTWidth / num_display_points)
                y2 = int(FFTHeight - abs(self.FFTData[i + 1]) * scale_factor)
                painter.drawLine(x1, y1, x2, y2)

    '''
    刷新测量数据
    '''
    def displayMeasure(self):
        # 获取com_CH1_Date1现在序列Index
        tag = self.ui.com_CH1_Date1.currentIndex()
        self.ui.lb_CH1_Date1.setText(self.tagProcess(1, tag))

        tag = self.ui.com_CH1_Date2.currentIndex()
        self.ui.lb_CH1_Date2.setText(self.tagProcess(1, tag))

        tag = self.ui.com_CH1_Date3.currentIndex()
        self.ui.lb_CH1_Date3.setText(self.tagProcess(1, tag))

        tag = self.ui.com_CH1_Date4.currentIndex()
        self.ui.lb_CH1_Date4.setText(self.tagProcess(1, tag))

        tag = self.ui.com_CH1_Date5.currentIndex()
        self.ui.lb_CH1_Date5.setText(self.tagProcess(1, tag))

        tag = self.ui.com_CH2_Date1.currentIndex()
        self.ui.lb_CH2_Date1.setText(self.tagProcess(2, tag))

        tag = self.ui.com_CH2_Date2.currentIndex()
        self.ui.lb_CH2_Date2.setText(self.tagProcess(2, tag))

        tag = self.ui.com_CH2_Date3.currentIndex()
        self.ui.lb_CH2_Date3.setText(self.tagProcess(2, tag))

        tag = self.ui.com_CH2_Date4.currentIndex()
        self.ui.lb_CH2_Date4.setText(self.tagProcess(2, tag))

        tag = self.ui.com_CH2_Date5.currentIndex()
        self.ui.lb_CH2_Date5.setText(self.tagProcess(2, tag))

    def tagProcess(self, chn, tag):
        if chn == 1:
            if tag == 0:
                return "------------"
            elif tag == 1:  # Vpp
                return self.getVpp(self.waveDataCH1, 1)
            elif tag == 2:  # Freq
                return self.getFreq(self.waveDataCH1, 1)
            elif tag == 3:  # Max
                return self.getMax(self.waveDataCH1, 1)
            elif tag == 4:  # Min
                return self.getMin(self.waveDataCH1, 1)
            elif tag == 5:  # Mean
                return self.getMean(self.waveDataCH1, 1)
            elif tag == 6:  # RMS
                return self.getRMS(self.waveDataCH1, 1)
        else:
            if tag == 0:
                return "------------"
            elif tag == 1:
                return self.getVpp(self.waveDataCH2,2)
            elif tag == 2:
                return self.getFreq(self.waveDataCH2,2)
            elif tag == 3:
                return self.getMax(self.waveDataCH2,2)
            elif tag == 4:
                return self.getMin(self.waveDataCH2,2)
            elif tag == 5:
                return self.getMean(self.waveDataCH2,2)
            elif tag == 6:
                return self.getRMS(self.waveDataCH2,2)

    def getVpp(self, data,chn):
        if chn == 1:
            count = self.ui.dial_OSC_Vertical_CH1.value()
        else:
            count = self.ui.dial_OSC_Vertical_CH2.value()
        # 只检测屏幕显示的波形
        start = self.waveDataStartIndex
        end = self.waveDataEndIndex
        print("max", max(data[start:end]))
        print("min", min(data[start:end]))

        return str((max(data[start:end]) - min(data[start:end]))* (1 / 255) * osc_vol_scale[count][2])

    def getMax(self, data, chn):
        if chn == 1:
            count = self.ui.dial_OSC_Vertical_CH1.value()
        else:
            count = self.ui.dial_OSC_Vertical_CH2.value()
        start = self.waveDataStartIndex
        end = self.waveDataEndIndex
        return str(max(data[start:end]) * (1 / 255) * osc_vol_scale[count][2])

    def getMin(self, data, chn):
        if chn == 1:
            count = self.ui.dial_OSC_Vertical_CH1.value()
        else:
            count = self.ui.dial_OSC_Vertical_CH2.value()
        start = self.waveDataStartIndex
        end = self.waveDataEndIndex
        return str(min(data[start:end]) * (1 / 255) * osc_vol_scale[count][2])

    def getMean(self, data, chn):
        if chn == 1:
            count = self.ui.dial_OSC_Vertical_CH1.value()
        else:
            count = self.ui.dial_OSC_Vertical_CH2.value()
        start = self.waveDataStartIndex
        end = self.waveDataEndIndex
        return str(np.mean(data[start:end]) * (1 / 255) * osc_vol_scale[count][2])

    def getRMS(self, data, chn):
        if chn == 1:
            count = self.ui.dial_OSC_Vertical_CH1.value()
        else:
            count = self.ui.dial_OSC_Vertical_CH2.value()
        start = self.waveDataStartIndex
        end = self.waveDataEndIndex
        return str(np.sqrt(np.mean(np.square(data[start:end])))* (1 / 255) * osc_vol_scale[count][2])

    def getFreq(self, data, chn):
        if chn == 1:
            # 通过FFT得到频率
            Freq = np.fft.fftfreq(len(data), 1 / 10000000)
        else:
            Freq = np.fft.fftfreq(len(data), 1 / 10000000)
        return


    # ///////////////////////////////////////////////////////////////
    '''
    btn_OSC_FFT按钮事件
    '''
    def FFTmode(self):
        print("FFT button clicked")
        if (self.FFTflag == 0):
            self.FFTflag = 1
            self.ui.btn_OSC_FFT.setStyleSheet(
                "QPushButton:hover {color: white;border: 2px solid white;font: 14pt ""クレPro by 宁静之雨，微信公众号njzyshare"";}QPushButton:pressed {background-color:rgb(31, 31, 31);border-style: inset;font: 14pt ""クレPro by 宁静之雨，微信公众号njzyshare"";}QPushButton{background-color: rgb(189, 147, 249);color: rgb(75, 59, 99);font: 14pt ""クレPro by 宁静之雨，微信公众号njzyshare"";}")
            self.ui.creditsLabel.setText("FFT Mode ON")
            QTimer.singleShot(
                2000, lambda: self.ui.creditsLabel.setText("Design By HarryWang"))

        else:
            self.FFTflag = 0
            self.ui.btn_OSC_FFT.setStyleSheet(
                "QPushButton:hover {color: white;border: 2px solid white;font: 14pt ""クレPro by 宁静之雨，微信公众号njzyshare"";}QPushButton:pressed {background-color:rgb(31, 31, 31);border-style: inset;font: 14pt ""クレPro by 宁静之雨，微信公众号njzyshare""; }QPushButton{font: 14pt ""クレPro by 宁静之雨，微信公众号njzyshare""; }")
            self.ui.creditsLabel.setText("FFT Mode OFF")
            QTimer.singleShot(
                2000, lambda: self.ui.creditsLabel.setText("Design By HarryWang"))
    '''
    btn_OSC_CH1_EN按钮事件
    '''

    def CH1_EN(self):
        print("CH1 button clicked")
        if (self.channelDisplayCH1 == 0):
            self.channelDisplayCH1 = 1
            self.ui.btn_OSC_CH1_EN.setStyleSheet(
                "QPushButton:hover {color: white;border: 2px solid white;font: 14pt ""クレPro by 宁静之雨，微信公众号njzyshare"";}QPushButton:pressed {background-color:rgb(31, 31, 31);border-style: inset;font: 14pt ""クレPro by 宁静之雨，微信公众号njzyshare"";}QPushButton{background-color: rgb(189, 147, 249);color: rgb(75, 59, 99);font: 14pt ""クレPro by 宁静之雨，微信公众号njzyshare"";}")
            self.ui.creditsLabel.setText("Channel 1 is enabled")
            QTimer.singleShot(
                2000, lambda: self.ui.creditsLabel.setText("Design By HarryWang"))
        else:
            self.channelDisplayCH1 = 0
            self.ui.btn_OSC_CH1_EN.setStyleSheet(
                "QPushButton:hover {color: white;border: 2px solid white;font: 14pt ""クレPro by 宁静之雨，微信公众号njzyshare"";}QPushButton:pressed {background-color:rgb(31, 31, 31);border-style: inset;font: 14pt ""クレPro by 宁静之雨，微信公众号njzyshare""; }QPushButton{font: 14pt ""クレPro by 宁静之雨，微信公众号njzyshare""; }")
            self.ui.creditsLabel.setText("Channel 1 is disabled")
            QTimer.singleShot(
                2000, lambda: self.ui.creditsLabel.setText("Design By HarryWang"))
    '''
    btn_OSC_CH2_EN按钮事件
    '''

    def CH2_EN(self):
        print("CH2 button clicked")
        if (self.channelDisplayCH2 == 0):
            self.channelDisplayCH2 = 1
            self.ui.btn_OSC_CH2_EN.setStyleSheet(
                "QPushButton:hover {color: white;border: 2px solid white;font: 14pt ""クレPro by 宁静之雨，微信公众号njzyshare"";}QPushButton:pressed {background-color:rgb(31, 31, 31);border-style: inset;font: 14pt ""クレPro by 宁静之雨，微信公众号njzyshare"";}QPushButton{background-color: rgb(189, 147, 249);color: rgb(75, 59, 99);font: 14pt ""クレPro by 宁静之雨，微信公众号njzyshare"";}")
            self.ui.creditsLabel.setText("Channel 2 is enabled")
            QTimer.singleShot(
                2000, lambda: self.ui.creditsLabel.setText("Design By HarryWang"))
        else:
            self.channelDisplayCH2 = 0
            self.ui.btn_OSC_CH2_EN.setStyleSheet(
                "QPushButton:hover {color: white;border: 2px solid white;font: 14pt ""クレPro by 宁静之雨，微信公众号njzyshare"";}QPushButton:pressed {background-color:rgb(31, 31, 31);border-style: inset;font: 14pt ""クレPro by 宁静之雨，微信公众号njzyshare""; }QPushButton{font: 14pt ""クレPro by 宁静之雨，微信公众号njzyshare""; }")
            self.ui.creditsLabel.setText("Channel 2 is disabled")
            QTimer.singleShot(
                2000, lambda: self.ui.creditsLabel.setText("Design By HarryWang"))
    '''
    btn_Run_Stop按钮事件
    '''

    def Run_Stop(self):
        print("Run_Stop button clicked")
        if (self.runflag == 0):  # 开始运行
            self.runflag = 1
            self.ui.fra_StatusPic.setStyleSheet(
                "border-image: url(:/images/images/images/图片6.png);")
            self.ui.creditsLabel.setText("Running")
            QTimer.singleShot(
                2000, lambda: self.ui.creditsLabel.setText("Design By HarryWang"))

        else:  # 停止运行
            self.runflag = 0
            self.ui.fra_StatusPic.setStyleSheet(
                "border-image: url(:/images/images/images/图片7.png);")
            self.ui.creditsLabel.setText("Stop")
            QTimer.singleShot(
                2000, lambda: self.ui.creditsLabel.setText("Design By HarryWang"))

    '''
    btn_Screenshot按钮事件
    '''

    def Screenshot(self):
        import time
        print("Screenshot button clicked")
        # 截取整个Page_OSC（Qwidget）界面，存入工程目录下的screenshot文件夹，以当前时间命名
        pixmap = QPixmap(self.ui.Page_OSC.size())
        self.ui.Page_OSC.render(pixmap)
        pixmap.save(
            "screenshot/" + time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()) + ".png")

        self.ui.creditsLabel.setText("Screenshot successful")
        # 2秒后恢复creditsLabel显示
        QTimer.singleShot(
            2000, lambda: self.ui.creditsLabel.setText("Design By HarryWang"))

    '''
    dial_OSC_Vertical_CH1按钮事件
    '''

    def setCH1_Vscale(self):
        print("dial_OSC_Vertical_CH1 button clicked")
        count = self.ui.dial_OSC_Vertical_CH1.value()
        # 发送 "CH1增益"+"osc_vol_scale[count][3]" 字符串拼接在一起
        self.main.server.send_message_to_client("CH1增益" + osc_vol_scale[count][3])
        self.ui.lb_OSC_Vertical_CH1.setText(osc_vol_scale[count][0])

    '''
    dial_OSC_Vertical_CH2按钮事件
    '''
    def setCH2_Vscale(self):
        print("dial_OSC_Vertical_CH2 button clicked")
        count = self.ui.dial_OSC_Vertical_CH2.value()
        # 发送 "CH2增益"+"osc_vol_scale[count][3]" 字符串拼接在一起
        self.main.server.send_message_to_client("CH2增益" + osc_vol_scale[count][3])
        self.ui.lb_OSC_Vertical_CH2.setText(osc_vol_scale[count][0])

    def setCH1_Offset(self):
        self.VerticalOffset_CH1 = self.ui.dial_OSC_Offset_CH1.value() - 200  # 通道1垂直偏移

    def setCH2_Offset(self):
        self.VerticalOffset_CH2 = self.ui.dial_OSC_Offset_CH2.value() - 200

    def setHorizontal(self):
        # 获取当前value值
        count = self.ui.dial_OSC_Horizontal.value()
        try:
            self.main.server.send_message_to_client("水平缩放" + osc_time_scale[count][0])
        except:
            pass
        self.ui.lb_OSC_Horizontal.setText(osc_time_scale[count][0])

class WorkerThread(QThread):
    trigger_repaint = Signal()

    def __init__(self, oscillograph_widget, parent=None):
        super().__init__(parent)
        self.oscillograph_widget = oscillograph_widget
        self.running = True

    def run(self):
        while self.running:
            # 当波形数据更新时，发出信号
            if self.oscillograph_widget.runflag == 1:
                self.oscillograph_widget.CalcFFT()
                self.oscillograph_widget.findTrigger()
            self.oscillograph_widget.displayMeasure()
            self.trigger_repaint.emit()
            # 模拟工作间隔
            self.msleep(200)   # 100ms 工作间隔

    def stop(self):
        self.running = False
