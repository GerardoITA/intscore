import os

from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget, QFileDialog
import sys

class mainView(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Conversione saves EU4'
        self.width = 350
        self.height = 200

        self.loginUI()
        self.show()
        self.buttons[0].clicked.connect(self.getFileName)


    def loginUI(self):
        left_shift = 25
        standard_length = 160
        initial_height = 40
        self.setWindowTitle(self.title)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)

        self.insertFile = [QLineEdit(self),QLineEdit(self)]
        for label in self.insertFile:
            label.setDisabled(True)
            label.setFixedWidth(standard_length)
            label.move(left_shift,initial_height*(self.insertFile.index(label)+1))
        self.buttons= [QPushButton('Select EU4 file', self), QPushButton('Select saving directory', self)]
        for button in self.buttons:
            button.move(left_shift + standard_length + 30, initial_height*(1+ self.buttons.index(button)))

        self.convertButton =QPushButton('Convert file', self)
        self.convertButton.move(int((self.width/2)-self.convertButton.width()/2), 110)


    def getFileName(self):
        file_filter = 'Data File (*.eu4)'
        QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Data File (*.eu4)'
        )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainView()
    sys.exit(app.exec_())