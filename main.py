import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLCDNumber, QVBoxLayout, QGridLayout)
from PyQt5.QtCore import Qt, QObject


class Calculator(QWidget):
    def __init__(self, parent = None):
        super(Calculator, self).__init__(parent)

        self.resultValue = 0
        self.memoryValue = 0
        self.putinNum = 0
        self.isNumAppendModel = True
        self.initUI()
        print('KEY\t记忆\t显示')
        self.showState()

    def showState(self):
        print('\t%s\t%s'%(self.memoryValue, self.resultValue))

    def initUI(self):
        self.lcdScreen = QLCDNumber()
        self.lcdScreen.setDigitCount(8)
        self.updateScreen()

        btn_1 = QPushButton('1')
        btn_2 = QPushButton('2')
        btn_3 = QPushButton('3')

        btn_plus = QPushButton('+')
        btn_equal = QPushButton('=')
        btn_CE = QPushButton('CE')

        btn_1.clicked.connect(lambda :self.numBtnPressed(1))
        btn_2.clicked.connect(lambda :self.numBtnPressed(2))
        btn_3.clicked.connect(lambda :self.numBtnPressed(3))
        btn_plus.clicked.connect(lambda :self.operatorBtn('+'))
        btn_equal.clicked.connect(self.getResult)
        btn_CE.clicked.connect(self.screenClear)

        btnGridLayout = QGridLayout()
        btnGridLayout.addWidget(btn_1, 0, 0)
        btnGridLayout.addWidget(btn_2, 0, 1)
        btnGridLayout.addWidget(btn_3, 0,2)
        btnGridLayout.addWidget(btn_plus, 0, 3)
        btnGridLayout.addWidget(btn_equal, 1, 0)
        btnGridLayout.addWidget(btn_CE, 1, 1)


        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.lcdScreen)
        mainLayout.addLayout(btnGridLayout)

        self.setLayout(mainLayout)

    def numBtnPressed(self, num):
        pass


    def operatorBtn(self, btn_name):
        pass


    def getResult(self):
        pass


    def screenClear(self):
        pass

    def updateScreen(self):
        self.lcdScreen.display(self.resultValue)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())






