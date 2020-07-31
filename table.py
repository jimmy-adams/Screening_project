import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import config
import json



class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("检索数据库")
        self.resize(400,300)
        self.layout= QVBoxLayout()
        
        self.layout1= QHBoxLayout()
        
        QHB_Widget = QWidget()
        
        
        
        
        
        
        #============Read & Load data from config.json===================#
        f = open("config.json", encoding='utf-8')
        self.data = json.load(f)
        #================================================================#

        #实现的效果是一样的，四行三列，所以要灵活运用函数，这里只是示范一下如何单独设置行列
        self.rootList = []
        root = QTreeWidget() # define a QtreeWidget() type object;
        self.generateTreeWidget(self.data, root)
        self.TableWidget=QTableWidget(len(self.rootList),2)
        
        #self.TableWidget.cellClicked.connect(self.cell_was_clicked)
        
        self.TableWidget.cellClicked.connect(self.cell_was_clicked)

        self.TableWidget.setContextMenuPolicy(Qt.CustomContextMenu)# Allow right click function
        
        self.TableWidget.customContextMenuRequested.connect(self.generateMenu)
       
        # TableWidget.setRowCount(4)
        # TableWidget.setColumnCount(3)

        print(len(self.rootList))

        #设置水平方向的表头标签与垂直方向上的表头标签，注意必须在初始化行列之后进行，否则，没有效果
        self.TableWidget.setHorizontalHeaderLabels(['目标词汇','替换词汇'])
        #Todo 优化1 设置垂直方向的表头标签
        #TableWidget.setVerticalHeaderLabels(['行1', '行2', '行3', '行4'])

        #TODO 优化 2 设置水平方向表格为自适应的伸缩模式
        ##TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #TODO 优化3 将表格变为禁止编辑
        #TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #TODO 优化 4 设置表格整行选中
        #TableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        #TODO 优化 5 将行与列的高度设置为所显示的内容的宽度高度匹配
        #QTableWidget.resizeColumnsToContents(TableWidget)
        #QTableWidget.resizeRowsToContents(TableWidget)

        #TODO 优化 6 表格头的显示与隐藏
        #TableWidget.verticalHeader().setVisible(False)
        #TableWidget.horizontalHeader().setVisible(False)

        #TOdo 优化7 在单元格内放置控件
        # comBox=QComboBox()
        # comBox.addItems(['男','女'])
        # comBox.addItem('未知')
        # comBox.setStyleSheet('QComboBox{margin:3px}')
        # TableWidget.setCellWidget(0,1,comBox)
        #添加数据
        for i in range(len(self.rootList)):
            newItem1 = QTableWidgetItem(self.rootList[i].text(0))
            self.TableWidget.setItem(i,0,newItem1)
            newItem2 = QTableWidgetItem(self.rootList[i].text(1))
            self.TableWidget.setItem(i,1,newItem2)      
        #===========================================================#
        self.btn = QPushButton('Refresh',self)  # The first button:
        
        self.btn.clicked.connect(self.refresh)
        
        self.btn1 = QPushButton('Save',self)    # The second button:
        
        self.btn1.clicked.connect(self.save)

        self.layout.addWidget(self.TableWidget)
        
        self.layout1.addWidget(self.btn)
        
        self.layout1.addWidget(self.btn1)
        
        QHB_Widget.setLayout(self.layout1)
        
        self.layout.addWidget(QHB_Widget)

        self.setLayout(self.layout)
        
        self.show()
    def cell_was_clicked(self, row, column):
        self.TableWidget.cellChanged.connect(self.cell_was_changed)
        
        self.x = row
        self.y = column
        
        
    def cell_was_changed(self,row,column):
        print('row:%d,column:%d was changed'% (row, column+1))
        
    def generateMenu(self,pos):
           try:
              
              self.contextMenu = QMenu()
              self.actionA = self.contextMenu.addAction(u'删除')
              self.actionB = self.contextMenu.addAction(u'插入')
              self.contextMenu.popup(QCursor.pos())  # 2菜单显示的位置
              action = self.contextMenu.exec_(self.TableWidget.mapToGlobal(pos))
              self.contextMenu.show()
              if action == self.actionA:
                 print('row:%d,column:%d was changed'% (self.x, self.y))
                 if self.y == 0:        # if the column is 1, it means the value change will not affect 
                    self.TableWidget.removeRow(self.x)
                 else:
                    newItem = QTableWidgetItem('')
                    self.TableWidget.setItem(self.x,1,newItem)
              elif action == self.actionB:
                 cur_len = self.TableWidget.rowCount()
                 self.TableWidget.insertRow(cur_len)
              self.contextMenu.close() #close the menu list  
              
           except Exception as e:
              print(e)

    #================================================================#   
    def generateTreeWidget(self, data, root):

        if isinstance(data, dict):
            for key in data.keys():
                child = QTreeWidgetItem()
                child.setText(0, key)
                if isinstance(root, QTreeWidget) == False:  # 非根节点，添加子节点
                    root.addChild(child)
                self.rootList.append(child)
                #print(key)
                value = data[key]
                self.generateTreeWidget(value, child)
        else:
            root.setText(1, str(data))
    #=============================================================#        
    def refresh(self):
        f = open("config.json", encoding='utf-8')
        self.data = json.load(f)
        self.rootList = []
        root = QTreeWidget() # define a QtreeWidget() type object;
        self.generateTreeWidget(self.data, root)
        self.TableWidget.setRowCount(len(self.rootList))
        #=================Overall update ========================#
        for i in range(len(self.rootList)):
            newItem1 = QTableWidgetItem(self.rootList[i].text(0))
            self.TableWidget.setItem(i,0,newItem1)
            newItem2 = QTableWidgetItem(self.rootList[i].text(1))
            self.TableWidget.setItem(i,1,newItem2)  
        #========================================================#
    def save(self):
        #===========================建立二次确认框====================================================#
        A = QMessageBox.question(self,'确认','确认保存且更新数据库？',QMessageBox.Yes | QMessageBox.No)
        #=============================================================================================#
        data = {}
        if A == QMessageBox.Yes:
          for i in range(self.TableWidget.rowCount()):
            #print(self.TableWidget.item(i,0).text())
            temp_dict = {self.TableWidget.item(i,0).text() : self.TableWidget.item(i,1).text()}
            data.update(temp_dict)
          #============update the dict========================#
          container = open("config.json",'w')
          json.dump(data,container)
          #===================================================#
        else:
          pass

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Table()
    sys.exit(app.exec_())