# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rbhusHostEditMod.ui'
#
# Created: Thu Jan 10 09:53:11 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
  _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
  def _fromUtf8(s):
    return s

try:
  _encoding = QtGui.QApplication.UnicodeUTF8
  def _translate(context, text, disambig):
    return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
  def _translate(context, text, disambig):
    return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    MainWindow.setObjectName(_fromUtf8("MainWindow"))
    MainWindow.resize(531, 72)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
    MainWindow.setSizePolicy(sizePolicy)
    self.centralwidget = QtGui.QWidget(MainWindow)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
    self.centralwidget.setSizePolicy(sizePolicy)
    self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
    self.gridLayout = QtGui.QGridLayout(self.centralwidget)
    self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
    self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
    self.labelImageName = QtGui.QLabel(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.labelImageName.sizePolicy().hasHeightForWidth())
    self.labelImageName.setSizePolicy(sizePolicy)
    self.labelImageName.setObjectName(_fromUtf8("labelImageName"))
    self.gridLayout.addWidget(self.labelImageName, 0, 0, 1, 1)
    self.lineEditImageName = QtGui.QLineEdit(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lineEditImageName.sizePolicy().hasHeightForWidth())
    self.lineEditImageName.setSizePolicy(sizePolicy)
    self.lineEditImageName.setObjectName(_fromUtf8("lineEditImageName"))
    self.gridLayout.addWidget(self.lineEditImageName, 0, 1, 1, 2)
    MainWindow.setCentralWidget(self.centralwidget)
    self.statusbar = QtGui.QStatusBar(MainWindow)
    self.statusbar.setObjectName(_fromUtf8("statusbar"))
    MainWindow.setStatusBar(self.statusbar)

    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow):
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
    self.labelImageName.setText(_translate("MainWindow", "imageName", None))

