# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Tue Aug 20 19:54:53 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(762, 554)
        self.satLista = QtGui.QComboBox(Dialog)
        self.satLista.setGeometry(QtCore.QRect(10, 60, 251, 27))
        self.satLista.setObjectName("satLista")
        self.headTitle = QtGui.QLabel(Dialog)
        self.headTitle.setGeometry(QtCore.QRect(310, 10, 171, 21))
        self.headTitle.setObjectName("headTitle")
        self.chanList1 = QtGui.QListView(Dialog)
        self.chanList1.setGeometry(QtCore.QRect(10, 100, 331, 371))
        self.chanList1.setObjectName("chanList1")
        self.testBtn = QtGui.QPushButton(Dialog)
        self.testBtn.setGeometry(QtCore.QRect(450, 510, 141, 27))
        self.testBtn.setObjectName("testBtn")
        self.leftBtn = QtGui.QToolButton(Dialog)
        self.leftBtn.setGeometry(QtCore.QRect(350, 300, 20, 20))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/arrow_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leftBtn.setIcon(icon)
        self.leftBtn.setObjectName("leftBtn")
        self.rightBtn = QtGui.QToolButton(Dialog)
        self.rightBtn.setGeometry(QtCore.QRect(370, 300, 20, 20))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/arrow_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rightBtn.setIcon(icon1)
        self.rightBtn.setObjectName("rightBtn")
        self.cancelBtn = QtGui.QPushButton(Dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(330, 510, 98, 27))
        self.cancelBtn.setObjectName("cancelBtn")
        self.uploadBtn = QtGui.QPushButton(Dialog)
        self.uploadBtn.setGeometry(QtCore.QRect(220, 510, 98, 27))
        self.uploadBtn.setObjectName("uploadBtn")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 66, 17))
        self.label_2.setObjectName("label_2")
        self.upBtn = QtGui.QToolButton(Dialog)
        self.upBtn.setGeometry(QtCore.QRect(695, 25, 31, 20))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/red_arrow_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upBtn.setIcon(icon2)
        self.upBtn.setObjectName("upBtn")
        self.downBtn = QtGui.QToolButton(Dialog)
        self.downBtn.setGeometry(QtCore.QRect(725, 25, 31, 20))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/red_arrow_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downBtn.setIcon(icon3)
        self.downBtn.setObjectName("downBtn")
        self.download = QtGui.QPushButton(Dialog)
        self.download.setGeometry(QtCore.QRect(270, 60, 98, 27))
        self.download.setObjectName("download")
        self.status = QtGui.QLabel(Dialog)
        self.status.setGeometry(QtCore.QRect(10, 480, 751, 21))
        self.status.setText("")
        self.status.setObjectName("status")
        self.chanList2 = QtGui.QTableView(Dialog)
        self.chanList2.setGeometry(QtCore.QRect(400, 60, 361, 411))
        self.chanList2.setObjectName("chanList2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.headTitle.setText(QtGui.QApplication.translate("Dialog", "ChannelList for RealBOX", None, QtGui.QApplication.UnicodeUTF8))
        self.testBtn.setText(QtGui.QApplication.translate("Dialog", "Test connectivity", None, QtGui.QApplication.UnicodeUTF8))
        self.leftBtn.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.rightBtn.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBtn.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.uploadBtn.setText(QtGui.QApplication.translate("Dialog", "Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Satellites", None, QtGui.QApplication.UnicodeUTF8))
        self.upBtn.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.downBtn.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.download.setText(QtGui.QApplication.translate("Dialog", "Download", None, QtGui.QApplication.UnicodeUTF8))

