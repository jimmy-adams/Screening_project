from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class MainWidget(QWidget):
    def __init__(self,parent=None):
        super(MainWidget,self).__init__(parent)
        self.setWindowTitle("QThread 例子")
        self.thread = Worker()
        self.listFile = QListWidget()
        self.btnStop = QPushButton('停止')
        self.btnStart = QPushButton('开始')
        
        #============================================#
         # creating a label widget 
        # by default label will display at top left corner 
        self.signal_lamp = QLabel(self)
        
        # making label square in size 
        self.signal_lamp.resize(20, 20) 
        # setting up border and radius 
        self.signal_lamp.setStyleSheet("background-color:red; border: 3px solid red;border-radius: 10px;") 
        #============================================#
        layout = QGridLayout(self)
        
        layout.addWidget(self.listFile,1,0,1,2)
        layout.addWidget(self.btnStart,2,1)
        layout.addWidget(self.btnStop,2,0)
        self.btnStart.clicked.connect( self.slotStart)
        self.btnStop.clicked.connect( self.slotStop)
        
        self.thread.sinOut.connect(self.slotAdd)

    def slotAdd(self,file_inf):
        if file_inf == 'red':
            self.signal_lamp.setStyleSheet("background-color:red; border: 3px solid red;border-radius: 10px;") 
        else:
            self.signal_lamp.setStyleSheet("background-color:green; border: 3px solid green;border-radius: 10px;") 
         

    def slotStart(self):
        #self.btnStart.setEnabled(False)
        self.thread.start()
    def slotStop(self):
        #self.btnStop.setEnabled(False)
        self.thread.terminate()

class Worker(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self,parent=None):
        super(Worker,self).__init__(parent)
        self.working = True
        self.num = 0

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        while self.working == True:
            if self.num % 2 ==0:
                file_str = 'green'
            else:
                file_str = 'red'
            self.num += 1
            # 发出信号
            self.sinOut.emit(file_str)
            # 线程休眠2秒
            self.sleep(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = MainWidget()
    demo.show()
    sys.exit(app.exec_())