import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTableView, QVBoxLayout, QHeaderView,QPushButton,QLineEdit,
                             QGridLayout)
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class TabelViewDemo(QWidget):
    def __init__(self, parent=None):
        super(TabelViewDemo, self).__init__(parent)
        self.resize(500,400)
        self.setWindowTitle('QTableView Demo')
        self.model = QStandardItemModel(4,4)
        modelTitle = ['转数','针数','次数','方式']
        self.model.setHorizontalHeaderLabels(modelTitle)
        row1 = ['3','4','4','0']
        row2 = ['1','3','5','7']
        row3 = ['3', '1', '66', '5']
        row4 = ['3', '6', '1', '1']
        modelContents = [row1,row2,row3,row4]
        for i in range(4):
            for j in range(4):
                item = QStandardItem(modelContents[i][j])
                self.model.setItem(i, j, item)

        self.tableView = QTableView()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setModel(self.model)

        btnAddRow = QPushButton('Add')
        btnRemoveRow = QPushButton('Del')
        btnAddRow.clicked.connect(self.appendRow)
        btnRemoveRow.clicked.connect(self.removeRow)
        btnClearBtn = QPushButton('Clear')
        btnClearBtn.clicked.connect(self.clearRows)

        btnFormLayout = QGridLayout()
        btnFormLayout.addWidget(btnAddRow,0,0)
        btnFormLayout.addWidget(btnRemoveRow,0,1)
        btnFormLayout.addWidget(btnClearBtn,0,2)


        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.tableView)
        mainLayout.addLayout(btnFormLayout)

        for i in range(self.model.columnCount()):
            titles = self.model.horizontalHeaderItem(i)
            print(titles.text())

        item_66 = QStandardItem('1')
        indexFromItem = self.model.indexFromItem(item_66)
        print('indexFromItem = ',indexFromItem.column())

        find = self.model.findItems('66', column = 2)
        for i in find:
            print(i.row(),i.column())

        self.setLayout(mainLayout)
        
    def appendRow(self):

        item = QStandardItem('')
        selectedIndex = self.tableView.currentIndex()
        print('当前选择行:',selectedIndex.row())
        if self.model.rowCount() > 0:
            self.model.insertRow(selectedIndex.row(),item)
        else:
            self.model.appendRow(item)

    def removeRow(self):
        selectedRows = self.tableView.selectionModel().selection().indexes()
        if len(selectedRows) > 0:
            self.model.removeRow(selectedRows[0].row())
            self.removeRow()
            print('remove one row')

    def clearRows(self):

        selectedRows = self.tableView.currentIndex()
        print('选择了第%d行,第%d列'%(selectedRows.row() + 1, selectedRows.column() + 1))
        # self.model.
        # itemList = []
        # for i in range(4):
        #     item = QStandardItem('')
        #     itemList.append(item)

        # for i in range(len(selectedRows)):
        #     for j in range(4):
        #         self.model.setItem(selectedRows[i].row(),i,itemList[j])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = TabelViewDemo()
    demo.show()
    sys.exit(app.exec_())
