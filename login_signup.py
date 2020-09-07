# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:37:30 2020

@author: Melody
"""
#!/usr/bin/python3
#coding:utf-8

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication,Qt
import sys
import json
import pyqt0


class SignupWindow(QWidget):
    def __init__(self, parent=None):
        super(SignupWindow, self).__init__(parent)
        usr = QLabel("新用户名：")
        pwd = QLabel("用户密码：")
        self.usrLineEdit = QLineEdit()
        self.pwdLineEdit = QLineEdit()
        self.pwdLineEdit.setEchoMode(QLineEdit.Password)

        gridLayout = QGridLayout()
        gridLayout.addWidget(usr, 0, 0, 1, 1)
        gridLayout.addWidget(pwd, 1, 0, 1, 1)
        gridLayout.addWidget(self.usrLineEdit, 0, 1, 1, 3);
        gridLayout.addWidget(self.pwdLineEdit, 1, 1, 1, 3);

        okBtn = QPushButton("确定")
        returnBtn = QPushButton("返回")
        btnLayout = QHBoxLayout()

        btnLayout.setSpacing(60)
        btnLayout.addWidget(okBtn)
        btnLayout.addWidget(returnBtn)

        dlgLayout = QVBoxLayout()
        dlgLayout.setContentsMargins(40, 40, 40, 40)
        dlgLayout.addLayout(gridLayout)
        dlgLayout.addStretch(40)
        dlgLayout.addLayout(btnLayout)

        self.setLayout(dlgLayout)
        okBtn.clicked.connect(self.register)
        returnBtn.clicked.connect(self.return_)
        self.setWindowTitle("注册界面")
        self.resize(300, 200)    
    
    def register(self):
        f = open("custom_data.json", encoding='utf-8')
        data = json.load(f)
        if data.get(self.usrLineEdit.text()) == None:
            temp_dict = {self.usrLineEdit.text():{'user_name':self.usrLineEdit.text() ,'account_password': self.pwdLineEdit.text()}}
            data.update(temp_dict)
        #============update the dict========================#
            container = open("custom_data.json",'w')
            json.dump(data,container)
        #===================================================#
        else:
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '账户已经存在')
            msg_box.exec()
        
    def return_(self):
        signup.close()
        login.show()
class LoginWindow(QWidget):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        usr = QLabel("用户：")
        pwd = QLabel("密码：")
        self.usrLineEdit = QLineEdit()
        self.pwdLineEdit = QLineEdit()
        self.pwdLineEdit.setEchoMode(QLineEdit.Password)

        gridLayout = QGridLayout()
        gridLayout.addWidget(usr, 0, 0, 1, 1)
        gridLayout.addWidget(pwd, 1, 0, 1, 1)
        gridLayout.addWidget(self.usrLineEdit, 0, 1, 1, 3);
        gridLayout.addWidget(self.pwdLineEdit, 1, 1, 1, 3);

        okBtn = QPushButton("确定")
        cancelBtn = QPushButton("注册")
        btnLayout = QHBoxLayout()

        btnLayout.setSpacing(60)
        btnLayout.addWidget(okBtn)
        btnLayout.addWidget(cancelBtn)

        dlgLayout = QVBoxLayout()
        dlgLayout.setContentsMargins(40, 40, 40, 40)
        dlgLayout.addLayout(gridLayout)
        dlgLayout.addStretch(40)
        dlgLayout.addLayout(btnLayout)

        self.setLayout(dlgLayout)
        okBtn.clicked.connect(self.accept)
        cancelBtn.clicked.connect(self.transfer)
        self.setWindowTitle("企业查重登录")
        self.resize(300, 200)

    def accept(self):
        if self.usrLineEdit.text().strip() == "szict" and self.pwdLineEdit.text() == "33322000":
            #super(LoginWindow, self).accept()
            self.win = pyqt0.Example()
            return 1
        else:
            QMessageBox.warning(self,
                    "警告",
                    "用户名或密码错误！",
                    QMessageBox.Yes)
            self.usrLineEdit.setFocus()
    
    def keyPressEvent(self, e):
        if str(e.key()) == '16777220':# confirm the pressed key is enter
            self.accept()

    def transfer(self):
        login.close()
        signup.show()
    def reject(self):
        QMessageBox.warning(self,
                            "警告",
                            "确定退出？",
                            QMessageBox.Yes)
        QCoreApplication.instance().quit

if __name__ == '__main__':
    app=QApplication(sys.argv)
    login = LoginWindow()
    signup = SignupWindow()
    login.show()
    sys.exit(app.exec_())

