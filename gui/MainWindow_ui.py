# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DSA(object):
    def setupUi(self, DSA):
        DSA.setObjectName("DSA")
        DSA.resize(813, 606)
        self.centralwidget = QtWidgets.QWidget(DSA)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageChoice = QtWidgets.QWidget()
        self.pageChoice.setObjectName("pageChoice")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.pageChoice)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.senderButton = QtWidgets.QPushButton(self.pageChoice)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.senderButton.sizePolicy().hasHeightForWidth())
        self.senderButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.senderButton.setFont(font)
        self.senderButton.setObjectName("senderButton")
        self.gridLayout_2.addWidget(self.senderButton, 0, 0, 1, 1)
        self.receiverButton = QtWidgets.QPushButton(self.pageChoice)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receiverButton.sizePolicy().hasHeightForWidth())
        self.receiverButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.receiverButton.setFont(font)
        self.receiverButton.setObjectName("receiverButton")
        self.gridLayout_2.addWidget(self.receiverButton, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.pageChoice)
        self.pageSender = QtWidgets.QWidget()
        self.pageSender.setObjectName("pageSender")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.pageSender)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textMessageSender = QtWidgets.QTextEdit(self.pageSender)
        self.textMessageSender.setObjectName("textMessageSender")
        self.gridLayout_3.addWidget(self.textMessageSender, 9, 0, 1, 3)
        self.senderParams = QtWidgets.QLabel(self.pageSender)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.senderParams.sizePolicy().hasHeightForWidth())
        self.senderParams.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.senderParams.setFont(font)
        self.senderParams.setLineWidth(-2)
        self.senderParams.setObjectName("senderParams")
        self.gridLayout_3.addWidget(self.senderParams, 0, 0, 1, 1)
        self.senderSignature = QtWidgets.QLabel(self.pageSender)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.senderSignature.sizePolicy().hasHeightForWidth())
        self.senderSignature.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.senderSignature.setFont(font)
        self.senderSignature.setLineWidth(-2)
        self.senderSignature.setObjectName("senderSignature")
        self.gridLayout_3.addWidget(self.senderSignature, 13, 1, 1, 2)
        self.saveKeysButton = QtWidgets.QPushButton(self.pageSender)
        self.saveKeysButton.setObjectName("saveKeysButton")
        self.gridLayout_3.addWidget(self.saveKeysButton, 7, 0, 1, 1)
        self.uploadKeysButton = QtWidgets.QPushButton(self.pageSender)
        self.uploadKeysButton.setObjectName("uploadKeysButton")
        self.gridLayout_3.addWidget(self.uploadKeysButton, 6, 0, 1, 1)
        self.generateParamsButton = QtWidgets.QPushButton(self.pageSender)
        self.generateParamsButton.setObjectName("generateParamsButton")
        self.gridLayout_3.addWidget(self.generateParamsButton, 1, 0, 1, 1)
        self.q_sender = QtWidgets.QLabel(self.pageSender)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.q_sender.sizePolicy().hasHeightForWidth())
        self.q_sender.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.q_sender.setFont(font)
        self.q_sender.setLineWidth(-2)
        self.q_sender.setObjectName("q_sender")
        self.gridLayout_3.addWidget(self.q_sender, 2, 2, 1, 1)
        self.g_sender = QtWidgets.QLabel(self.pageSender)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_sender.sizePolicy().hasHeightForWidth())
        self.g_sender.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.g_sender.setFont(font)
        self.g_sender.setLineWidth(-2)
        self.g_sender.setObjectName("g_sender")
        self.gridLayout_3.addWidget(self.g_sender, 3, 2, 1, 1)
        self.senderPublicKey = QtWidgets.QLabel(self.pageSender)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.senderPublicKey.sizePolicy().hasHeightForWidth())
        self.senderPublicKey.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.senderPublicKey.setFont(font)
        self.senderPublicKey.setLineWidth(-2)
        self.senderPublicKey.setObjectName("senderPublicKey")
        self.gridLayout_3.addWidget(self.senderPublicKey, 5, 1, 1, 2)
        self.senderKeys = QtWidgets.QLabel(self.pageSender)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.senderKeys.sizePolicy().hasHeightForWidth())
        self.senderKeys.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.senderKeys.setFont(font)
        self.senderKeys.setLineWidth(-2)
        self.senderKeys.setObjectName("senderKeys")
        self.gridLayout_3.addWidget(self.senderKeys, 4, 0, 1, 1)
        self.uploadParamsButton = QtWidgets.QPushButton(self.pageSender)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uploadParamsButton.sizePolicy().hasHeightForWidth())
        self.uploadParamsButton.setSizePolicy(sizePolicy)
        self.uploadParamsButton.setObjectName("uploadParamsButton")
        self.gridLayout_3.addWidget(self.uploadParamsButton, 2, 0, 1, 1)
        self.signButton = QtWidgets.QPushButton(self.pageSender)
        self.signButton.setObjectName("signButton")
        self.gridLayout_3.addWidget(self.signButton, 13, 0, 2, 1)
        self.senderMessage = QtWidgets.QLabel(self.pageSender)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.senderMessage.sizePolicy().hasHeightForWidth())
        self.senderMessage.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.senderMessage.setFont(font)
        self.senderMessage.setLineWidth(-2)
        self.senderMessage.setObjectName("senderMessage")
        self.gridLayout_3.addWidget(self.senderMessage, 8, 0, 1, 1)
        self.senderPrivatKey = QtWidgets.QLabel(self.pageSender)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.senderPrivatKey.sizePolicy().hasHeightForWidth())
        self.senderPrivatKey.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.senderPrivatKey.setFont(font)
        self.senderPrivatKey.setLineWidth(-2)
        self.senderPrivatKey.setObjectName("senderPrivatKey")
        self.gridLayout_3.addWidget(self.senderPrivatKey, 7, 1, 1, 2)
        self.p_sender = QtWidgets.QLabel(self.pageSender)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p_sender.sizePolicy().hasHeightForWidth())
        self.p_sender.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.p_sender.setFont(font)
        self.p_sender.setLineWidth(-2)
        self.p_sender.setObjectName("p_sender")
        self.gridLayout_3.addWidget(self.p_sender, 1, 2, 1, 1)
        self.generateKeysButton = QtWidgets.QPushButton(self.pageSender)
        self.generateKeysButton.setObjectName("generateKeysButton")
        self.gridLayout_3.addWidget(self.generateKeysButton, 5, 0, 1, 1)
        self.r_sender = QtWidgets.QLabel(self.pageSender)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r_sender.sizePolicy().hasHeightForWidth())
        self.r_sender.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.r_sender.setFont(font)
        self.r_sender.setLineWidth(-2)
        self.r_sender.setObjectName("r_sender")
        self.gridLayout_3.addWidget(self.r_sender, 14, 1, 1, 2)
        self.p_checkButton = QtWidgets.QPushButton(self.pageSender)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p_checkButton.sizePolicy().hasHeightForWidth())
        self.p_checkButton.setSizePolicy(sizePolicy)
        self.p_checkButton.setObjectName("p_checkButton")
        self.gridLayout_3.addWidget(self.p_checkButton, 1, 1, 1, 1)
        self.saveParamsButton = QtWidgets.QPushButton(self.pageSender)
        self.saveParamsButton.setObjectName("saveParamsButton")
        self.gridLayout_3.addWidget(self.saveParamsButton, 3, 0, 1, 1)
        self.q_checkButton = QtWidgets.QPushButton(self.pageSender)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.q_checkButton.sizePolicy().hasHeightForWidth())
        self.q_checkButton.setSizePolicy(sizePolicy)
        self.q_checkButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.q_checkButton.setObjectName("q_checkButton")
        self.gridLayout_3.addWidget(self.q_checkButton, 2, 1, 1, 1)
        self.s_sender = QtWidgets.QLabel(self.pageSender)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s_sender.sizePolicy().hasHeightForWidth())
        self.s_sender.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.s_sender.setFont(font)
        self.s_sender.setLineWidth(-2)
        self.s_sender.setObjectName("s_sender")
        self.gridLayout_3.addWidget(self.s_sender, 15, 1, 1, 2)
        self.saveButton = QtWidgets.QPushButton(self.pageSender)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout_3.addWidget(self.saveButton, 15, 0, 1, 1)
        self.senderRandK = QtWidgets.QLabel(self.pageSender)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.senderRandK.sizePolicy().hasHeightForWidth())
        self.senderRandK.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.senderRandK.setFont(font)
        self.senderRandK.setLineWidth(-2)
        self.senderRandK.setObjectName("senderRandK")
        self.gridLayout_3.addWidget(self.senderRandK, 11, 0, 1, 3)
        self.senderMessageHash = QtWidgets.QLabel(self.pageSender)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.senderMessageHash.sizePolicy().hasHeightForWidth())
        self.senderMessageHash.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.senderMessageHash.setFont(font)
        self.senderMessageHash.setLineWidth(-2)
        self.senderMessageHash.setObjectName("senderMessageHash")
        self.gridLayout_3.addWidget(self.senderMessageHash, 12, 0, 1, 3)
        self.stackedWidget.addWidget(self.pageSender)
        self.pageReciever = QtWidgets.QWidget()
        self.pageReciever.setObjectName("pageReciever")
        self.gridLayout = QtWidgets.QGridLayout(self.pageReciever)
        self.gridLayout.setObjectName("gridLayout")
        self.u2_Reciever = QtWidgets.QLabel(self.pageReciever)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.u2_Reciever.setFont(font)
        self.u2_Reciever.setObjectName("u2_Reciever")
        self.gridLayout.addWidget(self.u2_Reciever, 15, 1, 1, 3)
        self.params_Reciever = QtWidgets.QLabel(self.pageReciever)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.params_Reciever.setFont(font)
        self.params_Reciever.setObjectName("params_Reciever")
        self.gridLayout.addWidget(self.params_Reciever, 12, 0, 1, 1)
        self.uploadButtonReciever = QtWidgets.QPushButton(self.pageReciever)
        self.uploadButtonReciever.setObjectName("uploadButtonReciever")
        self.gridLayout.addWidget(self.uploadButtonReciever, 7, 0, 1, 1)
        self.publicKeySender = QtWidgets.QLabel(self.pageReciever)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.publicKeySender.setFont(font)
        self.publicKeySender.setObjectName("publicKeySender")
        self.gridLayout.addWidget(self.publicKeySender, 6, 1, 1, 3)
        self.uploadParamsKeyButton = QtWidgets.QPushButton(self.pageReciever)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uploadParamsKeyButton.sizePolicy().hasHeightForWidth())
        self.uploadParamsKeyButton.setSizePolicy(sizePolicy)
        self.uploadParamsKeyButton.setObjectName("uploadParamsKeyButton")
        self.gridLayout.addWidget(self.uploadParamsKeyButton, 2, 0, 2, 1)
        self.q_Reciever = QtWidgets.QLabel(self.pageReciever)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.q_Reciever.setFont(font)
        self.q_Reciever.setObjectName("q_Reciever")
        self.gridLayout.addWidget(self.q_Reciever, 2, 1, 1, 3)
        self.s_reciever = QtWidgets.QLabel(self.pageReciever)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.s_reciever.setFont(font)
        self.s_reciever.setObjectName("s_reciever")
        self.gridLayout.addWidget(self.s_reciever, 8, 1, 1, 3)
        self.u1_Reciever = QtWidgets.QLabel(self.pageReciever)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.u1_Reciever.setFont(font)
        self.u1_Reciever.setObjectName("u1_Reciever")
        self.gridLayout.addWidget(self.u1_Reciever, 14, 1, 1, 3)
        self.w_Reciever = QtWidgets.QLabel(self.pageReciever)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.w_Reciever.setFont(font)
        self.w_Reciever.setObjectName("w_Reciever")
        self.gridLayout.addWidget(self.w_Reciever, 13, 1, 1, 3)
        self.calculateButtonReciever = QtWidgets.QPushButton(self.pageReciever)
        self.calculateButtonReciever.setObjectName("calculateButtonReciever")
        self.gridLayout.addWidget(self.calculateButtonReciever, 14, 0, 1, 1)
        self.checkReciever = QtWidgets.QLabel(self.pageReciever)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkReciever.setFont(font)
        self.checkReciever.setObjectName("checkReciever")
        self.gridLayout.addWidget(self.checkReciever, 17, 0, 1, 2)
        self.p_Reciever = QtWidgets.QLabel(self.pageReciever)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p_Reciever.sizePolicy().hasHeightForWidth())
        self.p_Reciever.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.p_Reciever.setFont(font)
        self.p_Reciever.setObjectName("p_Reciever")
        self.gridLayout.addWidget(self.p_Reciever, 1, 1, 1, 3)
        self.r_reciever = QtWidgets.QLabel(self.pageReciever)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.r_reciever.setFont(font)
        self.r_reciever.setObjectName("r_reciever")
        self.gridLayout.addWidget(self.r_reciever, 7, 1, 1, 3)
        self.ParamsReciever = QtWidgets.QLabel(self.pageReciever)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ParamsReciever.setFont(font)
        self.ParamsReciever.setObjectName("ParamsReciever")
        self.gridLayout.addWidget(self.ParamsReciever, 0, 0, 1, 4)
        self.messageReciever = QtWidgets.QLabel(self.pageReciever)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.messageReciever.setFont(font)
        self.messageReciever.setObjectName("messageReciever")
        self.gridLayout.addWidget(self.messageReciever, 9, 0, 1, 4)
        self.g_Reciever = QtWidgets.QLabel(self.pageReciever)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.g_Reciever.setFont(font)
        self.g_Reciever.setObjectName("g_Reciever")
        self.gridLayout.addWidget(self.g_Reciever, 3, 1, 1, 3)
        self.HashMessageReciever = QtWidgets.QLabel(self.pageReciever)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.HashMessageReciever.setFont(font)
        self.HashMessageReciever.setObjectName("HashMessageReciever")
        self.gridLayout.addWidget(self.HashMessageReciever, 11, 0, 1, 1)
        self.textMessage = QtWidgets.QTextEdit(self.pageReciever)
        self.textMessage.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textMessage.setObjectName("textMessage")
        self.gridLayout.addWidget(self.textMessage, 10, 0, 1, 4)
        self.signSender = QtWidgets.QLabel(self.pageReciever)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.signSender.setFont(font)
        self.signSender.setObjectName("signSender")
        self.gridLayout.addWidget(self.signSender, 5, 0, 1, 2)
        self.v_Reciever = QtWidgets.QLabel(self.pageReciever)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.v_Reciever.setFont(font)
        self.v_Reciever.setObjectName("v_Reciever")
        self.gridLayout.addWidget(self.v_Reciever, 16, 1, 1, 3)
        self.checkButtonReciever = QtWidgets.QPushButton(self.pageReciever)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkButtonReciever.sizePolicy().hasHeightForWidth())
        self.checkButtonReciever.setSizePolicy(sizePolicy)
        self.checkButtonReciever.setObjectName("checkButtonReciever")
        self.gridLayout.addWidget(self.checkButtonReciever, 18, 0, 1, 4)
        self.stackedWidget.addWidget(self.pageReciever)
        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)
        DSA.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DSA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 20))
        self.menubar.setObjectName("menubar")
        DSA.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DSA)
        self.statusbar.setObjectName("statusbar")
        DSA.setStatusBar(self.statusbar)

        self.retranslateUi(DSA)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DSA)

    def retranslateUi(self, DSA):
        _translate = QtCore.QCoreApplication.translate
        DSA.setWindowTitle(_translate("DSA", "DSA"))
        self.senderButton.setText(_translate("DSA", "Отправитель"))
        self.receiverButton.setText(_translate("DSA", "Получатель"))
        self.senderParams.setText(_translate("DSA", "Общие параметры"))
        self.senderSignature.setText(_translate("DSA", "Подпись"))
        self.saveKeysButton.setText(_translate("DSA", "Сохранить ключи"))
        self.uploadKeysButton.setText(_translate("DSA", "Загрузить ключи"))
        self.generateParamsButton.setText(_translate("DSA", "Сгенерировать общие параметры"))
        self.q_sender.setText(_translate("DSA", "q:"))
        self.g_sender.setText(_translate("DSA", "g:"))
        self.senderPublicKey.setText(_translate("DSA", "Открытый ключ:"))
        self.senderKeys.setText(_translate("DSA", "Ключи отправителя"))
        self.uploadParamsButton.setText(_translate("DSA", "Загрузить общие параметры"))
        self.signButton.setText(_translate("DSA", "Подписать"))
        self.senderMessage.setText(_translate("DSA", "Ввод сообщения"))
        self.senderPrivatKey.setText(_translate("DSA", "Закрытый ключ:"))
        self.p_sender.setText(_translate("DSA", "p:"))
        self.generateKeysButton.setText(_translate("DSA", "Сгенерировать ключи"))
        self.r_sender.setText(_translate("DSA", "r:"))
        self.p_checkButton.setText(_translate("DSA", "!"))
        self.saveParamsButton.setText(_translate("DSA", "Сохранить общие параметры"))
        self.q_checkButton.setText(_translate("DSA", "!"))
        self.s_sender.setText(_translate("DSA", "s:"))
        self.saveButton.setText(_translate("DSA", "Сохранить"))
        self.senderRandK.setText(_translate("DSA", "k:"))
        self.senderMessageHash.setText(_translate("DSA", "Хэш сообщения:"))
        self.u2_Reciever.setText(_translate("DSA", "u2:"))
        self.params_Reciever.setText(_translate("DSA", "Вычисляемые параметры"))
        self.uploadButtonReciever.setText(_translate("DSA", "Загрузить сообщение"))
        self.publicKeySender.setText(_translate("DSA", "Открытый ключ:"))
        self.uploadParamsKeyButton.setText(_translate("DSA", "     Загрузить параметры   "))
        self.q_Reciever.setText(_translate("DSA", "q:"))
        self.s_reciever.setText(_translate("DSA", "s:"))
        self.u1_Reciever.setText(_translate("DSA", "u1:"))
        self.w_Reciever.setText(_translate("DSA", "w:"))
        self.calculateButtonReciever.setText(_translate("DSA", "Вычислить параметры"))
        self.checkReciever.setText(_translate("DSA", "Проверка подписи"))
        self.p_Reciever.setText(_translate("DSA", "p:"))
        self.r_reciever.setText(_translate("DSA", "r:"))
        self.ParamsReciever.setText(_translate("DSA", "Общие параметры и открытый ключ отправителя"))
        self.messageReciever.setText(_translate("DSA", "Полученное сообщение"))
        self.g_Reciever.setText(_translate("DSA", "g:"))
        self.HashMessageReciever.setText(_translate("DSA", "Хэш сообщения:"))
        self.signSender.setText(_translate("DSA", "Подпись отправителя"))
        self.v_Reciever.setText(_translate("DSA", "v:"))
        self.checkButtonReciever.setText(_translate("DSA", "Проверить подпись"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DSA = QtWidgets.QMainWindow()
    ui = Ui_DSA()
    ui.setupUi(DSA)
    DSA.show()
    sys.exit(app.exec_())
