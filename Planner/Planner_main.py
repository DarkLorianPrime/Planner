import os
import sys

import PyQt5.QtWidgets
from PyQt5.uic.properties import QtWidgets
from PyQt5 import *
import design
import sqlite3
from projects.Planner import Models, window_design

Name = ''
conn = sqlite3.connect(f'C:/USERS/{os.getlogin()}/AppData/Roaming/login.sqlite')
conn.execute('CREATE TABLE IF NOT EXISTS user(Login text)')
cur = conn.cursor()
cur.execute('DELETE FROM user')


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow, QtWidgets.QLineEdit, QtWidgets.QListWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Planner')
        self.Name = ''
        self.pushButton.clicked.connect(lambda: self.add_group())
        self.pushButton_2.clicked.connect(lambda: self.del_group())
        self.pushButton_3.clicked.connect(lambda: self.del_subgroup())
        self.pushButton_4.clicked.connect(lambda: self.add_subgroup())
        self.pushButton_5.clicked.connect(lambda: self.add_note())
        self.pushButton_6.clicked.connect(lambda: self.del_note())
        self.pushButton_8.clicked.connect(lambda: self.del_case())
        self.pushButton_7.clicked.connect(lambda: self.add_case())
        self.pushButton_9.clicked.connect(lambda: self.login())
        self.comboBox_2.currentIndexChanged.connect(lambda: self.subgroupselect())
        print('WAIT')
        self.connection_to_table()

    def subgroupselect(self):
        pass

    @staticmethod
    def connection_to_table():
        Models.connect_to_db()

    def add_case(self):
        print('case')

    def del_case(self):
        print('-case')

    def add_note(self):
        print('note')

    def del_note(self):
        print('-note')

    def check(self):
        print('Запустил')
        i_te = []
        self.comboBox_2.clear()
        cur.execute('select * from user')
        r = cur.fetchone()
        groups = Models.Groups.select().where(Models.Groups.user_name == r[0])
        for i in groups:
            i_te.append(i.group_name)
        if i_te:
            self.comboBox_2.addItems(i_te)
        return i_te

    def vtor(self):
        print('Запускаю')
        self.check()

    def login(self, t=0):
        try:
            if t == 1:
                print(1)
                self.check()
                return
            cur.execute('DELETE FROM user')
            self.comboBox_2.clear()
            v, s = self.lineEdit.text(), ''
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
                s += 'Группы не обнаружены! Без них вы не сможете добавлять подгруппы и дела!\n'
            if subgroups is None:
                s += 'Подгруппы не обнаружены, без них вы не сможете добавлять дела!\n'
            if notes is None:
                s += 'Заметки не обнаружены!\n'
            if cases is None:
                s += 'Дела не обнаружены!'
            if s != '':
                PyQt5.QtWidgets.QMessageBox.warning(self, 'Warning!', s)
        except Exception as ex:
            print(ex)

    def add_group(self):
        cur.execute('select * from user')
        r = cur.fetchone()
        New_test(what='группы', name=r[0]).show()

    def del_group(self):
        print('-group')

    def del_subgroup(self):
        print('-subgroup')

    def add_subgroup(self):
        print('subgroup')


class New_test(QtWidgets.QMainWindow, window_design.Ui_Dialog, QtWidgets.QLineEdit, QtWidgets.QListWidget):
    def __init__(self, what, name):
        try:
            super().__init__()
            self.setupUi(self)
            self.setWindowTitle('Planner')

            self.label.setText(f'Введите название {what}')
            if what == 'группы':
                self.pushButton.clicked.connect(lambda: self.add_group(name))
            if what == 'подгруппы':
                self.pushButton.clicked.connect(lambda: self.add_subgroup(name))
            self.pushButton_2.clicked.connect(lambda: self.destroy())
        except Exception as ex:
            print(ex)

    def add_group(self, name=None):
        z = Models.Groups.select().order_by(Models.Groups.group_id.desc())
        if name is None:
            PyQt5.QtWidgets.QMessageBox.warning(self, 'Warning!', 'Сначала авторизуйтесь!')
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
                    ExampleApp().login(1)
                else:
                    PyQt5.QtWidgets.QMessageBox.warning(self, 'Warning!', 'Такая группа уже существует!')
            else:
                PyQt5.QtWidgets.QMessageBox.warning(self, 'Warning!', 'Название группы не может повторяться.')

    def add_subgroup(self, name):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()