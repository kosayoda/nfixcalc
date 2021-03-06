# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.screen = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.screen.sizePolicy().hasHeightForWidth())
        self.screen.setSizePolicy(sizePolicy)
        self.screen.setSmallDecimalPoint(False)
        self.screen.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.screen.setProperty("intValue", 0)
        self.screen.setObjectName("screen")
        self.verticalLayout_2.addWidget(self.screen)
        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.info_label.sizePolicy().hasHeightForWidth())
        self.info_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.info_label.setFont(font)
        self.info_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.info_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.info_label.setLineWidth(0)
        self.info_label.setText("")
        self.info_label.setTextFormat(QtCore.Qt.AutoText)
        self.info_label.setObjectName("info_label")
        self.verticalLayout_2.addWidget(self.info_label, 0, QtCore.Qt.AlignVCenter)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridlayout = QtWidgets.QGridLayout(self.frame)
        self.gridlayout.setObjectName("gridlayout")
        self.key_ac = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_ac.sizePolicy().hasHeightForWidth())
        self.key_ac.setSizePolicy(sizePolicy)
        self.key_ac.setObjectName("key_ac")
        self.gridlayout.addWidget(self.key_ac, 0, 0, 1, 1)
        self.key_del = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_del.sizePolicy().hasHeightForWidth())
        self.key_del.setSizePolicy(sizePolicy)
        self.key_del.setObjectName("key_del")
        self.gridlayout.addWidget(self.key_del, 0, 1, 1, 1)
        self.key_mode = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_mode.sizePolicy().hasHeightForWidth())
        self.key_mode.setSizePolicy(sizePolicy)
        self.key_mode.setObjectName("key_mode")
        self.gridlayout.addWidget(self.key_mode, 0, 2, 1, 1)
        self.key_sign = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_sign.sizePolicy().hasHeightForWidth())
        self.key_sign.setSizePolicy(sizePolicy)
        self.key_sign.setObjectName("key_sign")
        self.gridlayout.addWidget(self.key_sign, 0, 3, 1, 1)
        self.key_quit = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_quit.sizePolicy().hasHeightForWidth())
        self.key_quit.setSizePolicy(sizePolicy)
        self.key_quit.setObjectName("key_quit")
        self.gridlayout.addWidget(self.key_quit, 0, 4, 1, 1)
        self.key_7 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_7.sizePolicy().hasHeightForWidth())
        self.key_7.setSizePolicy(sizePolicy)
        self.key_7.setObjectName("key_7")
        self.tokens = QtWidgets.QButtonGroup(MainWindow)
        self.tokens.setObjectName("tokens")
        self.tokens.addButton(self.key_7)
        self.gridlayout.addWidget(self.key_7, 1, 0, 1, 1)
        self.key_8 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_8.sizePolicy().hasHeightForWidth())
        self.key_8.setSizePolicy(sizePolicy)
        self.key_8.setObjectName("key_8")
        self.tokens.addButton(self.key_8)
        self.gridlayout.addWidget(self.key_8, 1, 1, 1, 1)
        self.key_9 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_9.sizePolicy().hasHeightForWidth())
        self.key_9.setSizePolicy(sizePolicy)
        self.key_9.setObjectName("key_9")
        self.tokens.addButton(self.key_9)
        self.gridlayout.addWidget(self.key_9, 1, 2, 1, 1)
        self.key_pow = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_pow.sizePolicy().hasHeightForWidth())
        self.key_pow.setSizePolicy(sizePolicy)
        self.key_pow.setObjectName("key_pow")
        self.tokens.addButton(self.key_pow)
        self.gridlayout.addWidget(self.key_pow, 1, 3, 1, 1)
        self.key_mod = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_mod.sizePolicy().hasHeightForWidth())
        self.key_mod.setSizePolicy(sizePolicy)
        self.key_mod.setObjectName("key_mod")
        self.tokens.addButton(self.key_mod)
        self.gridlayout.addWidget(self.key_mod, 1, 4, 1, 1)
        self.key_4 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_4.sizePolicy().hasHeightForWidth())
        self.key_4.setSizePolicy(sizePolicy)
        self.key_4.setObjectName("key_4")
        self.tokens.addButton(self.key_4)
        self.gridlayout.addWidget(self.key_4, 2, 0, 1, 1)
        self.key_5 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_5.sizePolicy().hasHeightForWidth())
        self.key_5.setSizePolicy(sizePolicy)
        self.key_5.setObjectName("key_5")
        self.tokens.addButton(self.key_5)
        self.gridlayout.addWidget(self.key_5, 2, 1, 1, 1)
        self.key_6 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_6.sizePolicy().hasHeightForWidth())
        self.key_6.setSizePolicy(sizePolicy)
        self.key_6.setObjectName("key_6")
        self.tokens.addButton(self.key_6)
        self.gridlayout.addWidget(self.key_6, 2, 2, 1, 1)
        self.key_mul = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_mul.sizePolicy().hasHeightForWidth())
        self.key_mul.setSizePolicy(sizePolicy)
        self.key_mul.setObjectName("key_mul")
        self.tokens.addButton(self.key_mul)
        self.gridlayout.addWidget(self.key_mul, 2, 3, 1, 1)
        self.key_div = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_div.sizePolicy().hasHeightForWidth())
        self.key_div.setSizePolicy(sizePolicy)
        self.key_div.setObjectName("key_div")
        self.tokens.addButton(self.key_div)
        self.gridlayout.addWidget(self.key_div, 2, 4, 1, 1)
        self.key_1 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_1.sizePolicy().hasHeightForWidth())
        self.key_1.setSizePolicy(sizePolicy)
        self.key_1.setObjectName("key_1")
        self.tokens.addButton(self.key_1)
        self.gridlayout.addWidget(self.key_1, 3, 0, 1, 1)
        self.key_2 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_2.sizePolicy().hasHeightForWidth())
        self.key_2.setSizePolicy(sizePolicy)
        self.key_2.setObjectName("key_2")
        self.tokens.addButton(self.key_2)
        self.gridlayout.addWidget(self.key_2, 3, 1, 1, 1)
        self.key_3 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_3.sizePolicy().hasHeightForWidth())
        self.key_3.setSizePolicy(sizePolicy)
        self.key_3.setObjectName("key_3")
        self.tokens.addButton(self.key_3)
        self.gridlayout.addWidget(self.key_3, 3, 2, 1, 1)
        self.key_add = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_add.sizePolicy().hasHeightForWidth())
        self.key_add.setSizePolicy(sizePolicy)
        self.key_add.setObjectName("key_add")
        self.tokens.addButton(self.key_add)
        self.gridlayout.addWidget(self.key_add, 3, 3, 1, 1)
        self.key_sub = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_sub.sizePolicy().hasHeightForWidth())
        self.key_sub.setSizePolicy(sizePolicy)
        self.key_sub.setObjectName("key_sub")
        self.tokens.addButton(self.key_sub)
        self.gridlayout.addWidget(self.key_sub, 3, 4, 1, 1)
        self.key_0 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_0.sizePolicy().hasHeightForWidth())
        self.key_0.setSizePolicy(sizePolicy)
        self.key_0.setObjectName("key_0")
        self.tokens.addButton(self.key_0)
        self.gridlayout.addWidget(self.key_0, 4, 0, 1, 1)
        self.key_period = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_period.sizePolicy().hasHeightForWidth())
        self.key_period.setSizePolicy(sizePolicy)
        self.key_period.setObjectName("key_period")
        self.tokens.addButton(self.key_period)
        self.gridlayout.addWidget(self.key_period, 4, 1, 1, 1)
        self.key_solve = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_solve.sizePolicy().hasHeightForWidth())
        self.key_solve.setSizePolicy(sizePolicy)
        self.key_solve.setObjectName("key_solve")
        self.gridlayout.addWidget(self.key_solve, 4, 2, 1, 1)
        self.key_extra1 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_extra1.sizePolicy().hasHeightForWidth())
        self.key_extra1.setSizePolicy(sizePolicy)
        self.key_extra1.setObjectName("key_extra1")
        self.gridlayout.addWidget(self.key_extra1, 4, 3, 1, 1)
        self.key_extra2 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_extra2.sizePolicy().hasHeightForWidth())
        self.key_extra2.setSizePolicy(sizePolicy)
        self.key_extra2.setObjectName("key_extra2")
        self.gridlayout.addWidget(self.key_extra2, 4, 4, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.key_quit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "nfixcalculator"))
        MainWindow.setWhatsThis(_translate("MainWindow", "A calculator for prefix, infix and postfix notation"))
        self.key_ac.setText(_translate("MainWindow", "AC"))
        self.key_ac.setShortcut(_translate("MainWindow", "Backspace"))
        self.key_del.setText(_translate("MainWindow", "Del"))
        self.key_del.setShortcut(_translate("MainWindow", "Del"))
        self.key_mode.setText(_translate("MainWindow", "Mode"))
        self.key_mode.setShortcut(_translate("MainWindow", "M"))
        self.key_sign.setText(_translate("MainWindow", "+/-"))
        self.key_sign.setShortcut(_translate("MainWindow", "Down"))
        self.key_quit.setText(_translate("MainWindow", "Quit"))
        self.key_quit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.key_7.setText(_translate("MainWindow", "7"))
        self.key_7.setShortcut(_translate("MainWindow", "7"))
        self.key_8.setText(_translate("MainWindow", "8"))
        self.key_8.setShortcut(_translate("MainWindow", "8"))
        self.key_9.setText(_translate("MainWindow", "9"))
        self.key_9.setShortcut(_translate("MainWindow", "9"))
        self.key_pow.setText(_translate("MainWindow", "^"))
        self.key_pow.setShortcut(_translate("MainWindow", "^"))
        self.key_mod.setText(_translate("MainWindow", "%"))
        self.key_mod.setShortcut(_translate("MainWindow", "%"))
        self.key_4.setText(_translate("MainWindow", "4"))
        self.key_4.setShortcut(_translate("MainWindow", "4"))
        self.key_5.setText(_translate("MainWindow", "5"))
        self.key_5.setShortcut(_translate("MainWindow", "5"))
        self.key_6.setText(_translate("MainWindow", "6"))
        self.key_6.setShortcut(_translate("MainWindow", "6"))
        self.key_mul.setText(_translate("MainWindow", "*"))
        self.key_mul.setShortcut(_translate("MainWindow", "*"))
        self.key_div.setText(_translate("MainWindow", "/"))
        self.key_div.setShortcut(_translate("MainWindow", "/"))
        self.key_1.setText(_translate("MainWindow", "1"))
        self.key_1.setShortcut(_translate("MainWindow", "1"))
        self.key_2.setText(_translate("MainWindow", "2"))
        self.key_2.setShortcut(_translate("MainWindow", "2"))
        self.key_3.setText(_translate("MainWindow", "3"))
        self.key_3.setShortcut(_translate("MainWindow", "3"))
        self.key_add.setText(_translate("MainWindow", "+"))
        self.key_add.setShortcut(_translate("MainWindow", "+"))
        self.key_sub.setText(_translate("MainWindow", "-"))
        self.key_sub.setShortcut(_translate("MainWindow", "-"))
        self.key_0.setText(_translate("MainWindow", "0"))
        self.key_0.setShortcut(_translate("MainWindow", "0"))
        self.key_period.setText(_translate("MainWindow", "."))
        self.key_period.setShortcut(_translate("MainWindow", "."))
        self.key_solve.setText(_translate("MainWindow", "Solve"))
        self.key_solve.setShortcut(_translate("MainWindow", "Return"))
        self.key_extra1.setText(_translate("MainWindow", "Enter ↑"))
        self.key_extra2.setText(_translate("MainWindow", "Check Equation"))
