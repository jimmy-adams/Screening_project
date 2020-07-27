# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:42:56 2020

@author: Melody
"""
import sys
import json
from PyQt5.QtWidgets import QWidget, QPushButton,QHBoxLayout, QVBoxLayout, QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore

#============Read & Load data from config.json===================#
f = open("config.json", encoding='utf-8')
data = json.load(f)
#================================================================#


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        
        centralwidget = QWidget()
        
        self.setCentralWidget(centralwidget)
        
        lay = QVBoxLayout(centralwidget)
        
        lay.setContentsMargins(0,0,0,0)
        
        self.btn = QPushButton('Update',self)
        
        self.btn.clicked.connect(self.showDialog)
        
        self.btn1 = QPushButton("加载文本文件")
        
        self.btn1.clicked.connect(self.getfiles)
        
        self.input0 = QLineEdit(self)
        
        self.input1 = QLineEdit(self)
                
        hbox0 = QHBoxLayout()
        #hbox0.setContentsMargins(0,0,0,0)as
        
        hbox1 = QHBoxLayout()
        
        hbox0.addWidget(QLabel("目标词汇"))
        
        hbox0.addWidget(self.input0)
        
        hbox0.addWidget(QLabel("替换为"))
        
        hbox0.addWidget(self.input1)
        
        hbox1.addWidget(self.btn1)
        
        hbox1.addWidget(self.btn)
        
        horizontalbox0 = QGroupBox()
        
        horizontalbox0.setLayout(hbox0)
        
        horizontalbox1 = QGroupBox()
        
        horizontalbox1.setLayout(hbox1)
        
        lay.addWidget(horizontalbox0)
        
        lay.addWidget(horizontalbox1)

        self.setGeometry(300, 300, 600, 400)
        
        self.setWindowTitle('查重平台')
        
        self.show()
        
    def getfiles(self):
        '''
        #==================get multiple files'name==========#
        selectedFiles = QFileDialog.getOpenFileNames(self,
                "Select one file to open",
                "/home",'Docement ( *.pdf *doc *docx *ppt)')
        print(len(selectedFiles[0]))
        for i in range(len(selectedFiles[0])):
            print(str(selectedFiles[0][i]))
            print("="*30)
        #====================================================#
        '''
        #==================get directory'name==========#
        dir_choose = QFileDialog.getExistingDirectory(self,  
                                    "选取文件夹") # 起始路径
        print(str(dir_choose))
        #====================================================#
    
    def showDialog(self):
        
        global config
        
        key = self.input0.text()
        print(self.input0.text())
        print(self.input1.text())
        print(type(key))
        
        #===================================================#
        #====check the possibility of validation============#
        #===================================================#
        temp_dict = {self.input0.text() : self.input1.text()}
        data.update(temp_dict)
        print(len(data.keys()))
        
        #============update the dict========================#
        dump_f = open("config.json",'w')
        json.dump(data,dump_f)
        #===================================================#
        '''

        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')

        if ok:
            self.le.setText(str(text))
        '''

if __name__ == '__main__':
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    ex = Example()
    sys.exit(app.exec_())
