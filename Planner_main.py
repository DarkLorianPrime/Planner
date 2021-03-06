import os
import sys

import PyQt5.QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, pyqtSlot
from PyQt5.uic.properties import QtWidgets
from PyQt5 import *
import design
import sqlite3
import Models, window_design
from logger import logger

Name = ''
conn = sqlite3.connect(f'C:/USERS/{os.getlogin()}/AppData/Roaming/login.sqlite')
conn.execute('CREATE TABLE IF NOT EXISTS user(Login text)')
cur = conn.cursor()
cur.execute('DELETE FROM user')


class Object_receiver(QObject):
    update = pyqtSignal()


class Shop(object):
    __instances = {}

    @staticmethod
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Shop, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow, QtWidgets.QLineEdit, QtWidgets.QListWidget):
    __metaclass__ = Shop()

    @logger()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Planner')
        self.Name = ''
        self.Restartmainwindow = pyqtSignal()
        self.pushButton.clicked.connect(lambda: self.add_group())
        self.pushButton_2.clicked.connect(lambda: self.del_group())
        self.pushButton_3.clicked.connect(lambda: self.del_subgroup())
        self.pushButton_4.clicked.connect(lambda: self.add_subgroup())
        self.pushButton_5.clicked.connect(lambda: self.add_note())
        self.pushButton_6.clicked.connect(lambda: self.del_note())
        self.pushButton_8.clicked.connect(lambda: self.del_case())
        self.pushButton_7.clicked.connect(lambda: self.add_case())
        self.pushButton_9.clicked.connect(lambda: self.login())
        self.g = self.check()
        self.comboBox_2.currentIndexChanged.connect(lambda: self.subgroupselect())
        self.c = Object_receiver()
        self.c.update.connect(lambda: self.check())
        print('WAIT')
        self.connection_to_table()

    @logger()
    def subgroupselect(self):
        pass

    @staticmethod
    @logger()
    def connection_to_table():
        Models.connect_to_db()

    @logger()
    def add_case(self):
        print('case')

    @logger()
    def del_case(self):
        print('-case')

    @logger()
    def add_note(self):
        print('note')

    @logger()
    def del_note(self):
        print('-note')

    @logger()
    def check(self):
        print('????????????????')
        i_te = []
        cur.execute('select * from user')
        r = cur.fetchone()
        r = ['\..']
        if r is None:
            return
        groups = Models.Groups.select().where(Models.Groups.user_name == r[0])
        for i in groups:
            i_te.append(i.group_name)
        if i_te:
            self.comboBox_2.clear()
            self.comboBox_2.addItems(i_te)
        return i_te

    @logger()
    def vtor(self):
        print('????????????????')
        self.check()

    @logger()
    def login(self, t=0):
        s = ''
        if t == 1:
            cur.execute('select * from user')
            v = cur.fetchone()[0]
        else:
            v = self.lineEdit.text()
        cur.execute('DELETE FROM user')
        self.comboBox_2.clear()
        cur.execute('insert into user values(?)', (v,))
        conn.commit()
        user_var = Models.Users.get_or_none(Models.Users.username == v)
        if user_var is None:
            Models.Users(username=self.Name).save()
        notes = Models.notes.get_or_none(Models.notes.user_name == v)
        subgroups = Models.subgroups.get_or_none(Models.subgroups.user_name == v)
        cases = Models.cases.get_or_none(Models.cases.user_name == v)
        i_te = self.check()
        if not i_te:
            s += '???????????? ???? ????????????????????! ?????? ?????? ???? ???? ?????????????? ?????????????????? ?????????????????? ?? ????????!\n'
        if subgroups is None:
            s += '?????????????????? ???? ????????????????????, ?????? ?????? ???? ???? ?????????????? ?????????????????? ????????!\n'
        if notes is None:
            s += '?????????????? ???? ????????????????????!\n'
        if cases is None:
            s += '???????? ???? ????????????????????!'
        if s != '':
            PyQt5.QtWidgets.QMessageBox.warning(self, 'Warning!', s)

    @logger()
    def add_group(self):
        cur.execute('select * from user')
        r = cur.fetchone()
        New_test(what='????????????', name=r[0]).show()

    @logger()
    def del_group(self):
        print('-group')

    @logger()
    def del_subgroup(self):
        print('-subgroup')

    @logger()
    def add_subgroup(self):
        print('subgroup')


class New_test(QtWidgets.QMainWindow, window_design.Ui_Dialog, QtWidgets.QLineEdit, QtWidgets.QListWidget):
    __metaclass__ = Shop()

    @logger()
    def __init__(self, what, name):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Planner')
        self.label.setText(f'?????????????? ???????????????? {what}')
        if what == '????????????':
            self.pushButton.clicked.connect(lambda: self.add_group(name))
        if what == '??????????????????':
            self.pushButton.clicked.connect(lambda: self.add_subgroup(name))
        self.pushButton_2.clicked.connect(lambda: self.destroy())

    @logger()
    def add_group(self, name=None):
        z = Models.Groups.select().order_by(Models.Groups.group_id.desc())
        if name is None:
            PyQt5.QtWidgets.QMessageBox.warning(self, 'Warning!', '?????????????? ??????????????????????????!')
        else:
            text = self.lineEdit.text()
            if text != '':
                if Models.Groups.get_or_none(Models.Groups.group_name == text) is None:
                    v = None
                    for i in z:
                        v = i.group_id
                        break
                    if v is None:
                        Models.Groups(group_id=0, group_name=text, user_name=name).save()
                    else:
                        Models.Groups(group_id=int(v) + 1, group_name=text, user_name=name).save()
                    self.destroy()
                    # ExampleApp().c.update.emit()
                    var = ExampleApp().g
                    print(var)
                else:
                    PyQt5.QtWidgets.QMessageBox.warning(self, 'Warning!', '?????????? ???????????? ?????? ????????????????????!')
            else:
                PyQt5.QtWidgets.QMessageBox.warning(self, 'Warning!', '???????????????? ???????????? ???? ?????????? ??????????????????????.')

    def add_subgroup(self, name):
        pass



@logger()
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()