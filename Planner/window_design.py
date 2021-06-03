from PyQt5.QtCore import QSize, QRect, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 400)
        Dialog.setMinimumSize(QSize(600, 400))
        Dialog.setMaximumSize(QSize(600, 600))
        Dialog.setStyleSheet(u"background-color: rgb(33, 34, 42); color: white;")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 340, 101, 21))
        self.pushButton.setStyleSheet(u"color: white; border: 0; font-size: 24px;")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(440, 340, 101, 21))
        self.pushButton_2.setStyleSheet(u"color: white; border: 0; font-size: 24px;")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 40, 411, 111))
        self.label.setStyleSheet(u"color: white; font-size: 24px;")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 210, 471, 71))
        self.lineEdit.setStyleSheet(u"border: 0; border-bottom: 1px inset red; color: white; font-size: 24px;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"ADD", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"EXIT", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 {text}", None))
        self.lineEdit.setText("")
    # retranslateUi

