# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player.ui'
#
# Created: Wed Mar 12 00:25:42 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_frmPlayer(object):
    def setupUi(self, frmPlayer):
        frmPlayer.setObjectName(_fromUtf8("frmPlayer"))
        frmPlayer.setEnabled(True)
        frmPlayer.resize(665, 496)
        frmPlayer.setMaximumSize(QtCore.QSize(100000, 100000))
        frmPlayer.setAutoFillBackground(False)
        frmPlayer.setStyleSheet(_fromUtf8("QWidget#frmPlayer{\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f00000, stop: 0.3 #00f000, stop: 1 #0000f0);\n"
"\n"
"}\n"
"\n"
"#layoutVideo{\n"
"    border: 1px solid #e9e9e9;\n"
"    border-radius:6px;\n"
"}\n"
"\n"
"#sldVolume::groove:horizontal {\n"
"     border: 1px solid #999999;\n"
"     height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"     margin: 2px 0;\n"
"    border-radius: 2px;\n"
" }\n"
"\n"
"#sldVolume::handle:horizontal {\n"
"     background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #4bd0d3, stop:0.2 #3b9b9e, stop:0.8 #4bd0d3, stop:1 #2b4040);\n"
"     border: 1px solid #5c5c5c;\n"
"     width: 18px;\n"
"     margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"     border-radius: 5px;\n"
" }\n"
""))
        self.verticalLayout = QtGui.QVBoxLayout(frmPlayer)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.layoutVideo = QtGui.QHBoxLayout()
        self.layoutVideo.setContentsMargins(-1, 0, -1, -1)
        self.layoutVideo.setObjectName(_fromUtf8("layoutVideo"))
        spacerItem = QtGui.QSpacerItem(0, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.layoutVideo.addItem(spacerItem)
        self.verticalLayout.addLayout(self.layoutVideo)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnChannelUp = QtGui.QPushButton(frmPlayer)
        self.btnChannelUp.setMaximumSize(QtCore.QSize(32, 32))
        self.btnChannelUp.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../usr/share/icons/huayra-limbo/scalable/acciones/up.svg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnChannelUp.setIcon(icon)
        self.btnChannelUp.setObjectName(_fromUtf8("btnChannelUp"))
        self.horizontalLayout.addWidget(self.btnChannelUp)
        self.btnChannelDown = QtGui.QPushButton(frmPlayer)
        self.btnChannelDown.setMaximumSize(QtCore.QSize(32, 32))
        self.btnChannelDown.setStyleSheet(_fromUtf8("color: rgb(125, 60, 255);"))
        self.btnChannelDown.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../usr/share/icons/huayra-limbo/scalable/acciones/down.svg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnChannelDown.setIcon(icon1)
        self.btnChannelDown.setObjectName(_fromUtf8("btnChannelDown"))
        self.horizontalLayout.addWidget(self.btnChannelDown)
        self.sldVolume = QtGui.QSlider(frmPlayer)
        self.sldVolume.setOrientation(QtCore.Qt.Horizontal)
        self.sldVolume.setObjectName(_fromUtf8("sldVolume"))
        self.horizontalLayout.addWidget(self.sldVolume)
        self.btnShowChannelsList = QtGui.QPushButton(frmPlayer)
        self.btnShowChannelsList.setMaximumSize(QtCore.QSize(30, 32))
        self.btnShowChannelsList.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../usr/share/icons/huayra-limbo/scalable/acciones/top.svg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnShowChannelsList.setIcon(icon2)
        self.btnShowChannelsList.setObjectName(_fromUtf8("btnShowChannelsList"))
        self.horizontalLayout.addWidget(self.btnShowChannelsList)
        self.btnFullScreen = QtGui.QPushButton(frmPlayer)
        self.btnFullScreen.setMaximumSize(QtCore.QSize(32, 32))
        self.btnFullScreen.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../usr/share/icons/huayra-limbo/scalable/acciones/view-fullscreen.svg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnFullScreen.setIcon(icon3)
        self.btnFullScreen.setObjectName(_fromUtf8("btnFullScreen"))
        self.horizontalLayout.addWidget(self.btnFullScreen)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listViewChannels = QtGui.QListView(frmPlayer)
        self.listViewChannels.setEnabled(True)
        self.listViewChannels.setMaximumSize(QtCore.QSize(16777215, 200))
        self.listViewChannels.setAutoFillBackground(False)
        self.listViewChannels.setObjectName(_fromUtf8("listViewChannels"))
        self.verticalLayout.addWidget(self.listViewChannels)

        self.retranslateUi(frmPlayer)
        QtCore.QMetaObject.connectSlotsByName(frmPlayer)

    def retranslateUi(self, frmPlayer):
        frmPlayer.setWindowTitle(QtGui.QApplication.translate("frmPlayer", "Huayra - Television Digital Abierta ", None, QtGui.QApplication.UnicodeUTF8))
        frmPlayer.setToolTip(QtGui.QApplication.translate("frmPlayer", "Visor de TDA Huayra", None, QtGui.QApplication.UnicodeUTF8))
        self.btnChannelUp.setToolTip(QtGui.QApplication.translate("frmPlayer", "Canal Arriba", None, QtGui.QApplication.UnicodeUTF8))
        self.btnChannelDown.setToolTip(QtGui.QApplication.translate("frmPlayer", "Canal Abajo", None, QtGui.QApplication.UnicodeUTF8))
        self.sldVolume.setToolTip(QtGui.QApplication.translate("frmPlayer", "Control de volumen", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFullScreen.setToolTip(QtGui.QApplication.translate("frmPlayer", "Pantalla Completa", None, QtGui.QApplication.UnicodeUTF8))

