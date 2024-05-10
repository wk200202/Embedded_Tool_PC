import sys
import os
import platform
from main_functions.Setting_Func import Setting_Manager
from main_functions.Socket_Thread import TCPServer
from main_functions.OSC_Func import OscillographWidget
from main_functions.DDS_Func import DDS_Manager

from modules import *
from widgets import *

# FIX Problem for High DPI and Scale above 100%
os.environ["QT_FONT_DPI"] = "125"

# SET AS GLOBAL WIDGETS
widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.server = None
        global widgets
        widgets = self.ui

        # 初始化OSC线程
        self.osc_thread = OscillographWidget(self.ui, widgets.widget_OSC_main, 2,self)

        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        self.setWindowTitle("Embedded Tools")  # 设置窗口标题
        widgets.titleRightInfo.setText("Setting")  # 设置窗口描述
        widgets.version.setText("V1.8.0")  # 设置版本号
        # 设置UI功能
        UIFunctions.uiDefinitions(self)
        # 左侧菜单栏按钮
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        widgets.btn_Setting.clicked.connect(self.buttonClick)  # 设置按钮
        widgets.btn_OSC.clicked.connect(self.buttonClick)  # 示波器按钮
        widgets.btn_UART.clicked.connect(self.buttonClick)  # 串口按钮
        widgets.btn_DDS.clicked.connect(self.buttonClick)  # DDS按钮
        # ///////////////////////////////////////////////////////////////
        # 功能页面按钮
        self.Setting_Button_Bind()
        self.OSC_Button_Bind()
        self.UART_Button_Bind()
        self.DDS_Button_Bind()

        # 主界面显示
        self.show()
        widgets.stackedWidget.setCurrentWidget(widgets.Page_Setting)
        widgets.btn_Setting.setStyleSheet(UIFunctions.selectMenu(widgets.btn_Setting.styleSheet()))

    # ////////////////////////////其他函数///////////////////////////////////
    '''
    Setting界面按钮绑定
    btn_Connect     : 连接按钮          QPushButton
    btn_Scan_WiFi   : 扫描WiFi列表按钮  QPushButton
    btn_Add_WiFi    : 添加WiFi配置按钮  QPushButton
    btn_Status_LED  : 状态LED按钮       QPushButton
    btn_Debug_Send  : 发送Debug命令按钮  QPushButton
    btn_Rst         : 重启按钮          QPushButton
    '''

    def Setting_Button_Bind(self):
        widgets.btn_Connect.clicked.connect(
            lambda: Setting_Manager.Server_start(self, self.osc_thread))
        widgets.btn_Scan_WiFi.clicked.connect(
            lambda: Setting_Manager.Scan_WiFi(self))
        widgets.btn_Add_WiFi.clicked.connect(
            lambda: Setting_Manager.Add_WiFi(self))
        widgets.btn_Status_LED.clicked.connect(
            lambda: Setting_Manager.Status_LED(self))
        widgets.btn_Debug_Send.clicked.connect(
            lambda: Setting_Manager.Debug_Send(self))
        widgets.btn_Rst.clicked.connect(lambda: Setting_Manager.Rst(self))

        # 显示本机IP
        widgets.le_Device_IP.setText(Setting_Manager.Get_Local_IP())

    '''
    OSC界面按钮绑定
    btn_OSC_FFT     : FFT按钮          QPushButton
    btn_OSC_CH1_EN  : CH1使能按钮      QPushButton
    btn_OSC_CH2_EN  : CH2使能按钮      QPushButton
    btn_Run_Stop    : 运行/停止按钮    QPushButton
    btn_Screenshot  : 截图按钮          QPushButton

    dial_OSC_Horizontal     : 水平缩放滑动条        QDial
    dial_OSC_Vertical_CH1   : CH1垂直缩放滑动条     QDial
    dial_OSC_Vertical_CH2   : CH2垂直缩放滑动条     QDial
    dial_OSC_Offset_CH1     : CH1偏移滑动条         QDial
    dial_OSC_Offset_CH2     : CH2偏移滑动条         QDial

    com_CH1_Date1   : CH1数据1选择框    QComboBox
    com_CH1_Date2   : CH1数据2选择框    QComboBox
    com_CH1_Date3   : CH1数据3选择框    QComboBox
    com_CH1_Date4   : CH1数据4选择框    QComboBox
    com_CH1_Date5   : CH1数据5选择框    QComboBox
    com_CH2_Date1   : CH2数据1选择框    QComboBox
    com_CH2_Date2   : CH2数据2选择框    QComboBox
    com_CH2_Date3   : CH2数据3选择框    QComboBox
    com_CH2_Date4   : CH2数据4选择框    QComboBox
    com_CH2_Date5   : CH2数据5选择框    QComboBox


    '''

    def OSC_Button_Bind(self):
        widgets.btn_OSC_FFT.clicked.connect(
            lambda: OscillographWidget.FFTmode(self.osc_thread))
        widgets.btn_OSC_CH1_EN.clicked.connect(
            lambda: OscillographWidget.CH1_EN(self.osc_thread))
        widgets.btn_OSC_CH2_EN.clicked.connect(
            lambda: OscillographWidget.CH2_EN(self.osc_thread))
        widgets.btn_Run_Stop.clicked.connect(
            lambda: OscillographWidget.Run_Stop(self.osc_thread))
        widgets.btn_Screenshot.clicked.connect(
            lambda: OscillographWidget.Screenshot(self.osc_thread))

        widgets.dial_OSC_Vertical_CH1.valueChanged.connect(
            lambda: OscillographWidget.setCH1_Vscale(self.osc_thread))
        widgets.dial_OSC_Vertical_CH2.valueChanged.connect(
            lambda: OscillographWidget.setCH2_Vscale(self.osc_thread))

    '''
    UART界面按钮绑定
    '''
    def UART_Button_Bind(self):
        pass
    '''
    DDS界面按钮绑定
    
    com_Wavetype    : 波形选择框    QComboBox
    le_DDS1_Vpp     : Vpp输入框     QLineEdit
    le_DDS1_Duty    : 占空比输入框  QLineEdit
    le_DDS1_Freq    : 频率输入框    QLineEdit
    btn_DDS1_Generate: 生成按钮      QPushButton
    btn_DDS1_Stop   : 停止按钮       QPushButton
    
    te_DDS_Date     : 波表数据框     QTextEdit
    le_DDS2_Freq    : 采样频率输入框    QLineEdit
    btn_DDS2_Generate: 生成按钮      QPushButton
    btn_DDS2_Stop   : 停止按钮       QPushButton
    
    le_PWM1_Freq    : 频率输入框    QLineEdit
    le_PWM2_Duty    : 占空比输入框  QLineEdit
    btn_PWM1_Generate: 生成按钮      QPushButton
    btn_PWM1_Stop   : 停止按钮       QPushButton
    btn_PWM1_Servo  : 舵机按钮       QPushButton
    
    le_PWM2_Freq    : 频率输入框    QLineEdit
    le_PWM2_Duty_2    : 占空比输入框  QLineEdit
    btn_PWM2_Generate: 生成按钮      QPushButton
    btn_PWM2_Stop   : 停止按钮       QPushButton
    btn_PWM2_Servo  : 舵机按钮       QPushButton
    
    '''
    def DDS_Button_Bind(self):
        widgets.btn_DDS1_Generate.clicked.connect(lambda: DDS_Manager.btn_DDS1_Generate_Clicked(self.server,self.ui))
        widgets.btn_DDS1_Stop.clicked.connect(lambda: DDS_Manager.btn_DDS1_Stop_Clicked(self.server,self.ui))

        widgets.btn_DDS2_Generate.clicked.connect(lambda: DDS_Manager.btn_DDS2_Generate_Clicked(self.server,self.ui))
        widgets.btn_DDS2_Stop.clicked.connect(lambda: DDS_Manager.btn_DDS2_Stop_Clicked(self.server,self.ui))

        widgets.btn_PWM1_Generate.clicked.connect(lambda: DDS_Manager.btn_PWM1_Generate_Clicked(self.server,self.ui))
        widgets.btn_PWM1_Stop.clicked.connect(lambda: DDS_Manager.btn_PWM1_Stop_Clicked(self.server,self.ui))
        widgets.btn_PWM1_Servo.clicked.connect(lambda: DDS_Manager.btn_PWM1_Servo_Clicked(self.server,self.ui))

        widgets.btn_PWM2_Generate.clicked.connect(lambda: DDS_Manager.btn_PWM2_Generate_Clicked(self.server,self.ui))
        widgets.btn_PWM2_Stop.clicked.connect(lambda: DDS_Manager.btn_PWM2_Stop_Clicked(self.server,self.ui))
        widgets.btn_PWM2_Servo.clicked.connect(lambda: DDS_Manager.btn_PWM2_Servo_Clicked(self.server,self.ui))

    # ///////////////////////////////////////////////////////////////

    # 按钮事件

    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW SETTINGS PAGE
        if btnName == "btn_Setting":
            widgets.stackedWidget.setCurrentWidget(widgets.Page_Setting)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            widgets.titleRightInfo.setText("Setting")  # 设置窗口描述

        # SHOW OSC PAGE
        if btnName == "btn_OSC":
            widgets.stackedWidget.setCurrentWidget(widgets.Page_OSC)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            widgets.titleRightInfo.setText("Virtual OSC")  # 设置窗口描述
            self.osc_thread.start_worker_thread()   # 启动示波器线程

        # SHOW UART PAGE
        if btnName == "btn_UART":
            widgets.stackedWidget.setCurrentWidget(
                widgets.Page_UART)  # SET PAGE
            # RESET ANOTHERS BUTTONS SELECTED
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(
                btn.styleSheet()))  # SELECT MENU
            widgets.titleRightInfo.setText("Serial Port")  # 设置窗口描述

        # SHOW DDS PAGE
        if btnName == "btn_DDS":
            widgets.stackedWidget.setCurrentWidget(
                widgets.Page_DDS)  # SET PAGE
            # RESET ANOTHERS BUTTONS SELECTED
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(
                btn.styleSheet()))  # SELECT MENU
            widgets.titleRightInfo.setText("DDS")  # 设置窗口描述

         # PRINT BTN NAME
        print(f'UI_Button "{btnName}" pressed!')

    # 调整窗口大小事件
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)
    # 鼠标点击事件

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()
        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
    # 关闭窗口事件

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '请确认', "请确认关闭", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            Setting_Manager.Server_stop(self)
            self.osc_thread.stop_worker_thread()
            QApplication.quit()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
