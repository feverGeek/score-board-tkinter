# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScoreBoard.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form:
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(515, 493)
        Form.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("font: 20pt \"Sans Serif\";\n"
"color: rgb(0, 85, 255);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listView = QtWidgets.QListView(Form)
        self.listView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.closePortButton = QtWidgets.QPushButton(self.groupBox)
        self.closePortButton.setObjectName("closePortButton")
        self.gridLayout.addWidget(self.closePortButton, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.searchButton = QtWidgets.QPushButton(self.groupBox)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout.addWidget(self.searchButton, 2, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.openPortButton = QtWidgets.QPushButton(self.groupBox)
        self.openPortButton.setObjectName("openPortButton")
        self.gridLayout.addWidget(self.openPortButton, 1, 2, 1, 1)
        self.checkButton = QtWidgets.QPushButton(self.groupBox)
        self.checkButton.setObjectName("checkButton")
        self.gridLayout.addWidget(self.checkButton, 2, 5, 1, 1)
        self.sendConButton = QtWidgets.QPushButton(self.groupBox)
        self.sendConButton.setObjectName("sendConButton")
        self.gridLayout.addWidget(self.sendConButton, 1, 5, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "ScoreBoard"))
        self.label_2.setText(_translate("Form", "无串口"))
        self.groupBox.setTitle(_translate("Form", "串口选择"))
        self.closePortButton.setText(_translate("Form", "关闭串口"))
        self.searchButton.setText(_translate("Form", "搜索串口"))
        self.label_3.setText(_translate("Form", "串口检测:"))
        self.openPortButton.setText(_translate("Form", "打开串口"))
        self.checkButton.setText(_translate("Form", "检查上线"))
        self.sendConButton.setText(_translate("Form", "发送连接"))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui_form = Ui_Form()
    ui_form.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
