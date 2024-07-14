import sys
from PySide6.QtWidgets import (QWidget, QApplication, QLabel, QPushButton,
                               QLineEdit, QVBoxLayout,QComboBox)
from PySide6.QtCore import Qt, Slot
from __feature__ import snake_case, true_property
from PySide6.QtGui import QPixmap

app = QApplication([])
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.set_layout(layout)
        self.resize(500,500)

my_win = MyWindow()
my_win.show()
sys.exit(app.exec())