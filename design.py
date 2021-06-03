# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerefLIYR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PyQt5.QtCore import QRect, QCoreApplication, QSize, QMetaObject
from PyQt5.QtWidgets import QFrame, QListWidget, QComboBox, QPushButton, QLabel, QLineEdit, QWidget, QTextBrowser

"""
                                        QPushButton {
                                            border: 0px;
                                            color: rgb(132, 43, 43);
                                            font-weight: bold;
                                            font-size: 24px; }
                                        QPushButton:hover { 
                                            border: 0px;
                                            color: rgb(102, 13, 13);
                                            font-weight: bold;
                                            font-size: 24px; 
                                      }
                                        """
"""
                                        QPushButton {
                                            border: 0px;
                                            color: rgb(40, 150, 38);
                                            font-weight: bold;
                                            font-size: 24px; }
                                        QPushButton:hover { 
                                            border: 0px;
                                            color: rgb(70, 180, 78);
                                            font-weight: bold;
                                            font-size: 24px; 
                                      }
                                        """
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1400, 900)
        MainWindow.setMinimumSize(QSize(1400, 900))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1920, 1080))
        self.centralwidget.setStyleSheet(u"background-color: rgb(33, 34, 42);")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(530, 190, 271, 41))
        self.comboBox.setMouseTracking(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(23, 24, 32);\n"
"color: rgb(181, 181, 181);\n"
"border: 0px;\n"
"font-size: 20px;\n"
"")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, -150, 41, 1071))
        self.line.setStyleSheet(u"color: black;")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(480, -130, 41, 1071))
        self.line_2.setStyleSheet(u"color: black;")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 0, 461, 921))
        self.listWidget.setStyleSheet(u"border: 0px;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(530, 90, 31, 31))
        self.pushButton.setStyleSheet("""
                                        QPushButton {
                                            border: 0px;
                                            color: rgb(40, 150, 38);
                                            font-weight: bold;
                                            font-size: 24px; }
                                        QPushButton:hover { 
                                            border: 0px;
                                            color: rgb(70, 180, 78);
                                            font-weight: bold;
                                            font-size: 24px; 
                                      }
                                        """)
        self.pushButton.setIconSize(QSize(32, 32))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(600, 90, 31, 31))
        self.pushButton_2.setStyleSheet("""
                                        QPushButton {
                                            border: 0px;
                                            color: rgb(132, 43, 43);
                                            font-weight: bold;
                                            font-size: 24px; }
                                        QPushButton:hover { 
                                            border: 0px;
                                            color: rgb(102, 13, 13);
                                            font-weight: bold;
                                            font-size: 24px; 
                                      }
                                        """)
        self.pushButton_2.setIconSize(QSize(32, 32))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(530, 0, 191, 31))
        self.label.setStyleSheet(u"color: white;\n"
"font-size: 24px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(530, 150, 191, 31))
        self.label_2.setStyleSheet(u"color: white;\n"
"font-size: 24px;")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(600, 240, 31, 31))
        self.pushButton_3.setStyleSheet("""
                                        QPushButton {
                                            border: 0px;
                                            color: rgb(132, 43, 43);
                                            font-weight: bold;
                                            font-size: 24px; }
                                        QPushButton:hover { 
                                            border: 0px;
                                            color: rgb(102, 13, 13);
                                            font-weight: bold;
                                            font-size: 24px; 
                                      }
                                        """)
        self.pushButton_3.setIconSize(QSize(32, 32))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(530, 240, 31, 31))
        self.pushButton_4.setStyleSheet("""
                                        QPushButton {
                                            border: 0px;
                                            color: rgb(40, 150, 38);
                                            font-weight: bold;
                                            font-size: 24px; }
                                        QPushButton:hover { 
                                            border: 0px;
                                            color: rgb(70, 180, 78);
                                            font-weight: bold;
                                            font-size: 24px; 
                                      }
                                        """)
        self.pushButton_4.setIconSize(QSize(32, 32))
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(530, 40, 271, 41))
        self.comboBox_2.setMouseTracking(False)
        self.comboBox_2.setStyleSheet(u"background-color: rgb(23, 24, 32);\n"
"color: rgb(181, 181, 181);\n"
"border: 0px;\n"
"font-size: 20px;\n"
"")
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(1360, 330, 41, 1071))
        self.line_3.setStyleSheet(u"color: black;")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.listWidget_2 = QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(990, 340, 371, 551))
        self.listWidget_2.setStyleSheet(u"border: 0px;")
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(940, 330, 41, 571))
        self.line_4.setStyleSheet(u"color: black;")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(960, 320, 421, 16))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(910, 30, 271, 41))
        self.label_3.setStyleSheet(u"color: white; font-size: 24px;")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(1040, 30, 331, 41))
        self.lineEdit.setStyleSheet(u"border: 0;\n"
"border-bottom: 4px inset red;\n"
"color: white; \n"
"font-size: 20px;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(960, 270, 161, 31))
        self.label_4.setStyleSheet(u"color: white; font-size: 24px;")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(1070, 270, 31, 31))
        self.pushButton_5.setStyleSheet("""
                                        QPushButton {
                                            border: 0px;
                                            color: rgb(40, 150, 38);
                                            font-weight: bold;
                                            font-size: 24px; }
                                        QPushButton:hover { 
                                            border: 0px;
                                            color: rgb(70, 180, 78);
                                            font-weight: bold;
                                            font-size: 24px; 
                                      }
                                        """)
        self.pushButton_5.setIconSize(QSize(32, 32))
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(1140, 270, 31, 31))
        self.pushButton_6.setStyleSheet("""
                                        QPushButton {
                                            border: 0px;
                                            color: rgb(132, 43, 43);
                                            font-weight: bold;
                                            font-size: 24px; }
                                        QPushButton:hover { 
                                            border: 0px;
                                            color: rgb(102, 13, 13);
                                            font-weight: bold;
                                            font-size: 24px; 
                                      }
                                        """)
        self.pushButton_6.setIconSize(QSize(32, 32))
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(790, 610, 31, 31))
        self.pushButton_7.setStyleSheet("""
                                        QPushButton {
                                            border: 0px;
                                            color: rgb(40, 150, 38);
                                            font-weight: bold;
                                            font-size: 24px; }
                                        QPushButton:hover { 
                                            border: 0px;
                                            color: rgb(70, 180, 78);
                                            font-weight: bold;
                                            font-size: 24px; 
                                      }
                                        """)
        self.pushButton_7.setIconSize(QSize(32, 32))
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(640, 610, 31, 31))
        self.pushButton_8.setStyleSheet("""
                                        QPushButton {
                                            border: 0px;
                                            color: rgb(132, 43, 43);
                                            font-weight: bold;
                                            font-size: 24px; }
                                        QPushButton:hover { 
                                            border: 0px;
                                            color: rgb(102, 13, 13);
                                            font-weight: bold;
                                            font-size: 24px; 
                                      }
                                        """)
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(1040, 90, 91, 31))
        self.pushButton_9.setStyleSheet("""
                                        QPushButton {
                                            border: 0px;
                                            color: white;
                                            font-weight: bold;
                                            font-size: 24px; }
                                        QPushButton:hover { 
                                            border: 1px inset gray;
                                            color: white;
                                            font-weight: bold;
                                            font-size: 24px; 
                                      }
                                        """)
        self.pushButton_8.setIconSize(QSize(32, 32))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(530, 650, 401, 141))
        self.textBrowser.setStyleSheet(u"color: white; border: 0;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.line.raise_()
        self.comboBox.raise_()
        self.line_2.raise_()
        self.listWidget.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.comboBox_2.raise_()
        self.line_3.raise_()
        self.listWidget_2.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.label_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.textBrowser.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        # self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0430\u0444\u044b", None))
        # self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"House", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sub-Group", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"+", None))
        # self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0444\u044b\u0432", None))
        # self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0423\u0431\u043e\u0440\u043a\u0430", None))
        # self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0430\u0444\u044b", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Your name:", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"\\..", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438:", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">\u0420\u0430\u0431\u043e\u0442\u0430 </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">\u0421 \u0434\u0435\u043b\u0430\u043c\u0438</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">(\u0432\u044b\u0434\u0435\u043b\u0438 \u043f\u0435\u0440"
                        "\u0435\u0434 \u0440\u0430\u0431\u043e\u0442\u043e\u0439)</span></p></body></html>", None))
    # retranslateUi
