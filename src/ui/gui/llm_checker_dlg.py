# Form implementation generated from reading ui file 'llm_checker_dlg.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgLlmChecker(object):
    def setupUi(self, dlgLlmChecker):
        dlgLlmChecker.setObjectName("dlgLlmChecker")
        dlgLlmChecker.resize(1017, 772)
        dlgLlmChecker.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(dlgLlmChecker)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.freSetting = QtWidgets.QFrame(parent=dlgLlmChecker)
        self.freSetting.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.freSetting.setObjectName("freSetting")
        self.vlytSetting = QtWidgets.QVBoxLayout(self.freSetting)
        self.vlytSetting.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinAndMaxSize)
        self.vlytSetting.setContentsMargins(4, 2, 4, 2)
        self.vlytSetting.setSpacing(2)
        self.vlytSetting.setObjectName("vlytSetting")
        self.freLLM = QtWidgets.QFrame(parent=self.freSetting)
        self.freLLM.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.freLLM.setObjectName("freLLM")
        self.hlytLLM = QtWidgets.QHBoxLayout(self.freLLM)
        self.hlytLLM.setContentsMargins(10, 4, 10, 4)
        self.hlytLLM.setObjectName("hlytLLM")
        self.lblLLM = QtWidgets.QLabel(parent=self.freLLM)
        self.lblLLM.setObjectName("lblLLM")
        self.hlytLLM.addWidget(self.lblLLM)
        self.lblApiKey = QtWidgets.QLabel(parent=self.freLLM)
        self.lblApiKey.setObjectName("lblApiKey")
        self.hlytLLM.addWidget(self.lblApiKey)
        self.edtAPiKey = QtWidgets.QLineEdit(parent=self.freLLM)
        self.edtAPiKey.setObjectName("edtAPiKey")
        self.hlytLLM.addWidget(self.edtAPiKey)
        self.lblBaseUrl = QtWidgets.QLabel(parent=self.freLLM)
        self.lblBaseUrl.setObjectName("lblBaseUrl")
        self.hlytLLM.addWidget(self.lblBaseUrl)
        self.edtBaseUrl = QtWidgets.QLineEdit(parent=self.freLLM)
        self.edtBaseUrl.setObjectName("edtBaseUrl")
        self.hlytLLM.addWidget(self.edtBaseUrl)
        self.hlytLLM.setStretch(2, 3)
        self.hlytLLM.setStretch(4, 2)
        self.vlytSetting.addWidget(self.freLLM)
        self.freTranslate = QtWidgets.QFrame(parent=self.freSetting)
        self.freTranslate.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.freTranslate.setObjectName("freTranslate")
        self.hlytTranslate = QtWidgets.QHBoxLayout(self.freTranslate)
        self.hlytTranslate.setContentsMargins(10, 4, 10, 4)
        self.hlytTranslate.setObjectName("hlytTranslate")
        self.lblLlmModel = QtWidgets.QLabel(parent=self.freTranslate)
        self.lblLlmModel.setObjectName("lblLlmModel")
        self.hlytTranslate.addWidget(self.lblLlmModel)
        self.cbbLlmModel = QtWidgets.QComboBox(parent=self.freTranslate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.cbbLlmModel.sizePolicy().hasHeightForWidth())
        self.cbbLlmModel.setSizePolicy(sizePolicy)
        self.cbbLlmModel.setObjectName("cbbLlmModel")
        self.cbbLlmModel.addItem("")
        self.hlytTranslate.addWidget(self.cbbLlmModel)
        self.btnLlmRefresh = QtWidgets.QPushButton(parent=self.freTranslate)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../resources/images/icons/更新.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnLlmRefresh.setIcon(icon)
        self.btnLlmRefresh.setObjectName("btnLlmRefresh")
        self.hlytTranslate.addWidget(self.btnLlmRefresh)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hlytTranslate.addItem(spacerItem)
        self.hlytTranslate.setStretch(1, 1)
        self.hlytTranslate.setStretch(3, 2)
        self.vlytSetting.addWidget(self.freTranslate)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.vlytSetting.addItem(spacerItem1)
        self.line = QtWidgets.QFrame(parent=self.freSetting)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.vlytSetting.addWidget(self.line)
        self.tabwtLLM = QtWidgets.QTabWidget(parent=self.freSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabwtLLM.sizePolicy().hasHeightForWidth())
        self.tabwtLLM.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.tabwtLLM.setFont(font)
        self.tabwtLLM.setObjectName("tabwtLLM")
        self.tabChat = QtWidgets.QWidget()
        self.tabChat.setObjectName("tabChat")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabChat)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalFrame = QtWidgets.QFrame(parent=self.tabChat)
        self.horizontalFrame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_4.setContentsMargins(10, 4, -1, 4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnSavePrompt = QtWidgets.QToolButton(parent=self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSavePrompt.sizePolicy().hasHeightForWidth())
        self.btnSavePrompt.setSizePolicy(sizePolicy)
        self.btnSavePrompt.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        font.setBold(True)
        self.btnSavePrompt.setFont(font)
        self.btnSavePrompt.setToolTipDuration(-1)
        self.btnSavePrompt.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../resources/images/icons/保存.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnSavePrompt.setIcon(icon1)
        self.btnSavePrompt.setAutoRepeatInterval(100)
        self.btnSavePrompt.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.btnSavePrompt.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.btnSavePrompt.setAutoRaise(False)
        self.btnSavePrompt.setArrowType(QtCore.Qt.ArrowType.NoArrow)
        self.btnSavePrompt.setObjectName("btnSavePrompt")
        self.horizontalLayout_4.addWidget(self.btnSavePrompt)
        self.btnSaveAs = QtWidgets.QPushButton(parent=self.horizontalFrame)
        self.btnSaveAs.setObjectName("btnSaveAs")
        self.horizontalLayout_4.addWidget(self.btnSaveAs)
        self.lblPrompt = QtWidgets.QLabel(parent=self.horizontalFrame)
        self.lblPrompt.setObjectName("lblPrompt")
        self.horizontalLayout_4.addWidget(self.lblPrompt)
        self.cbbPrompt = QtWidgets.QComboBox(parent=self.horizontalFrame)
        self.cbbPrompt.setObjectName("cbbPrompt")
        self.horizontalLayout_4.addWidget(self.cbbPrompt)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_4.setStretch(3, 1)
        self.horizontalLayout_4.setStretch(4, 2)
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.txtPrompt = QtWidgets.QTextEdit(parent=self.tabChat)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtPrompt.sizePolicy().hasHeightForWidth())
        self.txtPrompt.setSizePolicy(sizePolicy)
        self.txtPrompt.setAutoFillBackground(False)
        self.txtPrompt.setStyleSheet("")
        self.txtPrompt.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.txtPrompt.setObjectName("txtPrompt")
        self.verticalLayout.addWidget(self.txtPrompt)
        self.fraChat = QtWidgets.QFrame(parent=self.tabChat)
        self.fraChat.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fraChat.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fraChat.setObjectName("fraChat")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fraChat)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.vlytChat = QtWidgets.QVBoxLayout()
        self.vlytChat.setSpacing(2)
        self.vlytChat.setObjectName("vlytChat")
        self.edtChatMsg = QtWidgets.QTextEdit(parent=self.fraChat)
        self.edtChatMsg.setStyleSheet("")
        self.edtChatMsg.setObjectName("edtChatMsg")
        self.vlytChat.addWidget(self.edtChatMsg)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ckbHistory = QtWidgets.QCheckBox(parent=self.fraChat)
        self.ckbHistory.setObjectName("ckbHistory")
        self.horizontalLayout_3.addWidget(self.ckbHistory)
        self.spbHistoryNum = QtWidgets.QSpinBox(parent=self.fraChat)
        self.spbHistoryNum.setMinimum(2)
        self.spbHistoryNum.setMaximum(20)
        self.spbHistoryNum.setSingleStep(2)
        self.spbHistoryNum.setProperty("value", 8)
        self.spbHistoryNum.setObjectName("spbHistoryNum")
        self.horizontalLayout_3.addWidget(self.spbHistoryNum)
        self.ckbUsePrompt = QtWidgets.QCheckBox(parent=self.fraChat)
        self.ckbUsePrompt.setObjectName("ckbUsePrompt")
        self.horizontalLayout_3.addWidget(self.ckbUsePrompt)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btnSendMsg = QtWidgets.QPushButton(parent=self.fraChat)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btnSendMsg.setFont(font)
        self.btnSendMsg.setObjectName("btnSendMsg")
        self.horizontalLayout_3.addWidget(self.btnSendMsg)
        self.vlytChat.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.vlytChat)
        self.txtShowMsg = QtWidgets.QTextEdit(parent=self.fraChat)
        self.txtShowMsg.setStyleSheet("background: rgb(193, 231, 217)")
        self.txtShowMsg.setObjectName("txtShowMsg")
        self.horizontalLayout_2.addWidget(self.txtShowMsg)
        self.verticalLayout.addWidget(self.fraChat)
        self.tabwtLLM.addTab(self.tabChat, "")
        self.tabSubtitle = QtWidgets.QWidget()
        self.tabSubtitle.setObjectName("tabSubtitle")
        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.tabSubtitle)
        self.verticalLayout1.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout1.setObjectName("verticalLayout1")
        self.freTools = QtWidgets.QFrame(parent=self.tabSubtitle)
        self.freTools.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.freTools.setMidLineWidth(1)
        self.freTools.setObjectName("freTools")
        self.hlytTool = QtWidgets.QHBoxLayout(self.freTools)
        self.hlytTool.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.hlytTool.setContentsMargins(4, 6, 4, 6)
        self.hlytTool.setObjectName("hlytTool")
        self.btnOpenDemo = QtWidgets.QToolButton(parent=self.freTools)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpenDemo.sizePolicy().hasHeightForWidth())
        self.btnOpenDemo.setSizePolicy(sizePolicy)
        self.btnOpenDemo.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        font.setBold(True)
        self.btnOpenDemo.setFont(font)
        self.btnOpenDemo.setToolTipDuration(-1)
        self.btnOpenDemo.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btnOpenDemo.setStyleSheet("color: red")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../resources/images/icons/打开.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnOpenDemo.setIcon(icon2)
        self.btnOpenDemo.setAutoRepeatInterval(100)
        self.btnOpenDemo.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.btnOpenDemo.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.btnOpenDemo.setAutoRaise(False)
        self.btnOpenDemo.setArrowType(QtCore.Qt.ArrowType.NoArrow)
        self.btnOpenDemo.setObjectName("btnOpenDemo")
        self.hlytTool.addWidget(self.btnOpenDemo)
        self.btnRun = QtWidgets.QToolButton(parent=self.freTools)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRun.sizePolicy().hasHeightForWidth())
        self.btnRun.setSizePolicy(sizePolicy)
        self.btnRun.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        font.setBold(True)
        self.btnRun.setFont(font)
        self.btnRun.setToolTipDuration(-1)
        self.btnRun.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btnRun.setStyleSheet("color: rgb(255, 170, 0)")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../resources/images/icons/启动.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnRun.setIcon(icon3)
        self.btnRun.setAutoRepeatInterval(100)
        self.btnRun.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.btnRun.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.btnRun.setAutoRaise(False)
        self.btnRun.setArrowType(QtCore.Qt.ArrowType.NoArrow)
        self.btnRun.setObjectName("btnRun")
        self.hlytTool.addWidget(self.btnRun)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblLanguage = QtWidgets.QLabel(parent=self.freTools)
        self.lblLanguage.setObjectName("lblLanguage")
        self.horizontalLayout.addWidget(self.lblLanguage)
        self.cbbTargetLanguage = QtWidgets.QComboBox(parent=self.freTools)
        self.cbbTargetLanguage.setObjectName("cbbTargetLanguage")
        self.horizontalLayout.addWidget(self.cbbTargetLanguage)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.hlytTool.addLayout(self.horizontalLayout)
        self.verticalLayout1.addWidget(self.freTools)
        self.tbvDemo = QtWidgets.QTableView(parent=self.tabSubtitle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbvDemo.sizePolicy().hasHeightForWidth())
        self.tbvDemo.setSizePolicy(sizePolicy)
        self.tbvDemo.setBaseSize(QtCore.QSize(0, 0))
        self.tbvDemo.setStyleSheet("")
        self.tbvDemo.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.tbvDemo.setObjectName("tbvDemo")
        self.verticalLayout1.addWidget(self.tbvDemo)
        self.tabwtLLM.addTab(self.tabSubtitle, "")
        self.vlytSetting.addWidget(self.tabwtLLM)
        self.vlytSetting.setStretch(4, 2)
        self.verticalLayout_2.addWidget(self.freSetting)

        self.retranslateUi(dlgLlmChecker)
        self.tabwtLLM.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dlgLlmChecker)

    def retranslateUi(self, dlgLlmChecker):
        _translate = QtCore.QCoreApplication.translate
        dlgLlmChecker.setWindowTitle(_translate("dlgLlmChecker", "LLM 检测器"))
        self.lblLLM.setText(_translate("dlgLlmChecker", "LLM 配置："))
        self.lblApiKey.setText(_translate("dlgLlmChecker", "API Key"))
        self.lblBaseUrl.setText(_translate("dlgLlmChecker", "Base URL"))
        self.lblLlmModel.setText(_translate("dlgLlmChecker", "模型"))
        self.cbbLlmModel.setItemText(0, _translate("dlgLlmChecker", "gemma2:latest"))
        self.btnLlmRefresh.setText(_translate("dlgLlmChecker", "更新模型"))
        self.btnSavePrompt.setText(_translate("dlgLlmChecker", "保存提示语"))
        self.btnSaveAs.setText(_translate("dlgLlmChecker", "另存为..."))
        self.lblPrompt.setText(_translate("dlgLlmChecker", "提示语"))
        self.txtPrompt.setHtml(_translate("dlgLlmChecker", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p></body></html>"))
        self.ckbHistory.setText(_translate("dlgLlmChecker", "支持上下文"))
        self.ckbUsePrompt.setText(_translate("dlgLlmChecker", "使用提示语"))
        self.btnSendMsg.setText(_translate("dlgLlmChecker", "发送"))
        self.tabwtLLM.setTabText(self.tabwtLLM.indexOf(self.tabChat), _translate("dlgLlmChecker", "聊天模式"))
        self.btnOpenDemo.setText(_translate("dlgLlmChecker", "打开字幕样本"))
        self.btnRun.setText(_translate("dlgLlmChecker", " 导出台词"))
        self.lblLanguage.setText(_translate("dlgLlmChecker", "目标语言"))
        self.tabwtLLM.setTabText(self.tabwtLLM.indexOf(self.tabSubtitle), _translate("dlgLlmChecker", "字幕模式"))
