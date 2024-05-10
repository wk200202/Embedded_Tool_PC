'''
用于与MCU Wifi模块通信的数据格式化

发送数据格式：
数据包以HEX格式发送，数据包格式如下：
    1. 0x55 0xAA    数据包头
    2. 0x01         数据包类型
        2.1 0x01     数据包类型为0x01时，表示与Setting界面相关
        2.2 0x02     数据包类型为0x02时，表示与OSC界面相关
        2.3 0x03     数据包类型为0x03时，表示与UART界面相关
        2.4 0x04     数据包类型为0x04时，表示与DDS界面相关
    3. 0xXX 0xXX     数据包长度2位
    4. 0x01         数据包内容,限制在1000字节以内
    6. 0xAA 0x55    数据包尾

接收数据格式：
数据包以HEX格式接收，数据包格式如下：
    1. 0x55 0xAA    数据包头
    2. 0x01         数据包类型
        2.1 0x01     数据包类型为0x01时，表示与Setting界面相关
        2.2 0x02     数据包类型为0x02时，表示与OSC界面相关
        2.3 0x03     数据包类型为0x03时，表示与UART界面相关
        2.4 0x04     数据包类型为0x04时，表示与DDS界面相关
    4. ....         数据包内容
    5. 0xAA 0x55    数据包尾
'''
import queue
from threading import Thread

# 定义一个队列用于存储接收到的数据包
data_packet_queue = queue.Queue()

re_buffer = b'' # 接收缓冲区

class MCU_Format():
    def __init__(self):
        pass

    def format_data(data_type, data):
        '''
        格式化发送数据
        :param data_type: 数据包类型
        :param data: 数据包内容
        :return: 格式化后的数据
        '''
        data_len = len(data)
        data_len_high = data_len // 256
        data_len_low = data_len % 256
        data = bytes([0x55, 0xAA, data_type, data_len_high, data_len_low]) + data + bytes([0xAA, 0x55])
        return data

    # def parse_data(data, OSC_thread):
    #     '''
    #     解析接收数据
    #     :param data: 接收到的数据
    #     '''
    #     # formatted_bytes = [f'0{x:02x}' for x in data]
    #     # # 使用字符串的 join() 方法将格式化后的字节串连接成一个字符串
    #     # formatted_output = ' '.join(formatted_bytes)
    #     # # 打印输出格式化后的字节串
    #     # print(formatted_output)

    #     # 将数据缓存到缓冲区，若满足数据包格式，则解析数据包，否则继续缓存
    #     global re_buffer
    #     # 若data不以0x55 0xAA开头，则将data缓存到re_buffer中
    #     if data[0:2] != b'\x55\xAA':
    #         re_buffer += data
    #         # print("+++")
    #     else:
    #         re_buffer = data
    #         # print("找到数据包头")

    #     # 若data以0xAA 0x55结尾，则解析数据包
    #     if re_buffer[-2:] == b'\xAA\x55':
    #         data_type = re_buffer[2]
    #         data_len = len(re_buffer[3:-2])
    #         data_content = re_buffer[5:-2]
    #         # print('data_type:', data_type)
    #         print('data_len:', data_len)
    #         # print('data_content:', data_content)
            
    #         # 判断数据包类型
    #         if data_type == 0x01:       # 与Setting界面相关
    #             pass
    #         elif data_type == 0x02:     # 与OSC界面相关
    #             MCU_Format.OSC_data_format(data_content, OSC_thread)
    #         elif data_type == 0x03:     # 与UART界面相关
    #             pass
    #         elif data_type == 0x04:     # 与DDS界面相关
    #             pass

    #         re_buffer = b''
    #     else:
    #         return

    @staticmethod
    def parse_data(data,    ):
        global re_buffer
        re_buffer += data  # 将接收到的数据累加到缓冲区

        # 寻找数据包头和尾
        try:
            start_index = re_buffer.index(b'\x55\xAA')
            end_index = re_buffer.rindex(b'\xAA\x55') + 2  # 加2是因为要包括包尾本身
            if start_index != -1 and end_index != -1:
                # 从缓冲区中提取完整的数据包
                packet = re_buffer[start_index:end_index]
                # 将数据包存入队列
                data_packet_queue.put(packet)
                # 清理缓冲区，移除已处理的数据
                re_buffer = re_buffer[end_index:]
        except ValueError:
            # 数据包不完整，继续接收数据
            pass


    def OSC_data_format(re_buffer, OSC_thread):
        '''
        将传入数据解析为CH1和CH2的数据，更新给OSC界面
        '''
        CH1_data = []
        CH2_data = []

        # 解析数据
        for i in range(0, len(re_buffer), 2):
            # 提取CH1数据
            ch1_byte = int.from_bytes(
                re_buffer[i:i+1], byteorder='big', signed=True)
            ch1_byte = ch1_byte - 128
            CH1_data.append(ch1_byte)

            # 提取CH2数据
            ch2_byte = int.from_bytes(
                re_buffer[i+1:i+2], byteorder='big', signed=True)
            # 将CH2数据的高低位交换
            ch2_data = ((ch2_byte & 0x01) << 7) | ((ch2_byte & 0x02) << 5) | ((ch2_byte & 0x04) << 3) | ((ch2_byte & 0x08) << 1) | (
                (ch2_byte & 0x10) >> 1) | ((ch2_byte & 0x20) >> 3) | ((ch2_byte & 0x40) >> 5) | ((ch2_byte & 0x80) >> 7)
            ch2_byte = ch2_data - 128
            CH2_data.append(ch2_byte)

        # OSC_thread.UpdateWaveData(CH1_data,1)
        # OSC_thread.UpdateWaveData(CH2_data,2)
        # print('CH2_data:', CH2_data)

        # 寻找CH1最大值
        # max_CH2 = max(CH2_data)
        # # 寻找CH1最小值
        # min_CH2 = min(CH2_data)
        # print('CH2最大值：', max_CH2)
        # print('CH2最小值：', min_CH2)
        # 换算电压
        # voltage_CH2 = max_CH2 * (1 / 255) * 10
        # print("CH1最大值:", voltage_CH2)
        # voltage_CH2_min = min_CH2 * (1 / 255) * 10
        # print("CH1最小值:", voltage_CH2_min)
        # # 长度
        # print("CH1数据长度:", len(CH2_data))

        