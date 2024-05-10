'''
用于Setting界面的功能函数

主要功能：
    1.建立与MCU Wifi模块的Scoket TCP连接
    2.发送添加的WiFi账号和密码
    3.发送扫描WiFi列表的指令
    4.发送更多Debug信息的指令
    5.发送保持连接的指令
    6.发送断开连接的指令
    7.发送重启设别的指令

    8.接收MCU Wifi模块的返回数据

    9.解析MCU WiFi模块的返回数据
    9.1 解析扫描的WiFi列表
    9.2 解析设备初次连接的信息
    9.3 解析命令执行结果的信息

Setting界面的组件：
    le_Device_IP    : 设备IP地址        QLineEdit
    btn_Connect     : 连接按钮          QPushButton
    le_WiFi_name    : WiFi名称          QLineEdit
    le_WiFi_pw      : WiFi密码          QLineEdit
    btn_Scan_WiFi   : 扫描WiFi列表按钮  QPushButton
    btn_Add_WiFi    : 添加WiFi配置按钮  QPushButton
    btn_Status_LED  : 状态LED按钮       QPushButton
    te_Debug        : Debug命令输入框   QTextEdit
    btn_Debug_Send  : 发送Debug命令按钮  QPushButton
    btn_Rst         : 重启按钮          QPushButton
    te_Setting_Terminal : 设置界面终端  QTextEdit
'''
from . Socket_Thread import *

class Setting_Manager(object):

    '''
    关于服务器线程的操作
    '''
    def Server_start(self,OSC_thread):
        server_ip = self.ui.le_Device_IP.text()
        server_port = int(9090)
        self.ui.btn_Connect.setEnabled(False)
        self.server = TCPServer(self.ui, server_ip, server_port,OSC_thread)

    def Server_stop(self):
        if self.server is not None:
            self.server.stop()
    

    def Debug_Send(self):
        message = self.ui.te_Debug.toPlainText()
        self.server.send_message_to_client(message)

    # 获取本机的IP地址
    def Get_Local_IP():
        import socket
        local_ip = socket.gethostbyname(socket.gethostname())
        return local_ip

    '''
    向MCU WiFi模块发送扫描WiFi列表的指令
    '''
    def Scan_WiFi(self):
        pass

    '''
    向MCU WiFi模块发送添加WiFi账号和密码的指令
    '''
    def Add_WiFi(self):
        pass

    '''
    向MCU发送重启设备的指令
    '''
    def Rst(self):
        import time
        self.server.send_message_to_client("重启")
        self.ui.te_Setting_Terminal.append("rebooting...")
        self.ui.te_Setting_Terminal.append("Please reopen the client after seeing the disconnection")
