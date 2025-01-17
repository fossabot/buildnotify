# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data/preferences.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName("Preferences")
        Preferences.resize(470, 394)
        Preferences.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(Preferences)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Preferences)
        self.tabWidget.setObjectName("tabWidget")
        self.serversTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serversTab.sizePolicy().hasHeightForWidth())
        self.serversTab.setSizePolicy(sizePolicy)
        self.serversTab.setObjectName("serversTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.serversTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.serversTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cctrayPathList = QtWidgets.QListView(self.groupBox_2)
        self.cctrayPathList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.cctrayPathList.setObjectName("cctrayPathList")
        self.gridLayout_3.addWidget(self.cctrayPathList, 0, 0, 1, 7)
        self.configureProjectButton = QtWidgets.QPushButton(self.groupBox_2)
        self.configureProjectButton.setEnabled(False)
        self.configureProjectButton.setObjectName("configureProjectButton")
        self.gridLayout_3.addWidget(self.configureProjectButton, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 1, 1, 1)
        self.addButton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setObjectName("addButton")
        self.gridLayout_3.addWidget(self.addButton, 1, 4, 1, 1)
        self.removeButton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeButton.sizePolicy().hasHeightForWidth())
        self.removeButton.setSizePolicy(sizePolicy)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout_3.addWidget(self.removeButton, 1, 3, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.serversTab, "")
        self.notificationsTab = QtWidgets.QWidget()
        self.notificationsTab.setObjectName("notificationsTab")
        self.groupBox = QtWidgets.QGroupBox(self.notificationsTab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 421, 131))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 30, 401, 101))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.successfulBuildsCheckbox = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.successfulBuildsCheckbox.setObjectName("successfulBuildsCheckbox")
        self.gridLayout_2.addWidget(self.successfulBuildsCheckbox, 0, 0, 1, 1)
        self.brokenBuildsCheckbox = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.brokenBuildsCheckbox.setObjectName("brokenBuildsCheckbox")
        self.gridLayout_2.addWidget(self.brokenBuildsCheckbox, 0, 1, 1, 1)
        self.fixedBuildsCheckbox = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.fixedBuildsCheckbox.setObjectName("fixedBuildsCheckbox")
        self.gridLayout_2.addWidget(self.fixedBuildsCheckbox, 1, 0, 1, 1)
        self.stillFailingBuildsCheckbox = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.stillFailingBuildsCheckbox.setObjectName("stillFailingBuildsCheckbox")
        self.gridLayout_2.addWidget(self.stillFailingBuildsCheckbox, 1, 1, 1, 1)
        self.connectivityIssuesCheckbox = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.connectivityIssuesCheckbox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.connectivityIssuesCheckbox.setObjectName("connectivityIssuesCheckbox")
        self.gridLayout_2.addWidget(self.connectivityIssuesCheckbox, 2, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.notificationsTab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 160, 401, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.scriptCheckbox = QtWidgets.QCheckBox(self.groupBox_3)
        self.scriptCheckbox.setGeometry(QtCore.QRect(0, 20, 401, 31))
        self.scriptCheckbox.setObjectName("scriptCheckbox")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 391, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scriptLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.scriptLabel.setObjectName("scriptLabel")
        self.horizontalLayout_3.addWidget(self.scriptLabel)
        self.scriptLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.scriptLineEdit.setEnabled(False)
        self.scriptLineEdit.setText("")
        self.scriptLineEdit.setObjectName("scriptLineEdit")
        self.horizontalLayout_3.addWidget(self.scriptLineEdit)
        self.tabWidget.addTab(self.notificationsTab, "")
        self.miscTab = QtWidgets.QWidget()
        self.miscTab.setObjectName("miscTab")
        self.showLastBuildTimeCheckbox = QtWidgets.QCheckBox(self.miscTab)
        self.showLastBuildTimeCheckbox.setGeometry(QtCore.QRect(10, 60, 351, 31))
        self.showLastBuildTimeCheckbox.setObjectName("showLastBuildTimeCheckbox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.miscTab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 421, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pollingIntervalLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.pollingIntervalLabel.setObjectName("pollingIntervalLabel")
        self.horizontalLayout_2.addWidget(self.pollingIntervalLabel)
        self.pollingIntervalSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.pollingIntervalSpinBox.setMinimumSize(QtCore.QSize(130, 0))
        self.pollingIntervalSpinBox.setMaximumSize(QtCore.QSize(130, 16777215))
        self.pollingIntervalSpinBox.setWrapping(False)
        self.pollingIntervalSpinBox.setMinimum(1)
        self.pollingIntervalSpinBox.setMaximum(60)
        self.pollingIntervalSpinBox.setSingleStep(1)
        self.pollingIntervalSpinBox.setObjectName("pollingIntervalSpinBox")
        self.horizontalLayout_2.addWidget(self.pollingIntervalSpinBox)
        self.groupBox_4 = QtWidgets.QGroupBox(self.miscTab)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 109, 401, 131))
        self.groupBox_4.setObjectName("groupBox_4")
        self.sortBuildByName = QtWidgets.QRadioButton(self.groupBox_4)
        self.sortBuildByName.setGeometry(QtCore.QRect(0, 20, 191, 21))
        self.sortBuildByName.setObjectName("sortBuildByName")
        self.sortBuildByLastBuildTime = QtWidgets.QRadioButton(self.groupBox_4)
        self.sortBuildByLastBuildTime.setGeometry(QtCore.QRect(0, 40, 221, 21))
        self.sortBuildByLastBuildTime.setChecked(True)
        self.sortBuildByLastBuildTime.setObjectName("sortBuildByLastBuildTime")
        self.tabWidget.addTab(self.miscTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Preferences)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.scriptLabel.setBuddy(self.scriptLineEdit)
        self.pollingIntervalLabel.setBuddy(self.pollingIntervalSpinBox)

        self.retranslateUi(Preferences)
        self.tabWidget.setCurrentIndex(0)
        self.scriptCheckbox.toggled['bool'].connect(self.scriptLineEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Preferences)

    def retranslateUi(self, Preferences):
        _translate = QtCore.QCoreApplication.translate
        Preferences.setWindowTitle(_translate("Preferences", "Preferences"))
        self.groupBox_2.setTitle(_translate("Preferences", "Monitored servers"))
        self.configureProjectButton.setText(_translate("Preferences", "Configure"))
        self.addButton.setToolTip(_translate("Preferences", "Add"))
        self.addButton.setText(_translate("Preferences", "+"))
        self.removeButton.setToolTip(_translate("Preferences", "Remove"))
        self.removeButton.setText(_translate("Preferences", "-"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.serversTab), _translate("Preferences", "Servers"))
        self.groupBox.setTitle(_translate("Preferences", "Notification settings"))
        self.successfulBuildsCheckbox.setText(_translate("Preferences", "successful builds"))
        self.brokenBuildsCheckbox.setText(_translate("Preferences", "broken builds"))
        self.fixedBuildsCheckbox.setText(_translate("Preferences", "fixed builds"))
        self.stillFailingBuildsCheckbox.setText(_translate("Preferences", "still failing builds"))
        self.connectivityIssuesCheckbox.setText(_translate("Preferences", "connectivity issues"))
        self.groupBox_3.setTitle(_translate("Preferences", "Custom notifications"))
        self.scriptCheckbox.setText(_translate("Preferences", "Execute script for notifications"))
        self.scriptLabel.setText(_translate("Preferences", "Script"))
        self.scriptLineEdit.setToolTip(_translate("Preferences", "#status# and #projects# would be replaced by the build status and projects respectively"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.notificationsTab), _translate("Preferences", "Notifications"))
        self.showLastBuildTimeCheckbox.setText(_translate("Preferences", "show last build time for each project"))
        self.pollingIntervalLabel.setText(_translate("Preferences", "Server polling interval"))
        self.pollingIntervalSpinBox.setSuffix(_translate("Preferences", " seconds"))
        self.groupBox_4.setTitle(_translate("Preferences", "Build Sort order"))
        self.sortBuildByName.setText(_translate("Preferences", "Sort builds by name"))
        self.sortBuildByLastBuildTime.setText(_translate("Preferences", "Sort builds by last build time"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.miscTab), _translate("Preferences", "Misc"))

from . import icons_rc
