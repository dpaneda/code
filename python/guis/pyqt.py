import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Hola mundo"))
        layout.addWidget(QCheckBox("Uno"))
        layout.addWidget(QCheckBox("Dos"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QPushButton("Aceptar"))

        self.setLayout(layout)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
