# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:17:31 2020

@author: Melody
"""
import sys
from PyQt5.QtWidgets import *
import config
import json

#============Read & Load data from config.json===================#
f = open("config.json", encoding='utf-8')
data = json.load(f)
#================================================================#

class TreeWidget(QTreeWidget):
    def __init__(self):
        super(TreeWidget, self).__init__()

        self.setColumnCount(2)  # 共2列
        self.setHeaderLabels(['目标词汇', '替换词汇'])

        self.rootList = []
        root = self
        self.generateTreeWidget(data, root)

        print(len(self.rootList), self.rootList)

        self.insertTopLevelItems(0, self.rootList)
        self.initUI()
    def initUI(self):
        self.show()
    def generateTreeWidget(self, data, root):
        if isinstance(data, dict):
            for key in data.keys():
                child = QTreeWidgetItem()
                child.setText(0, key)
                if isinstance(root, QTreeWidget) == False:  # 非根节点，添加子节点
                    root.addChild(child)
                self.rootList.append(child)
                print(key)
                value = data[key]
                self.generateTreeWidget(value, child)
        else:
            root.setText(1, str(data))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TreeWidget()
    sys.exit(app.exec_())


