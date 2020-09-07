# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:42:56 2020

@author: Melody
"""
import sys
import time # import the time module to display the updated time
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
f = open('config.json', encoding='utf-8')
data = json.load(f)
#================================================================#
#=============try to make it a function==========================#

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        centralwidget = QWidget()
        
        self.setCentralWidget(centralwidget)
        
        #lay = QVBoxLayout(centralwidget)
        
        #lay.setContentsMargins(0,0,0,0)
        self.listFile = QListWidget()
        self.btn = QPushButton('Update',self)
        self.btn.clicked.connect(self.showDialog)
        
        self.btn1 = QPushButton("加载文本文件")
        self.btn1.clicked.connect(self.getfiles)
        
        self.btn2 = QPushButton("显示筛选库")
        self.btn2.clicked.connect(self.display)
        
        self.btn3 = QPushButton("Save")
        self.btn3.clicked.connect(self.display)
        
        self.input0 = QLineEdit(self)
        self.input1 = QLineEdit(self)
        
        #============================================#
         # creating a label widget 
        # by default label will display at top left corner 
        self.signal_lamp = QLabel(self) 
     
        # making label square in size 
        self.signal_lamp.resize(20, 20) 
  
        # setting up border and radius 
        self.signal_lamp.setStyleSheet("background-color:red; border: 3px solid red;border-radius: 10px;") 
        #============================================#
        HLayout0 = QHBoxLayout()
        HLayout0.setSpacing(380)
        HLayout0.addWidget(self.signal_lamp)
        HLayout0.addWidget(self.btn3)
        
        HLayout1 = QHBoxLayout()
        #HLayout1.setSpacing(10)
        HLayout1.addWidget(QLabel("目标词汇:"))
        HLayout1.addWidget(self.input0)
        HLayout1.addWidget(QLabel("替换为:"))
        HLayout1.addWidget(self.input1)
        
        HLayout2 = QHBoxLayout()
        #HLayout2.setSpacing(10)
        HLayout2.addWidget(self.btn2)
        HLayout2.addWidget(self.btn1)
        HLayout2.addWidget(self.btn)

        HLayout3 = QHBoxLayout()
        HLayout3.addWidget(self.listFile)
        
        dlgLayout = QVBoxLayout(centralwidget)
        dlgLayout.setContentsMargins(40, 20, 40, 40)
        #dlgLayout.addStretch(10)
        dlgLayout.addLayout(HLayout0)
        dlgLayout.addLayout(HLayout3)
        dlgLayout.addLayout(HLayout1)
        dlgLayout.addLayout(HLayout2)
        self.setLayout(dlgLayout)
        
        '''
        hbox0 = QHBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        
        hbox0.addWidget(self.btn3)
        
        hbox1.addWidget(QLabel("目标词汇"))
        hbox1.addWidget(self.input0)
        hbox1.addWidget(QLabel("替换为"))
        hbox1.addWidget(self.input1)
        
        hbox2.addWidget(self.btn2)
        hbox2.addWidget(self.btn1)
        hbox2.addWidget(self.btn)
        
        horizontalbox0 = QGroupBox()
        horizontalbox0.setLayout(hbox0)
        
        horizontalbox1 = QGroupBox()
        horizontalbox1.setLayout(hbox1)
        
        horizontalbox2 = QGroupBox()
        horizontalbox2.setLayout(hbox2)
        
        lay.addWidget(horizontalbox0)
        lay.addWidget(horizontalbox1)
        lay.addWidget(horizontalbox2)
        '''
        '''
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 60, 100, 30) 
        '''
        self.setGeometry(300, 300, 600, 400)
        
        self.setWindowTitle('查重平台')
        
        self.show()
        
    def getfiles(self):
        #============Read & Load data from config.json===================#
        f = open('config.json', encoding='utf-8')
        data = json.load(f)
        #================================================================#
        powerpoint = wc.gencache.EnsureDispatch("PowerPoint.Application")
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
        dir_choose = QFileDialog.getExistingDirectory(self,"选取文件夹") # 起始路径
        old_file_path = str(dir_choose) + '/'
        #==================================================#
        for root, dirs, files in os.walk(old_file_path):
          print('root_dir:', root)  # 当前目录路径
          for name in os.listdir(root):
              print(name)
              old_file = root + name 
              #Build a new folder in the same path with the screend files to store the modified files;
              new_file = root + 'backup_folder/'
              isExists = os.path.exists(new_file)
              # 判断结果
              isExists = os.path.exists(new_file)
              # 判断结果
              if not isExists:
                  # 如果不存在则创建目录
                  # 创建目录操作函数
                  os.makedirs(new_file)
                  print(new_file + ' 创建成功')
                  new_file = new_file + '/' + name
              else:
                  # 如果目录存在则不创建，并提示目录已存在
                  # need to be polished
                  print(new_file + ' 目录已存在') 
                  new_file = new_file + '/' + name
        #==========preprocess for doc===============================================#
        #==========convert the doc to docx,and delete the doc file==================#
                  '''
              if old_file.split(".")[-1] == 'doc':
                  try:
                      word = wc.gencache.EnsureDispatch('kwps.application')
                  except:
                      word=  wc.gencache.EnsureDispatch('word.application')
                  doc = word.Documents.Open(old_file)
                  doc.SaveAs("{}x".format(old_file), 12)#另存为后缀为".docx"的文件，其中参数12指docx文件
                  word.Quit
                  os.remove(old_file)
                  time.sleep(3)
                  doc.Close() #关闭原来word文件
                  '''
        #============================================================================#
              if old_file.split(".")[-1] == 'docx':
                  self.listFile.addItem(old_file + ":" + str(time.asctime( time.localtime(time.time()) )))
                  id_type = 1
                  document = Document(old_file)
                  document,display_list = screening_of_doc1.check_and_change(document, data, id_type)
                  document.save(new_file)
                  print('display is:')
                  print(len(display_list))
                  if len(display_list) > 0:
                      print(display_list)
                      key = display_list[0][0]
                      value = display_list[0][1]
                      self.listFile.addItem(key+"-->"+value + ":" + str(time.asctime( time.localtime(time.time()) ))) # display the time info
                  else:
                      pass
                  time.sleep(3)
        #============================================================================#
        #==========convert the ppt to pptx,and delete the ppt file==================#

        #============================================================================#
              if old_file.split(".")[-1] == 'pptx':
                  id_type = 2
                  document = Presentation(old_file)
                  document,display_list= screening_of_doc1.check_and_change(document, data, id_type)
                  document.save(new_file)
                  time.sleep(3)
              print("="*30)
        #====================================================#
        
        #==================================================#
        
        print("Finished")
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
