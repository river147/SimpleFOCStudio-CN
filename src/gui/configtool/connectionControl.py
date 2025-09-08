#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets

from src.gui.configtool.configureConnectionDialog import \
    ConfigureConnectionDialog
from src.gui.sharedcomnponets.sharedcomponets import GUIToolKit
from src.simpleFOCConnector import SimpleFOCDevice


class ConnectionControlGroupBox(QtWidgets.QGroupBox):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.device = SimpleFOCDevice.getInstance()

        self.setObjectName('connectionControl')
        self.setTitle('连接控制')

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName('generalControlHL')

        self.devCommandIDLabel = QtWidgets.QLabel("命令:")
        self.horizontalLayout.addWidget(self.devCommandIDLabel)

        self.devCommandIDLetter = QtWidgets.QLineEdit()
        self.devCommandIDLetter.setObjectName('devCommandIDLetter')
        self.devCommandIDLetter.editingFinished.connect(self.changeDevicedevCommandID)
        self.horizontalLayout.addWidget(self.devCommandIDLetter)
        self.devCommandIDLetter.setText(self.device.devCommandID)

        self.pullConfig = QtWidgets.QPushButton()
        self.pullConfig.setObjectName('pullConfig')
        self.pullConfig.setIcon(GUIToolKit.getIconByName('pull'))
        self.pullConfig.setText(' 拉取参数')
        self.pullConfig.clicked.connect(self.device.pullConfiguration)
        
        self.horizontalLayout.addWidget(self.pullConfig)

        self.connectDisconnectButton = QtWidgets.QPushButton(self)
        self.connectDisconnectButton.setIcon(GUIToolKit.getIconByName('connect'))
        self.connectDisconnectButton.setObjectName('connectDeviceButton')
        self.connectDisconnectButton.setText('连接')
        self.connectDisconnectButton.clicked.connect(self.connectDisconnectDeviceAction)

        self.horizontalLayout.addWidget(self.connectDisconnectButton)

        self.configureDeviceButton = QtWidgets.QPushButton(self)
        self.configureDeviceButton.setIcon(GUIToolKit.getIconByName('configure'))
        self.configureDeviceButton.setObjectName('configureDeviceButton')
        self.configureDeviceButton.setText('配置')
        self.configureDeviceButton.clicked.connect(self.configureDeviceAction)
        self.horizontalLayout.addWidget(self.configureDeviceButton)

        self.device.addConnectionStateListener(self)
        self.connectionStateChanged(self.device.isConnected)
    
    def changeDevicedevCommandID(self):
        self.device.devCommandID = self.devCommandIDLetter.text()

    def connectDisconnectDeviceAction(self):
        if self.device.isConnected:
            self.device.disConnect()
        else:
            connectionMode  = SimpleFOCDevice.PULL_CONFIG_ON_CONNECT
            self.device.connect(connectionMode)

    def connectionStateChanged(self, isConnected):
        if isConnected:
            self.connectDisconnectButton.setIcon(
                GUIToolKit.getIconByName('disconnect'))
            self.connectDisconnectButton.setText('断开连接')
        else:
            self.connectDisconnectButton.setIcon(
                GUIToolKit.getIconByName('connect'))
            self.connectDisconnectButton.setText('连接')

    def configureDeviceAction(self):
        dialog = ConfigureConnectionDialog()
        result = dialog.exec_()
        if result:
            connType, deviceConfig = dialog.getConfigValues()
            self.device.configureConnection(connType, deviceConfig)
