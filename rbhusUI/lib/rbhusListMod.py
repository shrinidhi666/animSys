# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lib/rbhusListMod.ui'
#
# Created: Tue May 22 21:59:27 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_mainRbhusList(object):
    def setupUi(self, mainRbhusList):
        mainRbhusList.setObjectName(_fromUtf8("mainRbhusList"))
        mainRbhusList.resize(799, 666)
        self.centralwidget = QtGui.QWidget(mainRbhusList)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.checkTHold = QtGui.QCheckBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkTHold.sizePolicy().hasHeightForWidth())
        self.checkTHold.setSizePolicy(sizePolicy)
        self.checkTHold.setObjectName(_fromUtf8("checkTHold"))
        self.gridLayout_3.addWidget(self.checkTHold, 0, 3, 1, 1)
        self.checkTDone = QtGui.QCheckBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkTDone.sizePolicy().hasHeightForWidth())
        self.checkTDone.setSizePolicy(sizePolicy)
        self.checkTDone.setObjectName(_fromUtf8("checkTDone"))
        self.gridLayout_3.addWidget(self.checkTDone, 0, 1, 1, 1)
        self.checkTActive = QtGui.QCheckBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkTActive.sizePolicy().hasHeightForWidth())
        self.checkTActive.setSizePolicy(sizePolicy)
        self.checkTActive.setObjectName(_fromUtf8("checkTActive"))
        self.gridLayout_3.addWidget(self.checkTActive, 0, 0, 1, 1)
        self.checkTAutohold = QtGui.QCheckBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkTAutohold.sizePolicy().hasHeightForWidth())
        self.checkTAutohold.setSizePolicy(sizePolicy)
        self.checkTAutohold.setObjectName(_fromUtf8("checkTAutohold"))
        self.gridLayout_3.addWidget(self.checkTAutohold, 0, 2, 1, 1)
        self.checkTAll = QtGui.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkTAll.setFont(font)
        self.checkTAll.setObjectName(_fromUtf8("checkTAll"))
        self.gridLayout_3.addWidget(self.checkTAll, 0, 4, 1, 1)
        self.horizontalLayout_5.addWidget(self.groupBox_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tableList = QtGui.QTableWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableList.sizePolicy().hasHeightForWidth())
        self.tableList.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(176, 176, 176))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 176, 176))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 244, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tableList.setPalette(palette)
        self.tableList.setFrameShadow(QtGui.QFrame.Raised)
        self.tableList.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed)
        self.tableList.setAlternatingRowColors(False)
        self.tableList.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableList.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableList.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableList.setGridStyle(QtCore.Qt.SolidLine)
        self.tableList.setWordWrap(False)
        self.tableList.setObjectName(_fromUtf8("tableList"))
        self.tableList.setColumnCount(0)
        self.tableList.setRowCount(0)
        self.tableList.horizontalHeader().setCascadingSectionResizes(True)
        self.tableList.horizontalHeader().setStretchLastSection(True)
        self.tableList.verticalHeader().setVisible(False)
        self.tableList.verticalHeader().setCascadingSectionResizes(True)
        self.horizontalLayout_3.addWidget(self.tableList)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.taskActivate = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taskActivate.sizePolicy().hasHeightForWidth())
        self.taskActivate.setSizePolicy(sizePolicy)
        self.taskActivate.setObjectName(_fromUtf8("taskActivate"))
        self.verticalLayout_2.addWidget(self.taskActivate)
        self.taskHold = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taskHold.sizePolicy().hasHeightForWidth())
        self.taskHold.setSizePolicy(sizePolicy)
        self.taskHold.setObjectName(_fromUtf8("taskHold"))
        self.verticalLayout_2.addWidget(self.taskHold)
        self.taskRerun = QtGui.QPushButton(self.frame)
        self.taskRerun.setObjectName(_fromUtf8("taskRerun"))
        self.verticalLayout_2.addWidget(self.taskRerun)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.line = QtGui.QFrame(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(176, 176, 176))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 176, 176))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 176, 176))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.line.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShadow(QtGui.QFrame.Raised)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.checkFailed = QtGui.QCheckBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkFailed.sizePolicy().hasHeightForWidth())
        self.checkFailed.setSizePolicy(sizePolicy)
        self.checkFailed.setObjectName(_fromUtf8("checkFailed"))
        self.gridLayout_2.addWidget(self.checkFailed, 1, 4, 1, 1)
        self.checkKilled = QtGui.QCheckBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkKilled.sizePolicy().hasHeightForWidth())
        self.checkKilled.setSizePolicy(sizePolicy)
        self.checkKilled.setObjectName(_fromUtf8("checkKilled"))
        self.gridLayout_2.addWidget(self.checkKilled, 1, 7, 1, 1)
        self.checkHold = QtGui.QCheckBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkHold.sizePolicy().hasHeightForWidth())
        self.checkHold.setSizePolicy(sizePolicy)
        self.checkHold.setObjectName(_fromUtf8("checkHold"))
        self.gridLayout_2.addWidget(self.checkHold, 1, 6, 1, 1)
        self.checkDone = QtGui.QCheckBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkDone.sizePolicy().hasHeightForWidth())
        self.checkDone.setSizePolicy(sizePolicy)
        self.checkDone.setObjectName(_fromUtf8("checkDone"))
        self.gridLayout_2.addWidget(self.checkDone, 1, 3, 1, 1)
        self.checkRunning = QtGui.QCheckBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkRunning.sizePolicy().hasHeightForWidth())
        self.checkRunning.setSizePolicy(sizePolicy)
        self.checkRunning.setObjectName(_fromUtf8("checkRunning"))
        self.gridLayout_2.addWidget(self.checkRunning, 1, 2, 1, 1)
        self.checkAssigned = QtGui.QCheckBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkAssigned.sizePolicy().hasHeightForWidth())
        self.checkAssigned.setSizePolicy(sizePolicy)
        self.checkAssigned.setObjectName(_fromUtf8("checkAssigned"))
        self.gridLayout_2.addWidget(self.checkAssigned, 1, 1, 1, 1)
        self.checkAutohold = QtGui.QCheckBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkAutohold.sizePolicy().hasHeightForWidth())
        self.checkAutohold.setSizePolicy(sizePolicy)
        self.checkAutohold.setObjectName(_fromUtf8("checkAutohold"))
        self.gridLayout_2.addWidget(self.checkAutohold, 1, 5, 1, 1)
        self.checkAll = QtGui.QCheckBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkAll.sizePolicy().hasHeightForWidth())
        self.checkAll.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkAll.setFont(font)
        self.checkAll.setObjectName(_fromUtf8("checkAll"))
        self.gridLayout_2.addWidget(self.checkAll, 1, 8, 1, 1)
        self.checkUnassigned = QtGui.QCheckBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkUnassigned.sizePolicy().hasHeightForWidth())
        self.checkUnassigned.setSizePolicy(sizePolicy)
        self.checkUnassigned.setObjectName(_fromUtf8("checkUnassigned"))
        self.gridLayout_2.addWidget(self.checkUnassigned, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.labelTotal = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTotal.sizePolicy().hasHeightForWidth())
        self.labelTotal.setSizePolicy(sizePolicy)
        self.labelTotal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelTotal.setAutoFillBackground(True)
        self.labelTotal.setFrameShape(QtGui.QFrame.WinPanel)
        self.labelTotal.setFrameShadow(QtGui.QFrame.Sunken)
        self.labelTotal.setTextFormat(QtCore.Qt.PlainText)
        self.labelTotal.setScaledContents(False)
        self.labelTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTotal.setMargin(2)
        self.labelTotal.setObjectName(_fromUtf8("labelTotal"))
        self.horizontalLayout.addWidget(self.labelTotal)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.tableFrames = QtGui.QTableWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tableFrames.sizePolicy().hasHeightForWidth())
        self.tableFrames.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(176, 176, 176))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 176, 176))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 244, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.tableFrames.setPalette(palette)
        self.tableFrames.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed|QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed)
        self.tableFrames.setAlternatingRowColors(False)
        self.tableFrames.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableFrames.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableFrames.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableFrames.setWordWrap(False)
        self.tableFrames.setObjectName(_fromUtf8("tableFrames"))
        self.tableFrames.setColumnCount(0)
        self.tableFrames.setRowCount(0)
        self.tableFrames.horizontalHeader().setCascadingSectionResizes(True)
        self.tableFrames.horizontalHeader().setStretchLastSection(True)
        self.tableFrames.verticalHeader().setVisible(False)
        self.horizontalLayout_4.addWidget(self.tableFrames)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.frameStop = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameStop.sizePolicy().hasHeightForWidth())
        self.frameStop.setSizePolicy(sizePolicy)
        self.frameStop.setObjectName(_fromUtf8("frameStop"))
        self.verticalLayout_4.addWidget(self.frameStop)
        self.frameHold = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameHold.sizePolicy().hasHeightForWidth())
        self.frameHold.setSizePolicy(sizePolicy)
        self.frameHold.setObjectName(_fromUtf8("frameHold"))
        self.verticalLayout_4.addWidget(self.frameHold)
        self.frameRerun = QtGui.QPushButton(self.frame_2)
        self.frameRerun.setObjectName(_fromUtf8("frameRerun"))
        self.verticalLayout_4.addWidget(self.frameRerun)
        self.horizontalLayout_4.addWidget(self.frame_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.checkRefresh = QtGui.QCheckBox(self.centralwidget)
        self.checkRefresh.setObjectName(_fromUtf8("checkRefresh"))
        self.horizontalLayout_2.addWidget(self.checkRefresh)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushRefresh = QtGui.QPushButton(self.centralwidget)
        self.pushRefresh.setObjectName(_fromUtf8("pushRefresh"))
        self.horizontalLayout_2.addWidget(self.pushRefresh)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        mainRbhusList.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainRbhusList)
        QtCore.QMetaObject.connectSlotsByName(mainRbhusList)

    def retranslateUi(self, mainRbhusList):
        mainRbhusList.setWindowTitle(QtGui.QApplication.translate("mainRbhusList", "rbhusList", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("mainRbhusList", "TASKS", None, QtGui.QApplication.UnicodeUTF8))
        self.checkTHold.setText(QtGui.QApplication.translate("mainRbhusList", "hold", None, QtGui.QApplication.UnicodeUTF8))
        self.checkTDone.setText(QtGui.QApplication.translate("mainRbhusList", "done", None, QtGui.QApplication.UnicodeUTF8))
        self.checkTActive.setText(QtGui.QApplication.translate("mainRbhusList", "active", None, QtGui.QApplication.UnicodeUTF8))
        self.checkTAutohold.setText(QtGui.QApplication.translate("mainRbhusList", "autohold", None, QtGui.QApplication.UnicodeUTF8))
        self.checkTAll.setText(QtGui.QApplication.translate("mainRbhusList", "ALL", None, QtGui.QApplication.UnicodeUTF8))
        self.tableList.setSortingEnabled(True)
        self.taskActivate.setText(QtGui.QApplication.translate("mainRbhusList", "activate", None, QtGui.QApplication.UnicodeUTF8))
        self.taskHold.setText(QtGui.QApplication.translate("mainRbhusList", "hold", None, QtGui.QApplication.UnicodeUTF8))
        self.taskRerun.setText(QtGui.QApplication.translate("mainRbhusList", "rerun", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("mainRbhusList", "FRAMES", None, QtGui.QApplication.UnicodeUTF8))
        self.checkFailed.setText(QtGui.QApplication.translate("mainRbhusList", "failed", None, QtGui.QApplication.UnicodeUTF8))
        self.checkKilled.setText(QtGui.QApplication.translate("mainRbhusList", "killed", None, QtGui.QApplication.UnicodeUTF8))
        self.checkHold.setText(QtGui.QApplication.translate("mainRbhusList", "hold", None, QtGui.QApplication.UnicodeUTF8))
        self.checkDone.setText(QtGui.QApplication.translate("mainRbhusList", "done", None, QtGui.QApplication.UnicodeUTF8))
        self.checkRunning.setText(QtGui.QApplication.translate("mainRbhusList", "running", None, QtGui.QApplication.UnicodeUTF8))
        self.checkAssigned.setText(QtGui.QApplication.translate("mainRbhusList", "assigned", None, QtGui.QApplication.UnicodeUTF8))
        self.checkAutohold.setText(QtGui.QApplication.translate("mainRbhusList", "autohold", None, QtGui.QApplication.UnicodeUTF8))
        self.checkAll.setText(QtGui.QApplication.translate("mainRbhusList", "ALL", None, QtGui.QApplication.UnicodeUTF8))
        self.checkUnassigned.setText(QtGui.QApplication.translate("mainRbhusList", "unassigned", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mainRbhusList", "total", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTotal.setText(QtGui.QApplication.translate("mainRbhusList", "22", None, QtGui.QApplication.UnicodeUTF8))
        self.tableFrames.setSortingEnabled(True)
        self.frameStop.setText(QtGui.QApplication.translate("mainRbhusList", "stop", None, QtGui.QApplication.UnicodeUTF8))
        self.frameHold.setText(QtGui.QApplication.translate("mainRbhusList", "hold", None, QtGui.QApplication.UnicodeUTF8))
        self.frameRerun.setText(QtGui.QApplication.translate("mainRbhusList", "rerun", None, QtGui.QApplication.UnicodeUTF8))
        self.checkRefresh.setText(QtGui.QApplication.translate("mainRbhusList", "autoRefresh", None, QtGui.QApplication.UnicodeUTF8))
        self.pushRefresh.setText(QtGui.QApplication.translate("mainRbhusList", "refresh", None, QtGui.QApplication.UnicodeUTF8))

