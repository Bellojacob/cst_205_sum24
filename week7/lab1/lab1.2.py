import sys
from PySide6.QtWidgets import (QWidget, QApplication, QLabel, QPushButton,
                               QLineEdit, QVBoxLayout,QComboBox, QDial)
from PySide6.QtCore import Qt, Slot
from __feature__ import snake_case, true_property
from PySide6.QtGui import QPixmap

app = QApplication([])
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        
        self.dial = QDial()
        self.dial.set_range(0, 100)
        self.dial.set_value(50)
        self.dial.valueChanged.connect(self.on_dial_value_changed)
        
        self.label = QLabel("Dial Value: 50")
        
        layout.add_widget(self.dial)
        layout.add_widget(self.label)
        
        self.set_layout(layout)
        self.resize(500, 500)

    @Slot()
    def on_dial_value_changed(self, value):
        self.label.setText(f"Dial Value: {value}")

my_win = MyWindow()
my_win.show()
sys.exit(app.exec())