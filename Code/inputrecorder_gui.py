# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inputrecorder_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.setEnabled(True)
		MainWindow.resize(445, 187)
		MainWindow.setMinimumSize(QtCore.QSize(160, 120))
		MainWindow.setMaximumSize(QtCore.QSize(445, 1000))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("img/technology.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		MainWindow.setWindowIcon(icon)
		MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
		MainWindow.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-color: none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #d8eaf9;\n"
"    border: 1px solid #1BA1E2;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #c6e2f9;\n"
"    border: 1px solid #1BA1E2;\n"
"}\n"
"#frame_top{\n"
"    background: white;\n"
"    border: 1px solid rgb(200, 200, 200);\n"
"    border-top: none;\n"
"}\n"
"#main_button_frame{\n"
"    /*background: white;*/\n"
"    border: 1px solid rgb(200, 200, 200);\n"
"    border-bottom: none;\n"
"    border-top: none;\n"
"    border-left: none;\n"
"}\n"
"QGroupBox{\n"
"    margin-bottom: 4px;\n"
"    border-bottom: none;\n"
"    border-right:none;\n"
"}\n"
"QGroupBox::title {\n"
"    color:  rgb(130, 130, 130);\n"
"    subcontrol-position: bottom center; /* position at the top center */\n"
"}\n"
"QLabel {\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setSpacing(6)
		self.verticalLayout.setObjectName("verticalLayout")
		self.frame_top = QtWidgets.QFrame(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.frame_top.sizePolicy().hasHeightForWidth())
		self.frame_top.setSizePolicy(sizePolicy)
		self.frame_top.setMinimumSize(QtCore.QSize(100, 100))
		self.frame_top.setFrameShape(QtWidgets.QFrame.Box)
		self.frame_top.setFrameShadow(QtWidgets.QFrame.Plain)
		self.frame_top.setObjectName("frame_top")
		self.main_button_frame = QtWidgets.QFrame(self.frame_top)
		self.main_button_frame.setGeometry(QtCore.QRect(0, 0, 161, 101))
		self.main_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.main_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.main_button_frame.setObjectName("main_button_frame")
		self.b_record = QtWidgets.QPushButton(self.main_button_frame)
		self.b_record.setEnabled(True)
		self.b_record.setGeometry(QtCore.QRect(20, 0, 61, 61))
		self.b_record.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.b_record.setText("")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("img/record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.b_record.setIcon(icon1)
		self.b_record.setIconSize(QtCore.QSize(40, 40))
		self.b_record.setCheckable(False)
		self.b_record.setAutoRepeat(False)
		self.b_record.setAutoDefault(False)
		self.b_record.setDefault(False)
		self.b_record.setFlat(False)
		self.b_record.setObjectName("b_record")
		self.b_play = QtWidgets.QPushButton(self.main_button_frame)
		self.b_play.setEnabled(True)
		self.b_play.setGeometry(QtCore.QRect(80, 0, 61, 61))
		self.b_play.setText("")
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap("img/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.b_play.setIcon(icon2)
		self.b_play.setIconSize(QtCore.QSize(40, 40))
		self.b_play.setObjectName("b_play")
		self.b_play.setEnabled(False)
		self.lcdNumber = QtWidgets.QLCDNumber(self.main_button_frame)
		self.lcdNumber.setGeometry(QtCore.QRect(20, 70, 121, 23))
		font = QtGui.QFont()
		font.setBold(False)
		font.setItalic(False)
		font.setUnderline(False)
		font.setWeight(50)
		font.setStrikeOut(False)
		self.lcdNumber.setFont(font)
		self.lcdNumber.setStyleSheet("QLCDNumber{\n"
"    color: red;\n"
"}")
		self.lcdNumber.setInputMethodHints(QtCore.Qt.ImhNone)
		self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
		self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
		self.lcdNumber.setLineWidth(1)
		self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
		self.lcdNumber.setProperty("value", 12.34)
		self.lcdNumber.setObjectName("lcdNumber")
		self.tabWidget = QtWidgets.QTabWidget(self.frame_top)
		self.tabWidget.setEnabled(True)
		self.tabWidget.setGeometry(QtCore.QRect(161, 0, 380, 99))
		self.tabWidget.setMaximumSize(QtCore.QSize(380, 16777215))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.tabWidget.setFont(font)
		self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    background: rgb(240, 240, 240);\n"
"    border:none;\n"
"}\n"
"QTabBar::tab:hover{\n"
"    background-color: #d8eaf9;\n"
"    border: 1px solid #1BA1E2;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    background: rgb(240, 240, 240);\n"
"}\n"
"QTabBar::tab:!selected {\n"
"    background: white;\n"
"\n"
"}\n"
"\n"
"/*QTabWidget::tab-bar {\n"
"    left: 5px; \n"
"}*/\n"
"/*rgb(240, 240, 240)*/")
		self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
		self.tabWidget.setObjectName("tabWidget")
		self.tab = QtWidgets.QWidget()
		self.tab.setObjectName("tab")
		self.sb_delay_r = QtWidgets.QSpinBox(self.tab)
		self.sb_delay_r.setGeometry(QtCore.QRect(10, 8, 24, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.sb_delay_r.setFont(font)
		self.sb_delay_r.setWrapping(False)
		self.sb_delay_r.setFrame(True)
		self.sb_delay_r.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
		self.sb_delay_r.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
		self.sb_delay_r.setObjectName("sb_delay_r")
		self.label_12 = QtWidgets.QLabel(self.tab)
		self.label_12.setGeometry(QtCore.QRect(40, 33, 91, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_12.setFont(font)
		self.label_12.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.label_12.setObjectName("label_12")
		self.label_11 = QtWidgets.QLabel(self.tab)
		self.label_11.setGeometry(QtCore.QRect(40, 58, 81, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_11.setFont(font)
		self.label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.label_11.setObjectName("label_11")
		self.cb_handle_k = QtWidgets.QCheckBox(self.tab)
		self.cb_handle_k.setGeometry(QtCore.QRect(19, 33, 16, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.cb_handle_k.setFont(font)
		self.cb_handle_k.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.cb_handle_k.setText("")
		self.cb_handle_k.setIconSize(QtCore.QSize(16, 16))
		self.cb_handle_k.setChecked(True)
		self.cb_handle_k.setObjectName("cb_handle_k")
		self.label_13 = QtWidgets.QLabel(self.tab)
		self.label_13.setGeometry(QtCore.QRect(40, 8, 81, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_13.setFont(font)
		self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.label_13.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.label_13.setObjectName("label_13")
		self.cb_handle_m = QtWidgets.QCheckBox(self.tab)
		self.cb_handle_m.setGeometry(QtCore.QRect(19, 58, 16, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.cb_handle_m.setFont(font)
		self.cb_handle_m.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.cb_handle_m.setText("")
		self.cb_handle_m.setIconSize(QtCore.QSize(16, 16))
		self.cb_handle_m.setObjectName("cb_handle_m")
		self.frame_2 = QtWidgets.QFrame(self.tab)
		self.frame_2.setGeometry(QtCore.QRect(135, 10, 5, 61))
		self.frame_2.setStyleSheet("QFrame{\n"
"    border: 1px solid rgb(200, 200, 200);\n"
"    border-bottom: none;\n"
"    border-top: none;\n"
"    border-left: none;\n"
"}")
		self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_2.setObjectName("frame_2")
		self.tabWidget.addTab(self.tab, "")
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		self.sb_speed = QtWidgets.QDoubleSpinBox(self.tab_2)
		self.sb_speed.setGeometry(QtCore.QRect(10, 58, 24, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.sb_speed.setFont(font)
		self.sb_speed.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.sb_speed.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
		self.sb_speed.setDecimals(1)
		self.sb_speed.setMaximum(10.0)
		self.sb_speed.setSingleStep(0.1)
		self.sb_speed.setProperty("value", 1.0)
		self.sb_speed.setObjectName("sb_speed")
		self.label_10 = QtWidgets.QLabel(self.tab_2)
		self.label_10.setGeometry(QtCore.QRect(40, 58, 75, 15))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_10.setFont(font)
		self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.label_10.setObjectName("label_10")
		self.label_9 = QtWidgets.QLabel(self.tab_2)
		self.label_9.setGeometry(QtCore.QRect(40, 32, 75, 15))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_9.setFont(font)
		self.label_9.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.label_9.setObjectName("label_9")
		self.label_8 = QtWidgets.QLabel(self.tab_2)
		self.label_8.setGeometry(QtCore.QRect(40, 8, 81, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_8.setFont(font)
		self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.label_8.setObjectName("label_8")
		self.sb_delay_p = QtWidgets.QSpinBox(self.tab_2)
		self.sb_delay_p.setGeometry(QtCore.QRect(10, 8, 24, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.sb_delay_p.setFont(font)
		self.sb_delay_p.setWrapping(False)
		self.sb_delay_p.setFrame(True)
		self.sb_delay_p.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
		self.sb_delay_p.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
		self.sb_delay_p.setObjectName("sb_delay_p")
		self.cb_loop = QtWidgets.QCheckBox(self.tab_2)
		self.cb_loop.setGeometry(QtCore.QRect(19, 33, 16, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.cb_loop.setFont(font)
		self.cb_loop.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.cb_loop.setText("")
		self.cb_loop.setIconSize(QtCore.QSize(16, 16))
		self.cb_loop.setObjectName("cb_loop")
		self.frame = QtWidgets.QFrame(self.tab_2)
		self.frame.setGeometry(QtCore.QRect(120, 10, 20, 61))
		self.frame.setStyleSheet("QFrame{\n"
"    border: 1px solid rgb(200, 200, 200);\n"
"    border-bottom: none;\n"
"    border-top: none;\n"
"    border-left: none;\n"
"}")
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.tabWidget.addTab(self.tab_2, "")
		self.tab_3 = QtWidgets.QWidget()
		self.tab_3.setObjectName("tab_3")
		self.b_load = QtWidgets.QPushButton(self.tab_3)
		self.b_load.setGeometry(QtCore.QRect(199, 31, 51, 18))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.b_load.setFont(font)
		self.b_load.setStyleSheet("#b_load{\n"
"    background: white;\n"
"    border: 1px solid rgb(200, 200, 200);\n"
"}\n"
"#b_load:hover{\n"
"    background-color: #d8eaf9;\n"
"    border: 1px solid #1BA1E2;\n"
"}\n"
"#b_load:pressed{\n"
"    background-color: #c6e2f9;\n"
"    border: 1px solid #1BA1E2;\n"
"}")
		self.b_load.setObjectName("b_load")
		self.b_save = QtWidgets.QPushButton(self.tab_3)
		self.b_save.setGeometry(QtCore.QRect(199, 8, 51, 18))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.b_save.setFont(font)
		self.b_save.setStyleSheet("#b_save{\n"
"    background: white;\n"
"    border: 1px solid rgb(200, 200, 200);\n"
"}\n"
"#b_save:hover{\n"
"    background-color: #d8eaf9;\n"
"    border: 1px solid #1BA1E2;\n"
"}\n"
"#b_save:pressed{\n"
"    background-color: #c6e2f9;\n"
"    border: 1px solid #1BA1E2;\n"
"}")
		self.b_save.setObjectName("b_save")
		self.entry_preset = QtWidgets.QComboBox(self.tab_3)
		self.entry_preset.setGeometry(QtCore.QRect(50, 31, 141, 18))
		self.entry_preset.setFrame(True)
		self.entry_preset.setObjectName("entry_preset")
		self.entry_preset.addItem("")
		self.entry_preset.addItem("")
		self.entry_preset.addItem("")
		self.entry_preset.addItem("")
		self.entry_preset.addItem("")
		self.entry_preset.addItem("")
		self.entry_name = QtWidgets.QLineEdit(self.tab_3)
		self.entry_name.setGeometry(QtCore.QRect(50, 8, 141, 18))
		self.entry_name.setText("")
		self.entry_name.setMaxLength(15)
		self.entry_name.setObjectName("entry_name")
		self.label = QtWidgets.QLabel(self.tab_3)
		self.label.setGeometry(QtCore.QRect(10, 8, 41, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label.setFont(font)
		self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.tab_3)
		self.label_2.setGeometry(QtCore.QRect(10, 32, 41, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_2.setFont(font)
		self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.label_2.setObjectName("label_2")
		self.b_remove = QtWidgets.QPushButton(self.tab_3)
		self.b_remove.setGeometry(QtCore.QRect(259, 30, 18, 18))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.b_remove.setFont(font)
		self.b_remove.setStyleSheet("#b_remove{\n"
"    background: white;\n"
"    border: 1px solid rgb(200, 200, 200);\n"
"}\n"
"#b_remove:hover{\n"
"    background-color: #d8eaf9;\n"
"    border: 1px solid #1BA1E2;\n"
"}\n"
"#b_remove:pressed{\n"
"    background-color: #c6e2f9;\n"
"    border: 1px solid #1BA1E2;\n"
"}")
		self.b_remove.setText("")
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap("img/red_cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.b_remove.setIcon(icon3)
		self.b_remove.setIconSize(QtCore.QSize(14, 14))
		self.b_remove.setObjectName("b_remove")
		self.tabWidget.addTab(self.tab_3, "")
		self.verticalLayout.addWidget(self.frame_top)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setSpacing(10)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.frame_midle = QtWidgets.QFrame(self.centralwidget)
		self.frame_midle.setMinimumSize(QtCore.QSize(0, 30))
		self.frame_midle.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_midle.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_midle.setObjectName("frame_midle")
		self.b_datatable = QtWidgets.QPushButton(self.frame_midle)
		self.b_datatable.setGeometry(QtCore.QRect(350, 4, 88, 23))
		self.b_datatable.setStyleSheet("#b_datatable{\n"
"    background: white;\n"
"    border: 1px solid rgb(200, 200, 200);\n"
"}\n"
"#b_datatable:hover{\n"
"    background-color: #d8eaf9;\n"
"    border: 1px solid #1BA1E2;\n"
"}\n"
"#b_datatable:pressed{\n"
"    background-color: #c6e2f9;\n"
"    border: 1px solid #1BA1E2;\n"
"}")
		self.b_datatable.setObjectName("b_datatable")
		self.label_3 = QtWidgets.QLabel(self.frame_midle)
		self.label_3.setGeometry(QtCore.QRect(3, 6, 51, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_3.setFont(font)
		self.label_3.setObjectName("label_3")
		self.l_name = QtWidgets.QLabel(self.frame_midle)
		self.l_name.setGeometry(QtCore.QRect(52, 6, 101, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.l_name.setFont(font)
		self.l_name.setTextFormat(QtCore.Qt.AutoText)
		self.l_name.setScaledContents(False)
		self.l_name.setWordWrap(False)
		self.l_name.setObjectName("l_name")
		self.label_5 = QtWidgets.QLabel(self.frame_midle)
		self.label_5.setGeometry(QtCore.QRect(263, 6, 41, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_5.setFont(font)
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(self.frame_midle)
		self.label_6.setGeometry(QtCore.QRect(162, 6, 41, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.label_6.setFont(font)
		self.label_6.setObjectName("label_6")
		self.separator = QtWidgets.QFrame(self.frame_midle)
		self.separator.setGeometry(QtCore.QRect(140, 0, 20, 31))
		self.separator.setStyleSheet("QFrame{\n"
"    border: 1px solid rgb(200, 200, 200);\n"
"    border-bottom: none;\n"
"    border-top: none;\n"
"    border-left: none;\n"
"}")
		self.separator.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.separator.setFrameShadow(QtWidgets.QFrame.Raised)
		self.separator.setObjectName("separator")
		self.separator_2 = QtWidgets.QFrame(self.frame_midle)
		self.separator_2.setGeometry(QtCore.QRect(240, 0, 20, 31))
		self.separator_2.setStyleSheet("QFrame{\n"
"    border: 1px solid rgb(200, 200, 200);\n"
"    border-bottom: none;\n"
"    border-top: none;\n"
"    border-left: none;\n"
"}")
		self.separator_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.separator_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.separator_2.setObjectName("separator_2")
		self.l_time = QtWidgets.QLabel(self.frame_midle)
		self.l_time.setGeometry(QtCore.QRect(203, 8, 47, 13))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.l_time.setFont(font)
		self.l_time.setObjectName("l_time")
		self.l_input = QtWidgets.QLabel(self.frame_midle)
		self.l_input.setGeometry(QtCore.QRect(305, 6, 41, 16))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.l_input.setFont(font)
		self.l_input.setObjectName("l_input")
		self.horizontalLayout_2.addWidget(self.frame_midle)
		self.verticalLayout.addLayout(self.horizontalLayout_2)
		self.frame_bottom = QtWidgets.QFrame(self.centralwidget)
		self.frame_bottom.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.frame_bottom.sizePolicy().hasHeightForWidth())
		self.frame_bottom.setSizePolicy(sizePolicy)
		self.frame_bottom.setMinimumSize(QtCore.QSize(0, 0))
		self.frame_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_bottom.setObjectName("frame_bottom")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_bottom)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.tableWidget = QtWidgets.QTableWidget(self.frame_bottom)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
		self.tableWidget.setSizePolicy(sizePolicy)
		self.tableWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
		self.tableWidget.setStyleSheet("QTableWidget {\n"
"    gridline-color: rgb(240, 240, 240);\n"
"\n"
"}\n"
"\n"
"")
		self.tableWidget.setShowGrid(True)
		self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
		self.tableWidget.setCornerButtonEnabled(True)
		self.tableWidget.setRowCount(9)
		self.tableWidget.setColumnCount(3)
		self.tableWidget.setObjectName("tableWidget")
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(2, item)
		self.tableWidget.horizontalHeader().setVisible(True)
		self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
		self.tableWidget.horizontalHeader().setDefaultSectionSize(136)
		self.tableWidget.horizontalHeader().setHighlightSections(True)
		self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
		self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
		self.tableWidget.horizontalHeader().setStretchLastSection(True)
		self.tableWidget.verticalHeader().setVisible(False)
		self.horizontalLayout.addWidget(self.tableWidget)
		self.verticalLayout.addWidget(self.frame_bottom)
		self.frame_bottom.raise_()
		self.frame_top.raise_()
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 445, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		self.tabWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Input Recorder"))
		self.label_12.setText(_translate("MainWindow", "Handle Keyboard"))
		self.label_11.setText(_translate("MainWindow", "Handle Mouse"))
		self.label_13.setText(_translate("MainWindow", "Start delay (s)"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Record option"))
		self.label_10.setText(_translate("MainWindow", "Speed"))
		self.label_9.setText(_translate("MainWindow", "Loop"))
		self.label_8.setText(_translate("MainWindow", "Start delay (s)"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Play option"))
		self.b_load.setText(_translate("MainWindow", "Load"))
		self.b_save.setText(_translate("MainWindow", "Save"))
		self.entry_preset.setItemText(0, _translate("MainWindow", "New Item"))
		self.entry_preset.setItemText(1, _translate("MainWindow", "New Item2"))
		self.entry_preset.setItemText(2, _translate("MainWindow", "New Item3"))
		self.entry_preset.setItemText(3, _translate("MainWindow", "New Item4"))
		self.entry_preset.setItemText(4, _translate("MainWindow", "New Item5"))
		self.entry_preset.setItemText(5, _translate("MainWindow", "New Item6"))
		self.label.setText(_translate("MainWindow", "Name"))
		self.label_2.setText(_translate("MainWindow", "Preset"))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Save / Load"))
		self.b_datatable.setText(_translate("MainWindow", "Show data Table"))
		self.label_3.setText(_translate("MainWindow", " Name :"))
		self.l_name.setText(_translate("MainWindow", "None"))
		self.label_5.setText(_translate("MainWindow", "Input :"))
		self.label_6.setText(_translate("MainWindow", "Time :"))
		self.l_time.setText(_translate("MainWindow", "None"))
		self.l_input.setText(_translate("MainWindow", "None"))
		item = self.tableWidget.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Time"))
		item = self.tableWidget.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "Action"))
		item = self.tableWidget.horizontalHeaderItem(2)
		item.setText(_translate("MainWindow", "Value"))

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	OtherWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(OtherWindow)
	OtherWindow.show()
	sys.exit(app.exec_())