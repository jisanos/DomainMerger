# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 637)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(10, 40, 281, 181))
        self.treeView.setObjectName("treeView")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 260, 241, 161))
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(10, 450, 241, 151))
        self.listView_2.setObjectName("listView_2")
        self.listView_3 = QtWidgets.QListView(self.centralwidget)
        self.listView_3.setGeometry(QtCore.QRect(305, 40, 261, 561))
        self.listView_3.setObjectName("listView_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 20, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 240, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 430, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 20, 131, 16))
        self.label_4.setObjectName("label_4")
        self.btn_add_blacklist = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_blacklist.setGeometry(QtCore.QRect(260, 280, 31, 31))
        self.btn_add_blacklist.setObjectName("btn_add_blacklist")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 340, 31, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 540, 31, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 480, 31, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(380, 610, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 610, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Blacklist Packs"))
        self.label_2.setText(_translate("MainWindow", "Custom Domain Blacklist"))
        self.label_3.setText(_translate("MainWindow", "Custom Domain Whitelist"))
        self.label_4.setText(_translate("MainWindow", "Complete Merged Blacklist"))
        self.btn_add_blacklist.setText(_translate("MainWindow", "+"))
        self.pushButton_2.setText(_translate("MainWindow", "-"))
        self.pushButton_3.setText(_translate("MainWindow", "-"))
        self.pushButton_4.setText(_translate("MainWindow", "+"))
        self.pushButton.setText(_translate("MainWindow", "Apply"))
