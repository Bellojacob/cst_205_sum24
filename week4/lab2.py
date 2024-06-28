"""
Jacob Bello
CST 205
6/25/2024
Week 4
***    Lab — PySide (Qt), Pt. 3   ***
"""
import sys
from PySide6.QtWidgets import (QWidget, QApplication, QLabel, QPushButton,
                               QLineEdit, QVBoxLayout,QComboBox, QHBoxLayout)
from PySide6.QtCore import Qt, Slot
from __feature__ import snake_case, true_property
from PySide6.QtGui import QPalette, QColor

#   task 1
# my_app = QApplication([])

# class ColorWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.window_title = "Background"
#         self.palette = Qt.blue
    
# my_win = ColorWindow()
# my_win.show()
# sys.exit(my_app.exec())

#   task 2
# my_app2 = QApplication([])

# class MyWindow(QWidget):
#     # create a gui that shows the buttons of an xbox controller

#     def __init__(self):
#         super().__init__()

#         h_layout1 = QHBoxLayout()
#         b1 = QPushButton("X")
#         h_layout1.add_widget(b1)
        

#         v_layout = QVBoxLayout()
#         b3 = QPushButton("Y")
#         b4 = QPushButton("A")
#         v_layout.add_widget(b3)
#         v_layout.add_widget(b4)

#         h_layout2 = QHBoxLayout()
#         b2 = QPushButton("B")
#         h_layout2.add_widget(b2)

#         main_layout = QHBoxLayout()
#         main_layout.add_layout(h_layout1)
#         main_layout.add_layout(v_layout)
#         main_layout.add_layout(h_layout2)

#         self.set_layout(main_layout)
#         self.resize(300,300)
        

# app = MyWindow()
# app.show()
# sys.exit(my_app2.exec())

#   task 3
app = QApplication([])

colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255)
}


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.my_combo_box = QComboBox()
        self.my_combo_box.add_items(colors)
        self.b1 = QPushButton("Select")
        self.b1.clicked.connect(self.open_win)

        vbox = QVBoxLayout()
        vbox.add_widget(self.my_combo_box)
        vbox.add_widget(self.b1)

        self.set_layout(vbox)
        self.resize(300,300)

    @Slot()
    def open_win(self):
        i = self.my_combo_box.current_index
        selected_text = self.my_combo_box.current_text
        selected_color = colors[selected_text]
        self.new_win = NewWindow(selected_color)
        self.new_win.show()

class NewWindow(QWidget):
    def __init__(self, color):
        super().__init__()
        self.resize(300,300)
        
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(*color))
        self.setPalette(palette)
        self.setAutoFillBackground(True)




my_win = MyWindow()
my_win.show()
sys.exit(app.exec())
