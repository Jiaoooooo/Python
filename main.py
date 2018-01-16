import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLCDNumber, QVBoxLayout, QGridLayout)
from PyQt5.QtCore import Qt, QObject


class Calculator(QWidget):
    def __init__(self, parent = None):
        super(Calculator, self).__init__(parent)

        self.screenValue = 0
        self.memoryNum = 0
        self.num_2 = 0
        self.isNumAppendModel = True
        self.initUI()

    def initUI(self):
        self.lcdScreen = QLCDNumber()
        self.lcdScreen.setDigitCount(8)
        self.updateScreen()

        btn_1 = QPushButton('1')
        btn_2 = QPushButton('2')
        btn_plus = QPushButton('+')
        btn_equal = QPushButton('=')
        btn_CE = QPushButton('CE')

        btn_1.clicked.connect(lambda :self.numBtnPressed(1))
        btn_2.clicked.connect(lambda :self.numBtnPressed(2))
        btn_plus.clicked.connect(lambda :self.operatorBtn('+'))
        btn_equal.clicked.connect(self.getResult)
        btn_CE.clicked.connect(self.screenClear)

        btnGridLayout = QGridLayout()
        btnGridLayout.addWidget(btn_1, 0, 0)
        btnGridLayout.addWidget(btn_2, 0, 1)
        btnGridLayout.addWidget(btn_plus, 0, 2)
        btnGridLayout.addWidget(btn_equal, 0, 3)
        btnGridLayout.addWidget(btn_CE, 1, 0)


        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.lcdScreen)
        mainLayout.addLayout(btnGridLayout)

        self.setLayout(mainLayout)

    def numBtnPressed(self, num):
        if self.lcdScreen.checkOverflow(self.screenValue * 10 + num) == False:
            self.screenValue = self.screenValue * 10 + num

        self.updateScreen()
        print('%s 键被按下,显示值为%s,记忆值为%s'%(num, self.screenValue, self.memoryNum))


    def operatorBtn(self, btn_name):

        self.isNumAppendModel = False
        self.memoryNum = self.screenValue
        print('记忆值为%s'%self.memoryNum)
        self.screenValue = 0
        if btn_name == '+':
            pass
        self.isNumAppendModel = True
        print('Btn %s 被按下, 记忆值变为%s' % (btn_name, self.memoryNum))

    def getResult(self):

        self.isNumAppendModel = False
        print('%s + %s = %s, '%(self.memoryNum, self.screenValue,self.memoryNum + self.screenValue))
        self.screenValue = self.screenValue + self.memoryNum
        self.updateScreen()
        self.memoryNum = self.screenValue
        self.screenValue = 0








    def screenClear(self):
        print('屏幕被清空')
        self.memoryNum = 0
        self.num_2 = 0
        self.screenValue = 0
        self.isNumAppendModel = True
        self.updateScreen()

    def updateScreen(self):
        print('screenValue = ', self.screenValue)
        self.lcdScreen.display(self.screenValue)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())






