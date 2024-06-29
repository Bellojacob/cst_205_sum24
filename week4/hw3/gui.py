import sys
from PySide6.QtWidgets import (QWidget, QApplication, QLabel, QPushButton,
                               QLineEdit, QVBoxLayout,QComboBox, QHBoxLayout)
from PySide6.QtCore import Qt, Slot
from __feature__ import snake_case, true_property

my_app = QApplication([])

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        my_list = ["Sepia", "Negative", "Grayscale", "Thumbnail", "None"]

        vbox = QVBoxLayout()
        qline = QLineEdit("Text")
        cbox = QComboBox()
        cbox.add_items(my_list)
        b1 = QPushButton("Search")

        vbox.add_widget(qline)
        vbox.add_widget(cbox)
        vbox.add_widget(b1)

        self.set_layout(vbox)
        self.resize(500,500)
        self.show()

my_win = MyWindow()
sys.exit(my_app.exec())