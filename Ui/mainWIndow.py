# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWIndow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(302, 578)
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(19, 196, 261, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.showimg = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.showimg.sizePolicy().hasHeightForWidth())
        self.showimg.setSizePolicy(sizePolicy)
        self.showimg.setText("")
        self.showimg.setScaledContents(True)
        self.showimg.setObjectName("showimg")
        self.verticalLayout.addWidget(self.showimg)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(19, 56, 261, 121))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.layoutWidget1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.imgPrevie = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.imgPrevie.sizePolicy().hasHeightForWidth())
        self.imgPrevie.setSizePolicy(sizePolicy)
        self.imgPrevie.setText("")
        self.imgPrevie.setScaledContents(True)
        self.imgPrevie.setObjectName("imgPrevie")
        self.verticalLayout_2.addWidget(self.imgPrevie)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 10, 277, 35))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_readFromClipboard = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_readFromClipboard.setObjectName("btn_readFromClipboard")
        self.horizontalLayout.addWidget(self.btn_readFromClipboard)
        self.btn_selectImg = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_selectImg.setObjectName("btn_selectImg")
        self.horizontalLayout.addWidget(self.btn_selectImg)
        self.btn_setting = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_setting.setObjectName("btn_setting")
        self.horizontalLayout.addWidget(self.btn_setting)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 350, 261, 192))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.latex1 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.latex1.setObjectName("latex1")
        self.gridLayout.addWidget(self.latex1, 0, 0, 1, 1)
        self.btn_copy1 = QtWidgets.QPushButton(self.layoutWidget3)
        self.btn_copy1.setObjectName("btn_copy1")
        self.gridLayout.addWidget(self.btn_copy1, 0, 1, 1, 1)
        self.latex2 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.latex2.setObjectName("latex2")
        self.gridLayout.addWidget(self.latex2, 1, 0, 1, 1)
        self.btn_copy2 = QtWidgets.QPushButton(self.layoutWidget3)
        self.btn_copy2.setObjectName("btn_copy2")
        self.gridLayout.addWidget(self.btn_copy2, 1, 1, 1, 1)
        self.latex3 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.latex3.setObjectName("latex3")
        self.gridLayout.addWidget(self.latex3, 2, 0, 1, 1)
        self.btn_copy3 = QtWidgets.QPushButton(self.layoutWidget3)
        self.btn_copy3.setObjectName("btn_copy3")
        self.gridLayout.addWidget(self.btn_copy3, 2, 1, 1, 1)
        self.latex4 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.latex4.setObjectName("latex4")
        self.gridLayout.addWidget(self.latex4, 3, 0, 1, 1)
        self.btn_copy4 = QtWidgets.QPushButton(self.layoutWidget3)
        self.btn_copy4.setObjectName("btn_copy4")
        self.gridLayout.addWidget(self.btn_copy4, 3, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Latex识别"))
        self.label_2.setText(_translate("MainWindow", "识别结果"))
        self.label.setText(_translate("MainWindow", "原图预览"))
        self.btn_readFromClipboard.setText(_translate("MainWindow", "读取剪切板"))
        self.btn_selectImg.setText(_translate("MainWindow", "选择图片"))
        self.btn_setting.setText(_translate("MainWindow", "设置"))
        self.label_3.setText(_translate("MainWindow", "LaTex代码"))
        self.btn_copy1.setText(_translate("MainWindow", "复制"))
        self.btn_copy2.setText(_translate("MainWindow", "复制"))
        self.btn_copy3.setText(_translate("MainWindow", "复制"))
        self.btn_copy4.setText(_translate("MainWindow", "复制"))
