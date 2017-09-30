# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\FELLab\Documents\GitHub\InstrumentLibrary-yolo\InstsAndQt\TKOscope\TK.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Oscilloscope(object):
    def setupUi(self, Oscilloscope):
        Oscilloscope.setObjectName("Oscilloscope")
        Oscilloscope.resize(508, 431)
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
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gbAveraging = QtWidgets.QGroupBox(self.tab_5)
        self.gbAveraging.setFlat(True)
        self.gbAveraging.setCheckable(True)
        self.gbAveraging.setObjectName("gbAveraging")
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout(self.gbAveraging)
        self.horizontalLayout_53.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.cbAveMode = QtWidgets.QComboBox(self.gbAveraging)
        self.cbAveMode.setObjectName("cbAveMode")
        self.cbAveMode.addItem("")
        self.cbAveMode.addItem("")
        self.horizontalLayout_53.addWidget(self.cbAveMode)
        self.sbAveNum = QtWidgets.QSpinBox(self.gbAveraging)
        self.sbAveNum.setProperty("value", 4)
        self.sbAveNum.setObjectName("sbAveNum")
        self.horizontalLayout_53.addWidget(self.sbAveNum)
        self.cbRolling = QtWidgets.QCheckBox(self.gbAveraging)
        self.cbRolling.setObjectName("cbRolling")
        self.horizontalLayout_53.addWidget(self.cbRolling)
        self.gridLayout_2.addWidget(self.gbAveraging, 0, 1, 1, 1)
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
        self.gridLayout_2.addWidget(self.groupBox_39, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 3, 1, 1)
        self.groupBox_40 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_40.setFlat(True)
        self.groupBox_40.setCheckable(False)
        self.groupBox_40.setObjectName("groupBox_40")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_40)
        self.gridLayout_10.setContentsMargins(0, 10, 0, 0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.tRatio = QFNumberEdit(self.groupBox_40)
        self.tRatio.setObjectName("tRatio")
        self.gridLayout_10.addWidget(self.tRatio, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_40, 0, 2, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 3)
        self.gridLayout_2.setColumnStretch(1, 4)
        self.gridLayout_2.setColumnStretch(2, 3)
        self.gridLayout_2.setColumnStretch(3, 8)
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
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.oscControlsWidget)

        self.retranslateUi(Oscilloscope)
        self.tabWidget.setCurrentIndex(0)
        self.cOChannel.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Oscilloscope)
        Oscilloscope.setTabOrder(self.tFELFreq, self.bOPause)
        Oscilloscope.setTabOrder(self.bOPause, self.cOGPIB)
        Oscilloscope.setTabOrder(self.cOGPIB, self.cOChannel)
        Oscilloscope.setTabOrder(self.cOChannel, self.gOsc)
        Oscilloscope.setTabOrder(self.gOsc, self.tabWidget)

    def retranslateUi(self, Oscilloscope):
        _translate = QtCore.QCoreApplication.translate
        Oscilloscope.setWindowTitle(_translate("Oscilloscope", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Oscilloscope", "Waveform"))
        self.gbAveraging.setTitle(_translate("Oscilloscope", "Averaging"))
        self.cbAveMode.setItemText(0, _translate("Oscilloscope", "Waveform"))
        self.cbAveMode.setItemText(1, _translate("Oscilloscope", "Peaks"))
        self.cbRolling.setText(_translate("Oscilloscope", "Rolling"))
        self.groupBox_39.setTitle(_translate("Oscilloscope", "FEL Freq (cm-1)"))
        self.tFELFreq.setText(_translate("Oscilloscope", "0"))
        self.groupBox_40.setTitle(_translate("Oscilloscope", "Ratio (%)"))
        self.tRatio.setText(_translate("Oscilloscope", "0"))
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
