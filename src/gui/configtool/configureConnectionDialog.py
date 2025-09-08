#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
from PyQt5 import (QtCore, QtGui, QtWidgets)

from src.gui.sharedcomnponets.sharedcomponets import SerialPortComboBox
from src.simpleFOCConnector import SimpleFOCDevice


class ConfigureSerailConnectionDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(SimpleFOCDevice.getInstance())

    def setupUi(self, device=None):
        self.setObjectName('Dialog')
        self.resize(700, 188)

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName('gridLayout')

        self.portNameLabel = QtWidgets.QLabel(self)
        self.portNameLabel.setObjectName('portNameLabel')
        self.gridLayout.addWidget(self.portNameLabel, 0, 0, 1, 1)

        self.portNameComboBox = SerialPortComboBox(self)
        self.portNameComboBox.setObjectName('portNameComboBox')
        self.portNameComboBox.setMinimumWidth(250)
        self.gridLayout.addWidget(self.portNameComboBox, 0, 1, 1, 1)

        self.bitRateLabel = QtWidgets.QLabel(self)
        self.bitRateLabel.setObjectName('bitRateLabel')
        self.gridLayout.addWidget(self.bitRateLabel, 0, 2, 1, 1)



        self.bitRatelineEdit = QtWidgets.QLineEdit(self)
        self.bitRatelineEdit.setObjectName('bitRatelineEdit')
        self.bitRatelineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("^[0-9]*$")))
        self.gridLayout.addWidget(self.bitRatelineEdit, 0, 3, 1, 1)

        self.parityLabel = QtWidgets.QLabel(self)
        self.parityLabel.setObjectName('parityLabel')
        self.gridLayout.addWidget(self.parityLabel, 1, 0, 1, 1)

        self.parityComboBox = QtWidgets.QComboBox(self)
        self.parityComboBox.setObjectName('parityComboBox')
        self.parityComboBox.addItems(serial.PARITY_NAMES.values())
        self.gridLayout.addWidget(self.parityComboBox, 1, 1, 1, 1)

        serial.PARITY_NAMES.values()

        self.byteSizeLabel = QtWidgets.QLabel(self)
        self.byteSizeLabel.setObjectName('byteSizeLabel')
        self.gridLayout.addWidget(self.byteSizeLabel, 1, 2, 1, 1)

        self.byteSizeComboBox = QtWidgets.QComboBox(self)
        self.byteSizeComboBox.setObjectName('byteSizeComboBox')
        byteSizeList = [str(serial.EIGHTBITS), str(serial.FIVEBITS), str(serial.SIXBITS),
                        str(serial.SEVENBITS)]
        self.byteSizeComboBox.addItems(byteSizeList)
        self.gridLayout.addWidget(self.byteSizeComboBox, 1, 3, 1, 1)

        self.stopBitsLabel = QtWidgets.QLabel(self)
        self.stopBitsLabel.setObjectName('stopBitsLabel')
        self.gridLayout.addWidget(self.stopBitsLabel, 2, 0, 1, 1)

        self.stopBitsComboBox = QtWidgets.QComboBox(self)
        byteStopBitsList = [str(serial.STOPBITS_ONE),
                            str(serial.STOPBITS_ONE_POINT_FIVE),
                            str(serial.STOPBITS_TWO)]
        self.stopBitsComboBox.addItems(byteStopBitsList)
        self.stopBitsComboBox.setObjectName('stopBitsComboBox')
        self.gridLayout.addWidget(self.stopBitsComboBox, 2, 1, 1, 1)

        self.connectionIDLabel = QtWidgets.QLabel(self)
        self.connectionIDLabel.setObjectName('connectionNameLabel')
        self.gridLayout.addWidget(self.connectionIDLabel, 2, 2, 1, 1)

        self.connectionIDlineEdit = QtWidgets.QLineEdit(self)
        self.connectionIDlineEdit.setMaxLength(10)
        self.connectionIDlineEdit.setObjectName('connectionNameEdit')
        self.gridLayout.addWidget(self.connectionIDlineEdit, 2, 3, 1, 1)


        self.setWindowTitle('配置串口连接')
        self.portNameLabel.setText('端口名称')
        self.bitRateLabel.setText('波特率')
        self.parityLabel.setText('校验位')
        self.byteSizeLabel.setText('数据位')
        self.stopBitsLabel.setText('停止位')
        self.connectionIDLabel.setText('连接ID')


        QtCore.QMetaObject.connectSlotsByName(self)

        if device is not None:
            self.fillForm(device)

    def fillForm(self, deviceConnector):
        self.connectionIDlineEdit.setText(deviceConnector.connectionID)
        self.portNameComboBox.setCurrentText(deviceConnector.serialPortName)
        self.bitRatelineEdit.setText(str(deviceConnector.serialRate))
        self.stopBitsComboBox.setCurrentText(str(deviceConnector.stopBits))
        self.byteSizeComboBox.setCurrentText(str(deviceConnector.serialByteSize))
        self.parityComboBox.setCurrentText(str(deviceConnector.serialParity))

    def getConfigValues(self):
        values = {
            'connectionID': self.connectionIDlineEdit.text(),
            'serialPortName': self.portNameComboBox.currentText(),
            'serialRate': self.bitRatelineEdit.text(),
            'stopBits': self.stopBitsExtractor(self.stopBitsComboBox.currentText()),
            'serialByteSize': int(str(self.byteSizeComboBox.currentText())),
            'serialParity':  list(serial.PARITY_NAMES.keys())[list(serial.PARITY_NAMES.values()).index(self.parityComboBox.currentText())][0]
        }
        return values

    def stopBitsExtractor(self, value):
        if value == '1.5':
            return float(self.stopBitsComboBox.currentText())
        else:
            return int(self.stopBitsComboBox.currentText())
        
class ConfigureWirelessConnectionDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUI(SimpleFOCDevice.getInstance())

    def setupUI(self, device=None):
        self.layout = QtWidgets.QFormLayout()

        self.ip = QtWidgets.QLineEdit()
        self.port = QtWidgets.QLineEdit()
        
        self.layout.addRow("IP地址:", self.ip)
        self.layout.addRow("TCP端口:", self.port)
        self.setLayout(self.layout)
        self.setWindowTitle('配置TCP连接')
        if device is not None:
            self.fillForm(device)

    def fillForm(self, deviceConnector):
        self.ip.setText(deviceConnector.ip)
        self.port.setText(deviceConnector.port)

    def getConfigValues(self):
        values = {
            'ip': self.ip.text(),
            'port': self.port.text(),
        }
        return values

class ConfigureConnectionDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.stackIndex = 0
        self.setupUi(SimpleFOCDevice.getInstance())

    def setupUi(self, device=None):
         
        self.layout = QtWidgets.QVBoxLayout()
        self.configType = "Serial"
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItem("串口")
        self.comboBox.addItem("无线")
        self.layout.addWidget(QtWidgets.QLabel("请选择配置类型"))
        self.layout.addWidget(self.comboBox)

        self.stackedWidget = QtWidgets.QStackedWidget()
        self.serialConfigWidget = ConfigureSerailConnectionDialog()
        self.wirelessConfigWidget = ConfigureWirelessConnectionDialog()

        self.stackedWidget.addWidget(self.serialConfigWidget)
        self.stackedWidget.addWidget(self.wirelessConfigWidget)

        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName('buttonBox')

        self.layout.addWidget(self.stackedWidget)
        self.layout.addWidget(self.buttonBox)
        self.comboBox.currentIndexChanged.connect(self.displayConfigWidget)

        self.buttonBox.accepted.connect(self.acceptCallback)
        self.buttonBox.rejected.connect(self.reject)
        self.stackedWidget.setCurrentIndex(self.stackIndex)
        
        self.setLayout(self.layout)
        self.setWindowTitle('配置连接')

    def displayConfigWidget(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def getConfigValues(self):
        currentIndex = self.stackedWidget.currentIndex()
        if self.configType == "Serial":  # Serial Config Selected
            config = self.serialConfigWidget.getConfigValues()
        else:  # Wireless Config Selected
            config = self.wirelessConfigWidget.getConfigValues()

        return self.configType, config
    
    def acceptCallback(self):
        # Custom logic here
        currentIndex = self.stackedWidget.currentIndex()
        if currentIndex == 0:  # Serial Config Selected
            self.configType = "Serial"
        else:  # Wireless Config Selected
            self.configType = "Wireless"
            
        self.stackIndex = currentIndex
        # After custom logic, call accept() to close the dialog
        self.accept()

