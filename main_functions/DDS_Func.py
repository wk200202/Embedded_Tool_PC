'''
DDS界面，主要用于对DAC模块分频系数的计算，和PWM模块分频系数的计算
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
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


class DDS_Manager():
    def __init__(self):
        pass

    '''
    DAC常规波形计算
    参数：波形类型，设置的频率，设置的幅度，设置的占空比
    返回：波形波表数据，一个周期200个点
         DAC的采样频率，如：输入频率为1KHz，一个周期200个点，那么采样频率为200KHz
    '''
    def DAC_Routine_Calc(wave_type, freq, amplitude, duty):
        wavedata = []
        # 计算占空比
        if duty > 100:
            duty = 100
        elif duty < 0:
            duty = 0
        if amplitude > 3.3:
            amplitude = 3.3
        elif amplitude < 0:
            amplitude = 0
        if wave_type == "Sine wave":
            wavedata = DDS_Manager.SineWave(amplitude, duty)
        elif wave_type == "Square wave":
            wavedata = DDS_Manager.SquareWave(amplitude, duty)
        elif wave_type == "Triangular wave":
            wavedata = DDS_Manager.TriangleWave(amplitude, duty)

        # 画出波形
        # plt.plot(wavedata)
        # plt.show()

        # 计算采样频率
        sample_freq = freq * 200
        return wavedata, sample_freq
    '''
    计算Sin波形的波表数据，一个周期的200个点
    参数：波形的幅度，对应关系3.3V——4095，做限幅处理
         占空比，正弦波占空比为无效参数
    返回：波形波表数据，范围在0-4095之间
    '''
    def SineWave(amplitude, duty):
        wavedata = []
        amplitude = amplitude * 4095 / 3.3
        for i in range(200):
            wavedata.append(int((amplitude/2)*math.sin(2*math.pi*i/200)+amplitude/2))
        return wavedata

    '''
    计算方波波形的波表数据，一个周期的200个点
    参数：波形的幅度，对应关系3.3V——4095，做限幅处理
         占空比，范围在0-100之间
    返回：波形波表数据，范围在0-4095之间
    '''
    def SquareWave(amplitude, duty):
        wavedata = []
        amplitude = amplitude * 4095 / 3.3
        for i in range(200):
            if i < 200*duty/100:
                wavedata.append(int(amplitude))
            else:
                wavedata.append(0)
        return wavedata

    '''
    计算三角波波形的波表数据，一个周期的200个点
    参数：波形的幅度，对应关系3.3V——4095，做限幅处理
            占空比，三角波占空比为无效参数
    返回：波形波表数据，范围在0-4095之间
    '''
    def TriangleWave(amplitude, duty):
        wavedata = []
        amplitude = amplitude * 4095 / 3.3
        for i in range(200):
            if i < 100:
                wavedata.append(int(i*amplitude/100))
            else:
                wavedata.append(int((200-i)*amplitude/100))
        return wavedata

    '''
    打包波形数据，将波形数据打包成一个字节流，用于发送给MCU,波形数据为uint32_t类型
    第一个字节：DDS1 = 0x64
    第2-5字节：采样频率
    第4-403字节：波形数据
    '''
    def Pack_WaveData(wave_type, freq, amplitude, duty):
        wavedata, sample_freq = DDS_Manager.DAC_Routine_Calc(wave_type, freq, amplitude, duty)
        data = []
        # print("sample_freq:", sample_freq)
        data.append(0x64)
        data.append((sample_freq >> 24) & 0xff)
        data.append((sample_freq >> 16) & 0xff)
        data.append((sample_freq >> 8) & 0xff)
        data.append(sample_freq & 0xff)

        for i in wavedata:
            data.append(i & 0xff)
            data.append(i >> 8)
        return data

    '''
    格式化波表内容，将波表数据格式化成需要发送的数据包
    DDS2 = 0x65
    采样频率 uint32_t
    波形数据
    '''
    def Pack_WaveData2(data,freq):
        senddata = []
        data = data.split(',')
        #将波形数据打包成一个字节流，用于发送给MCU,波形数据为uint16_t类型
        senddata.append(0x65)

        senddata.append((freq >> 24) & 0xff)
        senddata.append((freq >> 16) & 0xff)
        senddata.append((freq >> 8) & 0xff)
        senddata.append(freq & 0xff)

        for i in data:
            try:
                senddata.append(int(i) & 0xff)
                senddata.append(int(i) >> 8)
            except:
                pass
        return senddata

    '''
    用于PWM的波形数据打包
    PWM1 = 0x66 PWM2 = 0x67
    PWM频率，占空比
    '''
    def Pack_WaveData3(freq,duty,who):
        senddata = []
        if who == "PWM1":
            senddata.append(0x66)
        elif who == "PWM2":
            senddata.append(0x67)
        senddata.append((freq >> 24) & 0xff)
        senddata.append((freq >> 16) & 0xff)
        senddata.append((freq >> 8) & 0xff)
        senddata.append(freq & 0xff)

        senddata.append(duty)
        return senddata


    ##################按钮事件##################
    def btn_DDS1_Generate_Clicked(server, ui):
        wave_type = ui.com_Wavetype.currentText()
        freq = ui.le_DDS1_Freq.text()
        amplitude = ui.le_DDS1_Vpp.text()
        duty = ui.le_DDS1_Duty.text()

        # 若有空值，则报错
        if wave_type == "" or freq == "" or amplitude == "" or duty == "":
            # 在对应的文本框中显示错误信息
            if freq == "":
                ui.le_DDS1_Freq.setText("Please input the frequency")
            if amplitude == "":
                ui.le_DDS1_Vpp.setText("Please input the Amplitude")
            if duty == "":
                ui.le_DDS1_Duty.setText("Please input the Duty")
        # 若非数值，则报错，amplitede可以为小数
        elif not freq.isdigit() or not amplitude.replace(".", "").isdigit() or not duty.isdigit():
            if not freq.isdigit():
                ui.le_DDS1_Freq.setText("Please input the number")
            if not amplitude.replace(".", "").isdigit():
                ui.le_DDS1_Vpp.setText("Please input the number")
            if not duty.isdigit():
                ui.le_DDS1_Duty.setText("Please input the number")
        else:
            # 转化为int类型
            freq = int(freq)
            amplitude = float(amplitude)
            duty = int(duty)
            # print(DDS_Manager.Pack_WaveData(wave_type, freq, amplitude, duty))
            # try:
            server.send_message_to_client_long(DDS_Manager.Pack_WaveData(wave_type, freq, amplitude, duty))
            # 失能产生按钮
            ui.btn_DDS1_Generate.setEnabled(False)
            # 启用停止按钮
            ui.btn_DDS1_Stop.setEnabled(True)
            # except:
            #     print("Send Error")

    def btn_DDS1_Stop_Clicked(server, ui):
        try:
            server.send_message_to_client("DDS1_Stop")
            # 失能停止按钮
            ui.btn_DDS1_Stop.setEnabled(False)
            # 启用产生按钮
            ui.btn_DDS1_Generate.setEnabled(True)
        except:
            print("Send Error")

    def btn_DDS2_Generate_Clicked(server, ui):
        #将te_DDS_Date内的波表格式化后发送
        data = ui.te_DDS_Date.toPlainText()
        freq = ui.le_DDS2_Freq.text()
        if data == "" or freq == "":
            if data == "":
                ui.te_DDS2_Data.setText("Please input the data")
            if freq == "":
                ui.le_DDS2_Freq.setText("Please input the frequency")
        elif not freq.isdigit():
            ui.le_DDS2_Freq.setText("Please input the number")
        else:
            freq = int(freq)
            # print(DDS_Manager.Pack_WaveData2(data, freq))
            try:
                server.send_message_to_client_long(DDS_Manager.Pack_WaveData2(data, freq))
                ui.btn_DDS2_Generate.setEnabled(False)
                ui.btn_DDS2_Stop.setEnabled(True)
            except:
                print("Send Error")

    def btn_DDS2_Stop_Clicked(server, ui):
        try:
            server.send_message_to_client("DDS2_Stop")
            ui.btn_DDS2_Stop.setEnabled(False)
            ui.btn_DDS2_Generate.setEnabled(True)
        except:
            print("Send Error")





    def btn_PWM1_Generate_Clicked(server, ui):
        freq = ui.le_PWM1_Freq.text()
        duty = ui.le_PWM2_Duty.text()
        if freq == "" or duty == "":
            if freq == "":
                ui.le_PWM1_Freq.setText("Please input the frequency")
            if duty == "":
                ui.le_PWM2_Duty.setText("Please input the duty")
        elif not freq.isdigit() or not duty.isdigit():
            if not freq.isdigit():
                ui.le_PWM1_Freq.setText("Please input the number")
            if not duty.isdigit():
                ui.le_PWM2_Duty.setText("Please input the number")
        else:
            freq = int(freq)
            duty = int(duty)
            # print(DDS_Manager.Pack_WaveData3(freq, duty, "PWM1"))
            try:
                server.send_message_to_client_long(DDS_Manager.Pack_WaveData3(freq, duty, "PWM1"))
                ui.btn_PWM1_Generate.setEnabled(False)
                ui.btn_PWM1_Stop.setEnabled(True)
            except:
                print("Send Error")

    def btn_PWM1_Stop_Clicked(server, ui):
        try:
            server.send_message_to_client("PWM1_Stop")
            ui.btn_PWM1_Stop.setEnabled(False)
            ui.btn_PWM1_Generate.setEnabled(True)
        except:
            print("Send Error")

    def btn_PWM1_Servo_Clicked(server, ui):
        freq = 20000
        duty = 50
        # print(DDS_Manager.Pack_WaveData3(freq, duty, "PWM1"))
        try:
            server.send_message_to_client_long(DDS_Manager.Pack_WaveData3(freq, duty, "PWM1"))
            ui.btn_PWM2_Generate.setEnabled(False)
            ui.btn_PWM2_Stop.setEnabled(True)
        except:
            print("Send Error")

    def btn_PWM2_Generate_Clicked(server, ui):
        freq = ui.le_PWM2_Freq.text()
        duty = ui.le_PWM2_Duty_2.text()
        if freq == "" or duty == "":
            if freq == "":
                ui.le_PWM2_Freq.setText("Please input the frequency")
            if duty == "":
                ui.le_PWM2_Duty_2.setText("Please input the duty")
        elif not freq.isdigit() or not duty.isdigit():
            if not freq.isdigit():
                ui.le_PWM2_Freq.setText("Please input the number")
            if not duty.isdigit():
                ui.le_PWM2_Duty_2.setText("Please input the number")
        else:
            freq = int(freq)
            duty = int(duty)
            # print(DDS_Manager.Pack_WaveData3(freq, duty, "PWM2"))
            try:
                server.send_message_to_client_long(DDS_Manager.Pack_WaveData3(freq, duty, "PWM2"))
                ui.btn_PWM2_Generate.setEnabled(False)
                ui.btn_PWM2_Stop.setEnabled(True)
            except:
                print("Send Error")

    def btn_PWM2_Stop_Clicked(server, ui):
        try:
            server.send_message_to_client("PWM2_Stop")
            ui.btn_PWM2_Stop.setEnabled(False)
            ui.btn_PWM2_Generate.setEnabled(True)
        except:
            print("Send Error")

    def btn_PWM2_Servo_Clicked(server, ui):
        freq = 20000
        duty = 50
        # print(DDS_Manager.Pack_WaveData3(freq, duty, "PWM2"))
        try:
            server.send_message_to_client_long(DDS_Manager.Pack_WaveData3(freq, duty, "PWM2"))
            ui.btn_PWM2_Generate.setEnabled(False)
            ui.btn_PWM2_Stop.setEnabled(True)
        except:
            print("Send Error")





            
            

