## 版本记录

```
v1.0.0							2024.4.14
主界面UI逻辑和动画框架构建
完成Setting，UART界面的设计
基于QChart插入，建立UART波形绘制界面
```

```
v1.1.0							2024.4.16
选择QPainter作为OSC波形绘制组件
OSC，DDS界面设计完成
主要界面适配任意拉伸变化
现存bug：最大化下存在移动变小，原因为止
```

```
v1.2.0							2024.4.17
修复最大化移动窗口突然变小bug

```

```
v1.3.0							2024.4.23
完成对TCP Server的线程实现
修复拾取IP误取虚拟网卡IP的Bug
完成Setting界面的重构
完成对ESP32的通信Debug

```

```
v1.4.0							2024.4.28
完成对OSC背景绘制的实现
完成对波形绘制
完成FFT功能
修复OSC界面按钮bug
完成水平移动功能
```

```
v1.5.0							2024.4.29
修改网格生成逻辑，应对伸缩变换
完成暂停启动功能
完成截图功能，截图后将以时间格式保存在工程目录中
完成测量QcomboBox的功能绑定，功能待完成
适配偏移二进制输入格式，DFS输入为低电平，0V将以0x00表示，范围：-128~127

需解决：
	时基对应采样率待计算
	衰减增益，须在双向通信的前提下进行
	参数的计算以屏幕内波形为范围
```

```
v1.6.0							2024.4.30
修改测量数据的刷新逻辑
完成触发电平改变的滚轮逻辑
修改触发电平下的波形显示逻辑
```

```
v1.7.0                          2024.5.1
完成与MCU的双向通信
完成重启设备按钮逻辑
完成垂直电压双通道的调节
```

```
v1.8.0                          2024.5.7
重构消息接受，使用环形缓冲区接受
开辟帧处理线程，提高主线程刷新率
优化OSC绘画逻辑，下一步将移动数据计算到新线程，进一步降低对主线程的影响
```

```
v1.9.0                          2024.5.10
完成DDS界面所有功能，与MCU联调完成
调整部分参数传递
存在问题：
	MCU的预分频和周期适配较差，存在部分频率精度查的问题—————自适应算法怎么写？做到1Hz到20Mhz准确分屏
```

```
v2.0.0                          2024.5.13
完成与MCU不同界面的切换选择功能
完成与OSC界面测量量功能
	存在问题：AD9288电源可能存在问题，具体偏移量还需要与示波器一起计算
完成OSC界面的水平分辨率功能，现有7挡分辨率
	后期考虑添加插针功能
完成OSC界面水平偏移的功能
	现存在触发功能会失效的问题有待解决
基本功能已经实现
环形缓冲区超出问题，原因为帧头帧尾的丢失，导致解析的失败，存在偶发性
```



## 文件结构

```
- images
- modules
  - __init__.py
  - app_functions.py
    - 用于实现App的逻辑功能
  - app_settings.py
    - 用于全局配置
  - resources_rc.py
  - ui_functions.py
    - 用于界面动画的实现
  - ui_main.py
    - 主界面的设置
    - 按钮事件的绑定
- themes
- widgets
- main.py
- main.ui
- setup.py
```

## UI界面颜色

```css
QPushButton:hover {
	color: white;
	border: 2px solid white;
	/*padding-left: 15px;*/
}
QPushButton:pressed {
	/*color: white;*/
	background-color:rgb(31, 31, 31);
	border-style: inset;
	/*padding-left: 15px;*/
}



QPushButton:hover {
	color: white;
	border: 2px solid white;
	font: 14pt "クレPro by 宁静之雨，微信公众号njzyshare";
}
QPushButton:pressed {
	/*color: white;*/
	background-color:rgb(31, 31, 31);
	border-style: inset;
	font: 14pt "クレPro by 宁静之雨，微信公众号njzyshare";
}
QPushButton
{
	font: 14pt "クレPro by 宁静之雨，微信公众号njzyshare";
}
```



```css
黑灰		color: rgb(33, 37, 43);
紫色		color: rgb(189, 147, 249);
深紫色	   color: rgb(75, 59, 99)
粉色		color: rgb(255, 100, 123)
通道1黄色	color: rgb(255, 255, 127);
通道2蓝色	color: rgb(0, 85, 255);


按钮未选中  background-color: rgb(143, 32, 235);
按钮悬空   background-color: rgb(157, 56, 238);
按钮按下   background-color: rgb(106, 23, 177);

OSC button
使能
background-color: rgb(189, 147, 249);
color: rgb(75, 59, 99)
失能

```



font: 14pt "クレPro by 宁静之雨，微信公众号njzyshare";



```css
QComboBox {
    font-family: "クレPro by 宁静之雨，微信公众号njzyshare";
    font-size: 17px;
}
```





连接指示灯

```
红灯
border-radius: 15px;
background-color: rgb(220, 0, 0);
border-color: rgb(173, 0, 0);

绿灯
border-radius: 15px;
background-color: rgb(0, 255, 0);
border-color: rgb(0, 170, 127);
```

