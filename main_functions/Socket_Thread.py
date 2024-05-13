'''
用于Scoket通信的线程
电脑作为TCP Server,MCU作为TCP Client
'''
import collections
import threading
import socket
import time

from PySide6.QtCore import QThread, Signal


class TCPServer:

    def __init__(self, ui, server_ip, server_port,OSC_thread,uart_thread):

        self.ui = ui  # 主界面
        self.ip = server_ip  # 服务器ip地址
        self.OSC_thread = OSC_thread
        self.uart_thread = uart_thread
        self.port = server_port  # 服务器端口号
        self.is_running = False  # 是否已经启动

        self.socket = None  # socket
        self.socketThread = None  # 新的 socket receive 线程
        

        #清空终端
        self.ui.te_Setting_Terminal.clear()
        self.ui.te_Setting_Terminal.append("Terminal of Embedded Tools")
        self.ui.te_Setting_Terminal.append("Powered by Python")

        self.ui.te_Setting_Terminal.append("")
        self.ui.te_Setting_Terminal.append("=> Server IP: " + self.ip)
        self.ui.te_Setting_Terminal.append("=> Server starting")

        self.ring_buffer = RingBuffer(1024 * 1024 * 10)  # 环形缓冲区大小

        # 启动数据解析线程
        self.parsing_thread = ParsingThread(self.ring_buffer, self.OSC_thread,self.uart_thread)
        self.parsing_thread.start()

        self.start()

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((self.ip, self.port))  # 绑定IP与端口
            self.socket.listen(1)  # 设定最大连接数
            self.startSocketReceiveThread()

    def stop(self):
        try:
            if self.is_running:
                self.is_running = False
                if self.socketThread.is_running:
                    self.socketThread.stop()
                    self.parsing_thread.stop()
        except Exception as e:
            print(e)

    def startSocketReceiveThread(self):
        self.socketThread = ServerSocketReceiveThread(self.socket)
        self.socketThread.clientConnection.connect(
            self.socket_client_connect_trigger)
        self.socketThread.receivedClientData.connect(self.show_client_message)
        self.socketThread.receivedClientDataFormat.connect(self.clinet_message_format)
        self.socketThread.serverStatus.connect(self.server_status_trigger)
        self.socketThread.start()

    def server_status_trigger(self, status):
        self.ui.te_Setting_Terminal.append(status)

    def socket_client_connect_trigger(self, state):
        if state == 'connect':
            self.ui.te_Setting_Terminal.append("=> Device Connected")
            #失能连接按钮
            self.ui.btn_Connect.setEnabled(False)
            self.ui.btn_Status_LED.setStyleSheet("border-radius: 15px;background-color: rgb(0, 255, 0);border-color: rgb(0, 170, 127);")
        else:
            self.ui.te_Setting_Terminal.append("=> Device Disconnected")
            #使能连接按钮
            self.ui.btn_Connect.setEnabled(True)
            self.ui.btn_Status_LED.setStyleSheet("border-radius: 15px;background-color: rgb(220, 0, 0);border-color: rgb(173, 0, 0);")

    def show_client_message(self, message):
        self.ui.te_Setting_Terminal.append('<= ' + message)

    def clinet_message_format(self, message):
        self.ring_buffer.write(message)

    def send_message_to_client(self, message):
        if self.is_running:
            self.ui.te_Setting_Terminal.append('=> Send:\t'+ message)
            self.socketThread.send_data_to_client(message)

    def send_message_to_client_long(self, message):
        # 传入数据为[]格式,转化为二进制数据发送
        if self.is_running:
            # print(message)
            self.ui.te_Setting_Terminal.append('=> Send:\t'+ str(message))
            self.socketThread.send_data_to_client_long(message)


class ServerSocketReceiveThread(QThread):
    clientConnection = Signal(str)  # 向主线程发送连接状态标志
    receivedClientData = Signal(str)  # 向主线程发送接受到客户端的数据
    receivedClientDataFormat = Signal(bytes)  # 想主线程发送需要解析的透传数据，数据格式为Hex
    serverStatus = Signal(str)  # 向主线程发送服务器状态

    def __init__(self, serverSocket):
        super(ServerSocketReceiveThread, self).__init__()
        self.serverSocket = serverSocket
        self.clientSocket = None
        self.addr = None
        self.is_running = True
        self.TransmissionFlag = False
        

    def run(self):
        self.serverStatus.emit("=> Waiting for Device to Connect......")
        self.clientSocket, self.addr = self.serverSocket.accept()  # 接受客户端的连接
        self.emitConnectEvent('connect')  # 发送通知到主界面
        self.startReceiveData()

    def startReceiveData(self):
        while self.is_running:
            try:
                if not self.TransmissionFlag:
                    data = self.clientSocket.recv(1024).decode('utf-8')
                    if not data:
                        self.emitConnectEvent('disconnect')
                        break
                    # 若消息为"Transmission\r\n"则进入传输模式
                    if data == "Transmission\r\n":
                        self.TransmissionFlag = True
                    self.sendClientDataToUi(data)
                else:
                    data = self.clientSocket.recv(1024 * 30)
                    if not data:
                        self.emitConnectEvent('disconnect')
                        break
                    self.sendClientDataToFormat(data)

            except ConnectionResetError as reason:
                self.sendClientDataToUi("=> Device Leaves Conversation")
                self.is_running = False
                self.emitConnectEvent('disconnect')  # 发送通知到主界面
                break
        self.clientSocket.close()
        self.serverSocket.close()
        self.serverStatus.emit("=> Service Shut Down")


    def send_data_to_client(self, message):
        command = None
        if message == 'None':
            command = 0
        elif message == "重启":
            command = 1
        elif message == "CH1增益10":
            command = 2
        elif message == "CH1增益5":
            command = 3
        elif message == "CH1增益2":
            command = 4
        elif message == "CH1增益1":
            command = 5
        elif message == "CH1增益1/2":
            command = 6
        elif message == "CH1增益1/5":
            command = 7
        elif message == "CH1增益1/10":
            command = 8
        elif message == "CH1增益1/20":
            command = 9
        elif message == "CH1增益1/50":
            command = 10
        elif message == "CH1增益1/100":
            command = 11
        elif message == "CH2增益10":
            command = 12
        elif message == "CH2增益5":
            command = 13
        elif message == "CH2增益2":
            command = 14
        elif message == "CH2增益1":
            command = 15
        elif message == "CH2增益1/2":
            command = 16
        elif message == "CH2增益1/5":
            command = 17
        elif message == "CH2增益1/10":
            command = 18
        elif message == "CH2增益1/20":
            command = 19
        elif message == "CH2增益1/50":
            command = 20
        elif message == "CH2增益1/100":
            command = 21
        elif message == "水平缩放10us/div":
            command = 22
        elif message == "水平缩放20us/div":
            command = 23
        elif message == "水平缩放50us/div":
            command = 24
        elif message == "水平缩放100us/div":
            command = 25
        elif message == "水平缩放200us/div":
            command = 26
        elif message == "水平缩放500us/div":
            command = 27
        elif message == "水平缩放1ms/div":
            command = 28

        elif message == "DDS1_Stop":
            command = 50
        elif message == "DDS2_Stop":
            command = 51
        elif message == "PWM1_Stop":
            command = 52
        elif message == "PWM2_Stop":
            command = 53

        elif message == "OpenOSC":
            command = 200
        elif message == "OpenUART":
            command = 201
        elif message == "OpenDDS":
            command = 202

        try:
            if command is not None:
                self.clientSocket.send(bytes([command]))
            else:
                print("=> Error :unknown command")
        except Exception as reason:
            print("=> Error :", reason)

    def send_data_to_client_long(self, message):
        '''
        发送长数据,传入的数据为bytes数组，以二进制形式发送
        '''
        try:
            self.clientSocket.send(bytes(message))
        except Exception as reason:
            print("=> Error :", reason)

    def stop(self):
        if self.is_running:
            self.is_running = False

    def emitConnectEvent(self, state):
        self.clientConnection.emit(state)

    def sendClientDataToUi(self, message):
        self.receivedClientData.emit(message)

    def sendClientDataToFormat(self, data):
        self.receivedClientDataFormat.emit(data)

            
class RingBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = bytearray(size)
        self.head = 0
        self.tail = 0

    def write(self, data):
        data_len = len(data)
        space = self.size - self.available()
        # print("space:", space)
        if data_len > space:
            raise OverflowError("Ring buffer can't fit data.")
        to_end = min(data_len, self.size - self.tail)
        self.buffer[self.tail: self.tail + to_end] = data[:to_end]
        self.tail = (self.tail + to_end) % self.size

        if to_end < data_len:
            to_start = data_len - to_end
            self.buffer[:self.tail + to_start] = data[to_end:to_end + to_start]
            self.tail = (self.tail + to_start) % self.size


    def read(self, length):
        if length > self.available():
            raise ValueError("Not enough data in buffer.")

        data = self.buffer[self.head %
                           self.size: (self.head + length) % self.size]
        self.head = (self.head + length) % self.size
        return data

    def available(self):
        return (self.tail - self.head + self.size) % self.size

    # 获取剩余空间
    def space(self):
        return self.size - self.available()

    def clear(self):
        with self.lock:
            self.head = self.tail = 0


class ParsingThread(threading.Thread):
    def __init__(self, ring_buffer, osc_thread, uart_thread):
        super(ParsingThread, self).__init__()
        self.ring_buffer = ring_buffer
        self.osc_thread = osc_thread
        self.uart_thread = uart_thread
        self.running = True
        self.last_tail_index = self.ring_buffer.head

        self.head_index = -1
        self.tail_index = -1

    def run(self):
        while self.running:
            # 判断是否有数据
            while(self.ring_buffer.available() > 4):
                try:
                    data = self.find_and_parse_frame()
                    if data:
                        # 根据数据类型处理数据
                        if data['type'] == 0x02:  # 与OSC界面相关
                            MCU_Format.OSC_data_format(data['content'], self.osc_thread)
                        elif data['type'] == 0x03:  # 与UART界面相关
                            MCU_Format.UART_data_format(data['content'], self.uart_thread)
                except Exception as e:
                    print(f"Error parsing frame: {e}")

    def find_and_parse_frame(self):
        if self.ring_buffer.available() > 4:  # 确保有足够的数据进行搜索
            # 从上次读取的结束位置开始搜索帧头
            self.head_index = self.ring_buffer.buffer.find(b'\x55\xAA', self.last_tail_index)

            if self.head_index == -1:
                return None

            # 从帧头位置开始搜索帧尾
            self.tail_index = self.ring_buffer.buffer.find(b'\xAA\x55', self.head_index + 2)  # 从帧头之后的位置开始搜索
            if self.tail_index == -1:
                return None

            # 提取数据帧
            length = self.tail_index - self.head_index + 2
            if length > self.ring_buffer.available():
                print("Error: Frame length exceeds available data.")
                return None

            data_frame = self.ring_buffer.read(length)

            # 解析数据包类型和内容
            data_type = data_frame[2]
            data_content = data_frame[3:-2]

            # 更新上次帧尾索引为当前帧尾索引
            self.last_tail_index = self.tail_index + 2
            self.head_index = -1
            self.tail_index = -1

            # 返回解析结果
            return {
                'type': data_type,
                'content': data_content
            }

    def stop(self):
        self.running = False


class MCU_Format():
    @staticmethod
    def OSC_data_format(data_content, osc_thread):
        # 将解析出的数据传递给 OSC 线程处理
        CH1_data = []
        CH2_data = []

        # 解析数据
        for i in range(0, len(data_content), 2):
            # 提取CH2数据
            ch2_byte = int.from_bytes(
                data_content[i:i + 1], byteorder='big', signed=True)
            ch2_byte = ch2_byte - 128
            CH2_data.append(ch2_byte)

            # 提取CH1数据
            ch1_byte = int.from_bytes(
                data_content[i + 1:i + 2], byteorder='big', signed=True)
            # 将CH2数据的高低位交换
            ch1_data = ((ch1_byte & 0x01) << 7) | ((ch1_byte & 0x02) << 5) | ((ch1_byte & 0x04) << 3) | (
                        (ch1_byte & 0x08) << 1) | (
                               (ch1_byte & 0x10) >> 1) | ((ch1_byte & 0x20) >> 3) | ((ch1_byte & 0x40) >> 5) | (
                                   (ch1_byte & 0x80) >> 7)
            ch1_byte = ch1_data - 128 + 4
            CH1_data.append(ch1_byte)
        if osc_thread.runflag == 1:
            osc_thread.UpdateWaveData(CH1_data, 1)
            osc_thread.UpdateWaveData(CH2_data, 2)

    @staticmethod
    def UART_data_format(data_content, uart_thread):
        '''
        将接收的数据解析出data1,data2,data3,data4
        MCU的发送格式为：%d,%d,%d,%d\r\n
        以\n为结束符，以逗号分隔
        若传入数据不包含\n，则放入缓存区，等待下一次数据到来，再进行解析
        '''
        # 将bytearray转为str
        data_str = data_content.decode()

        # 若数据不包含\n，则放入缓存区，并将缓存区转换为字符串
        if '\n' not in data_str:
            if uart_thread.buffer:
                # 将缓存区的数据转换为字符串
                uart_thread.buffer_str += ''.join(uart_thread.buffer)
                # 清空缓存区
                uart_thread.buffer = []
            # 将当前数据添加到缓存区字符串
            uart_thread.buffer_str += data_str
        else:
            # 若数据包含\n，则将缓存区数据和当前数据合并
            # 将缓存区字符串和当前数据字符串合并
            full_data_str = uart_thread.buffer_str + data_str
            # 将合并后的字符串按照逗号分隔
            full_data_list = full_data_str.split(',')
            # 清空缓存区字符串
            uart_thread.buffer_str = ''
            # 将数据转为int
            data_ints = list(map(int, full_data_list))
            # 绘制数据
            uart_thread.UART_seriesUpdate(data_ints[0], data_ints[1], data_ints[2], data_ints[3])
