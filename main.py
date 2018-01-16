import sys
from enum import Enum
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLCDNumber, QVBoxLayout, QGridLayout, QMessageBox)
from PyQt5.QtCore import Qt, QObject

class Operator(Enum):
    plus = 11
    minus = 12
    multi = 13
    divide = 14


class Calculator(QWidget):
    def __init__(self, parent = None):
        super(Calculator, self).__init__(parent)

        self.resultValue = 0
        self.memoryValue = 0
        self.putInNum = 0
        self.initUI()
        self.operator = ''
        print('KEY\t\t记忆\t\t输入\t\t显示')
        self.showState()

    def showState(self):
        print('\t\t%s\t\t%s\t\t%s'%(self.memoryValue, self.putInNum, self.resultValue))

    def initUI(self):
        self.lcdScreen = QLCDNumber()
        self.lcdScreen.setDigitCount(8)
        self.updateScreen()

        btn_1 = QPushButton('1')
        btn_2 = QPushButton('2')
        btn_3 = QPushButton('3')
        btn_4 = QPushButton('4')
        btn_5 = QPushButton('5')
        btn_6 = QPushButton('6')
        btn_7 = QPushButton('7')
        btn_8 = QPushButton('8')
        btn_9 = QPushButton('9')
        btn_0 = QPushButton('0')

        btn_demical = QPushButton('.')
        btn_convert = QPushButton('±')
        btn_C = QPushButton('C')
        btn_back = QPushButton('←')

        btn_plus = QPushButton('+')
        btn_minus = QPushButton('-')
        btn_multi = QPushButton('x')
        btn_divid = QPushButton('/')
        btn_equal = QPushButton('=')
        btn_CE = QPushButton('CE')

        btn_1.clicked.connect(lambda :self.numBtnPressed(1))
        btn_2.clicked.connect(lambda :self.numBtnPressed(2))
        btn_3.clicked.connect(lambda :self.numBtnPressed(3))
        btn_4.clicked.connect(lambda: self.numBtnPressed(4))
        btn_5.clicked.connect(lambda: self.numBtnPressed(5))
        btn_6.clicked.connect(lambda: self.numBtnPressed(6))
        btn_7.clicked.connect(lambda: self.numBtnPressed(7))
        btn_8.clicked.connect(lambda: self.numBtnPressed(8))
        btn_9.clicked.connect(lambda: self.numBtnPressed(9))
        btn_0.clicked.connect(lambda: self.numBtnPressed(0))

        btn_demical.clicked.connect(self.demicalBtnPressed)
        btn_convert.clicked.connect(self.convertBtnPressed)


        btn_plus.clicked.connect(lambda : self.operatorBtn(11))
        btn_minus.clicked.connect(lambda: self.operatorBtn(12))
        btn_multi.clicked.connect(lambda: self.operatorBtn(13))
        btn_divid.clicked.connect(lambda: self.operatorBtn(14))
        btn_equal.clicked.connect(self.getResult)
        btn_CE.clicked.connect(self.screenClear)

        btnGridLayout = QGridLayout()
        btnGridLayout.addWidget( btn_CE, 0, 0)
        btnGridLayout.addWidget( btn_C, 0, 1)
        btnGridLayout.addWidget(btn_back, 0, 2)
        btnGridLayout.addWidget(btn_divid, 0, 3)
        btnGridLayout.addWidget(btn_7, 1, 0)
        btnGridLayout.addWidget(btn_8, 1, 1)
        btnGridLayout.addWidget(btn_9, 1, 2)
        btnGridLayout.addWidget(btn_multi, 1, 3)
        btnGridLayout.addWidget(btn_4, 2, 0)
        btnGridLayout.addWidget(btn_5, 2, 1)
        btnGridLayout.addWidget(btn_6, 2, 2)
        btnGridLayout.addWidget(btn_minus,2, 3)
        btnGridLayout.addWidget(btn_1, 3, 0)
        btnGridLayout.addWidget(btn_2, 3, 1)
        btnGridLayout.addWidget(btn_3, 3, 2)
        btnGridLayout.addWidget(btn_plus, 3, 3)
        btnGridLayout.addWidget(btn_convert, 4, 0)
        btnGridLayout.addWidget(btn_0, 4, 1)
        btnGridLayout.addWidget(btn_demical,4, 2)
        btnGridLayout.addWidget(btn_equal, 4, 3)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.lcdScreen)
        mainLayout.addLayout(btnGridLayout)

        self.setLayout(mainLayout)
        self.setWindowTitle('阿焦的计算器')
        self.resize(300,300)

    def numBtnPressed(self, num):

        if self.putInNum < 0:
            putInResulet = self.putInNum * 10 - num
        else:
            putInResulet = self.putInNum * 10 + num

        if self.lcdScreen.checkOverflow(putInResulet) == False:
            self.putInNum = putInResulet
            self.resultValue = self.putInNum
        self.updateScreen()
        print(num, end='')
        self.showState()


    def operatorBtn(self, btn_enum):
        tuple1 = ('+','-','x','/')
        self.memoryValue = self.resultValue
        self.putInNum = 0
        print(tuple1[btn_enum-11], end='')
        self.operator = Operator(btn_enum)
        self.showState()

    def demicalBtnPressed(self):
        pass

    def convertBtnPressed(self):
        self.putInNum = -self.putInNum
        self.resultValue = self.putInNum
        self.updateScreen()
        print('±',end='')
        self.showState()


    def getResult(self):
        print('=',end='')
        calculateResult = self.resultValue
        if self.operator == Operator.plus:
            calculateResult = self.memoryValue + self.putInNum
        elif self.operator == Operator.minus:
            calculateResult = self.memoryValue - self.putInNum
        elif self.operator == Operator.multi:
            calculateResult = self.memoryValue * self.putInNum
        elif self.operator == Operator.divide:
            if self.putInNum  != 0:
                calculateResult = self.memoryValue / self.putInNum
            else:
                self.reportError()

        if self.lcdScreen.checkOverflow(calculateResult) == False:
            self.resultValue = calculateResult
            self.memoryValue = calculateResult
            self.putInNum = 0
        self.updateScreen()
        self.showState()
        self.operator = ''


    def screenClear(self):
        self.memoryValue = 0
        self.putInNum = 0
        self.resultValue = 0
        self.updateScreen()
        print('CE', end='')
        self.showState()

    def updateScreen(self):
        self.lcdScreen.display(self.resultValue)

    def reportError(self):
        QMessageBox.warning(self,'错误','除数不能是0!')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())






