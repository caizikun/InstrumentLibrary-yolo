# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dvalovcin\Documents\GitHub\MotorDriver-cloaked\motordriver\movementWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 146)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bm10 = QtWidgets.QPushButton(self.centralwidget)
        self.bm10.setObjectName("bm10")
        self.horizontalLayout_2.addWidget(self.bm10)
        self.bm05 = QtWidgets.QPushButton(self.centralwidget)
        self.bm05.setObjectName("bm05")
        self.horizontalLayout_2.addWidget(self.bm05)
        self.bm01 = QtWidgets.QPushButton(self.centralwidget)
        self.bm01.setObjectName("bm01")
        self.horizontalLayout_2.addWidget(self.bm01)
        self.sbAngle = SpinBox(self.centralwidget)
        self.sbAngle.setObjectName("sbAngle")
        self.horizontalLayout_2.addWidget(self.sbAngle)
        self.bp01 = QtWidgets.QPushButton(self.centralwidget)
        self.bp01.setObjectName("bp01")
        self.horizontalLayout_2.addWidget(self.bp01)
        self.bp05 = QtWidgets.QPushButton(self.centralwidget)
        self.bp05.setObjectName("bp05")
        self.horizontalLayout_2.addWidget(self.bp05)
        self.bp10 = QtWidgets.QPushButton(self.centralwidget)
        self.bp10.setObjectName("bp10")
        self.horizontalLayout_2.addWidget(self.bp10)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bStop = QtWidgets.QPushButton(self.centralwidget)
        self.bStop.setObjectName("bStop")
        self.horizontalLayout.addWidget(self.bStop)
        self.bGo = QtWidgets.QPushButton(self.centralwidget)
        self.bGo.setObjectName("bGo")
        self.horizontalLayout.addWidget(self.bGo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.bQuit = QtWidgets.QPushButton(self.centralwidget)
        self.bQuit.setObjectName("bQuit")
        self.horizontalLayout.addWidget(self.bQuit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tFitA = QFNumberEdit(self.centralwidget)
        self.tFitA.setMaximumSize(QtCore.QSize(30, 16777215))
        self.tFitA.setInputMask("")
        self.tFitA.setFrame(False)
        self.tFitA.setAlignment(QtCore.Qt.AlignCenter)
        self.tFitA.setObjectName("tFitA")
        self.horizontalLayout_3.addWidget(self.tFitA)
        self.labelCosCalc = QtWidgets.QLabel(self.centralwidget)
        self.labelCosCalc.setObjectName("labelCosCalc")
        self.horizontalLayout_3.addWidget(self.labelCosCalc)
        self.tFitMu = QFNumberEdit(self.centralwidget)
        self.tFitMu.setMaximumSize(QtCore.QSize(30, 16777215))
        self.tFitMu.setInputMask("")
        self.tFitMu.setFrame(False)
        self.tFitMu.setAlignment(QtCore.Qt.AlignCenter)
        self.tFitMu.setObjectName("tFitMu")
        self.horizontalLayout_3.addWidget(self.tFitMu)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.tFitC = QFNumberEdit(self.centralwidget)
        self.tFitC.setMaximumSize(QtCore.QSize(30, 16777215))
        self.tFitC.setInputMask("")
        self.tFitC.setFrame(False)
        self.tFitC.setAlignment(QtCore.Qt.AlignCenter)
        self.tFitC.setObjectName("tFitC")
        self.horizontalLayout_3.addWidget(self.tFitC)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.tCosCalc = QFNumberEdit(self.centralwidget)
        self.tCosCalc.setMaximumSize(QtCore.QSize(60, 16777215))
        self.tCosCalc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tCosCalc.setReadOnly(True)
        self.tCosCalc.setObjectName("tCosCalc")
        self.horizontalLayout_3.addWidget(self.tCosCalc)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.bCloseDevice = QtWidgets.QPushButton(self.centralwidget)
        self.bCloseDevice.setCheckable(True)
        self.bCloseDevice.setObjectName("bCloseDevice")
        self.horizontalLayout_3.addWidget(self.bCloseDevice)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 21))
        self.menubar.setObjectName("menubar")
        self.menuMore = QtWidgets.QMenu(self.menubar)
        self.menuMore.setObjectName("menuMore")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.mMoreSettings = QtWidgets.QAction(MainWindow)
        self.mMoreSettings.setObjectName("mMoreSettings")
        self.mMoreZero = QtWidgets.QAction(MainWindow)
        self.mMoreZero.setObjectName("mMoreZero")
        self.menuMore.addAction(self.mMoreSettings)
        self.menuMore.addAction(self.mMoreZero)
        self.menubar.addAction(self.menuMore.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.bm10.setText(_translate("MainWindow", "-10°", None))
        self.bm05.setText(_translate("MainWindow", "-5°", None))
        self.bm01.setText(_translate("MainWindow", "-1°", None))
        self.bp01.setText(_translate("MainWindow", "+1°", None))
        self.bp05.setText(_translate("MainWindow", "+5°", None))
        self.bp10.setText(_translate("MainWindow", "+10°", None))
        self.bStop.setText(_translate("MainWindow", "Stop", None))
        self.bGo.setText(_translate("MainWindow", "Go", None))
        self.bQuit.setText(_translate("MainWindow", "Quit", None))
        self.tFitA.setText(_translate("MainWindow", "1.0", None))
        self.labelCosCalc.setText(_translate("MainWindow", "   cos<sup>4</sup>(θ+", None))
        self.tFitMu.setText(_translate("MainWindow", "0.0", None))
        self.label.setText(_translate("MainWindow", "°)+", None))
        self.tFitC.setText(_translate("MainWindow", "0.0", None))
        self.label_2.setText(_translate("MainWindow", " = ", None))
        self.tCosCalc.setText(_translate("MainWindow", "0.0", None))
        self.bCloseDevice.setText(_translate("MainWindow", "Open Device", None))
        self.menuMore.setTitle(_translate("MainWindow", "More", None))
        self.mMoreSettings.setText(_translate("MainWindow", "Control Panel", None))
        self.mMoreZero.setText(_translate("MainWindow", "Set Zero", None))

from InstsAndQt.customQt import QFNumberEdit

from pyqtgraph import SpinBox

