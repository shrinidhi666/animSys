# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rbhusPipeSubmitRenderMod.ui'
#
# Created: Thu Jul 23 15:56:02 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_rbhusSubmit(object):
    def setupUi(self, rbhusSubmit):
        rbhusSubmit.setObjectName(_fromUtf8("rbhusSubmit"))
        rbhusSubmit.resize(575, 588)
        self.centralwidget = QtGui.QWidget(rbhusSubmit)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labeFileType = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labeFileType.sizePolicy().hasHeightForWidth())
        self.labeFileType.setSizePolicy(sizePolicy)
        self.labeFileType.setObjectName(_fromUtf8("labeFileType"))
        self.gridLayout.addWidget(self.labeFileType, 2, 0, 1, 1)
        self.lineEditCameras = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditCameras.sizePolicy().hasHeightForWidth())
        self.lineEditCameras.setSizePolicy(sizePolicy)
        self.lineEditCameras.setObjectName(_fromUtf8("lineEditCameras"))
        self.gridLayout.addWidget(self.lineEditCameras, 9, 1, 1, 1)
        self.labelFileName = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelFileName.sizePolicy().hasHeightForWidth())
        self.labelFileName.setSizePolicy(sizePolicy)
        self.labelFileName.setObjectName(_fromUtf8("labelFileName"))
        self.gridLayout.addWidget(self.labelFileName, 1, 0, 1, 1)
        self.autoOutName = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoOutName.sizePolicy().hasHeightForWidth())
        self.autoOutName.setSizePolicy(sizePolicy)
        self.autoOutName.setText(_fromUtf8(""))
        self.autoOutName.setIconSize(QtCore.QSize(12, 12))
        self.autoOutName.setObjectName(_fromUtf8("autoOutName"))
        self.gridLayout.addWidget(self.autoOutName, 6, 4, 1, 1)
        self.labelImageType = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelImageType.sizePolicy().hasHeightForWidth())
        self.labelImageType.setSizePolicy(sizePolicy)
        self.labelImageType.setObjectName(_fromUtf8("labelImageType"))
        self.gridLayout.addWidget(self.labelImageType, 5, 0, 1, 1)
        self.labeRenderer = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labeRenderer.sizePolicy().hasHeightForWidth())
        self.labeRenderer.setSizePolicy(sizePolicy)
        self.labeRenderer.setObjectName(_fromUtf8("labeRenderer"))
        self.gridLayout.addWidget(self.labeRenderer, 13, 0, 1, 1)
        self.labelOutDir = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelOutDir.sizePolicy().hasHeightForWidth())
        self.labelOutDir.setSizePolicy(sizePolicy)
        self.labelOutDir.setObjectName(_fromUtf8("labelOutDir"))
        self.gridLayout.addWidget(self.labelOutDir, 4, 0, 1, 1)
        self.labelAfterTime = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelAfterTime.sizePolicy().hasHeightForWidth())
        self.labelAfterTime.setSizePolicy(sizePolicy)
        self.labelAfterTime.setObjectName(_fromUtf8("labelAfterTime"))
        self.gridLayout.addWidget(self.labelAfterTime, 18, 0, 1, 1)
        self.labelHostGroup = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHostGroup.sizePolicy().hasHeightForWidth())
        self.labelHostGroup.setSizePolicy(sizePolicy)
        self.labelHostGroup.setObjectName(_fromUtf8("labelHostGroup"))
        self.gridLayout.addWidget(self.labelHostGroup, 11, 0, 1, 1)
        self.labelLayer = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLayer.sizePolicy().hasHeightForWidth())
        self.labelLayer.setSizePolicy(sizePolicy)
        self.labelLayer.setObjectName(_fromUtf8("labelLayer"))
        self.gridLayout.addWidget(self.labelLayer, 15, 0, 1, 1)
        self.labelDescription = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDescription.sizePolicy().hasHeightForWidth())
        self.labelDescription.setSizePolicy(sizePolicy)
        self.labelDescription.setObjectName(_fromUtf8("labelDescription"))
        self.gridLayout.addWidget(self.labelDescription, 24, 0, 1, 1)
        self.labelOsType = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelOsType.sizePolicy().hasHeightForWidth())
        self.labelOsType.setSizePolicy(sizePolicy)
        self.labelOsType.setObjectName(_fromUtf8("labelOsType"))
        self.gridLayout.addWidget(self.labelOsType, 16, 0, 1, 1)
        self.lineEditFileName = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditFileName.sizePolicy().hasHeightForWidth())
        self.lineEditFileName.setSizePolicy(sizePolicy)
        self.lineEditFileName.setToolTip(_fromUtf8(""))
        self.lineEditFileName.setDragEnabled(True)
        self.lineEditFileName.setObjectName(_fromUtf8("lineEditFileName"))
        self.gridLayout.addWidget(self.lineEditFileName, 1, 1, 1, 1)
        self.labelImageName = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelImageName.sizePolicy().hasHeightForWidth())
        self.labelImageName.setSizePolicy(sizePolicy)
        self.labelImageName.setObjectName(_fromUtf8("labelImageName"))
        self.gridLayout.addWidget(self.labelImageName, 6, 0, 1, 1)
        self.labelAfterTask = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelAfterTask.sizePolicy().hasHeightForWidth())
        self.labelAfterTask.setSizePolicy(sizePolicy)
        self.labelAfterTask.setObjectName(_fromUtf8("labelAfterTask"))
        self.gridLayout.addWidget(self.labelAfterTask, 17, 0, 1, 1)
        self.labelResolution = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelResolution.sizePolicy().hasHeightForWidth())
        self.labelResolution.setSizePolicy(sizePolicy)
        self.labelResolution.setObjectName(_fromUtf8("labelResolution"))
        self.gridLayout.addWidget(self.labelResolution, 10, 0, 1, 1)
        self.lineEditDescription = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditDescription.sizePolicy().hasHeightForWidth())
        self.lineEditDescription.setSizePolicy(sizePolicy)
        self.lineEditDescription.setDragEnabled(True)
        self.lineEditDescription.setObjectName(_fromUtf8("lineEditDescription"))
        self.gridLayout.addWidget(self.lineEditDescription, 24, 1, 1, 1)
        self.lineEditOutName = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditOutName.sizePolicy().hasHeightForWidth())
        self.lineEditOutName.setSizePolicy(sizePolicy)
        self.lineEditOutName.setDragEnabled(True)
        self.lineEditOutName.setReadOnly(False)
        self.lineEditOutName.setObjectName(_fromUtf8("lineEditOutName"))
        self.gridLayout.addWidget(self.lineEditOutName, 6, 1, 1, 1)
        self.lineEditFrange = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditFrange.sizePolicy().hasHeightForWidth())
        self.lineEditFrange.setSizePolicy(sizePolicy)
        self.lineEditFrange.setToolTip(_fromUtf8(""))
        self.lineEditFrange.setObjectName(_fromUtf8("lineEditFrange"))
        self.gridLayout.addWidget(self.lineEditFrange, 8, 1, 1, 1)
        self.afterTimeEdit = QtGui.QDateTimeEdit(self.centralwidget)
        self.afterTimeEdit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.afterTimeEdit.sizePolicy().hasHeightForWidth())
        self.afterTimeEdit.setSizePolicy(sizePolicy)
        self.afterTimeEdit.setTime(QtCore.QTime(14, 0, 0))
        self.afterTimeEdit.setCurrentSection(QtGui.QDateTimeEdit.YearSection)
        self.afterTimeEdit.setCalendarPopup(True)
        self.afterTimeEdit.setObjectName(_fromUtf8("afterTimeEdit"))
        self.gridLayout.addWidget(self.afterTimeEdit, 18, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditHostGroups = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditHostGroups.sizePolicy().hasHeightForWidth())
        self.lineEditHostGroups.setSizePolicy(sizePolicy)
        self.lineEditHostGroups.setReadOnly(True)
        self.lineEditHostGroups.setObjectName(_fromUtf8("lineEditHostGroups"))
        self.gridLayout.addWidget(self.lineEditHostGroups, 11, 1, 1, 1)
        self.pushSelectHostGroups = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushSelectHostGroups.sizePolicy().hasHeightForWidth())
        self.pushSelectHostGroups.setSizePolicy(sizePolicy)
        self.pushSelectHostGroups.setObjectName(_fromUtf8("pushSelectHostGroups"))
        self.gridLayout.addWidget(self.pushSelectHostGroups, 11, 2, 1, 1)
        self.labelUser = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelUser.sizePolicy().hasHeightForWidth())
        self.labelUser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelUser.setFont(font)
        self.labelUser.setObjectName(_fromUtf8("labelUser"))
        self.gridLayout.addWidget(self.labelUser, 0, 1, 1, 1)
        self.checkSloppy = QtGui.QCheckBox(self.centralwidget)
        self.checkSloppy.setObjectName(_fromUtf8("checkSloppy"))
        self.gridLayout.addWidget(self.checkSloppy, 17, 2, 1, 1)
        self.comboFileType = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboFileType.sizePolicy().hasHeightForWidth())
        self.comboFileType.setSizePolicy(sizePolicy)
        self.comboFileType.setObjectName(_fromUtf8("comboFileType"))
        self.gridLayout.addWidget(self.comboFileType, 2, 1, 1, 1)
        self.checkAfterTime = QtGui.QCheckBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkAfterTime.sizePolicy().hasHeightForWidth())
        self.checkAfterTime.setSizePolicy(sizePolicy)
        self.checkAfterTime.setObjectName(_fromUtf8("checkAfterTime"))
        self.gridLayout.addWidget(self.checkAfterTime, 18, 2, 1, 1)
        self.labelPrio = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPrio.sizePolicy().hasHeightForWidth())
        self.labelPrio.setSizePolicy(sizePolicy)
        self.labelPrio.setObjectName(_fromUtf8("labelPrio"))
        self.gridLayout.addWidget(self.labelPrio, 19, 0, 1, 1)
        self.lineEditLayer = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditLayer.sizePolicy().hasHeightForWidth())
        self.lineEditLayer.setSizePolicy(sizePolicy)
        self.lineEditLayer.setToolTip(_fromUtf8(""))
        self.lineEditLayer.setObjectName(_fromUtf8("lineEditLayer"))
        self.gridLayout.addWidget(self.lineEditLayer, 15, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.comboRes = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboRes.sizePolicy().hasHeightForWidth())
        self.comboRes.setSizePolicy(sizePolicy)
        self.comboRes.setObjectName(_fromUtf8("comboRes"))
        self.horizontalLayout.addWidget(self.comboRes)
        self.lineEditRes = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditRes.sizePolicy().hasHeightForWidth())
        self.lineEditRes.setSizePolicy(sizePolicy)
        self.lineEditRes.setToolTip(_fromUtf8(""))
        self.lineEditRes.setObjectName(_fromUtf8("lineEditRes"))
        self.horizontalLayout.addWidget(self.lineEditRes)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 10, 1, 1, 1)
        self.pushSubmit = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushSubmit.sizePolicy().hasHeightForWidth())
        self.pushSubmit.setSizePolicy(sizePolicy)
        self.pushSubmit.setObjectName(_fromUtf8("pushSubmit"))
        self.gridLayout.addWidget(self.pushSubmit, 26, 2, 1, 1)
        self.labelFrange = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelFrange.sizePolicy().hasHeightForWidth())
        self.labelFrange.setSizePolicy(sizePolicy)
        self.labelFrange.setObjectName(_fromUtf8("labelFrange"))
        self.gridLayout.addWidget(self.labelFrange, 8, 0, 1, 1)
        self.lineEditAfterTask = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditAfterTask.sizePolicy().hasHeightForWidth())
        self.lineEditAfterTask.setSizePolicy(sizePolicy)
        self.lineEditAfterTask.setObjectName(_fromUtf8("lineEditAfterTask"))
        self.gridLayout.addWidget(self.lineEditAfterTask, 17, 1, 1, 1)
        self.labelCamera = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCamera.sizePolicy().hasHeightForWidth())
        self.labelCamera.setSizePolicy(sizePolicy)
        self.labelCamera.setObjectName(_fromUtf8("labelCamera"))
        self.gridLayout.addWidget(self.labelCamera, 9, 0, 1, 1)
        self.comboPrio = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboPrio.sizePolicy().hasHeightForWidth())
        self.comboPrio.setSizePolicy(sizePolicy)
        self.comboPrio.setObjectName(_fromUtf8("comboPrio"))
        self.comboPrio.addItem(_fromUtf8(""))
        self.comboPrio.addItem(_fromUtf8(""))
        self.comboPrio.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboPrio, 19, 1, 1, 1)
        self.comboRenderer = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboRenderer.sizePolicy().hasHeightForWidth())
        self.comboRenderer.setSizePolicy(sizePolicy)
        self.comboRenderer.setObjectName(_fromUtf8("comboRenderer"))
        self.gridLayout.addWidget(self.comboRenderer, 13, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.checkHold = QtGui.QCheckBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkHold.sizePolicy().hasHeightForWidth())
        self.checkHold.setSizePolicy(sizePolicy)
        self.checkHold.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkHold.setObjectName(_fromUtf8("checkHold"))
        self.horizontalLayout_2.addWidget(self.checkHold)
        self.gridLayout.addLayout(self.horizontalLayout_2, 26, 1, 1, 1)
        self.comboOsType = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboOsType.sizePolicy().hasHeightForWidth())
        self.comboOsType.setSizePolicy(sizePolicy)
        self.comboOsType.setObjectName(_fromUtf8("comboOsType"))
        self.gridLayout.addWidget(self.comboOsType, 16, 1, 1, 1)
        self.labelBatching = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBatching.sizePolicy().hasHeightForWidth())
        self.labelBatching.setSizePolicy(sizePolicy)
        self.labelBatching.setObjectName(_fromUtf8("labelBatching"))
        self.gridLayout.addWidget(self.labelBatching, 21, 0, 1, 1)
        self.comboImageType = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboImageType.sizePolicy().hasHeightForWidth())
        self.comboImageType.setSizePolicy(sizePolicy)
        self.comboImageType.setObjectName(_fromUtf8("comboImageType"))
        self.gridLayout.addWidget(self.comboImageType, 5, 1, 1, 1)
        self.checkBatching = QtGui.QCheckBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBatching.sizePolicy().hasHeightForWidth())
        self.checkBatching.setSizePolicy(sizePolicy)
        self.checkBatching.setObjectName(_fromUtf8("checkBatching"))
        self.gridLayout.addWidget(self.checkBatching, 21, 2, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labelMinBatch = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMinBatch.sizePolicy().hasHeightForWidth())
        self.labelMinBatch.setSizePolicy(sizePolicy)
        self.labelMinBatch.setObjectName(_fromUtf8("labelMinBatch"))
        self.horizontalLayout_3.addWidget(self.labelMinBatch)
        self.spinMinBatch = QtGui.QSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinMinBatch.sizePolicy().hasHeightForWidth())
        self.spinMinBatch.setSizePolicy(sizePolicy)
        self.spinMinBatch.setMinimum(1)
        self.spinMinBatch.setMaximum(999999999)
        self.spinMinBatch.setObjectName(_fromUtf8("spinMinBatch"))
        self.horizontalLayout_3.addWidget(self.spinMinBatch)
        spacerItem2 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.labelMaxBatch = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMaxBatch.sizePolicy().hasHeightForWidth())
        self.labelMaxBatch.setSizePolicy(sizePolicy)
        self.labelMaxBatch.setObjectName(_fromUtf8("labelMaxBatch"))
        self.horizontalLayout_3.addWidget(self.labelMaxBatch)
        self.spinMaxBatch = QtGui.QSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinMaxBatch.sizePolicy().hasHeightForWidth())
        self.spinMaxBatch.setSizePolicy(sizePolicy)
        self.spinMaxBatch.setMinimum(1)
        self.spinMaxBatch.setMaximum(999999999)
        self.spinMaxBatch.setObjectName(_fromUtf8("spinMaxBatch"))
        self.horizontalLayout_3.addWidget(self.spinMaxBatch)
        self.gridLayout.addLayout(self.horizontalLayout_3, 21, 1, 1, 1)
        self.comboDirectory = QtGui.QComboBox(self.centralwidget)
        self.comboDirectory.setObjectName(_fromUtf8("comboDirectory"))
        self.gridLayout.addWidget(self.comboDirectory, 4, 1, 1, 1)
        rbhusSubmit.setCentralWidget(self.centralwidget)

        self.retranslateUi(rbhusSubmit)
        QtCore.QMetaObject.connectSlotsByName(rbhusSubmit)

    def retranslateUi(self, rbhusSubmit):
        rbhusSubmit.setWindowTitle(_translate("rbhusSubmit", "rbhusSubmit", None))
        self.labeFileType.setText(_translate("rbhusSubmit", "fileType", None))
        self.lineEditCameras.setToolTip(_translate("rbhusSubmit", "comma seperated list of cameras to render", None))
        self.lineEditCameras.setText(_translate("rbhusSubmit", "default", None))
        self.labelFileName.setText(_translate("rbhusSubmit", "fileName", None))
        self.labelImageType.setText(_translate("rbhusSubmit", "imageType", None))
        self.labeRenderer.setText(_translate("rbhusSubmit", "renderer", None))
        self.labelOutDir.setText(_translate("rbhusSubmit", "directory", None))
        self.labelAfterTime.setText(_translate("rbhusSubmit", "afterTime ", None))
        self.labelHostGroup.setText(_translate("rbhusSubmit", "hostGroup", None))
        self.labelLayer.setText(_translate("rbhusSubmit", "layers", None))
        self.labelDescription.setText(_translate("rbhusSubmit", "description", None))
        self.labelOsType.setText(_translate("rbhusSubmit", "osType", None))
        self.lineEditFileName.setWhatsThis(_translate("rbhusSubmit", "comma seperated list of files to render", None))
        self.labelImageName.setText(_translate("rbhusSubmit", "outName", None))
        self.labelAfterTask.setText(_translate("rbhusSubmit", "afterTasks", None))
        self.labelResolution.setText(_translate("rbhusSubmit", "resolution", None))
        self.lineEditDescription.setText(_translate("rbhusSubmit", "default", None))
        self.lineEditOutName.setToolTip(_translate("rbhusSubmit", "name of the image file. eg: wtf.png", None))
        self.lineEditOutName.setWhatsThis(_translate("rbhusSubmit", "<html><head/><body><p>name of the image file. eg: <span style=\" font-weight:600;\">wtfigo.png</span></p></body></html>", None))
        self.lineEditOutName.setText(_translate("rbhusSubmit", "default", None))
        self.lineEditFrange.setWhatsThis(_translate("rbhusSubmit", "<html><head/><body><p>frame range in the format</p><p>startframe-endframe:byframes</p><p>eg:</p><p>render frames from 1 to 100     : <span style=\" font-weight:600;\">1-100</span></p><p>render every 5th frame from 1 to 100     : <span style=\" font-weight:600;\">1-100:5</span></p><p>render 1 frame         :<span style=\" font-weight:600;\"> 1</span></p><p><br/></p><p><br/></p></body></html>", None))
        self.lineEditFrange.setText(_translate("rbhusSubmit", "1", None))
        self.afterTimeEdit.setDisplayFormat(_translate("rbhusSubmit", "yyyy-M-d h:mm A", None))
        self.label.setText(_translate("rbhusSubmit", "USER", None))
        self.lineEditHostGroups.setToolTip(_translate("rbhusSubmit", "comma seperated list of cameras to render", None))
        self.lineEditHostGroups.setText(_translate("rbhusSubmit", "default", None))
        self.pushSelectHostGroups.setText(_translate("rbhusSubmit", "select", None))
        self.labelUser.setText(_translate("rbhusSubmit", "TextLabel", None))
        self.checkSloppy.setText(_translate("rbhusSubmit", "sloppy", None))
        self.checkAfterTime.setText(_translate("rbhusSubmit", "enable", None))
        self.labelPrio.setText(_translate("rbhusSubmit", "priority", None))
        self.lineEditLayer.setText(_translate("rbhusSubmit", "default", None))
        self.lineEditRes.setWhatsThis(_translate("rbhusSubmit", "<html><head/><body><p>frame range in the format</p><p>startframe-endframe:byframes</p><p>eg:</p><p>render frames from 1 to 100     : <span style=\" font-weight:600;\">1-100</span></p><p>render every 5th frame from 1 to 100     : <span style=\" font-weight:600;\">1-100:5</span></p><p>render 1 frame         :<span style=\" font-weight:600;\"> 1</span></p><p><br/></p><p><br/></p></body></html>", None))
        self.lineEditRes.setText(_translate("rbhusSubmit", "default", None))
        self.pushSubmit.setText(_translate("rbhusSubmit", "submit", None))
        self.labelFrange.setText(_translate("rbhusSubmit", "fRange     ", None))
        self.lineEditAfterTask.setText(_translate("rbhusSubmit", "0", None))
        self.labelCamera.setText(_translate("rbhusSubmit", "cameras", None))
        self.comboPrio.setItemText(0, _translate("rbhusSubmit", "low", None))
        self.comboPrio.setItemText(1, _translate("rbhusSubmit", "normal", None))
        self.comboPrio.setItemText(2, _translate("rbhusSubmit", "high", None))
        self.checkHold.setText(_translate("rbhusSubmit", "deactivate", None))
        self.labelBatching.setText(_translate("rbhusSubmit", "batching", None))
        self.checkBatching.setText(_translate("rbhusSubmit", "enable", None))
        self.labelMinBatch.setText(_translate("rbhusSubmit", "min", None))
        self.labelMaxBatch.setText(_translate("rbhusSubmit", "max", None))

