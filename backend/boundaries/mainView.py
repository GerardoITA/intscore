import os
from pathlib import Path
from backend.controllers.fileConverter import fileConverter as c
from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QWidget, QFileDialog, QLabel
import sys

class mainView(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Conversione saves EU4'
        self.width = 350
        self.height = 200

        self.loginUI()
        self.show()
        self.buttons[0].clicked.connect(self.getEu4File)
        self.buttons[1].clicked.connect(self.getSaveFolder)
        self.convertButton.clicked.connect(self.save)
        self.contextLabel = QLabel("", self)

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
            label.setText("")
        self.buttons= [QPushButton('Select EU4 file', self), QPushButton('Select saving directory', self)]
        for button in self.buttons:
            button.move(left_shift + standard_length + 30, initial_height*(1+ self.buttons.index(button)))

        self.convertButton =QPushButton('Convert file', self)
        self.convertButton.adjustSize()
        self.convertButton.move(int((self.width/2)-(self.convertButton.width()/2)), 130)


    def labelText(self, txt):
        self.contextLabel.setText(txt)
        self.contextLabel.adjustSize()
        self.contextLabel.setGeometry(int((self.width/2)-(self.contextLabel.width()/2)),110, self.contextLabel.width(), self.contextLabel.height())
        self.contextLabel.show()
    def save(self):

        if self.insertFile[0].text() == "":
            self.labelText('Inserisci il file di input')
            self.contextLabel.setStyleSheet("Color:red")
        elif self.insertFile[1].text() == "":
            self.labelText('Inserisci la cartella di output')
            self.contextLabel.setStyleSheet("Color:red")
        else:
            controller = c(self.insertFile[0].text(), self.insertFile[1].text())
            controller.parser(controller.in_fn, controller.out_fn)
    def getEu4File(self):
        file_filter = 'Data File (*.eu4)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Data File (*.eu4)'
        )
        self.insertFile[0].setText(str(response[0]))

    def getSaveFolder(self):
        dir_name = QFileDialog.getExistingDirectory(self, 'Select a Directory')
        if dir_name:
            path = Path(dir_name)
            self.insertFile[1].setText(str(path))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainView()
    sys.exit(app.exec_())