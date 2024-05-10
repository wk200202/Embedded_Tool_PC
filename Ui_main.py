# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDial,
    QFrame, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1602, 900)
        MainWindow.setMinimumSize(QSize(940, 560))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setAutoFillBackground(False)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	"
                        "\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
""
                        "}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
""
                        "#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* E"
                        "xtra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons ."
                        "QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////"
                        "////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border"
                        "-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  "
                        "QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: "
                        "none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::s"
                        "ub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-a"
                        "lt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
""
                        "	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: "
                        "0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	b"
                        "order-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout_35 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setMaximumSize(QSize(16777215, 16777215))
        self.bgApp.setStyleSheet(u"QFrame#bgApp{\n"
"	border: 1px solid #343b48;\n"
"	border-radius: 5px;\n"
"}")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"border-radius: 21px;\n"
"border-image: url(:/images/images/images/Weixin Image_20240414210221.jpg);")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare"])
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setStyleSheet(u"font: 13pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(71, 27, 121, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        self.titleLeftDescription.setMouseTracking(False)
        self.titleLeftDescription.setStyleSheet(u"font: 8pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(0, 0))
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        font2 = QFont()
        font2.setFamilies([u"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare"])
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        self.toggleButton.setFont(font2)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.toggleButton.setAutoDefault(False)

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_Setting = QPushButton(self.topMenu)
        self.btn_Setting.setObjectName(u"btn_Setting")
        sizePolicy.setHeightForWidth(self.btn_Setting.sizePolicy().hasHeightForWidth())
        self.btn_Setting.setSizePolicy(sizePolicy)
        self.btn_Setting.setMinimumSize(QSize(0, 45))
        self.btn_Setting.setFont(font2)
        self.btn_Setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Setting.setLayoutDirection(Qt.LeftToRight)
        self.btn_Setting.setStyleSheet(u"background-image: url(:/icons/images/icons/\u8bbe\u7f6e.png);font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.verticalLayout_8.addWidget(self.btn_Setting)

        self.btn_OSC = QPushButton(self.topMenu)
        self.btn_OSC.setObjectName(u"btn_OSC")
        sizePolicy.setHeightForWidth(self.btn_OSC.sizePolicy().hasHeightForWidth())
        self.btn_OSC.setSizePolicy(sizePolicy)
        self.btn_OSC.setMinimumSize(QSize(0, 45))
        self.btn_OSC.setFont(font2)
        self.btn_OSC.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_OSC.setLayoutDirection(Qt.LeftToRight)
        self.btn_OSC.setStyleSheet(u"background-image: url(:/icons/images/icons/\u793a\u6ce2\u5668.png);font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.verticalLayout_8.addWidget(self.btn_OSC)

        self.btn_UART = QPushButton(self.topMenu)
        self.btn_UART.setObjectName(u"btn_UART")
        sizePolicy.setHeightForWidth(self.btn_UART.sizePolicy().hasHeightForWidth())
        self.btn_UART.setSizePolicy(sizePolicy)
        self.btn_UART.setMinimumSize(QSize(0, 45))
        self.btn_UART.setFont(font2)
        self.btn_UART.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_UART.setToolTipDuration(-1)
        self.btn_UART.setLayoutDirection(Qt.LeftToRight)
        self.btn_UART.setAutoFillBackground(False)
        self.btn_UART.setStyleSheet(u"background-image: url(:/icons/images/icons/smls icon_\u4e32\u53e3\u52a9\u624b.png);font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.btn_UART.setAutoRepeatInterval(97)

        self.verticalLayout_8.addWidget(self.btn_UART)

        self.btn_DDS = QPushButton(self.topMenu)
        self.btn_DDS.setObjectName(u"btn_DDS")
        sizePolicy.setHeightForWidth(self.btn_DDS.sizePolicy().hasHeightForWidth())
        self.btn_DDS.setSizePolicy(sizePolicy)
        self.btn_DDS.setMinimumSize(QSize(0, 45))
        self.btn_DDS.setFont(font2)
        self.btn_DDS.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_DDS.setLayoutDirection(Qt.LeftToRight)
        self.btn_DDS.setStyleSheet(u"background-image: url(:/icons/images/icons/\u66f2\u7ebf.png);font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.verticalLayout_8.addWidget(self.btn_DDS)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setMinimumSize(QSize(0, 0))
        self.contentBox.setStyleSheet(u"")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        self.titleRightInfo.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font2)
        self.titleRightInfo.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon1)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.Page_Setting = QWidget()
        self.Page_Setting.setObjectName(u"Page_Setting")
        self.Page_Setting.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.Page_Setting)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.te_Setting_Terminal = QTextEdit(self.Page_Setting)
        self.te_Setting_Terminal.setObjectName(u"te_Setting_Terminal")
        self.te_Setting_Terminal.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.te_Setting_Terminal.sizePolicy().hasHeightForWidth())
        self.te_Setting_Terminal.setSizePolicy(sizePolicy1)
        self.te_Setting_Terminal.setMinimumSize(QSize(500, 700))
        self.te_Setting_Terminal.setMaximumSize(QSize(600, 16777215))
        self.te_Setting_Terminal.setFont(font2)
        self.te_Setting_Terminal.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid black;\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(171, 178, 191);\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.te_Setting_Terminal.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.te_Setting_Terminal)

        self.frame_6 = QFrame(self.Page_Setting)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(640, 700))
        self.frame_6.setStyleSheet(u"QFrame#frame_6{\n"
"	border: 1px solid #343b48;\n"
"	/*background-color: rgb(126, 199, 193);*/\n"
"	border-radius: 5px;\n"
"\n"
"}\n"
"QFrame#frame_7{\n"
"	/*background-color: rgb(161, 217, 218);*/\n"
"	border-radius:20px;\n"
"\n"
"}\n"
"QFrame#frame_8{\n"
"	/*background-color: rgb(161, 217, 218);*/\n"
"	border-radius:20px;\n"
"\n"
"}\n"
"QPushButton {\n"
"	border-radius:20px;\n"
"	/*background-color: rgb(255, 255, 255);*/\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: white;\n"
"	border: 2px solid white;\n"
"	/*padding-left: 15px;*/\n"
"}\n"
"QPushButton:pressed {\n"
"	/*color: white;*/\n"
"	background-color:rgb(31, 31, 31);\n"
"	border-style: inset;\n"
"	/*padding-left: 15px;*/\n"
"}\n"
"QLineEdit{\n"
"	/*color: rgb(0, 0, 0);*/\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:15px;\n"
"}\n"
"QLabel#info_text{\n"
"	font-size:22px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(5, 5, 7, 5)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy3)
        self.frame_7.setMaximumSize(QSize(16777215, 400))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_5 = QSpacerItem(230, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy4)
        self.frame_9.setMinimumSize(QSize(100, 40))
        self.frame_9.setMaximumSize(QSize(100, 40))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(9, 0, 30, 0)
        self.info_text = QLabel(self.frame_9)
        self.info_text.setObjectName(u"info_text")
        self.info_text.setMinimumSize(QSize(85, 35))
        font4 = QFont()
        font4.setFamilies([u"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare"])
        font4.setPointSize(18)
        font4.setBold(False)
        font4.setItalic(False)
        self.info_text.setFont(font4)
        self.info_text.setStyleSheet(u"font: 18pt  \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.info_text.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.info_text)


        self.horizontalLayout_8.addWidget(self.frame_9)

        self.horizontalSpacer_6 = QSpacerItem(230, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 5, -1, 5)
        self.lb_Device_IP = QLabel(self.frame_7)
        self.lb_Device_IP.setObjectName(u"lb_Device_IP")
        self.lb_Device_IP.setMinimumSize(QSize(130, 30))
        self.lb_Device_IP.setMaximumSize(QSize(120, 16777215))
        self.lb_Device_IP.setFont(font2)
        self.lb_Device_IP.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_Device_IP.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lb_Device_IP)

        self.le_Device_IP = QLineEdit(self.frame_7)
        self.le_Device_IP.setObjectName(u"le_Device_IP")
        self.le_Device_IP.setMinimumSize(QSize(284, 40))
        self.le_Device_IP.setFont(font2)
        self.le_Device_IP.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid black;\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.le_Device_IP.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.le_Device_IP)

        self.btn_Connect = QPushButton(self.frame_7)
        self.btn_Connect.setObjectName(u"btn_Connect")
        self.btn_Connect.setMinimumSize(QSize(200, 45))
        self.btn_Connect.setFont(font2)
        self.btn_Connect.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Connect.setStyleSheet(u"border-radius: 5px;font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_10.addWidget(self.btn_Connect)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 5, -1, 5)
        self.lb_WiFi_name = QLabel(self.frame_7)
        self.lb_WiFi_name.setObjectName(u"lb_WiFi_name")
        self.lb_WiFi_name.setMinimumSize(QSize(130, 30))
        self.lb_WiFi_name.setMaximumSize(QSize(120, 16777215))
        self.lb_WiFi_name.setFont(font2)
        self.lb_WiFi_name.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_WiFi_name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.lb_WiFi_name)

        self.le_WiFi_name = QLineEdit(self.frame_7)
        self.le_WiFi_name.setObjectName(u"le_WiFi_name")
        self.le_WiFi_name.setMinimumSize(QSize(284, 40))
        self.le_WiFi_name.setFont(font2)
        self.le_WiFi_name.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid black;\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_15.addWidget(self.le_WiFi_name)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 5, -1, 5)
        self.lb_WiFi_pw = QLabel(self.frame_7)
        self.lb_WiFi_pw.setObjectName(u"lb_WiFi_pw")
        self.lb_WiFi_pw.setMinimumSize(QSize(130, 30))
        self.lb_WiFi_pw.setMaximumSize(QSize(120, 16777215))
        self.lb_WiFi_pw.setFont(font2)
        self.lb_WiFi_pw.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_WiFi_pw.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.lb_WiFi_pw)

        self.le_WiFi_pw = QLineEdit(self.frame_7)
        self.le_WiFi_pw.setObjectName(u"le_WiFi_pw")
        self.le_WiFi_pw.setMinimumSize(QSize(284, 40))
        self.le_WiFi_pw.setFont(font2)
        self.le_WiFi_pw.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid black;\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_17.addWidget(self.le_WiFi_pw)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.btn_Scan_WiFi = QPushButton(self.frame_7)
        self.btn_Scan_WiFi.setObjectName(u"btn_Scan_WiFi")
        self.btn_Scan_WiFi.setMinimumSize(QSize(200, 45))
        self.btn_Scan_WiFi.setFont(font2)
        self.btn_Scan_WiFi.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Scan_WiFi.setStyleSheet(u"border-radius: 5px;font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_18.addWidget(self.btn_Scan_WiFi)

        self.btn_Add_WiFi = QPushButton(self.frame_7)
        self.btn_Add_WiFi.setObjectName(u"btn_Add_WiFi")
        self.btn_Add_WiFi.setMinimumSize(QSize(200, 45))
        self.btn_Add_WiFi.setFont(font2)
        self.btn_Add_WiFi.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Add_WiFi.setStyleSheet(u"border-radius: 5px;font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_18.addWidget(self.btn_Add_WiFi)

        self.btn_Status_LED = QPushButton(self.frame_7)
        self.btn_Status_LED.setObjectName(u"btn_Status_LED")
        self.btn_Status_LED.setEnabled(False)
        self.btn_Status_LED.setMinimumSize(QSize(30, 30))
        self.btn_Status_LED.setMaximumSize(QSize(30, 30))
        self.btn_Status_LED.setFont(font)
        self.btn_Status_LED.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Status_LED.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(220, 0, 0);\n"
"border-color: rgb(173, 0, 0);")

        self.horizontalLayout_18.addWidget(self.btn_Status_LED)

        self.btn_Status = QLabel(self.frame_7)
        self.btn_Status.setObjectName(u"btn_Status")
        self.btn_Status.setEnabled(False)
        self.btn_Status.setMinimumSize(QSize(120, 30))
        self.btn_Status.setMaximumSize(QSize(120, 16777215))
        self.btn_Status.setFont(font2)
        self.btn_Status.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.btn_Status.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.btn_Status)


        self.verticalLayout_5.addLayout(self.horizontalLayout_18)


        self.horizontalLayout_19.addLayout(self.verticalLayout_5)


        self.verticalLayout_21.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFont(font)
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_9 = QSpacerItem(170, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(200, 45))
        self.frame_10.setMaximumSize(QSize(16777215, 45))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 10, 180, 30))
        self.label_16.setFont(font4)
        self.label_16.setStyleSheet(u"font: 18pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.frame_10)

        self.horizontalSpacer_10 = QSpacerItem(170, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_10)


        self.verticalLayout_24.addLayout(self.horizontalLayout_20)


        self.verticalLayout_9.addLayout(self.verticalLayout_24)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.te_Debug = QTextEdit(self.frame_8)
        self.te_Debug.setObjectName(u"te_Debug")
        sizePolicy3.setHeightForWidth(self.te_Debug.sizePolicy().hasHeightForWidth())
        self.te_Debug.setSizePolicy(sizePolicy3)
        self.te_Debug.setMinimumSize(QSize(520, 100))
        self.te_Debug.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid black;\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.verticalLayout_9.addWidget(self.te_Debug)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_Rst = QPushButton(self.frame_8)
        self.btn_Rst.setObjectName(u"btn_Rst")
        self.btn_Rst.setMinimumSize(QSize(200, 45))
        self.btn_Rst.setFont(font2)
        self.btn_Rst.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Rst.setStyleSheet(u"border-radius: 5px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_12.addWidget(self.btn_Rst)

        self.btn_Debug_Send = QPushButton(self.frame_8)
        self.btn_Debug_Send.setObjectName(u"btn_Debug_Send")
        self.btn_Debug_Send.setMinimumSize(QSize(200, 45))
        self.btn_Debug_Send.setStyleSheet(u"border-radius: 5px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_12.addWidget(self.btn_Debug_Send)


        self.verticalLayout_9.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_16.addLayout(self.verticalLayout_9)


        self.verticalLayout_21.addWidget(self.frame_8)


        self.horizontalLayout_6.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.Page_Setting)
        self.Page_OSC = QWidget()
        self.Page_OSC.setObjectName(u"Page_OSC")
        self.Page_OSC.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.Page_OSC)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.Page_OSC)
        self.frame.setObjectName(u"frame")
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMinimumSize(QSize(1150, 0))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.frame_17 = QFrame(self.frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(0, 0, 0);\n"
"border-color: rgb(99, 99, 99);")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_17)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.fra_StatusPic = QFrame(self.frame_17)
        self.fra_StatusPic.setObjectName(u"fra_StatusPic")
        self.fra_StatusPic.setMinimumSize(QSize(110, 30))
        self.fra_StatusPic.setMaximumSize(QSize(176, 52))
        self.fra_StatusPic.setStyleSheet(u"border-image: url(:/images/images/images/\u56fe\u72476.png);")
        self.fra_StatusPic.setFrameShape(QFrame.StyledPanel)
        self.fra_StatusPic.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_26.addWidget(self.fra_StatusPic)

        self.horizontalSpacer_3 = QSpacerItem(155, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_3)

        self.Slider_WaveHorzontal = QSlider(self.frame_17)
        self.Slider_WaveHorzontal.setObjectName(u"Slider_WaveHorzontal")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Slider_WaveHorzontal.sizePolicy().hasHeightForWidth())
        self.Slider_WaveHorzontal.setSizePolicy(sizePolicy5)
        self.Slider_WaveHorzontal.setMinimumSize(QSize(520, 30))
        self.Slider_WaveHorzontal.setStyleSheet(u"horizontalSlider.setValue(50)")
        self.Slider_WaveHorzontal.setOrientation(Qt.Horizontal)

        self.horizontalLayout_26.addWidget(self.Slider_WaveHorzontal, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.btn_OSC_FFT = QPushButton(self.frame_17)
        self.btn_OSC_FFT.setObjectName(u"btn_OSC_FFT")
        self.btn_OSC_FFT.setEnabled(True)
        self.btn_OSC_FFT.setMinimumSize(QSize(80, 30))
        self.btn_OSC_FFT.setMaximumSize(QSize(115, 16777215))
        self.btn_OSC_FFT.setStyleSheet(u"QPushButton:hover {\n"
"	color: white;\n"
"	border: 2px solid white;\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"}\n"
"QPushButton:pressed {\n"
"	/*color: white;*/\n"
"	background-color:rgb(31, 31, 31);\n"
"	border-style: inset;\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"}\n"
"QPushButton\n"
"{\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"}\n"
"\n"
"")

        self.horizontalLayout_33.addWidget(self.btn_OSC_FFT)

        self.btn_OSC_CH1_EN = QPushButton(self.frame_17)
        self.btn_OSC_CH1_EN.setObjectName(u"btn_OSC_CH1_EN")
        self.btn_OSC_CH1_EN.setEnabled(True)
        self.btn_OSC_CH1_EN.setMinimumSize(QSize(80, 30))
        self.btn_OSC_CH1_EN.setMaximumSize(QSize(115, 16777215))
        self.btn_OSC_CH1_EN.setStyleSheet(u"QPushButton:hover {\n"
"	color: white;\n"
"	border: 2px solid white;\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"}\n"
"QPushButton:pressed {\n"
"	/*color: white;*/\n"
"	background-color:rgb(31, 31, 31);\n"
"	border-style: inset;\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"}\n"
"QPushButton\n"
"{\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(75, 59, 99);\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"}")

        self.horizontalLayout_33.addWidget(self.btn_OSC_CH1_EN)

        self.btn_OSC_CH2_EN = QPushButton(self.frame_17)
        self.btn_OSC_CH2_EN.setObjectName(u"btn_OSC_CH2_EN")
        self.btn_OSC_CH2_EN.setEnabled(True)
        self.btn_OSC_CH2_EN.setMinimumSize(QSize(80, 30))
        self.btn_OSC_CH2_EN.setMaximumSize(QSize(115, 16777215))
        self.btn_OSC_CH2_EN.setStyleSheet(u"QPushButton:hover {\n"
"	color: white;\n"
"	border: 2px solid white;\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"}\n"
"QPushButton:pressed {\n"
"	/*color: white;*/\n"
"	background-color:rgb(31, 31, 31);\n"
"	border-style: inset;\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"}\n"
"QPushButton\n"
"{\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(75, 59, 99);\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"}")

        self.horizontalLayout_33.addWidget(self.btn_OSC_CH2_EN)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_33)


        self.verticalLayout_14.addLayout(self.horizontalLayout_26)

        self.widget_OSC_main = QWidget(self.frame_17)
        self.widget_OSC_main.setObjectName(u"widget_OSC_main")
        self.widget_OSC_main.setMinimumSize(QSize(1080, 600))
        self.widget_OSC_main.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid rgb(98, 98, 98);\n"
"background-color: rgb(0, 0, 0);")

        self.verticalLayout_14.addWidget(self.widget_OSC_main)

        self.frame_43 = QFrame(self.frame_17)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMaximumSize(QSize(16777215, 110))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_43)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.frame_28 = QFrame(self.frame_43)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 40))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_28)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(-1, -1, 189, 42))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lb_Port_17 = QLabel(self.layoutWidget)
        self.lb_Port_17.setObjectName(u"lb_Port_17")
        self.lb_Port_17.setEnabled(False)
        self.lb_Port_17.setMinimumSize(QSize(10, 40))
        self.lb_Port_17.setStyleSheet(u"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"color: rgb(255, 255, 127);")
        self.lb_Port_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.lb_Port_17)

        self.com_CH1_Date1 = QComboBox(self.layoutWidget)
        self.com_CH1_Date1.addItem("")
        self.com_CH1_Date1.addItem("")
        self.com_CH1_Date1.addItem("")
        self.com_CH1_Date1.addItem("")
        self.com_CH1_Date1.addItem("")
        self.com_CH1_Date1.addItem("")
        self.com_CH1_Date1.addItem("")
        self.com_CH1_Date1.setObjectName(u"com_CH1_Date1")
        self.com_CH1_Date1.setMinimumSize(QSize(80, 40))
        self.com_CH1_Date1.setCursor(QCursor(Qt.PointingHandCursor))
        self.com_CH1_Date1.setMouseTracking(True)
        self.com_CH1_Date1.setStyleSheet(u" QComboBox QAbstractItemView{\n"
"	background-color: rgb(33, 37, 43);\n"
"    border-radius:5px 5px 5px 5px;\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"	font-size:14px;\n"
" }\n"
" QComboBox{\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"	border-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 127);\n"
"}\n"
"  QComboBox::drop-down {\n"
"      width: 0px;\n"
"      border:none;\n"
"  }")

        self.horizontalLayout_9.addWidget(self.com_CH1_Date1)

        self.lb_CH1_Date1 = QLabel(self.layoutWidget)
        self.lb_CH1_Date1.setObjectName(u"lb_CH1_Date1")
        self.lb_CH1_Date1.setEnabled(False)
        self.lb_CH1_Date1.setMinimumSize(QSize(85, 40))
        self.lb_CH1_Date1.setStyleSheet(u"color: rgb(255, 255, 127);\n"
"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_CH1_Date1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.lb_CH1_Date1)


        self.horizontalLayout_55.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_43)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 40))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.layoutWidget_2 = QWidget(self.frame_29)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(-1, -1, 189, 42))
        self.horizontalLayout_30 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.lb_Port_20 = QLabel(self.layoutWidget_2)
        self.lb_Port_20.setObjectName(u"lb_Port_20")
        self.lb_Port_20.setEnabled(False)
        self.lb_Port_20.setMinimumSize(QSize(10, 40))
        self.lb_Port_20.setStyleSheet(u"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"color: rgb(255, 255, 127);")
        self.lb_Port_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.lb_Port_20)

        self.com_CH1_Date2 = QComboBox(self.layoutWidget_2)
        self.com_CH1_Date2.addItem("")
        self.com_CH1_Date2.addItem("")
        self.com_CH1_Date2.addItem("")
        self.com_CH1_Date2.addItem("")
        self.com_CH1_Date2.addItem("")
        self.com_CH1_Date2.addItem("")
        self.com_CH1_Date2.addItem("")
        self.com_CH1_Date2.setObjectName(u"com_CH1_Date2")
        self.com_CH1_Date2.setMinimumSize(QSize(80, 40))
        self.com_CH1_Date2.setCursor(QCursor(Qt.PointingHandCursor))
        self.com_CH1_Date2.setMouseTracking(True)
        self.com_CH1_Date2.setStyleSheet(u" QComboBox QAbstractItemView{\n"
"	background-color: rgb(33, 37, 43);\n"
"    border-radius:5px 5px 5px 5px;\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"	font-size:14px;\n"
" }\n"
" QComboBox{\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"	border-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 127);\n"
"}\n"
"  QComboBox::drop-down {\n"
"      width: 0px;\n"
"      border:none;\n"
"  }")

        self.horizontalLayout_30.addWidget(self.com_CH1_Date2)

        self.lb_CH1_Date2 = QLabel(self.layoutWidget_2)
        self.lb_CH1_Date2.setObjectName(u"lb_CH1_Date2")
        self.lb_CH1_Date2.setEnabled(False)
        self.lb_CH1_Date2.setMinimumSize(QSize(85, 40))
        self.lb_CH1_Date2.setStyleSheet(u"color: rgb(255, 255, 127);\n"
"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_CH1_Date2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.lb_CH1_Date2)


        self.horizontalLayout_55.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_43)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 40))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.layoutWidget_3 = QWidget(self.frame_30)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(-1, -1, 189, 42))
        self.horizontalLayout_31 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.lb_Port_22 = QLabel(self.layoutWidget_3)
        self.lb_Port_22.setObjectName(u"lb_Port_22")
        self.lb_Port_22.setEnabled(False)
        self.lb_Port_22.setMinimumSize(QSize(10, 40))
        self.lb_Port_22.setStyleSheet(u"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"color: rgb(255, 255, 127);")
        self.lb_Port_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.lb_Port_22)

        self.com_CH1_Date3 = QComboBox(self.layoutWidget_3)
        self.com_CH1_Date3.addItem("")
        self.com_CH1_Date3.addItem("")
        self.com_CH1_Date3.addItem("")
        self.com_CH1_Date3.addItem("")
        self.com_CH1_Date3.addItem("")
        self.com_CH1_Date3.addItem("")
        self.com_CH1_Date3.addItem("")
        self.com_CH1_Date3.setObjectName(u"com_CH1_Date3")
        self.com_CH1_Date3.setMinimumSize(QSize(80, 40))
        self.com_CH1_Date3.setCursor(QCursor(Qt.PointingHandCursor))
        self.com_CH1_Date3.setMouseTracking(True)
        self.com_CH1_Date3.setStyleSheet(u" QComboBox QAbstractItemView{\n"
"	background-color: rgb(33, 37, 43);\n"
"    border-radius:5px 5px 5px 5px;\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"	font-size:14px;\n"
" }\n"
" QComboBox{\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"	border-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 127);\n"
"}\n"
"  QComboBox::drop-down {\n"
"      width: 0px;\n"
"      border:none;\n"
"  }")

        self.horizontalLayout_31.addWidget(self.com_CH1_Date3)

        self.lb_CH1_Date3 = QLabel(self.layoutWidget_3)
        self.lb_CH1_Date3.setObjectName(u"lb_CH1_Date3")
        self.lb_CH1_Date3.setEnabled(False)
        self.lb_CH1_Date3.setMinimumSize(QSize(85, 40))
        self.lb_CH1_Date3.setStyleSheet(u"color: rgb(255, 255, 127);\n"
"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_CH1_Date3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.lb_CH1_Date3)


        self.horizontalLayout_55.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_43)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(0, 40))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.layoutWidget_4 = QWidget(self.frame_31)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(-1, -1, 189, 42))
        self.horizontalLayout_32 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.lb_Port_24 = QLabel(self.layoutWidget_4)
        self.lb_Port_24.setObjectName(u"lb_Port_24")
        self.lb_Port_24.setEnabled(False)
        self.lb_Port_24.setMinimumSize(QSize(10, 40))
        self.lb_Port_24.setStyleSheet(u"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"color: rgb(255, 255, 127);")
        self.lb_Port_24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.lb_Port_24)

        self.com_CH1_Date4 = QComboBox(self.layoutWidget_4)
        self.com_CH1_Date4.addItem("")
        self.com_CH1_Date4.addItem("")
        self.com_CH1_Date4.addItem("")
        self.com_CH1_Date4.addItem("")
        self.com_CH1_Date4.addItem("")
        self.com_CH1_Date4.addItem("")
        self.com_CH1_Date4.addItem("")
        self.com_CH1_Date4.setObjectName(u"com_CH1_Date4")
        self.com_CH1_Date4.setMinimumSize(QSize(80, 40))
        self.com_CH1_Date4.setCursor(QCursor(Qt.PointingHandCursor))
        self.com_CH1_Date4.setMouseTracking(True)
        self.com_CH1_Date4.setStyleSheet(u" QComboBox QAbstractItemView{\n"
"	background-color: rgb(33, 37, 43);\n"
"    border-radius:5px 5px 5px 5px;\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"	font-size:14px;\n"
" }\n"
" QComboBox{\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"	border-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 127);\n"
"}\n"
"  QComboBox::drop-down {\n"
"      width: 0px;\n"
"      border:none;\n"
"  }")

        self.horizontalLayout_32.addWidget(self.com_CH1_Date4)

        self.lb_CH1_Date4 = QLabel(self.layoutWidget_4)
        self.lb_CH1_Date4.setObjectName(u"lb_CH1_Date4")
        self.lb_CH1_Date4.setEnabled(False)
        self.lb_CH1_Date4.setMinimumSize(QSize(85, 40))
        self.lb_CH1_Date4.setStyleSheet(u"color: rgb(255, 255, 127);\n"
"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_CH1_Date4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.lb_CH1_Date4)


        self.horizontalLayout_55.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_43)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 40))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.layoutWidget_5 = QWidget(self.frame_32)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(-1, -1, 189, 42))
        self.horizontalLayout_43 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.lb_Port_26 = QLabel(self.layoutWidget_5)
        self.lb_Port_26.setObjectName(u"lb_Port_26")
        self.lb_Port_26.setEnabled(False)
        self.lb_Port_26.setMinimumSize(QSize(10, 40))
        self.lb_Port_26.setStyleSheet(u"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"color: rgb(255, 255, 127);")
        self.lb_Port_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_43.addWidget(self.lb_Port_26)

        self.com_CH1_Date5 = QComboBox(self.layoutWidget_5)
        self.com_CH1_Date5.addItem("")
        self.com_CH1_Date5.addItem("")
        self.com_CH1_Date5.addItem("")
        self.com_CH1_Date5.addItem("")
        self.com_CH1_Date5.addItem("")
        self.com_CH1_Date5.addItem("")
        self.com_CH1_Date5.addItem("")
        self.com_CH1_Date5.setObjectName(u"com_CH1_Date5")
        self.com_CH1_Date5.setMinimumSize(QSize(80, 40))
        self.com_CH1_Date5.setCursor(QCursor(Qt.PointingHandCursor))
        self.com_CH1_Date5.setMouseTracking(True)
        self.com_CH1_Date5.setStyleSheet(u" QComboBox QAbstractItemView{\n"
"	background-color: rgb(33, 37, 43);\n"
"    border-radius:5px 5px 5px 5px;\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"	font-size:14px;\n"
" }\n"
" QComboBox{\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"	border-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 127);\n"
"}\n"
"  QComboBox::drop-down {\n"
"      width: 0px;\n"
"      border:none;\n"
"  }")

        self.horizontalLayout_43.addWidget(self.com_CH1_Date5)

        self.lb_CH1_Date5 = QLabel(self.layoutWidget_5)
        self.lb_CH1_Date5.setObjectName(u"lb_CH1_Date5")
        self.lb_CH1_Date5.setEnabled(False)
        self.lb_CH1_Date5.setMinimumSize(QSize(85, 40))
        self.lb_CH1_Date5.setStyleSheet(u"color: rgb(255, 255, 127);\n"
"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_CH1_Date5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_43.addWidget(self.lb_CH1_Date5)


        self.horizontalLayout_55.addWidget(self.frame_32)


        self.verticalLayout_7.addLayout(self.horizontalLayout_55)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.frame_38 = QFrame(self.frame_43)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(0, 40))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.layoutWidget_12 = QWidget(self.frame_38)
        self.layoutWidget_12.setObjectName(u"layoutWidget_12")
        self.layoutWidget_12.setGeometry(QRect(-1, -1, 189, 42))
        self.horizontalLayout_76 = QHBoxLayout(self.layoutWidget_12)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.lb_Port_38 = QLabel(self.layoutWidget_12)
        self.lb_Port_38.setObjectName(u"lb_Port_38")
        self.lb_Port_38.setEnabled(False)
        self.lb_Port_38.setMinimumSize(QSize(10, 40))
        self.lb_Port_38.setStyleSheet(u"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"color: rgb(0, 85, 255);")
        self.lb_Port_38.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_76.addWidget(self.lb_Port_38)

        self.com_CH2_Date1 = QComboBox(self.layoutWidget_12)
        self.com_CH2_Date1.addItem("")
        self.com_CH2_Date1.addItem("")
        self.com_CH2_Date1.addItem("")
        self.com_CH2_Date1.addItem("")
        self.com_CH2_Date1.addItem("")
        self.com_CH2_Date1.addItem("")
        self.com_CH2_Date1.addItem("")
        self.com_CH2_Date1.setObjectName(u"com_CH2_Date1")
        self.com_CH2_Date1.setMinimumSize(QSize(80, 40))
        self.com_CH2_Date1.setCursor(QCursor(Qt.PointingHandCursor))
        self.com_CH2_Date1.setMouseTracking(True)
        self.com_CH2_Date1.setStyleSheet(u" QComboBox QAbstractItemView{\n"
"	background-color: rgb(33, 37, 43);\n"
"    border-radius:5px 5px 5px 5px;\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"	font-size:14px;\n"
" }\n"
" QComboBox{\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"	border-color: rgb(0, 0, 0);\n"
"	color: rgb(0, 85, 255);\n"
"}\n"
"  QComboBox::drop-down {\n"
"      width: 0px;\n"
"      border:none;\n"
"  }")

        self.horizontalLayout_76.addWidget(self.com_CH2_Date1)

        self.lb_CH2_Date1 = QLabel(self.layoutWidget_12)
        self.lb_CH2_Date1.setObjectName(u"lb_CH2_Date1")
        self.lb_CH2_Date1.setEnabled(False)
        self.lb_CH2_Date1.setMinimumSize(QSize(85, 40))
        self.lb_CH2_Date1.setStyleSheet(u"color: rgb(0, 85, 255);\n"
"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_CH2_Date1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_76.addWidget(self.lb_CH2_Date1)


        self.horizontalLayout_75.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_43)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(0, 40))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.layoutWidget_13 = QWidget(self.frame_39)
        self.layoutWidget_13.setObjectName(u"layoutWidget_13")
        self.layoutWidget_13.setGeometry(QRect(-1, -1, 189, 42))
        self.horizontalLayout_77 = QHBoxLayout(self.layoutWidget_13)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.lb_Port_40 = QLabel(self.layoutWidget_13)
        self.lb_Port_40.setObjectName(u"lb_Port_40")
        self.lb_Port_40.setEnabled(False)
        self.lb_Port_40.setMinimumSize(QSize(10, 40))
        self.lb_Port_40.setStyleSheet(u"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"color: rgb(0, 85, 255);")
        self.lb_Port_40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_77.addWidget(self.lb_Port_40)

        self.com_CH2_Date2 = QComboBox(self.layoutWidget_13)
        self.com_CH2_Date2.addItem("")
        self.com_CH2_Date2.addItem("")
        self.com_CH2_Date2.addItem("")
        self.com_CH2_Date2.addItem("")
        self.com_CH2_Date2.addItem("")
        self.com_CH2_Date2.addItem("")
        self.com_CH2_Date2.addItem("")
        self.com_CH2_Date2.setObjectName(u"com_CH2_Date2")
        self.com_CH2_Date2.setMinimumSize(QSize(80, 40))
        self.com_CH2_Date2.setCursor(QCursor(Qt.PointingHandCursor))
        self.com_CH2_Date2.setMouseTracking(True)
        self.com_CH2_Date2.setStyleSheet(u" QComboBox QAbstractItemView{\n"
"	background-color: rgb(33, 37, 43);\n"
"    border-radius:5px 5px 5px 5px;\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"	font-size:14px;\n"
" }\n"
" QComboBox{\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"	border-color: rgb(0, 0, 0);\n"
"	color: rgb(0, 85, 255);\n"
"}\n"
"  QComboBox::drop-down {\n"
"      width: 0px;\n"
"      border:none;\n"
"  }")

        self.horizontalLayout_77.addWidget(self.com_CH2_Date2)

        self.lb_CH2_Date2 = QLabel(self.layoutWidget_13)
        self.lb_CH2_Date2.setObjectName(u"lb_CH2_Date2")
        self.lb_CH2_Date2.setEnabled(False)
        self.lb_CH2_Date2.setMinimumSize(QSize(85, 40))
        self.lb_CH2_Date2.setStyleSheet(u"color: rgb(0, 85, 255);\n"
"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_CH2_Date2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_77.addWidget(self.lb_CH2_Date2)


        self.horizontalLayout_75.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.frame_43)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(0, 40))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.layoutWidget_14 = QWidget(self.frame_40)
        self.layoutWidget_14.setObjectName(u"layoutWidget_14")
        self.layoutWidget_14.setGeometry(QRect(-1, -1, 189, 42))
        self.horizontalLayout_78 = QHBoxLayout(self.layoutWidget_14)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.lb_Port_42 = QLabel(self.layoutWidget_14)
        self.lb_Port_42.setObjectName(u"lb_Port_42")
        self.lb_Port_42.setEnabled(False)
        self.lb_Port_42.setMinimumSize(QSize(10, 40))
        self.lb_Port_42.setStyleSheet(u"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"color: rgb(0, 85, 255);")
        self.lb_Port_42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_78.addWidget(self.lb_Port_42)

        self.com_CH2_Date3 = QComboBox(self.layoutWidget_14)
        self.com_CH2_Date3.addItem("")
        self.com_CH2_Date3.addItem("")
        self.com_CH2_Date3.addItem("")
        self.com_CH2_Date3.addItem("")
        self.com_CH2_Date3.addItem("")
        self.com_CH2_Date3.addItem("")
        self.com_CH2_Date3.addItem("")
        self.com_CH2_Date3.setObjectName(u"com_CH2_Date3")
        self.com_CH2_Date3.setMinimumSize(QSize(80, 40))
        self.com_CH2_Date3.setCursor(QCursor(Qt.PointingHandCursor))
        self.com_CH2_Date3.setMouseTracking(True)
        self.com_CH2_Date3.setStyleSheet(u" QComboBox QAbstractItemView{\n"
"	background-color: rgb(33, 37, 43);\n"
"    border-radius:5px 5px 5px 5px;\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"	font-size:14px;\n"
" }\n"
" QComboBox{\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"	border-color: rgb(0, 0, 0);\n"
"	color: rgb(0, 85, 255);\n"
"}\n"
"  QComboBox::drop-down {\n"
"      width: 0px;\n"
"      border:none;\n"
"  }")

        self.horizontalLayout_78.addWidget(self.com_CH2_Date3)

        self.lb_CH2_Date3 = QLabel(self.layoutWidget_14)
        self.lb_CH2_Date3.setObjectName(u"lb_CH2_Date3")
        self.lb_CH2_Date3.setEnabled(False)
        self.lb_CH2_Date3.setMinimumSize(QSize(85, 40))
        self.lb_CH2_Date3.setStyleSheet(u"color: rgb(0, 85, 255);\n"
"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_CH2_Date3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_78.addWidget(self.lb_CH2_Date3)


        self.horizontalLayout_75.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.frame_43)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(0, 40))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.layoutWidget_15 = QWidget(self.frame_41)
        self.layoutWidget_15.setObjectName(u"layoutWidget_15")
        self.layoutWidget_15.setGeometry(QRect(-1, -1, 189, 42))
        self.horizontalLayout_79 = QHBoxLayout(self.layoutWidget_15)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.lb_Port_44 = QLabel(self.layoutWidget_15)
        self.lb_Port_44.setObjectName(u"lb_Port_44")
        self.lb_Port_44.setEnabled(False)
        self.lb_Port_44.setMinimumSize(QSize(10, 40))
        self.lb_Port_44.setStyleSheet(u"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"color: rgb(0, 85, 255);")
        self.lb_Port_44.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_79.addWidget(self.lb_Port_44)

        self.com_CH2_Date4 = QComboBox(self.layoutWidget_15)
        self.com_CH2_Date4.addItem("")
        self.com_CH2_Date4.addItem("")
        self.com_CH2_Date4.addItem("")
        self.com_CH2_Date4.addItem("")
        self.com_CH2_Date4.addItem("")
        self.com_CH2_Date4.addItem("")
        self.com_CH2_Date4.addItem("")
        self.com_CH2_Date4.setObjectName(u"com_CH2_Date4")
        self.com_CH2_Date4.setMinimumSize(QSize(80, 40))
        self.com_CH2_Date4.setCursor(QCursor(Qt.PointingHandCursor))
        self.com_CH2_Date4.setMouseTracking(True)
        self.com_CH2_Date4.setStyleSheet(u" QComboBox QAbstractItemView{\n"
"	background-color: rgb(33, 37, 43);\n"
"    border-radius:5px 5px 5px 5px;\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"	font-size:14px;\n"
" }\n"
" QComboBox{\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"	border-color: rgb(0, 0, 0);\n"
"	color: rgb(0, 85, 255);\n"
"}\n"
"  QComboBox::drop-down {\n"
"      width: 0px;\n"
"      border:none;\n"
"  }")

        self.horizontalLayout_79.addWidget(self.com_CH2_Date4)

        self.lb_CH2_Date4 = QLabel(self.layoutWidget_15)
        self.lb_CH2_Date4.setObjectName(u"lb_CH2_Date4")
        self.lb_CH2_Date4.setEnabled(False)
        self.lb_CH2_Date4.setMinimumSize(QSize(85, 40))
        self.lb_CH2_Date4.setStyleSheet(u"color: rgb(0, 85, 255);\n"
"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_CH2_Date4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_79.addWidget(self.lb_CH2_Date4)


        self.horizontalLayout_75.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_43)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(0, 40))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.layoutWidget_16 = QWidget(self.frame_42)
        self.layoutWidget_16.setObjectName(u"layoutWidget_16")
        self.layoutWidget_16.setGeometry(QRect(-1, -1, 189, 42))
        self.horizontalLayout_80 = QHBoxLayout(self.layoutWidget_16)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.lb_Port_46 = QLabel(self.layoutWidget_16)
        self.lb_Port_46.setObjectName(u"lb_Port_46")
        self.lb_Port_46.setEnabled(False)
        self.lb_Port_46.setMinimumSize(QSize(10, 40))
        self.lb_Port_46.setStyleSheet(u"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"color: rgb(0, 85, 255);")
        self.lb_Port_46.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_80.addWidget(self.lb_Port_46)

        self.com_CH2_Date5 = QComboBox(self.layoutWidget_16)
        self.com_CH2_Date5.addItem("")
        self.com_CH2_Date5.addItem("")
        self.com_CH2_Date5.addItem("")
        self.com_CH2_Date5.addItem("")
        self.com_CH2_Date5.addItem("")
        self.com_CH2_Date5.addItem("")
        self.com_CH2_Date5.addItem("")
        self.com_CH2_Date5.setObjectName(u"com_CH2_Date5")
        self.com_CH2_Date5.setMinimumSize(QSize(80, 40))
        self.com_CH2_Date5.setCursor(QCursor(Qt.PointingHandCursor))
        self.com_CH2_Date5.setMouseTracking(True)
        self.com_CH2_Date5.setStyleSheet(u" QComboBox QAbstractItemView{\n"
"	background-color: rgb(33, 37, 43);\n"
"    border-radius:5px 5px 5px 5px;\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"	font-size:14px;\n"
" }\n"
" QComboBox{\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"	border-color: rgb(0, 0, 0);\n"
"	color: rgb(0, 85, 255);\n"
"}\n"
"  QComboBox::drop-down {\n"
"      width: 0px;\n"
"      border:none;\n"
"  }")

        self.horizontalLayout_80.addWidget(self.com_CH2_Date5)

        self.lb_CH2_Date5 = QLabel(self.layoutWidget_16)
        self.lb_CH2_Date5.setObjectName(u"lb_CH2_Date5")
        self.lb_CH2_Date5.setEnabled(False)
        self.lb_CH2_Date5.setMinimumSize(QSize(85, 40))
        self.lb_CH2_Date5.setStyleSheet(u"color: rgb(0, 85, 255);\n"
"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_CH2_Date5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_80.addWidget(self.lb_CH2_Date5)


        self.horizontalLayout_75.addWidget(self.frame_42)


        self.verticalLayout_7.addLayout(self.horizontalLayout_75)


        self.verticalLayout_13.addLayout(self.verticalLayout_7)


        self.verticalLayout_14.addWidget(self.frame_43)


        self.verticalLayout_16.addLayout(self.verticalLayout_14)


        self.horizontalLayout_81.addWidget(self.frame_17)

        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.frame_24 = QFrame(self.frame)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid rgb(33, 37, 43);")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_24)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.lb_Port_12 = QLabel(self.frame_24)
        self.lb_Port_12.setObjectName(u"lb_Port_12")
        self.lb_Port_12.setEnabled(False)
        self.lb_Port_12.setMinimumSize(QSize(120, 25))
        self.lb_Port_12.setStyleSheet(u"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_Port_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.lb_Port_12)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_3)

        self.lb_OSC_Horizontal = QLabel(self.frame_24)
        self.lb_OSC_Horizontal.setObjectName(u"lb_OSC_Horizontal")
        self.lb_OSC_Horizontal.setEnabled(False)
        self.lb_OSC_Horizontal.setMinimumSize(QSize(120, 35))
        self.lb_OSC_Horizontal.setStyleSheet(u"border: 0px;\n"
"font: 18pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"color: rgb(189, 147, 249);")
        self.lb_OSC_Horizontal.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.lb_OSC_Horizontal)


        self.horizontalLayout_57.addLayout(self.verticalLayout_27)

        self.dial_OSC_Horizontal = QDial(self.frame_24)
        self.dial_OSC_Horizontal.setObjectName(u"dial_OSC_Horizontal")
        self.dial_OSC_Horizontal.setEnabled(True)
        self.dial_OSC_Horizontal.setMouseTracking(False)

        self.horizontalLayout_57.addWidget(self.dial_OSC_Horizontal)


        self.verticalLayout_34.addLayout(self.horizontalLayout_57)


        self.verticalLayout_45.addWidget(self.frame_24)

        self.frame_27 = QFrame(self.frame)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid rgb(33, 37, 43);")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_27)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.lb_Port_9 = QLabel(self.frame_27)
        self.lb_Port_9.setObjectName(u"lb_Port_9")
        self.lb_Port_9.setEnabled(False)
        self.lb_Port_9.setMinimumSize(QSize(120, 25))
        self.lb_Port_9.setStyleSheet(u"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_Port_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.lb_Port_9)

        self.lb_Port_10 = QLabel(self.frame_27)
        self.lb_Port_10.setObjectName(u"lb_Port_10")
        self.lb_Port_10.setEnabled(False)
        self.lb_Port_10.setMinimumSize(QSize(120, 25))
        self.lb_Port_10.setStyleSheet(u"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_Port_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.lb_Port_10)

        self.lb_OSC_Vertical_CH1 = QLabel(self.frame_27)
        self.lb_OSC_Vertical_CH1.setObjectName(u"lb_OSC_Vertical_CH1")
        self.lb_OSC_Vertical_CH1.setEnabled(False)
        self.lb_OSC_Vertical_CH1.setMinimumSize(QSize(120, 35))
        self.lb_OSC_Vertical_CH1.setStyleSheet(u"border: 0px;\n"
"font: 18pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"color: rgb(189, 147, 249);")
        self.lb_OSC_Vertical_CH1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.lb_OSC_Vertical_CH1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_37.addItem(self.verticalSpacer_4)

        self.lb_Port_11 = QLabel(self.frame_27)
        self.lb_Port_11.setObjectName(u"lb_Port_11")
        self.lb_Port_11.setEnabled(False)
        self.lb_Port_11.setMinimumSize(QSize(120, 25))
        self.lb_Port_11.setStyleSheet(u"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_Port_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.lb_Port_11)

        self.lb_OSC_Vertical_CH2 = QLabel(self.frame_27)
        self.lb_OSC_Vertical_CH2.setObjectName(u"lb_OSC_Vertical_CH2")
        self.lb_OSC_Vertical_CH2.setEnabled(False)
        self.lb_OSC_Vertical_CH2.setMinimumSize(QSize(120, 35))
        self.lb_OSC_Vertical_CH2.setStyleSheet(u"border: 0px;\n"
"font: 18pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"color: rgb(189, 147, 249);")
        self.lb_OSC_Vertical_CH2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.lb_OSC_Vertical_CH2)


        self.horizontalLayout_65.addLayout(self.verticalLayout_37)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.dial_OSC_Vertical_CH1 = QDial(self.frame_27)
        self.dial_OSC_Vertical_CH1.setObjectName(u"dial_OSC_Vertical_CH1")
        self.dial_OSC_Vertical_CH1.setEnabled(True)
        self.dial_OSC_Vertical_CH1.setMouseTracking(False)
        self.dial_OSC_Vertical_CH1.setMaximum(9)
        self.dial_OSC_Vertical_CH1.setSingleStep(1)
        self.dial_OSC_Vertical_CH1.setPageStep(1)
        self.dial_OSC_Vertical_CH1.setTracking(True)
        self.dial_OSC_Vertical_CH1.setWrapping(False)

        self.verticalLayout_38.addWidget(self.dial_OSC_Vertical_CH1)

        self.dial_OSC_Vertical_CH2 = QDial(self.frame_27)
        self.dial_OSC_Vertical_CH2.setObjectName(u"dial_OSC_Vertical_CH2")
        self.dial_OSC_Vertical_CH2.setEnabled(True)
        self.dial_OSC_Vertical_CH2.setMouseTracking(False)
        self.dial_OSC_Vertical_CH2.setMaximum(9)
        self.dial_OSC_Vertical_CH2.setPageStep(1)

        self.verticalLayout_38.addWidget(self.dial_OSC_Vertical_CH2)


        self.horizontalLayout_65.addLayout(self.verticalLayout_38)


        self.verticalLayout_39.addLayout(self.horizontalLayout_65)


        self.verticalLayout_45.addWidget(self.frame_27)

        self.frame_26 = QFrame(self.frame)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid rgb(33, 37, 43);")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_26)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.lb_Port_4 = QLabel(self.frame_26)
        self.lb_Port_4.setObjectName(u"lb_Port_4")
        self.lb_Port_4.setEnabled(False)
        self.lb_Port_4.setMinimumSize(QSize(120, 25))
        self.lb_Port_4.setStyleSheet(u"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_Port_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.lb_Port_4)

        self.lb_Port_5 = QLabel(self.frame_26)
        self.lb_Port_5.setObjectName(u"lb_Port_5")
        self.lb_Port_5.setEnabled(False)
        self.lb_Port_5.setMinimumSize(QSize(120, 25))
        self.lb_Port_5.setStyleSheet(u"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_Port_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.lb_Port_5)

        self.lb_OSC_Offset_CH1 = QLabel(self.frame_26)
        self.lb_OSC_Offset_CH1.setObjectName(u"lb_OSC_Offset_CH1")
        self.lb_OSC_Offset_CH1.setEnabled(False)
        self.lb_OSC_Offset_CH1.setMinimumSize(QSize(120, 35))
        self.lb_OSC_Offset_CH1.setStyleSheet(u"border: 0px;\n"
"font: 18pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"color: rgb(189, 147, 249);")
        self.lb_OSC_Offset_CH1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.lb_OSC_Offset_CH1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_40.addItem(self.verticalSpacer_5)

        self.lb_Port_6 = QLabel(self.frame_26)
        self.lb_Port_6.setObjectName(u"lb_Port_6")
        self.lb_Port_6.setEnabled(False)
        self.lb_Port_6.setMinimumSize(QSize(120, 25))
        self.lb_Port_6.setStyleSheet(u"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_Port_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.lb_Port_6)

        self.lb_OSC_Offset_CH2 = QLabel(self.frame_26)
        self.lb_OSC_Offset_CH2.setObjectName(u"lb_OSC_Offset_CH2")
        self.lb_OSC_Offset_CH2.setEnabled(False)
        self.lb_OSC_Offset_CH2.setMinimumSize(QSize(120, 35))
        self.lb_OSC_Offset_CH2.setStyleSheet(u"border: 0px;\n"
"font: 18pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"color: rgb(189, 147, 249);")
        self.lb_OSC_Offset_CH2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.lb_OSC_Offset_CH2)


        self.horizontalLayout_66.addLayout(self.verticalLayout_40)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.dial_OSC_Offset_CH1 = QDial(self.frame_26)
        self.dial_OSC_Offset_CH1.setObjectName(u"dial_OSC_Offset_CH1")
        self.dial_OSC_Offset_CH1.setEnabled(True)
        self.dial_OSC_Offset_CH1.setMouseTracking(False)
        self.dial_OSC_Offset_CH1.setMaximum(200)
        self.dial_OSC_Offset_CH1.setPageStep(10)

        self.verticalLayout_41.addWidget(self.dial_OSC_Offset_CH1)

        self.dial_OSC_Offset_CH2 = QDial(self.frame_26)
        self.dial_OSC_Offset_CH2.setObjectName(u"dial_OSC_Offset_CH2")
        self.dial_OSC_Offset_CH2.setEnabled(True)
        self.dial_OSC_Offset_CH2.setMouseTracking(False)
        self.dial_OSC_Offset_CH2.setMaximum(200)

        self.verticalLayout_41.addWidget(self.dial_OSC_Offset_CH2)


        self.horizontalLayout_66.addLayout(self.verticalLayout_41)


        self.verticalLayout_42.addLayout(self.horizontalLayout_66)


        self.verticalLayout_45.addWidget(self.frame_26)

        self.frame_25 = QFrame(self.frame)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid rgb(33, 37, 43);")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_25)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.lb_Port_16 = QLabel(self.frame_25)
        self.lb_Port_16.setObjectName(u"lb_Port_16")
        self.lb_Port_16.setEnabled(False)
        self.lb_Port_16.setMinimumSize(QSize(120, 35))
        self.lb_Port_16.setStyleSheet(u"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_Port_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_67.addWidget(self.lb_Port_16)

        self.com_Trigger_Channal = QComboBox(self.frame_25)
        self.com_Trigger_Channal.addItem("")
        self.com_Trigger_Channal.addItem("")
        self.com_Trigger_Channal.setObjectName(u"com_Trigger_Channal")
        self.com_Trigger_Channal.setMinimumSize(QSize(100, 35))
        self.com_Trigger_Channal.setCursor(QCursor(Qt.PointingHandCursor))
        self.com_Trigger_Channal.setStyleSheet(u" QComboBox QAbstractItemView{\n"
"	background-color: rgb(33, 37, 43);\n"
"    border-radius:5px 5px 5px 5px;\n"
"	font-size:14px;\n"
" }")

        self.horizontalLayout_67.addWidget(self.com_Trigger_Channal)


        self.verticalLayout_43.addLayout(self.horizontalLayout_67)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.lb_Port_14 = QLabel(self.frame_25)
        self.lb_Port_14.setObjectName(u"lb_Port_14")
        self.lb_Port_14.setEnabled(False)
        self.lb_Port_14.setMinimumSize(QSize(120, 35))
        self.lb_Port_14.setStyleSheet(u"border: 0px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_Port_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_68.addWidget(self.lb_Port_14)

        self.com_Trigger_Way = QComboBox(self.frame_25)
        self.com_Trigger_Way.addItem("")
        self.com_Trigger_Way.addItem("")
        self.com_Trigger_Way.setObjectName(u"com_Trigger_Way")
        self.com_Trigger_Way.setMinimumSize(QSize(100, 35))
        self.com_Trigger_Way.setCursor(QCursor(Qt.PointingHandCursor))
        self.com_Trigger_Way.setStyleSheet(u" QComboBox QAbstractItemView{\n"
"	background-color: rgb(33, 37, 43);\n"
"    border-radius:5px 5px 5px 5px;\n"
"	font-size:14px;\n"
" }")

        self.horizontalLayout_68.addWidget(self.com_Trigger_Way)


        self.verticalLayout_43.addLayout(self.horizontalLayout_68)


        self.verticalLayout_44.addLayout(self.verticalLayout_43)


        self.verticalLayout_45.addWidget(self.frame_25)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.btn_Screenshot = QPushButton(self.frame)
        self.btn_Screenshot.setObjectName(u"btn_Screenshot")
        self.btn_Screenshot.setMinimumSize(QSize(115, 50))
        self.btn_Screenshot.setMaximumSize(QSize(115, 16777215))
        self.btn_Screenshot.setStyleSheet(u"QPushButton:hover {\n"
"	color: white;\n"
"	border: 2px solid white;\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"}\n"
"QPushButton:pressed {\n"
"	/*color: white;*/\n"
"	background-color:rgb(31, 31, 31);\n"
"	border-style: inset;\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"}\n"
"QPushButton\n"
"{\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"}")

        self.horizontalLayout_69.addWidget(self.btn_Screenshot)

        self.btn_Run_Stop = QPushButton(self.frame)
        self.btn_Run_Stop.setObjectName(u"btn_Run_Stop")
        self.btn_Run_Stop.setMinimumSize(QSize(115, 50))
        self.btn_Run_Stop.setMaximumSize(QSize(115, 16777215))
        self.btn_Run_Stop.setStyleSheet(u"QPushButton:hover {\n"
"	color: white;\n"
"	border: 2px solid white;\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"}\n"
"QPushButton:pressed {\n"
"	/*color: white;*/\n"
"	background-color:rgb(31, 31, 31);\n"
"	border-style: inset;\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"}\n"
"QPushButton\n"
"{\n"
"	font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"}")

        self.horizontalLayout_69.addWidget(self.btn_Run_Stop)


        self.verticalLayout_45.addLayout(self.horizontalLayout_69)


        self.horizontalLayout_81.addLayout(self.verticalLayout_45)


        self.verticalLayout_19.addLayout(self.horizontalLayout_81)


        self.verticalLayout.addWidget(self.frame)

        self.stackedWidget.addWidget(self.Page_OSC)
        self.Page_UART = QWidget()
        self.Page_UART.setObjectName(u"Page_UART")
        self.horizontalLayout_27 = QHBoxLayout(self.Page_UART)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.frame_12 = QFrame(self.Page_UART)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer_19 = QSpacerItem(230, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_19)

        self.frame_19 = QFrame(self.frame_12)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy4.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy4)
        self.frame_19.setMinimumSize(QSize(100, 40))
        self.frame_19.setMaximumSize(QSize(100, 40))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(9, 0, 30, 0)
        self.info_text_7 = QLabel(self.frame_19)
        self.info_text_7.setObjectName(u"info_text_7")
        self.info_text_7.setMinimumSize(QSize(85, 35))
        self.info_text_7.setFont(font4)
        self.info_text_7.setStyleSheet(u"font: 18pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.info_text_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.info_text_7)


        self.horizontalLayout_34.addWidget(self.frame_19)

        self.horizontalSpacer_20 = QSpacerItem(230, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_20)


        self.verticalLayout_10.addLayout(self.horizontalLayout_34)

        self.Chart_UART = QWidget(self.frame_12)
        self.Chart_UART.setObjectName(u"Chart_UART")
        self.Chart_UART.setMinimumSize(QSize(200, 700))
        self.Chart_UART.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid black;\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.Chart_UART)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)


        self.horizontalLayout_27.addWidget(self.frame_12)

        self.frame_2 = QFrame(self.Page_UART)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(500, 16777215))
        self.frame_2.setStyleSheet(u"QPushButton:hover {\n"
"	color: white;\n"
"	border: 2px solid white;\n"
"	/*padding-left: 15px;*/\n"
"}\n"
"QPushButton:pressed {\n"
"	/*color: white;*/\n"
"	background-color:rgb(31, 31, 31);\n"
"	border-style: inset;\n"
"	/*padding-left: 15px;*/\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(300, 280))
        self.frame_5.setMaximumSize(QSize(16777215, 300))
        self.frame_5.setStyleSheet(u"QComboBox {\n"
"    font-family: \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";\n"
"    font-size: 17px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lb_Port = QLabel(self.frame_5)
        self.lb_Port.setObjectName(u"lb_Port")
        self.lb_Port.setEnabled(False)
        self.lb_Port.setMinimumSize(QSize(120, 35))
        self.lb_Port.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_Port.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.lb_Port)

        self.com_Port = QComboBox(self.frame_5)
        self.com_Port.setObjectName(u"com_Port")
        self.com_Port.setMinimumSize(QSize(120, 35))
        self.com_Port.setCursor(QCursor(Qt.PointingHandCursor))
        self.com_Port.setStyleSheet(u" QComboBox QAbstractItemView{\n"
"	background-color: rgb(33, 37, 43);\n"
"    border-radius:5px 5px 5px 5px;\n"
"	font-size:14px;\n"
" }")

        self.horizontalLayout_13.addWidget(self.com_Port)


        self.verticalLayout_12.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lb_Baud = QLabel(self.frame_5)
        self.lb_Baud.setObjectName(u"lb_Baud")
        self.lb_Baud.setEnabled(False)
        self.lb_Baud.setMinimumSize(QSize(120, 35))
        self.lb_Baud.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_Baud.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.lb_Baud)

        self.com_Baud = QComboBox(self.frame_5)
        self.com_Baud.addItem("")
        self.com_Baud.addItem("")
        self.com_Baud.addItem("")
        self.com_Baud.addItem("")
        self.com_Baud.addItem("")
        self.com_Baud.addItem("")
        self.com_Baud.addItem("")
        self.com_Baud.addItem("")
        self.com_Baud.setObjectName(u"com_Baud")
        self.com_Baud.setMinimumSize(QSize(120, 35))
        self.com_Baud.setCursor(QCursor(Qt.PointingHandCursor))
        self.com_Baud.setStyleSheet(u" QComboBox QAbstractItemView{\n"
"	background-color: rgb(33, 37, 43);\n"
"    border-radius:5px 5px 5px 5px;\n"
"	font-size:14px;\n"
" }")

        self.horizontalLayout_14.addWidget(self.com_Baud)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.lb_Check_bit = QLabel(self.frame_5)
        self.lb_Check_bit.setObjectName(u"lb_Check_bit")
        self.lb_Check_bit.setEnabled(False)
        self.lb_Check_bit.setMinimumSize(QSize(120, 35))
        self.lb_Check_bit.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_Check_bit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.lb_Check_bit)

        self.com_Check_bit = QComboBox(self.frame_5)
        self.com_Check_bit.addItem("")
        self.com_Check_bit.addItem("")
        self.com_Check_bit.addItem("")
        self.com_Check_bit.addItem("")
        self.com_Check_bit.addItem("")
        self.com_Check_bit.setObjectName(u"com_Check_bit")
        self.com_Check_bit.setMinimumSize(QSize(120, 35))
        self.com_Check_bit.setCursor(QCursor(Qt.PointingHandCursor))
        self.com_Check_bit.setStyleSheet(u" QComboBox QAbstractItemView{\n"
"	background-color: rgb(33, 37, 43);\n"
"    border-radius:5px 5px 5px 5px;\n"
"	font-size:14px;\n"
" }\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_37.addWidget(self.com_Check_bit)


        self.verticalLayout_12.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.lb_Stop_bit = QLabel(self.frame_5)
        self.lb_Stop_bit.setObjectName(u"lb_Stop_bit")
        self.lb_Stop_bit.setEnabled(False)
        self.lb_Stop_bit.setMinimumSize(QSize(120, 35))
        self.lb_Stop_bit.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_Stop_bit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.lb_Stop_bit)

        self.com_Stop_bit = QComboBox(self.frame_5)
        self.com_Stop_bit.addItem("")
        self.com_Stop_bit.addItem("")
        self.com_Stop_bit.addItem("")
        self.com_Stop_bit.setObjectName(u"com_Stop_bit")
        self.com_Stop_bit.setMinimumSize(QSize(120, 35))
        self.com_Stop_bit.setCursor(QCursor(Qt.PointingHandCursor))
        self.com_Stop_bit.setStyleSheet(u" QComboBox QAbstractItemView{\n"
"	background-color: rgb(33, 37, 43);\n"
"    border-radius:5px 5px 5px 5px;\n"
"	font-size:14px;\n"
" }")

        self.horizontalLayout_38.addWidget(self.com_Stop_bit)


        self.verticalLayout_12.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.btn_UART_ctrl = QPushButton(self.frame_5)
        self.btn_UART_ctrl.setObjectName(u"btn_UART_ctrl")
        self.btn_UART_ctrl.setMinimumSize(QSize(180, 45))
        self.btn_UART_ctrl.setFont(font2)
        self.btn_UART_ctrl.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_UART_ctrl.setStyleSheet(u"border-radius: 5px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_39.addWidget(self.btn_UART_ctrl)

        self.btn_UART_LED = QPushButton(self.frame_5)
        self.btn_UART_LED.setObjectName(u"btn_UART_LED")
        self.btn_UART_LED.setEnabled(False)
        self.btn_UART_LED.setMinimumSize(QSize(30, 30))
        self.btn_UART_LED.setMaximumSize(QSize(30, 30))
        self.btn_UART_LED.setFont(font)
        self.btn_UART_LED.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_UART_LED.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(220, 0, 0);\n"
"border-color: rgb(173, 0, 0);")

        self.horizontalLayout_39.addWidget(self.btn_UART_LED)


        self.verticalLayout_12.addLayout(self.horizontalLayout_39)

        self.btn_UART_auto = QPushButton(self.frame_5)
        self.btn_UART_auto.setObjectName(u"btn_UART_auto")
        self.btn_UART_auto.setMinimumSize(QSize(180, 45))
        self.btn_UART_auto.setFont(font2)
        self.btn_UART_auto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_UART_auto.setStyleSheet(u"border-radius: 5px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.verticalLayout_12.addWidget(self.btn_UART_auto)


        self.horizontalLayout_40.addLayout(self.verticalLayout_12)


        self.verticalLayout_17.addWidget(self.frame_5)

        self.frame_11 = QFrame(self.frame_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.frame_4 = QFrame(self.frame_11)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(300, 100))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_4)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(False)
        self.label_8.setMinimumSize(QSize(50, 35))
        self.label_8.setMaximumSize(QSize(16777215, 16777215))
        self.label_8.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.label_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer)

        self.cb_Rec_HEX = QCheckBox(self.frame_4)
        self.cb_Rec_HEX.setObjectName(u"cb_Rec_HEX")
        self.cb_Rec_HEX.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.cb_Rec_HEX.sizePolicy().hasHeightForWidth())
        self.cb_Rec_HEX.setSizePolicy(sizePolicy6)
        self.cb_Rec_HEX.setMinimumSize(QSize(100, 0))
        self.cb_Rec_HEX.setMaximumSize(QSize(16777215, 16777215))
        self.cb_Rec_HEX.setLayoutDirection(Qt.LeftToRight)
        self.cb_Rec_HEX.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_36.addWidget(self.cb_Rec_HEX)

        self.btn_Rec_Clear = QPushButton(self.frame_4)
        self.btn_Rec_Clear.setObjectName(u"btn_Rec_Clear")
        self.btn_Rec_Clear.setMinimumSize(QSize(150, 35))
        self.btn_Rec_Clear.setMaximumSize(QSize(16777215, 16777215))
        self.btn_Rec_Clear.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_36.addWidget(self.btn_Rec_Clear)


        self.verticalLayout_29.addLayout(self.horizontalLayout_36)

        self.te_UART_RecTerminal = QTextEdit(self.frame_4)
        self.te_UART_RecTerminal.setObjectName(u"te_UART_RecTerminal")
        self.te_UART_RecTerminal.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.te_UART_RecTerminal.sizePolicy().hasHeightForWidth())
        self.te_UART_RecTerminal.setSizePolicy(sizePolicy3)
        self.te_UART_RecTerminal.setMinimumSize(QSize(200, 150))
        self.te_UART_RecTerminal.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid black;\n"
"background-color: rgb(33, 37, 43);\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.verticalLayout_29.addWidget(self.te_UART_RecTerminal)


        self.verticalLayout_31.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame_11)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(300, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_3)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(False)
        self.label_7.setMinimumSize(QSize(50, 35))
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        self.label_7.setContextMenuPolicy(Qt.NoContextMenu)
        self.label_7.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_7)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)

        self.cb_Send_HEX = QCheckBox(self.frame_3)
        self.cb_Send_HEX.setObjectName(u"cb_Send_HEX")
        self.cb_Send_HEX.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.cb_Send_HEX.sizePolicy().hasHeightForWidth())
        self.cb_Send_HEX.setSizePolicy(sizePolicy6)
        self.cb_Send_HEX.setMinimumSize(QSize(100, 0))
        self.cb_Send_HEX.setMaximumSize(QSize(16777215, 16777215))
        self.cb_Send_HEX.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_11.addWidget(self.cb_Send_HEX)

        self.btn_UART_Send = QPushButton(self.frame_3)
        self.btn_UART_Send.setObjectName(u"btn_UART_Send")
        self.btn_UART_Send.setMinimumSize(QSize(150, 35))
        self.btn_UART_Send.setMaximumSize(QSize(16777215, 16777215))
        self.btn_UART_Send.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_11.addWidget(self.btn_UART_Send)


        self.verticalLayout_32.addLayout(self.horizontalLayout_11)

        self.te_UART_SendTerminal = QTextEdit(self.frame_3)
        self.te_UART_SendTerminal.setObjectName(u"te_UART_SendTerminal")
        sizePolicy3.setHeightForWidth(self.te_UART_SendTerminal.sizePolicy().hasHeightForWidth())
        self.te_UART_SendTerminal.setSizePolicy(sizePolicy3)
        self.te_UART_SendTerminal.setMinimumSize(QSize(200, 50))
        self.te_UART_SendTerminal.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid black;\n"
"background-color: rgb(33, 37, 43);\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.verticalLayout_32.addWidget(self.te_UART_SendTerminal)


        self.verticalLayout_31.addWidget(self.frame_3)


        self.horizontalLayout_41.addLayout(self.verticalLayout_31)


        self.verticalLayout_17.addWidget(self.frame_11)


        self.horizontalLayout_42.addLayout(self.verticalLayout_17)


        self.horizontalLayout_27.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.Page_UART)
        self.Page_DDS = QWidget()
        self.Page_DDS.setObjectName(u"Page_DDS")
        self.verticalLayout_36 = QVBoxLayout(self.Page_DDS)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.Page_DDS)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"QPushButton:hover {\n"
"	color: white;\n"
"	border: 2px solid white;\n"
"	/*padding-left: 15px;*/\n"
"}\n"
"QPushButton:pressed {\n"
"	/*color: white;*/\n"
"	background-color:rgb(31, 31, 31);\n"
"	border-style: inset;\n"
"	/*padding-left: 15px;*/\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy3.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy3)
        self.frame_18.setMinimumSize(QSize(700, 700))
        self.frame_18.setMaximumSize(QSize(16777215, 16777215))
        self.frame_18.setStyleSheet(u"QFrame#frame_18{\n"
"	border: 1px solid #343b48;\n"
"	/*background-color: rgb(126, 199, 193);*/\n"
"	border-radius: 5px;\n"
"}")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_18)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalSpacer_13 = QSpacerItem(230, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_13)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy4.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy4)
        self.frame_20.setMinimumSize(QSize(220, 40))
        self.frame_20.setMaximumSize(QSize(100, 40))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(9, 0, 30, 0)
        self.info_text_4 = QLabel(self.frame_20)
        self.info_text_4.setObjectName(u"info_text_4")
        self.info_text_4.setMinimumSize(QSize(210, 35))
        self.info_text_4.setFont(font4)
        self.info_text_4.setStyleSheet(u"font: 18pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.info_text_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.info_text_4)


        self.horizontalLayout_44.addWidget(self.frame_20)

        self.horizontalSpacer_14 = QSpacerItem(230, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_14)


        self.verticalLayout_20.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.lb_Wavetype = QLabel(self.frame_18)
        self.lb_Wavetype.setObjectName(u"lb_Wavetype")
        self.lb_Wavetype.setEnabled(True)
        self.lb_Wavetype.setMinimumSize(QSize(120, 30))
        self.lb_Wavetype.setMaximumSize(QSize(120, 16777215))
        self.lb_Wavetype.setFont(font2)
        self.lb_Wavetype.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_Wavetype.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.lb_Wavetype)

        self.com_Wavetype = QComboBox(self.frame_18)
        self.com_Wavetype.addItem("")
        self.com_Wavetype.addItem("")
        self.com_Wavetype.addItem("")
        self.com_Wavetype.setObjectName(u"com_Wavetype")
        self.com_Wavetype.setMinimumSize(QSize(120, 35))
        self.com_Wavetype.setCursor(QCursor(Qt.PointingHandCursor))
        self.com_Wavetype.setStyleSheet(u" QComboBox QAbstractItemView{\n"
"	background-color: rgb(33, 37, 43);\n"
"    border-radius:5px 5px 5px 5px;\n"
"	font-size:14px;\n"
" }\n"
" QComboBox {    font-family: \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";    font-size: 17px;}")

        self.horizontalLayout_28.addWidget(self.com_Wavetype)


        self.verticalLayout_20.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(-1, 5, -1, 5)
        self.lb_DDS1_Vpp = QLabel(self.frame_18)
        self.lb_DDS1_Vpp.setObjectName(u"lb_DDS1_Vpp")
        self.lb_DDS1_Vpp.setMinimumSize(QSize(120, 30))
        self.lb_DDS1_Vpp.setMaximumSize(QSize(120, 16777215))
        self.lb_DDS1_Vpp.setFont(font2)
        self.lb_DDS1_Vpp.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_DDS1_Vpp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.lb_DDS1_Vpp)

        self.le_DDS1_Vpp = QLineEdit(self.frame_18)
        self.le_DDS1_Vpp.setObjectName(u"le_DDS1_Vpp")
        self.le_DDS1_Vpp.setMinimumSize(QSize(284, 40))
        self.le_DDS1_Vpp.setFont(font2)
        self.le_DDS1_Vpp.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid black;\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_47.addWidget(self.le_DDS1_Vpp)


        self.verticalLayout_20.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(-1, 5, -1, 5)
        self.lb_DDS1_Duty = QLabel(self.frame_18)
        self.lb_DDS1_Duty.setObjectName(u"lb_DDS1_Duty")
        self.lb_DDS1_Duty.setMinimumSize(QSize(120, 30))
        self.lb_DDS1_Duty.setMaximumSize(QSize(120, 16777215))
        self.lb_DDS1_Duty.setFont(font2)
        self.lb_DDS1_Duty.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_DDS1_Duty.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.lb_DDS1_Duty)

        self.le_DDS1_Duty = QLineEdit(self.frame_18)
        self.le_DDS1_Duty.setObjectName(u"le_DDS1_Duty")
        self.le_DDS1_Duty.setMinimumSize(QSize(284, 40))
        self.le_DDS1_Duty.setFont(font2)
        self.le_DDS1_Duty.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid black;\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_49.addWidget(self.le_DDS1_Duty)


        self.verticalLayout_20.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(-1, 5, -1, 5)
        self.lb_DDS1_Freq = QLabel(self.frame_18)
        self.lb_DDS1_Freq.setObjectName(u"lb_DDS1_Freq")
        self.lb_DDS1_Freq.setMinimumSize(QSize(120, 30))
        self.lb_DDS1_Freq.setMaximumSize(QSize(120, 16777215))
        self.lb_DDS1_Freq.setFont(font2)
        self.lb_DDS1_Freq.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_DDS1_Freq.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.lb_DDS1_Freq)

        self.le_DDS1_Freq = QLineEdit(self.frame_18)
        self.le_DDS1_Freq.setObjectName(u"le_DDS1_Freq")
        self.le_DDS1_Freq.setMinimumSize(QSize(284, 40))
        self.le_DDS1_Freq.setFont(font2)
        self.le_DDS1_Freq.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid black;\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_50.addWidget(self.le_DDS1_Freq)


        self.verticalLayout_20.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.btn_DDS1_Generate = QPushButton(self.frame_18)
        self.btn_DDS1_Generate.setObjectName(u"btn_DDS1_Generate")
        self.btn_DDS1_Generate.setMinimumSize(QSize(200, 45))
        self.btn_DDS1_Generate.setFont(font2)
        self.btn_DDS1_Generate.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_DDS1_Generate.setStyleSheet(u"border-radius: 5px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_48.addWidget(self.btn_DDS1_Generate)

        self.btn_DDS1_Stop = QPushButton(self.frame_18)
        self.btn_DDS1_Stop.setObjectName(u"btn_DDS1_Stop")
        self.btn_DDS1_Stop.setEnabled(False)
        self.btn_DDS1_Stop.setMinimumSize(QSize(200, 45))
        self.btn_DDS1_Stop.setFont(font2)
        self.btn_DDS1_Stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_DDS1_Stop.setStyleSheet(u"border-radius: 5px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_48.addWidget(self.btn_DDS1_Stop)


        self.verticalLayout_20.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalSpacer_15 = QSpacerItem(230, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_15)

        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy4.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy4)
        self.frame_21.setMinimumSize(QSize(230, 40))
        self.frame_21.setMaximumSize(QSize(100, 40))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(9, 0, 30, 0)
        self.info_text_5 = QLabel(self.frame_21)
        self.info_text_5.setObjectName(u"info_text_5")
        self.info_text_5.setMinimumSize(QSize(220, 35))
        self.info_text_5.setFont(font4)
        self.info_text_5.setStyleSheet(u"font: 18pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.info_text_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.info_text_5)


        self.horizontalLayout_46.addWidget(self.frame_21)

        self.horizontalSpacer_16 = QSpacerItem(230, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_16)


        self.verticalLayout_20.addLayout(self.horizontalLayout_46)

        self.te_DDS_Date = QTextEdit(self.frame_18)
        self.te_DDS_Date.setObjectName(u"te_DDS_Date")
        sizePolicy3.setHeightForWidth(self.te_DDS_Date.sizePolicy().hasHeightForWidth())
        self.te_DDS_Date.setSizePolicy(sizePolicy3)
        self.te_DDS_Date.setMinimumSize(QSize(520, 100))
        self.te_DDS_Date.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid black;\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.verticalLayout_20.addWidget(self.te_DDS_Date)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(-1, 5, -1, 5)
        self.lb_DDS2_Freq = QLabel(self.frame_18)
        self.lb_DDS2_Freq.setObjectName(u"lb_DDS2_Freq")
        self.lb_DDS2_Freq.setMinimumSize(QSize(200, 30))
        self.lb_DDS2_Freq.setMaximumSize(QSize(120, 16777215))
        self.lb_DDS2_Freq.setFont(font2)
        self.lb_DDS2_Freq.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_DDS2_Freq.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_52.addWidget(self.lb_DDS2_Freq)

        self.le_DDS2_Freq = QLineEdit(self.frame_18)
        self.le_DDS2_Freq.setObjectName(u"le_DDS2_Freq")
        self.le_DDS2_Freq.setMinimumSize(QSize(284, 40))
        self.le_DDS2_Freq.setFont(font2)
        self.le_DDS2_Freq.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid black;\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_52.addWidget(self.le_DDS2_Freq)


        self.verticalLayout_20.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.btn_DDS2_Generate = QPushButton(self.frame_18)
        self.btn_DDS2_Generate.setObjectName(u"btn_DDS2_Generate")
        self.btn_DDS2_Generate.setMinimumSize(QSize(200, 45))
        self.btn_DDS2_Generate.setFont(font2)
        self.btn_DDS2_Generate.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_DDS2_Generate.setStyleSheet(u"border-radius: 5px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_54.addWidget(self.btn_DDS2_Generate)

        self.btn_DDS2_Stop = QPushButton(self.frame_18)
        self.btn_DDS2_Stop.setObjectName(u"btn_DDS2_Stop")
        self.btn_DDS2_Stop.setEnabled(False)
        self.btn_DDS2_Stop.setMinimumSize(QSize(200, 45))
        self.btn_DDS2_Stop.setFont(font2)
        self.btn_DDS2_Stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_DDS2_Stop.setStyleSheet(u"border-radius: 5px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_54.addWidget(self.btn_DDS2_Stop)


        self.verticalLayout_20.addLayout(self.horizontalLayout_54)


        self.horizontalLayout_63.addWidget(self.frame_18)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy3.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy3)
        self.frame_14.setMaximumSize(QSize(16777215, 400))
        self.frame_14.setStyleSheet(u"QFrame#frame_14{\n"
"	border: 1px solid #343b48;\n"
"	/*background-color: rgb(126, 199, 193);*/\n"
"	border-radius: 5px;\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_14)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_7 = QSpacerItem(230, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_7)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy4.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy4)
        self.frame_15.setMinimumSize(QSize(100, 40))
        self.frame_15.setMaximumSize(QSize(100, 40))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(9, 0, 30, 0)
        self.info_text_2 = QLabel(self.frame_15)
        self.info_text_2.setObjectName(u"info_text_2")
        self.info_text_2.setMinimumSize(QSize(85, 35))
        self.info_text_2.setFont(font4)
        self.info_text_2.setStyleSheet(u"font: 18pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.info_text_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.info_text_2)


        self.horizontalLayout_22.addWidget(self.frame_15)

        self.horizontalSpacer_8 = QSpacerItem(230, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_8)


        self.verticalLayout_18.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 5, -1, 5)
        self.lb_PWM1_Freq = QLabel(self.frame_14)
        self.lb_PWM1_Freq.setObjectName(u"lb_PWM1_Freq")
        self.lb_PWM1_Freq.setMinimumSize(QSize(120, 30))
        self.lb_PWM1_Freq.setMaximumSize(QSize(120, 16777215))
        self.lb_PWM1_Freq.setFont(font2)
        self.lb_PWM1_Freq.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_PWM1_Freq.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.lb_PWM1_Freq)

        self.le_PWM1_Freq = QLineEdit(self.frame_14)
        self.le_PWM1_Freq.setObjectName(u"le_PWM1_Freq")
        self.le_PWM1_Freq.setMinimumSize(QSize(284, 40))
        self.le_PWM1_Freq.setFont(font2)
        self.le_PWM1_Freq.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid black;\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_24.addWidget(self.le_PWM1_Freq)


        self.verticalLayout_18.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(-1, 5, -1, 5)
        self.lb_PWM2_Duty = QLabel(self.frame_14)
        self.lb_PWM2_Duty.setObjectName(u"lb_PWM2_Duty")
        self.lb_PWM2_Duty.setMinimumSize(QSize(120, 30))
        self.lb_PWM2_Duty.setMaximumSize(QSize(120, 16777215))
        self.lb_PWM2_Duty.setFont(font2)
        self.lb_PWM2_Duty.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_PWM2_Duty.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.lb_PWM2_Duty)

        self.le_PWM2_Duty = QLineEdit(self.frame_14)
        self.le_PWM2_Duty.setObjectName(u"le_PWM2_Duty")
        self.le_PWM2_Duty.setMinimumSize(QSize(284, 40))
        self.le_PWM2_Duty.setFont(font2)
        self.le_PWM2_Duty.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid black;\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_25.addWidget(self.le_PWM2_Duty)


        self.verticalLayout_18.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.btn_PWM1_Generate = QPushButton(self.frame_14)
        self.btn_PWM1_Generate.setObjectName(u"btn_PWM1_Generate")
        self.btn_PWM1_Generate.setMinimumSize(QSize(0, 45))
        self.btn_PWM1_Generate.setFont(font2)
        self.btn_PWM1_Generate.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_PWM1_Generate.setStyleSheet(u"border-radius: 5px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_21.addWidget(self.btn_PWM1_Generate)

        self.btn_PWM1_Stop = QPushButton(self.frame_14)
        self.btn_PWM1_Stop.setObjectName(u"btn_PWM1_Stop")
        self.btn_PWM1_Stop.setEnabled(False)
        self.btn_PWM1_Stop.setMinimumSize(QSize(0, 45))
        self.btn_PWM1_Stop.setFont(font2)
        self.btn_PWM1_Stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_PWM1_Stop.setStyleSheet(u"border-radius: 5px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_21.addWidget(self.btn_PWM1_Stop)

        self.btn_PWM1_Servo = QPushButton(self.frame_14)
        self.btn_PWM1_Servo.setObjectName(u"btn_PWM1_Servo")
        self.btn_PWM1_Servo.setEnabled(True)
        self.btn_PWM1_Servo.setMinimumSize(QSize(0, 45))
        self.btn_PWM1_Servo.setFont(font2)
        self.btn_PWM1_Servo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_PWM1_Servo.setStyleSheet(u"border-radius: 5px;\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_21.addWidget(self.btn_PWM1_Servo)


        self.verticalLayout_18.addLayout(self.horizontalLayout_21)


        self.verticalLayout_22.addLayout(self.verticalLayout_18)


        self.verticalLayout_33.addWidget(self.frame_14)

        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy3.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy3)
        self.frame_16.setMaximumSize(QSize(16777215, 400))
        self.frame_16.setStyleSheet(u"QFrame#frame_16{\n"
"	border: 1px solid #343b48;\n"
"	/*background-color: rgb(126, 199, 193);*/\n"
"	border-radius: 5px;\n"
"}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_16)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalSpacer_21 = QSpacerItem(230, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_21)

        self.frame_23 = QFrame(self.frame_16)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy4.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy4)
        self.frame_23.setMinimumSize(QSize(100, 40))
        self.frame_23.setMaximumSize(QSize(100, 40))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(9, 0, 30, 0)
        self.info_text_8 = QLabel(self.frame_23)
        self.info_text_8.setObjectName(u"info_text_8")
        self.info_text_8.setMinimumSize(QSize(85, 35))
        self.info_text_8.setFont(font4)
        self.info_text_8.setStyleSheet(u"font: 18pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.info_text_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_59.addWidget(self.info_text_8)


        self.horizontalLayout_58.addWidget(self.frame_23)

        self.horizontalSpacer_22 = QSpacerItem(230, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_22)


        self.verticalLayout_30.addLayout(self.horizontalLayout_58)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(-1, 5, -1, 5)
        self.lb_PWM2_Freq = QLabel(self.frame_16)
        self.lb_PWM2_Freq.setObjectName(u"lb_PWM2_Freq")
        self.lb_PWM2_Freq.setMinimumSize(QSize(120, 30))
        self.lb_PWM2_Freq.setMaximumSize(QSize(120, 16777215))
        self.lb_PWM2_Freq.setFont(font2)
        self.lb_PWM2_Freq.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_PWM2_Freq.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.lb_PWM2_Freq)

        self.le_PWM2_Freq = QLineEdit(self.frame_16)
        self.le_PWM2_Freq.setObjectName(u"le_PWM2_Freq")
        self.le_PWM2_Freq.setMinimumSize(QSize(284, 40))
        self.le_PWM2_Freq.setFont(font2)
        self.le_PWM2_Freq.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid black;\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_60.addWidget(self.le_PWM2_Freq)


        self.verticalLayout_30.addLayout(self.horizontalLayout_60)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(-1, 5, -1, 5)
        self.lb_PWM2_Duty_2 = QLabel(self.frame_16)
        self.lb_PWM2_Duty_2.setObjectName(u"lb_PWM2_Duty_2")
        self.lb_PWM2_Duty_2.setMinimumSize(QSize(120, 30))
        self.lb_PWM2_Duty_2.setMaximumSize(QSize(120, 16777215))
        self.lb_PWM2_Duty_2.setFont(font2)
        self.lb_PWM2_Duty_2.setStyleSheet(u"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.lb_PWM2_Duty_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_61.addWidget(self.lb_PWM2_Duty_2)

        self.le_PWM2_Duty_2 = QLineEdit(self.frame_16)
        self.le_PWM2_Duty_2.setObjectName(u"le_PWM2_Duty_2")
        self.le_PWM2_Duty_2.setMinimumSize(QSize(284, 40))
        self.le_PWM2_Duty_2.setFont(font2)
        self.le_PWM2_Duty_2.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid black;\n"
"background-color: rgb(33, 37, 43);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_61.addWidget(self.le_PWM2_Duty_2)


        self.verticalLayout_30.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.btn_PWM2_Generate = QPushButton(self.frame_16)
        self.btn_PWM2_Generate.setObjectName(u"btn_PWM2_Generate")
        self.btn_PWM2_Generate.setMinimumSize(QSize(0, 45))
        self.btn_PWM2_Generate.setFont(font2)
        self.btn_PWM2_Generate.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_PWM2_Generate.setStyleSheet(u"border-radius: 5px;font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_62.addWidget(self.btn_PWM2_Generate)

        self.btn_PWM2_Stop = QPushButton(self.frame_16)
        self.btn_PWM2_Stop.setObjectName(u"btn_PWM2_Stop")
        self.btn_PWM2_Stop.setEnabled(False)
        self.btn_PWM2_Stop.setMinimumSize(QSize(0, 45))
        self.btn_PWM2_Stop.setFont(font2)
        self.btn_PWM2_Stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_PWM2_Stop.setStyleSheet(u"border-radius: 5px;font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_62.addWidget(self.btn_PWM2_Stop)

        self.btn_PWM2_Servo = QPushButton(self.frame_16)
        self.btn_PWM2_Servo.setObjectName(u"btn_PWM2_Servo")
        self.btn_PWM2_Servo.setMinimumSize(QSize(0, 45))
        self.btn_PWM2_Servo.setFont(font2)
        self.btn_PWM2_Servo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_PWM2_Servo.setStyleSheet(u"border-radius: 5px;font: 14pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")

        self.horizontalLayout_62.addWidget(self.btn_PWM2_Servo)


        self.verticalLayout_30.addLayout(self.horizontalLayout_62)


        self.verticalLayout_28.addLayout(self.verticalLayout_30)


        self.verticalLayout_33.addWidget(self.frame_16)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_2)


        self.horizontalLayout_63.addLayout(self.verticalLayout_33)


        self.horizontalLayout_64.addLayout(self.horizontalLayout_63)


        self.verticalLayout_36.addWidget(self.frame_13)

        self.stackedWidget.addWidget(self.Page_DDS)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 20))
        font5 = QFont()
        font5.setFamilies([u"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare"])
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setStyleSheet(u"font: 10pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setStyleSheet(u"font: 10pt \"\u30af\u30ecPro by \u5b81\u9759\u4e4b\u96e8\uff0c\u5fae\u4fe1\u516c\u4f17\u53f7njzyshare\";")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_35.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Embedded Tools", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Embedded Tools", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Design By HarryWang", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Function bar", None))
        self.btn_Setting.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.btn_OSC.setText(QCoreApplication.translate("MainWindow", u"Virtual OSC", None))
        self.btn_UART.setText(QCoreApplication.translate("MainWindow", u"Serial Port", None))
        self.btn_DDS.setText(QCoreApplication.translate("MainWindow", u"DDS", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Setting</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.te_Setting_Terminal.setToolTip(QCoreApplication.translate("MainWindow", u"Terminal", None))
#endif // QT_CONFIG(tooltip)
        self.te_Setting_Terminal.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please connect the device", None))
        self.info_text.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.lb_Device_IP.setText(QCoreApplication.translate("MainWindow", u"Local IP", None))
#if QT_CONFIG(tooltip)
        self.le_Device_IP.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bf7\u67e5\u770bLCD\u663e\u793a\u4fe1\u606f", None))
#endif // QT_CONFIG(tooltip)
        self.le_Device_IP.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please view the device LCD interface", None))
#if QT_CONFIG(tooltip)
        self.btn_Connect.setToolTip(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u8bbe\u5907", None))
#endif // QT_CONFIG(tooltip)
        self.btn_Connect.setText(QCoreApplication.translate("MainWindow", u"Connecting Device", None))
        self.lb_WiFi_name.setText(QCoreApplication.translate("MainWindow", u"WiFi Name", None))
#if QT_CONFIG(tooltip)
        self.le_WiFi_name.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165WIFi\u540d\u79f0", None))
#endif // QT_CONFIG(tooltip)
        self.le_WiFi_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter the WiFI name you want to add", None))
        self.lb_WiFi_pw.setText(QCoreApplication.translate("MainWindow", u"WiFi Password", None))
#if QT_CONFIG(tooltip)
        self.le_WiFi_pw.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u5bf9\u5e94\u7684WIFI\u5bc6\u7801", None))
#endif // QT_CONFIG(tooltip)
        self.le_WiFi_pw.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter the WiFI password you want to add", None))
#if QT_CONFIG(tooltip)
        self.btn_Scan_WiFi.setToolTip(QCoreApplication.translate("MainWindow", u"\u626b\u63cfWIFi", None))
#endif // QT_CONFIG(tooltip)
        self.btn_Scan_WiFi.setText(QCoreApplication.translate("MainWindow", u"Scan WiFi", None))
#if QT_CONFIG(tooltip)
        self.btn_Add_WiFi.setToolTip(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0WIfi\u914d\u7f6e\u7ed9\u8bbe\u5907", None))
#endif // QT_CONFIG(tooltip)
        self.btn_Add_WiFi.setText(QCoreApplication.translate("MainWindow", u"Add WiFi Config", None))
#if QT_CONFIG(tooltip)
        self.btn_Status_LED.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_Status_LED.setText("")
#if QT_CONFIG(tooltip)
        self.btn_Status.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u8bbe\u5907\u72b6\u6001</p><p>\u7ea2\u8272\uff1a\u672a\u8fde\u63a5</p><p>\u7eff\u8272\uff1a\u8054\u673a\u6210\u529f</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_Status.setText(QCoreApplication.translate("MainWindow", u"Device Status", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"More", None))
#if QT_CONFIG(tooltip)
        self.te_Debug.setToolTip(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u7279\u6b8a\u7684\u6307\u4ee4", None))
#endif // QT_CONFIG(tooltip)
        self.te_Debug.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Debugging with Standard Formats", None))
#if QT_CONFIG(tooltip)
        self.btn_Rst.setToolTip(QCoreApplication.translate("MainWindow", u"\u91cd\u542f\u8bbe\u5907", None))
#endif // QT_CONFIG(tooltip)
        self.btn_Rst.setText(QCoreApplication.translate("MainWindow", u"Restart Device", None))
#if QT_CONFIG(tooltip)
        self.btn_Debug_Send.setToolTip(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
#endif // QT_CONFIG(tooltip)
        self.btn_Debug_Send.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.btn_OSC_FFT.setText(QCoreApplication.translate("MainWindow", u"FFT", None))
        self.btn_OSC_CH1_EN.setText(QCoreApplication.translate("MainWindow", u"CH1", None))
        self.btn_OSC_CH2_EN.setText(QCoreApplication.translate("MainWindow", u"CH2", None))
        self.lb_Port_17.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.com_CH1_Date1.setItemText(0, QCoreApplication.translate("MainWindow", u"------", None))
        self.com_CH1_Date1.setItemText(1, QCoreApplication.translate("MainWindow", u"Vpp", None))
        self.com_CH1_Date1.setItemText(2, QCoreApplication.translate("MainWindow", u"Freq", None))
        self.com_CH1_Date1.setItemText(3, QCoreApplication.translate("MainWindow", u"Max", None))
        self.com_CH1_Date1.setItemText(4, QCoreApplication.translate("MainWindow", u"Min", None))
        self.com_CH1_Date1.setItemText(5, QCoreApplication.translate("MainWindow", u"Mean", None))
        self.com_CH1_Date1.setItemText(6, QCoreApplication.translate("MainWindow", u"RMS", None))

#if QT_CONFIG(tooltip)
        self.com_CH1_Date1.setToolTip(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387\u9009\u62e9", None))
#endif // QT_CONFIG(tooltip)
        self.lb_CH1_Date1.setText(QCoreApplication.translate("MainWindow", u"------------", None))
        self.lb_Port_20.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.com_CH1_Date2.setItemText(0, QCoreApplication.translate("MainWindow", u"------", None))
        self.com_CH1_Date2.setItemText(1, QCoreApplication.translate("MainWindow", u"Vpp", None))
        self.com_CH1_Date2.setItemText(2, QCoreApplication.translate("MainWindow", u"Freq", None))
        self.com_CH1_Date2.setItemText(3, QCoreApplication.translate("MainWindow", u"Max", None))
        self.com_CH1_Date2.setItemText(4, QCoreApplication.translate("MainWindow", u"Min", None))
        self.com_CH1_Date2.setItemText(5, QCoreApplication.translate("MainWindow", u"Mean", None))
        self.com_CH1_Date2.setItemText(6, QCoreApplication.translate("MainWindow", u"RMS", None))

#if QT_CONFIG(tooltip)
        self.com_CH1_Date2.setToolTip(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387\u9009\u62e9", None))
#endif // QT_CONFIG(tooltip)
        self.lb_CH1_Date2.setText(QCoreApplication.translate("MainWindow", u"------------", None))
        self.lb_Port_22.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.com_CH1_Date3.setItemText(0, QCoreApplication.translate("MainWindow", u"------", None))
        self.com_CH1_Date3.setItemText(1, QCoreApplication.translate("MainWindow", u"Vpp", None))
        self.com_CH1_Date3.setItemText(2, QCoreApplication.translate("MainWindow", u"Freq", None))
        self.com_CH1_Date3.setItemText(3, QCoreApplication.translate("MainWindow", u"Max", None))
        self.com_CH1_Date3.setItemText(4, QCoreApplication.translate("MainWindow", u"Min", None))
        self.com_CH1_Date3.setItemText(5, QCoreApplication.translate("MainWindow", u"Mean", None))
        self.com_CH1_Date3.setItemText(6, QCoreApplication.translate("MainWindow", u"RMS", None))

#if QT_CONFIG(tooltip)
        self.com_CH1_Date3.setToolTip(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387\u9009\u62e9", None))
#endif // QT_CONFIG(tooltip)
        self.lb_CH1_Date3.setText(QCoreApplication.translate("MainWindow", u"------------", None))
        self.lb_Port_24.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.com_CH1_Date4.setItemText(0, QCoreApplication.translate("MainWindow", u"------", None))
        self.com_CH1_Date4.setItemText(1, QCoreApplication.translate("MainWindow", u"Vpp", None))
        self.com_CH1_Date4.setItemText(2, QCoreApplication.translate("MainWindow", u"Freq", None))
        self.com_CH1_Date4.setItemText(3, QCoreApplication.translate("MainWindow", u"Max", None))
        self.com_CH1_Date4.setItemText(4, QCoreApplication.translate("MainWindow", u"Min", None))
        self.com_CH1_Date4.setItemText(5, QCoreApplication.translate("MainWindow", u"Mean", None))
        self.com_CH1_Date4.setItemText(6, QCoreApplication.translate("MainWindow", u"RMS", None))

#if QT_CONFIG(tooltip)
        self.com_CH1_Date4.setToolTip(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387\u9009\u62e9", None))
#endif // QT_CONFIG(tooltip)
        self.lb_CH1_Date4.setText(QCoreApplication.translate("MainWindow", u"------------", None))
        self.lb_Port_26.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.com_CH1_Date5.setItemText(0, QCoreApplication.translate("MainWindow", u"------", None))
        self.com_CH1_Date5.setItemText(1, QCoreApplication.translate("MainWindow", u"Vpp", None))
        self.com_CH1_Date5.setItemText(2, QCoreApplication.translate("MainWindow", u"Freq", None))
        self.com_CH1_Date5.setItemText(3, QCoreApplication.translate("MainWindow", u"Max", None))
        self.com_CH1_Date5.setItemText(4, QCoreApplication.translate("MainWindow", u"Min", None))
        self.com_CH1_Date5.setItemText(5, QCoreApplication.translate("MainWindow", u"Mean", None))
        self.com_CH1_Date5.setItemText(6, QCoreApplication.translate("MainWindow", u"RMS", None))

#if QT_CONFIG(tooltip)
        self.com_CH1_Date5.setToolTip(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387\u9009\u62e9", None))
#endif // QT_CONFIG(tooltip)
        self.lb_CH1_Date5.setText(QCoreApplication.translate("MainWindow", u"------------", None))
        self.lb_Port_38.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.com_CH2_Date1.setItemText(0, QCoreApplication.translate("MainWindow", u"------", None))
        self.com_CH2_Date1.setItemText(1, QCoreApplication.translate("MainWindow", u"Vpp", None))
        self.com_CH2_Date1.setItemText(2, QCoreApplication.translate("MainWindow", u"Freq", None))
        self.com_CH2_Date1.setItemText(3, QCoreApplication.translate("MainWindow", u"Max", None))
        self.com_CH2_Date1.setItemText(4, QCoreApplication.translate("MainWindow", u"Min", None))
        self.com_CH2_Date1.setItemText(5, QCoreApplication.translate("MainWindow", u"Mean", None))
        self.com_CH2_Date1.setItemText(6, QCoreApplication.translate("MainWindow", u"RMS", None))

#if QT_CONFIG(tooltip)
        self.com_CH2_Date1.setToolTip(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387\u9009\u62e9", None))
#endif // QT_CONFIG(tooltip)
        self.lb_CH2_Date1.setText(QCoreApplication.translate("MainWindow", u"------------", None))
        self.lb_Port_40.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.com_CH2_Date2.setItemText(0, QCoreApplication.translate("MainWindow", u"------", None))
        self.com_CH2_Date2.setItemText(1, QCoreApplication.translate("MainWindow", u"Vpp", None))
        self.com_CH2_Date2.setItemText(2, QCoreApplication.translate("MainWindow", u"Freq", None))
        self.com_CH2_Date2.setItemText(3, QCoreApplication.translate("MainWindow", u"Max", None))
        self.com_CH2_Date2.setItemText(4, QCoreApplication.translate("MainWindow", u"Min", None))
        self.com_CH2_Date2.setItemText(5, QCoreApplication.translate("MainWindow", u"Mean", None))
        self.com_CH2_Date2.setItemText(6, QCoreApplication.translate("MainWindow", u"RMS", None))

#if QT_CONFIG(tooltip)
        self.com_CH2_Date2.setToolTip(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387\u9009\u62e9", None))
#endif // QT_CONFIG(tooltip)
        self.lb_CH2_Date2.setText(QCoreApplication.translate("MainWindow", u"------------", None))
        self.lb_Port_42.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.com_CH2_Date3.setItemText(0, QCoreApplication.translate("MainWindow", u"------", None))
        self.com_CH2_Date3.setItemText(1, QCoreApplication.translate("MainWindow", u"Vpp", None))
        self.com_CH2_Date3.setItemText(2, QCoreApplication.translate("MainWindow", u"Freq", None))
        self.com_CH2_Date3.setItemText(3, QCoreApplication.translate("MainWindow", u"Max", None))
        self.com_CH2_Date3.setItemText(4, QCoreApplication.translate("MainWindow", u"Min", None))
        self.com_CH2_Date3.setItemText(5, QCoreApplication.translate("MainWindow", u"Mean", None))
        self.com_CH2_Date3.setItemText(6, QCoreApplication.translate("MainWindow", u"RMS", None))

#if QT_CONFIG(tooltip)
        self.com_CH2_Date3.setToolTip(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387\u9009\u62e9", None))
#endif // QT_CONFIG(tooltip)
        self.lb_CH2_Date3.setText(QCoreApplication.translate("MainWindow", u"------------", None))
        self.lb_Port_44.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.com_CH2_Date4.setItemText(0, QCoreApplication.translate("MainWindow", u"------", None))
        self.com_CH2_Date4.setItemText(1, QCoreApplication.translate("MainWindow", u"Vpp", None))
        self.com_CH2_Date4.setItemText(2, QCoreApplication.translate("MainWindow", u"Freq", None))
        self.com_CH2_Date4.setItemText(3, QCoreApplication.translate("MainWindow", u"Max", None))
        self.com_CH2_Date4.setItemText(4, QCoreApplication.translate("MainWindow", u"Min", None))
        self.com_CH2_Date4.setItemText(5, QCoreApplication.translate("MainWindow", u"Mean", None))
        self.com_CH2_Date4.setItemText(6, QCoreApplication.translate("MainWindow", u"RMS", None))

#if QT_CONFIG(tooltip)
        self.com_CH2_Date4.setToolTip(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387\u9009\u62e9", None))
#endif // QT_CONFIG(tooltip)
        self.lb_CH2_Date4.setText(QCoreApplication.translate("MainWindow", u"------------", None))
        self.lb_Port_46.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.com_CH2_Date5.setItemText(0, QCoreApplication.translate("MainWindow", u"------", None))
        self.com_CH2_Date5.setItemText(1, QCoreApplication.translate("MainWindow", u"Vpp", None))
        self.com_CH2_Date5.setItemText(2, QCoreApplication.translate("MainWindow", u"Freq", None))
        self.com_CH2_Date5.setItemText(3, QCoreApplication.translate("MainWindow", u"Max", None))
        self.com_CH2_Date5.setItemText(4, QCoreApplication.translate("MainWindow", u"Min", None))
        self.com_CH2_Date5.setItemText(5, QCoreApplication.translate("MainWindow", u"Mean", None))
        self.com_CH2_Date5.setItemText(6, QCoreApplication.translate("MainWindow", u"RMS", None))

#if QT_CONFIG(tooltip)
        self.com_CH2_Date5.setToolTip(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387\u9009\u62e9", None))
#endif // QT_CONFIG(tooltip)
        self.lb_CH2_Date5.setText(QCoreApplication.translate("MainWindow", u"------------", None))
        self.lb_Port_12.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u5e73\u5206\u8fa8\u7387", None))
        self.lb_OSC_Horizontal.setText(QCoreApplication.translate("MainWindow", u"100us/div", None))
        self.lb_Port_9.setText(QCoreApplication.translate("MainWindow", u"\u5782\u76f4\u5206\u8fa8\u7387", None))
        self.lb_Port_10.setText(QCoreApplication.translate("MainWindow", u"CH1", None))
        self.lb_OSC_Vertical_CH1.setText(QCoreApplication.translate("MainWindow", u"100mV/div", None))
        self.lb_Port_11.setText(QCoreApplication.translate("MainWindow", u"CH2", None))
        self.lb_OSC_Vertical_CH2.setText(QCoreApplication.translate("MainWindow", u"100mV/div", None))
        self.lb_Port_4.setText(QCoreApplication.translate("MainWindow", u"\u7535\u5e73\u504f\u79fb", None))
        self.lb_Port_5.setText(QCoreApplication.translate("MainWindow", u"CH1", None))
        self.lb_OSC_Offset_CH1.setText(QCoreApplication.translate("MainWindow", u"0.00V", None))
        self.lb_Port_6.setText(QCoreApplication.translate("MainWindow", u"CH2", None))
        self.lb_OSC_Offset_CH2.setText(QCoreApplication.translate("MainWindow", u"0.00V", None))
        self.lb_Port_16.setText(QCoreApplication.translate("MainWindow", u"\u89e6\u53d1\u901a\u9053", None))
        self.com_Trigger_Channal.setItemText(0, QCoreApplication.translate("MainWindow", u"CH1", None))
        self.com_Trigger_Channal.setItemText(1, QCoreApplication.translate("MainWindow", u"CH2", None))

#if QT_CONFIG(tooltip)
        self.com_Trigger_Channal.setToolTip(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387\u9009\u62e9", None))
#endif // QT_CONFIG(tooltip)
        self.lb_Port_14.setText(QCoreApplication.translate("MainWindow", u"\u89e6\u53d1\u65b9\u5f0f", None))
        self.com_Trigger_Way.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4e0a\u5347\u6cbf", None))
        self.com_Trigger_Way.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e0b\u964d\u6cbf", None))

#if QT_CONFIG(tooltip)
        self.com_Trigger_Way.setToolTip(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387\u9009\u62e9", None))
#endif // QT_CONFIG(tooltip)
        self.btn_Screenshot.setText(QCoreApplication.translate("MainWindow", u"\u622a\u56fe", None))
        self.btn_Run_Stop.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c/\u6682\u505c", None))
        self.info_text_7.setText(QCoreApplication.translate("MainWindow", u"Chart", None))
        self.lb_Port.setText(QCoreApplication.translate("MainWindow", u"Serial Port", None))
#if QT_CONFIG(tooltip)
        self.com_Port.setToolTip(QCoreApplication.translate("MainWindow", u"\u7aef\u53e3\u9009\u62e9", None))
#endif // QT_CONFIG(tooltip)
        self.lb_Baud.setText(QCoreApplication.translate("MainWindow", u"Baud Rate", None))
        self.com_Baud.setItemText(0, QCoreApplication.translate("MainWindow", u"1200", None))
        self.com_Baud.setItemText(1, QCoreApplication.translate("MainWindow", u"9600", None))
        self.com_Baud.setItemText(2, QCoreApplication.translate("MainWindow", u"14400", None))
        self.com_Baud.setItemText(3, QCoreApplication.translate("MainWindow", u"19200", None))
        self.com_Baud.setItemText(4, QCoreApplication.translate("MainWindow", u"38400", None))
        self.com_Baud.setItemText(5, QCoreApplication.translate("MainWindow", u"57600", None))
        self.com_Baud.setItemText(6, QCoreApplication.translate("MainWindow", u"115200", None))
        self.com_Baud.setItemText(7, QCoreApplication.translate("MainWindow", u"230400", None))

#if QT_CONFIG(tooltip)
        self.com_Baud.setToolTip(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387\u9009\u62e9", None))
#endif // QT_CONFIG(tooltip)
        self.lb_Check_bit.setText(QCoreApplication.translate("MainWindow", u"Check Bit", None))
        self.com_Check_bit.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.com_Check_bit.setItemText(1, QCoreApplication.translate("MainWindow", u"Even", None))
        self.com_Check_bit.setItemText(2, QCoreApplication.translate("MainWindow", u"Odd", None))
        self.com_Check_bit.setItemText(3, QCoreApplication.translate("MainWindow", u"Space", None))
        self.com_Check_bit.setItemText(4, QCoreApplication.translate("MainWindow", u"Mark", None))

#if QT_CONFIG(tooltip)
        self.com_Check_bit.setToolTip(QCoreApplication.translate("MainWindow", u"\u6821\u9a8c\u4f4d\u9009\u62e9", None))
#endif // QT_CONFIG(tooltip)
        self.lb_Stop_bit.setText(QCoreApplication.translate("MainWindow", u"Number Of Stops", None))
        self.com_Stop_bit.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.com_Stop_bit.setItemText(1, QCoreApplication.translate("MainWindow", u"1.5", None))
        self.com_Stop_bit.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))

#if QT_CONFIG(tooltip)
        self.com_Stop_bit.setToolTip(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u4f4d\u9009\u62e9", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_UART_ctrl.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6253\u5f00\u4e32\u53e3</p><p>\u7ea2\u8272\uff1a\u672a\u6253\u5f00</p><p>\u7eff\u8272\uff1a\u6253\u5f00</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_UART_ctrl.setText(QCoreApplication.translate("MainWindow", u"Open COM", None))
#if QT_CONFIG(tooltip)
        self.btn_UART_LED.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_UART_LED.setText("")
#if QT_CONFIG(tooltip)
        self.btn_UART_auto.setToolTip(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u8c03\u8282\u6ce2\u5f62\u81f3\u6574\u4e2a\u5c4f\u5e55", None))
#endif // QT_CONFIG(tooltip)
        self.btn_UART_auto.setText(QCoreApplication.translate("MainWindow", u"Auto Chart", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Receivie Terminal", None))
#if QT_CONFIG(tooltip)
        self.cb_Rec_HEX.setToolTip(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u5341\u516d\u8fdb\u5236\u663e\u793a", None))
#endif // QT_CONFIG(tooltip)
        self.cb_Rec_HEX.setText(QCoreApplication.translate("MainWindow", u"HEX", None))
#if QT_CONFIG(tooltip)
        self.btn_Rec_Clear.setToolTip(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
#endif // QT_CONFIG(tooltip)
        self.btn_Rec_Clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Send Terminal", None))
#if QT_CONFIG(tooltip)
        self.cb_Send_HEX.setToolTip(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u5341\u516d\u8fdb\u5236\u53d1\u9001", None))
#endif // QT_CONFIG(tooltip)
        self.cb_Send_HEX.setText(QCoreApplication.translate("MainWindow", u"HEX", None))
#if QT_CONFIG(tooltip)
        self.btn_UART_Send.setToolTip(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
#endif // QT_CONFIG(tooltip)
        self.btn_UART_Send.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.info_text_4.setText(QCoreApplication.translate("MainWindow", u"Specific waveform", None))
#if QT_CONFIG(tooltip)
        self.lb_Wavetype.setToolTip(QCoreApplication.translate("MainWindow", u"\u6ce2\u5f62\u7c7b\u578b", None))
#endif // QT_CONFIG(tooltip)
        self.lb_Wavetype.setText(QCoreApplication.translate("MainWindow", u"Wave type", None))
        self.com_Wavetype.setItemText(0, QCoreApplication.translate("MainWindow", u"Sine wave", None))
        self.com_Wavetype.setItemText(1, QCoreApplication.translate("MainWindow", u"Triangular wave", None))
        self.com_Wavetype.setItemText(2, QCoreApplication.translate("MainWindow", u"Square wave", None))

#if QT_CONFIG(tooltip)
        self.com_Wavetype.setToolTip(QCoreApplication.translate("MainWindow", u"\u7aef\u53e3\u9009\u62e9", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lb_DDS1_Vpp.setToolTip(QCoreApplication.translate("MainWindow", u"\u5cf0\u5cf0\u503c", None))
#endif // QT_CONFIG(tooltip)
        self.lb_DDS1_Vpp.setText(QCoreApplication.translate("MainWindow", u"Peak peak", None))
#if QT_CONFIG(tooltip)
        self.le_DDS1_Vpp.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4ea7\u751f\u6ce2\u5f62\u5cf0\u5cf0\u503c", None))
#endif // QT_CONFIG(tooltip)
        self.le_DDS1_Vpp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter Generate Waveform Peak", None))
#if QT_CONFIG(tooltip)
        self.lb_DDS1_Duty.setToolTip(QCoreApplication.translate("MainWindow", u"\u5360\u7a7a\u6bd4", None))
#endif // QT_CONFIG(tooltip)
        self.lb_DDS1_Duty.setText(QCoreApplication.translate("MainWindow", u"Duty", None))
#if QT_CONFIG(tooltip)
        self.le_DDS1_Duty.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4ea7\u751f\u6ce2\u5f62\u5360\u7a7a\u6bd4", None))
#endif // QT_CONFIG(tooltip)
        self.le_DDS1_Duty.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter the generated waveform duty cycle", None))
#if QT_CONFIG(tooltip)
        self.lb_DDS1_Freq.setToolTip(QCoreApplication.translate("MainWindow", u"\u9891\u7387", None))
#endif // QT_CONFIG(tooltip)
        self.lb_DDS1_Freq.setText(QCoreApplication.translate("MainWindow", u"Freq", None))
#if QT_CONFIG(tooltip)
        self.le_DDS1_Freq.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4ea7\u751f\u6ce2\u5f62\u9891\u7387", None))
#endif // QT_CONFIG(tooltip)
        self.le_DDS1_Freq.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter the generated waveform frequency", None))
#if QT_CONFIG(tooltip)
        self.btn_DDS1_Generate.setToolTip(QCoreApplication.translate("MainWindow", u"\u4ea7\u751f\u6ce2\u5f62", None))
#endif // QT_CONFIG(tooltip)
        self.btn_DDS1_Generate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
#if QT_CONFIG(tooltip)
        self.btn_DDS1_Stop.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u6ce2\u5f62", None))
#endif // QT_CONFIG(tooltip)
        self.btn_DDS1_Stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.info_text_5.setText(QCoreApplication.translate("MainWindow", u"Arbitrary waveform", None))
#if QT_CONFIG(tooltip)
        self.te_DDS_Date.setToolTip(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u4efb\u610f\u6ce2\u5f62\u6570\u636e", None))
#endif // QT_CONFIG(tooltip)
        self.te_DDS_Date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please put the processed data in the box according to the format", None))
        self.lb_DDS2_Freq.setText(QCoreApplication.translate("MainWindow", u"Sampling frequency", None))
#if QT_CONFIG(tooltip)
        self.le_DDS2_Freq.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u6b64\u6ce2\u5f62\u7684\u91c7\u6837\u9891\u7387", None))
#endif // QT_CONFIG(tooltip)
        self.le_DDS2_Freq.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter the sampling frequency for this waveform", None))
#if QT_CONFIG(tooltip)
        self.btn_DDS2_Generate.setToolTip(QCoreApplication.translate("MainWindow", u"\u4ea7\u751f\u6ce2\u5f62", None))
#endif // QT_CONFIG(tooltip)
        self.btn_DDS2_Generate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
#if QT_CONFIG(tooltip)
        self.btn_DDS2_Stop.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u6ce2\u5f62", None))
#endif // QT_CONFIG(tooltip)
        self.btn_DDS2_Stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.info_text_2.setText(QCoreApplication.translate("MainWindow", u"PWM-1", None))
        self.lb_PWM1_Freq.setText(QCoreApplication.translate("MainWindow", u"Freq", None))
#if QT_CONFIG(tooltip)
        self.le_PWM1_Freq.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165PWM\u6ce2\u7684\u9891\u7387", None))
#endif // QT_CONFIG(tooltip)
        self.le_PWM1_Freq.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter the frequency of the PWM wave", None))
        self.lb_PWM2_Duty.setText(QCoreApplication.translate("MainWindow", u"Duty", None))
#if QT_CONFIG(tooltip)
        self.le_PWM2_Duty.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165PWM\u6ce2\u7684\u5360\u7a7a\u6bd4", None))
#endif // QT_CONFIG(tooltip)
        self.le_PWM2_Duty.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter the duty cycle of the PWM wave", None))
#if QT_CONFIG(tooltip)
        self.btn_PWM1_Generate.setToolTip(QCoreApplication.translate("MainWindow", u"\u4ea7\u751fPWM", None))
#endif // QT_CONFIG(tooltip)
        self.btn_PWM1_Generate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
#if QT_CONFIG(tooltip)
        self.btn_PWM1_Stop.setToolTip(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u8f93\u51faPWM", None))
#endif // QT_CONFIG(tooltip)
        self.btn_PWM1_Stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
#if QT_CONFIG(tooltip)
        self.btn_PWM1_Servo.setToolTip(QCoreApplication.translate("MainWindow", u"\u8235\u673a\u4e00\u952e\u5f52\u96f6", None))
#endif // QT_CONFIG(tooltip)
        self.btn_PWM1_Servo.setText(QCoreApplication.translate("MainWindow", u"Servo Init", None))
        self.info_text_8.setText(QCoreApplication.translate("MainWindow", u"PWM-2", None))
        self.lb_PWM2_Freq.setText(QCoreApplication.translate("MainWindow", u"Freq", None))
#if QT_CONFIG(tooltip)
        self.le_PWM2_Freq.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165PWM\u6ce2\u7684\u9891\u7387", None))
#endif // QT_CONFIG(tooltip)
        self.le_PWM2_Freq.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter the frequency of the PWM wave", None))
        self.lb_PWM2_Duty_2.setText(QCoreApplication.translate("MainWindow", u"Duty", None))
#if QT_CONFIG(tooltip)
        self.le_PWM2_Duty_2.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165PWM\u6ce2\u7684\u5360\u7a7a\u6bd4", None))
#endif // QT_CONFIG(tooltip)
        self.le_PWM2_Duty_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please enter the duty cycle of the PWM wave", None))
#if QT_CONFIG(tooltip)
        self.btn_PWM2_Generate.setToolTip(QCoreApplication.translate("MainWindow", u"\u4ea7\u751fPWM", None))
#endif // QT_CONFIG(tooltip)
        self.btn_PWM2_Generate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
#if QT_CONFIG(tooltip)
        self.btn_PWM2_Stop.setToolTip(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u8f93\u51faPWM", None))
#endif // QT_CONFIG(tooltip)
        self.btn_PWM2_Stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
#if QT_CONFIG(tooltip)
        self.btn_PWM2_Servo.setToolTip(QCoreApplication.translate("MainWindow", u"\u8235\u673a\u4e00\u952e\u5f52\u96f6", None))
#endif // QT_CONFIG(tooltip)
        self.btn_PWM2_Servo.setText(QCoreApplication.translate("MainWindow", u"Servo Init", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Design By HarryWang", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.3.0", None))
    # retranslateUi

