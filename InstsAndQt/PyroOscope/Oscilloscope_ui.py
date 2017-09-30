# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\FELLab\Documents\GitHub\InstrumentLibrary-yolo\InstsAndQt\PyroOscope\Oscilloscope.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Oscilloscope(object):
    def setupUi(self, Oscilloscope):
        Oscilloscope.setObjectName("Oscilloscope")
        Oscilloscope.resize(741, 543)
        self.verticalLayout = QtWidgets.QVBoxLayout(Oscilloscope)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Oscilloscope)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gOsc = PlotWidget(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gOsc.sizePolicy().hasHeightForWidth())
        self.gOsc.setSizePolicy(sizePolicy)
        self.gOsc.setObjectName("gOsc")
        self.verticalLayout_2.addWidget(self.gOsc)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.bOscInit = QtWidgets.QPushButton(self.tab_4)
        self.bOscInit.setObjectName("bOscInit")
        self.horizontalLayout_4.addWidget(self.bOscInit)
        self.bOPop = QtWidgets.QPushButton(self.tab_4)
        self.bOPop.setObjectName("bOPop")
        self.horizontalLayout_4.addWidget(self.bOPop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.bLogDir = QtWidgets.QPushButton(self.tab_5)
        self.bLogDir.setObjectName("bLogDir")
        self.horizontalLayout_7.addWidget(self.bLogDir)
        self.bLogData = QtWidgets.QPushButton(self.tab_5)
        self.bLogData.setCheckable(True)
        self.bLogData.setObjectName("bLogData")
        self.horizontalLayout_7.addWidget(self.bLogData)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_29 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_29.setFlat(True)
        self.groupBox_29.setObjectName("groupBox_29")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.groupBox_29)
        self.horizontalLayout_27.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.tCdSt = QFNumberEdit(self.groupBox_29)
        self.tCdSt.setObjectName("tCdSt")
        self.horizontalLayout_27.addWidget(self.tCdSt)
        self.gridLayout_5.addWidget(self.groupBox_29, 0, 2, 1, 1)
        self.groupBox_30 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_30.setFlat(True)
        self.groupBox_30.setObjectName("groupBox_30")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.groupBox_30)
        self.horizontalLayout_28.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.tCdEn = QFNumberEdit(self.groupBox_30)
        self.tCdEn.setObjectName("tCdEn")
        self.horizontalLayout_28.addWidget(self.tCdEn)
        self.gridLayout_5.addWidget(self.groupBox_30, 1, 2, 1, 1)
        self.groupBox_27 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_27.setFlat(True)
        self.groupBox_27.setObjectName("groupBox_27")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.groupBox_27)
        self.horizontalLayout_25.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.tFpSt = QFNumberEdit(self.groupBox_27)
        self.tFpSt.setObjectName("tFpSt")
        self.horizontalLayout_25.addWidget(self.tFpSt)
        self.gridLayout_5.addWidget(self.groupBox_27, 0, 1, 1, 1)
        self.groupBox_28 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_28.setFlat(True)
        self.groupBox_28.setObjectName("groupBox_28")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.groupBox_28)
        self.horizontalLayout_26.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.tFpEn = QFNumberEdit(self.groupBox_28)
        self.tFpEn.setObjectName("tFpEn")
        self.horizontalLayout_26.addWidget(self.tFpEn)
        self.gridLayout_5.addWidget(self.groupBox_28, 1, 1, 1, 1)
        self.groupBox_25 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_25.setFlat(True)
        self.groupBox_25.setObjectName("groupBox_25")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.groupBox_25)
        self.horizontalLayout_23.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.tBgSt = QFNumberEdit(self.groupBox_25)
        self.tBgSt.setText("")
        self.tBgSt.setObjectName("tBgSt")
        self.horizontalLayout_23.addWidget(self.tBgSt)
        self.gridLayout_5.addWidget(self.groupBox_25, 0, 0, 1, 1)
        self.groupBox_26 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_26.setFlat(True)
        self.groupBox_26.setObjectName("groupBox_26")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.groupBox_26)
        self.horizontalLayout_24.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.tBgEn = QFNumberEdit(self.groupBox_26)
        self.tBgEn.setText("")
        self.tBgEn.setObjectName("tBgEn")
        self.horizontalLayout_24.addWidget(self.tBgEn)
        self.gridLayout_5.addWidget(self.groupBox_26, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_5)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_10.setFlat(True)
        self.groupBox_10.setObjectName("groupBox_10")
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_45.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.tOscPulses = QtWidgets.QLineEdit(self.groupBox_10)
        self.tOscPulses.setEnabled(False)
        self.tOscPulses.setObjectName("tOscPulses")
        self.horizontalLayout_45.addWidget(self.tOscPulses)
        self.gridLayout.addWidget(self.groupBox_10, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cPyroMode = QtWidgets.QComboBox(self.groupBox)
        self.cPyroMode.setObjectName("cPyroMode")
        self.cPyroMode.addItem("")
        self.cPyroMode.addItem("")
        self.horizontalLayout_2.addWidget(self.cPyroMode)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cFELCoupler = QtWidgets.QComboBox(self.groupBox_2)
        self.cFELCoupler.setObjectName("cFELCoupler")
        self.cFELCoupler.addItem("")
        self.cFELCoupler.addItem("")
        self.horizontalLayout_3.addWidget(self.cFELCoupler)
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 3, 1, 1)
        self.groupBox_53 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_53.setFlat(True)
        self.groupBox_53.setObjectName("groupBox_53")
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout(self.groupBox_53)
        self.horizontalLayout_47.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.tOscCDRatio = QFNumberEdit(self.groupBox_53)
        self.tOscCDRatio.setObjectName("tOscCDRatio")
        self.horizontalLayout_47.addWidget(self.tOscCDRatio)
        self.gridLayout.addWidget(self.groupBox_53, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_55 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_55.setFlat(True)
        self.groupBox_55.setObjectName("groupBox_55")
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout(self.groupBox_55)
        self.horizontalLayout_53.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.tSpotSize = QFNumberEdit(self.groupBox_55)
        self.tSpotSize.setObjectName("tSpotSize")
        self.horizontalLayout_53.addWidget(self.tSpotSize)
        self.gridLayout_2.addWidget(self.groupBox_55, 1, 1, 1, 1)
        self.groupBox_39 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_39.setFlat(True)
        self.groupBox_39.setCheckable(False)
        self.groupBox_39.setObjectName("groupBox_39")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_39)
        self.gridLayout_9.setContentsMargins(0, 10, 0, 0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.tFELFreq = QFNumberEdit(self.groupBox_39)
        self.tFELFreq.setObjectName("tFELFreq")
        self.gridLayout_9.addWidget(self.tFELFreq, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_39, 1, 0, 1, 1)
        self.groupBox_58 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_58.setFlat(True)
        self.groupBox_58.setObjectName("groupBox_58")
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout(self.groupBox_58)
        self.horizontalLayout_55.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.tEffectiveField = QFNumberEdit(self.groupBox_58)
        self.tEffectiveField.setObjectName("tEffectiveField")
        self.horizontalLayout_55.addWidget(self.tEffectiveField)
        self.gridLayout_2.addWidget(self.groupBox_58, 1, 3, 1, 1)
        self.groupBox_57 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_57.setFlat(True)
        self.groupBox_57.setObjectName("groupBox_57")
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout(self.groupBox_57)
        self.horizontalLayout_51.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.tWindowTransmission = QFNumberEdit(self.groupBox_57)
        self.tWindowTransmission.setObjectName("tWindowTransmission")
        self.horizontalLayout_51.addWidget(self.tWindowTransmission)
        self.gridLayout_2.addWidget(self.groupBox_57, 1, 2, 1, 1)
        self.groupBox_41 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_41.setFlat(True)
        self.groupBox_41.setCheckable(False)
        self.groupBox_41.setObjectName("groupBox_41")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_41)
        self.gridLayout_11.setContentsMargins(0, 10, 0, 0)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.tFELRR = QtWidgets.QLineEdit(self.groupBox_41)
        self.tFELRR.setObjectName("tFELRR")
        self.gridLayout_11.addWidget(self.tFELRR, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_41, 1, 4, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tFELPol = QtWidgets.QLineEdit(self.groupBox_3)
        self.tFELPol.setObjectName("tFELPol")
        self.horizontalLayout_5.addWidget(self.tFELPol)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 4, 1, 1)
        self.groupBox_60 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_60.setEnabled(False)
        self.groupBox_60.setFlat(True)
        self.groupBox_60.setObjectName("groupBox_60")
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout(self.groupBox_60)
        self.horizontalLayout_57.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        self.tIntensity = QtWidgets.QLineEdit(self.groupBox_60)
        self.tIntensity.setObjectName("tIntensity")
        self.horizontalLayout_57.addWidget(self.tIntensity)
        self.gridLayout_2.addWidget(self.groupBox_60, 0, 3, 1, 1)
        self.groupBox_59 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_59.setEnabled(False)
        self.groupBox_59.setFlat(True)
        self.groupBox_59.setObjectName("groupBox_59")
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout(self.groupBox_59)
        self.horizontalLayout_56.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.tEField = QtWidgets.QLineEdit(self.groupBox_59)
        self.tEField.setObjectName("tEField")
        self.horizontalLayout_56.addWidget(self.tEField)
        self.gridLayout_2.addWidget(self.groupBox_59, 0, 2, 1, 1)
        self.groupBox_40 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_40.setFlat(True)
        self.groupBox_40.setCheckable(False)
        self.groupBox_40.setObjectName("groupBox_40")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_40)
        self.gridLayout_10.setContentsMargins(0, 10, 0, 0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.tFELP = QFNumberEdit(self.groupBox_40)
        self.tFELP.setEnabled(False)
        self.tFELP.setReadOnly(True)
        self.tFELP.setObjectName("tFELP")
        self.gridLayout_10.addWidget(self.tFELP, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_40, 0, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tCalFactor = QFNumberEdit(self.groupBox_4)
        self.tCalFactor.setObjectName("tCalFactor")
        self.horizontalLayout_6.addWidget(self.tCalFactor)
        self.gridLayout_2.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.oscControlsWidget = QtWidgets.QWidget(Oscilloscope)
        self.oscControlsWidget.setObjectName("oscControlsWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.oscControlsWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bOPause = QtWidgets.QPushButton(self.oscControlsWidget)
        self.bOPause.setCheckable(True)
        self.bOPause.setChecked(True)
        self.bOPause.setObjectName("bOPause")
        self.horizontalLayout.addWidget(self.bOPause)
        self.groupBox_31 = QtWidgets.QGroupBox(self.oscControlsWidget)
        self.groupBox_31.setFlat(True)
        self.groupBox_31.setObjectName("groupBox_31")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.groupBox_31)
        self.horizontalLayout_29.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.cOGPIB = InstrumentGPIB(self.groupBox_31)
        self.cOGPIB.setObjectName("cOGPIB")
        self.horizontalLayout_29.addWidget(self.cOGPIB)
        self.horizontalLayout.addWidget(self.groupBox_31)
        self.groupBox_32 = QtWidgets.QGroupBox(self.oscControlsWidget)
        self.groupBox_32.setFlat(True)
        self.groupBox_32.setObjectName("groupBox_32")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.groupBox_32)
        self.horizontalLayout_30.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.cOChannel = QtWidgets.QComboBox(self.groupBox_32)
        self.cOChannel.setObjectName("cOChannel")
        self.cOChannel.addItem("")
        self.cOChannel.addItem("")
        self.cOChannel.addItem("")
        self.cOChannel.addItem("")
        self.horizontalLayout_30.addWidget(self.cOChannel)
        self.horizontalLayout.addWidget(self.groupBox_32)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.oscControlsWidget)

        self.retranslateUi(Oscilloscope)
        self.tabWidget.setCurrentIndex(0)
        self.cPyroMode.setCurrentIndex(1)
        self.cOChannel.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Oscilloscope)
        Oscilloscope.setTabOrder(self.tBgSt, self.tFpSt)
        Oscilloscope.setTabOrder(self.tFpSt, self.tCdSt)
        Oscilloscope.setTabOrder(self.tCdSt, self.tBgEn)
        Oscilloscope.setTabOrder(self.tBgEn, self.tFpEn)
        Oscilloscope.setTabOrder(self.tFpEn, self.tCdEn)
        Oscilloscope.setTabOrder(self.tCdEn, self.tOscPulses)
        Oscilloscope.setTabOrder(self.tOscPulses, self.tOscCDRatio)
        Oscilloscope.setTabOrder(self.tOscCDRatio, self.cPyroMode)
        Oscilloscope.setTabOrder(self.cPyroMode, self.cFELCoupler)
        Oscilloscope.setTabOrder(self.cFELCoupler, self.tCalFactor)
        Oscilloscope.setTabOrder(self.tCalFactor, self.tFELP)
        Oscilloscope.setTabOrder(self.tFELP, self.tEField)
        Oscilloscope.setTabOrder(self.tEField, self.tIntensity)
        Oscilloscope.setTabOrder(self.tIntensity, self.tFELPol)
        Oscilloscope.setTabOrder(self.tFELPol, self.tFELFreq)
        Oscilloscope.setTabOrder(self.tFELFreq, self.tSpotSize)
        Oscilloscope.setTabOrder(self.tSpotSize, self.tWindowTransmission)
        Oscilloscope.setTabOrder(self.tWindowTransmission, self.tEffectiveField)
        Oscilloscope.setTabOrder(self.tEffectiveField, self.tFELRR)
        Oscilloscope.setTabOrder(self.tFELRR, self.bOPause)
        Oscilloscope.setTabOrder(self.bOPause, self.cOGPIB)
        Oscilloscope.setTabOrder(self.cOGPIB, self.cOChannel)
        Oscilloscope.setTabOrder(self.cOChannel, self.bLogDir)
        Oscilloscope.setTabOrder(self.bLogDir, self.bLogData)
        Oscilloscope.setTabOrder(self.bLogData, self.tabWidget)
        Oscilloscope.setTabOrder(self.tabWidget, self.gOsc)
        Oscilloscope.setTabOrder(self.gOsc, self.bOPop)
        Oscilloscope.setTabOrder(self.bOPop, self.bOscInit)

    def retranslateUi(self, Oscilloscope):
        _translate = QtCore.QCoreApplication.translate
        Oscilloscope.setWindowTitle(_translate("Oscilloscope", "Form"))
        self.bOscInit.setText(_translate("Oscilloscope", "Initialize Regions"))
        self.bOPop.setText(_translate("Oscilloscope", "Pop Out"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Oscilloscope", "Waveform"))
        self.bLogDir.setText(_translate("Oscilloscope", "Choose Dir..."))
        self.bLogData.setText(_translate("Oscilloscope", "Log Pulses"))
        self.groupBox_29.setTitle(_translate("Oscilloscope", "Cavity Dump Start"))
        self.groupBox_30.setTitle(_translate("Oscilloscope", "Cavity Dump End"))
        self.groupBox_27.setTitle(_translate("Oscilloscope", "Front Porch Start"))
        self.groupBox_28.setTitle(_translate("Oscilloscope", "Front Porch End"))
        self.groupBox_25.setTitle(_translate("Oscilloscope", "Background Start"))
        self.groupBox_26.setTitle(_translate("Oscilloscope", "Background End"))
        self.groupBox_10.setTitle(_translate("Oscilloscope", "No. Pulses"))
        self.groupBox.setTitle(_translate("Oscilloscope", "Pyro Mode"))
        self.cPyroMode.setItemText(0, _translate("Oscilloscope", "Instant"))
        self.cPyroMode.setItemText(1, _translate("Oscilloscope", "Integrating"))
        self.groupBox_2.setTitle(_translate("Oscilloscope", "Coupler"))
        self.cFELCoupler.setItemText(0, _translate("Oscilloscope", "Cavity Dump"))
        self.cFELCoupler.setItemText(1, _translate("Oscilloscope", "Hole"))
        self.groupBox_53.setTitle(_translate("Oscilloscope", "CD Ratio"))
        self.tOscCDRatio.setText(_translate("Oscilloscope", "0.007"))
        self.groupBox_55.setTitle(_translate("Oscilloscope", "Spot Size(cm)"))
        self.tSpotSize.setToolTip(_translate("Oscilloscope", "Radius of FEL spot size"))
        self.tSpotSize.setText(_translate("Oscilloscope", "0.05"))
        self.groupBox_39.setTitle(_translate("Oscilloscope", "FEL Freq (cm-1)"))
        self.tFELFreq.setText(_translate("Oscilloscope", "0"))
        self.groupBox_58.setTitle(_translate("Oscilloscope", "Sample E_eff"))
        self.tEffectiveField.setText(_translate("Oscilloscope", "1.0"))
        self.groupBox_57.setTitle(_translate("Oscilloscope", "Window Trans"))
        self.tWindowTransmission.setText(_translate("Oscilloscope", "1.0"))
        self.groupBox_41.setTitle(_translate("Oscilloscope", "Rep Rate (Hz)"))
        self.tFELRR.setText(_translate("Oscilloscope", "1.07"))
        self.groupBox_3.setTitle(_translate("Oscilloscope", "FEL Pol"))
        self.tFELPol.setText(_translate("Oscilloscope", "H"))
        self.groupBox_60.setTitle(_translate("Oscilloscope", "I (kW/cm2)"))
        self.tIntensity.setText(_translate("Oscilloscope", "0.0"))
        self.groupBox_59.setTitle(_translate("Oscilloscope", "E (kV/cm)"))
        self.tEField.setText(_translate("Oscilloscope", "0.0"))
        self.groupBox_40.setTitle(_translate("Oscilloscope", "FEL Energy (mJ)"))
        self.tFELP.setText(_translate("Oscilloscope", "0"))
        self.groupBox_4.setTitle(_translate("Oscilloscope", "Pyro Cal (mJ/mV)"))
        self.tCalFactor.setText(_translate("Oscilloscope", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Oscilloscope", "Misc Settings"))
        self.bOPause.setText(_translate("Oscilloscope", "Pause"))
        self.groupBox_31.setTitle(_translate("Oscilloscope", "GPIB"))
        self.cOGPIB.setToolTip(_translate("Oscilloscope", "GPIB0::5::INSTR"))
        self.groupBox_32.setTitle(_translate("Oscilloscope", "Channel"))
        self.cOChannel.setItemText(0, _translate("Oscilloscope", "1"))
        self.cOChannel.setItemText(1, _translate("Oscilloscope", "2"))
        self.cOChannel.setItemText(2, _translate("Oscilloscope", "3"))
        self.cOChannel.setItemText(3, _translate("Oscilloscope", "4"))

from InstsAndQt.customQt import QFNumberEdit
from InstsAndQt.instrumentgpib import InstrumentGPIB
from pyqtgraph import PlotWidget
