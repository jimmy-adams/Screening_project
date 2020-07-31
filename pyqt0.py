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
import screening_of_doc1

#================================================================#
import os
from docx import Document #pip install python-docx
import pptx #pip install python-pptx
from pptx import Presentation
from win32com import client as wc
import table # 数据库显示模块

#================================================================#

#============Read & Load data from config.json===================#
cur_path = os.path.abspath(__file__)
parent_path = os.path.abspath(os.path.dirname(cur_path) + os.path.sep )
file_path = parent_path +'\config.json'
print(parent_path)
f = open(file_path, encoding='utf-8')
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
        
        self.btn2 = QPushButton("显示筛选库")
        
        self.btn2.clicked.connect(self.display)
        
        self.input0 = QLineEdit(self)
        
        self.input1 = QLineEdit(self)
                
        hbox0 = QHBoxLayout()
        #hbox0.setContentsMargins(0,0,0,0)as
        
        hbox1 = QHBoxLayout()
        
        hbox0.addWidget(QLabel("目标词汇"))
        
        hbox0.addWidget(self.input0)
        
        hbox0.addWidget(QLabel("替换为"))
        
        hbox0.addWidget(self.input1)
        
        hbox1.addWidget(self.btn2)
        
        hbox1.addWidget(self.btn1)
        
        hbox1.addWidget(self.btn)
        
        horizontalbox0 = QGroupBox()
        
        horizontalbox0.setLayout(hbox0)
        
        horizontalbox1 = QGroupBox()
        
        horizontalbox1.setLayout(hbox1)
        
        lay.addWidget(horizontalbox0)
        
        lay.addWidget(horizontalbox1)
        '''
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 60, 100, 30) 
        '''
        self.setGeometry(300, 300, 600, 400)
        
        self.setWindowTitle('查重平台')
        
        self.show()
        
    def getfiles(self):
        word = wc.Dispatch("Word.Application")
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
        old_file_path = str(dir_choose) + '/'
        print(old_file_path)
        
        for name in os.listdir(old_file_path):
            print(name)
            old_file = old_file_path + name 
            new_file = old_file_path + name
        #==========preprocess for doc===============================================#
        #==========convert the doc to docx,and delete the doc file==================#
            if old_file.split(".")[-1] == 'doc':
                doc = word.Documents.Open(old_file)
                doc.SaveAs("{}x".format(old_file), 12)#另存为后缀为".docx"的文件，其中参数12指docx文件
                doc.Close() #关闭原来word文件
                os.remove(old_file)
        #============================================================================#
            if old_file.split(".")[-1] == 'docx':
                id_type = 1
                document = Document(old_file)
                document = screening_of_doc1.check_and_change(document, data, id_type)
                document.save(new_file)
        #============================================================================#
        #==========convert the ppt to pptx,and delete the ppt file==================#
            if old_file.split(".")[-1] == 'ppt':
                ppt = powerpoint.Presentations.Open(old_file)
                ppt.SaveAs(old_file[:-4]+'.pptx')#另存为后缀为".pptx"的文件，其中参数12指pptx文件
                os.remove(old_file)
                ppt.Close() #关闭原来word文件
                #os.unlink(old_file) 
        #============================================================================#
            if old_file.split(".")[-1] == 'pptx':
                id_type = 2
                document = Presentation(old_file)
                document = screening_of_doc1.check_and_change(document, data, id_type)
                document.save(new_file)
            
            print("="*30)
        #====================================================#
        
    def showDialog(self):
        
        global config
        
        key = self.input0.text()
        print(self.input0.text())
        print(self.input1.text())
        print(type(key))
        
        #===================================================#
        #====check the possibility of validation============#
        if len(key) == 0:
            print('no input')
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '请输入目标值')
            msg_box.exec()
        else:
            #===================================================#
            temp_dict = {self.input0.text() : self.input1.text()}
            data.update(temp_dict)
            print(len(data.keys()))
            
            #============update the dict========================#
            dump_f = open("config.json",'w')
            json.dump(data,dump_f)
            #===================================================#
            
    def display(self):
        self.win = table.Table()
        
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
    
    desktop = QApplication.desktop()  # 获取坐标
    x = (desktop.width() - ex.width()) // 2
    y = (desktop.height() - ex.height()) // 2
    ex.move(x, y)  # 移动
    sys.exit(app.exec_())
