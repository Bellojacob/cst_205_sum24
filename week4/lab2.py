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

# task 1
my_app = QApplication([])

class ColorWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.window_title = "Background"
        self.palette = Qt.blue
    
my_win = ColorWindow()
my_win.show()
sys.exit(my_app.exec())

#   task 2
my_app2 = QApplication([])

class MyWindow(QWidget):
    # create a gui that shows the buttons of an xbox controller

    def __init__(self):
        super().__init__()

        h_layout1 = QHBoxLayout()
        b1 = QPushButton("X")
        h_layout1.add_widget(b1)
        

        v_layout = QVBoxLayout()
        b3 = QPushButton("Y")
        b4 = QPushButton("A")
        v_layout.add_widget(b3)
        v_layout.add_widget(b4)

        h_layout2 = QHBoxLayout()
        b2 = QPushButton("B")
        h_layout2.add_widget(b2)

        main_layout = QHBoxLayout()
        main_layout.add_layout(h_layout1)
        main_layout.add_layout(v_layout)
        main_layout.add_layout(h_layout2)

        self.set_layout(main_layout)
        self.resize(300,300)
        

app = MyWindow()
app.show()
sys.exit(my_app2.exec())

#   task 3
app = QApplication([])

colors = ["red","green","blue"]



class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # create combo box and add my list to combo box
        self.my_combo_box = QComboBox()
        self.my_combo_box.add_items(colors)

        # add push button
        b1 = QPushButton("Select")
        

        # create a layout and add combobox and button
        vbox = QVBoxLayout()
        vbox.add_widget(self.my_combo_box)
        vbox.add_widget(b1)

        # set layout and properties
        self.set_layout(vbox)
        self.resize(300,300)

        # add connection for button
        b1.clicked.connect(self.open_win)

    # method when button is clicked to get current index of my_combo_box and 
    # call function NewWindow with the index as a parameter
    @Slot()
    def open_win(self):
        i = self.my_combo_box.current_index
        self.new_win = NewWindow(i)
        self.new_win.show()

class NewWindow(QWidget):
    def __init__(self, num):
        super().__init__()
        self.resize(300,300)

        # based on the current index display a new gui displaying the color when the
        # select button is pushed
        if num == 0:
            self.window_title = "Red"
            self.palette = Qt.red
        elif num == 1:
            self.window_title = "Green"
            self.palette = Qt.green
        elif num == 2:
            self.window_title = "Blue"
            self.palette = Qt.blue





my_win = MyWindow()
my_win.show()
sys.exit(app.exec())
