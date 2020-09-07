# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 11:24:46 2020

@author: Melody
"""
# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5 import QtCore 
from PyQt5.QtCore import Qt 
import sys 
  
  
class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 
  
  
        # set the title 
        self.setWindowTitle("round label") 
  
        # setting  the geometry of window 
        self.setGeometry(60, 60, 600, 400) 
  
        # creating a label widget 
        # by default label will display at top left corner 
        self.label_1 = QLabel(self) 
  
        # moving position 
        self.label_1.move(100, 100) 
  
        # making label square in size 
        self.label_1.resize(40, 40) 
  
        # setting up border and radius 
        self.label_1.setStyleSheet("background-color:green; border: 3px solid green;border-radius: 20px;") 
  
        # show all the widgets 
        self.show() 
  
  
# create pyqt5 app 
App = QApplication(sys.argv) 
  
# create the instance of our Window 
window = Window() 
  
# start the app 
sys.exit(App.exec())


