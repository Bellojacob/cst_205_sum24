"""
Jacob Bello
CST 205
6/25/2024
Week 4
***    Lab — PySide (Qt), Pt. 2   ***
"""
import sys
from PySide6.QtWidgets import (QWidget, QApplication, QLabel, QPushButton,
                               QLineEdit, QVBoxLayout,QComboBox, QHBoxLayout)
from PySide6.QtCore import Qt, Slot
from __feature__ import snake_case, true_property

#   Task 1

# my_app = QApplication([])

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.label1 = QLabel('Label 1')
        
#         btn1 = QPushButton('Button 1')
#         btn1.clicked.connect(self.btn1_click)
#         btn2 = QPushButton('Button 2')
#         btn2.clicked.connect(self.btn2_click)

#         vbox = QVBoxLayout()
        
#         vbox.add_widget(self.label1)
#         vbox.add_widget(btn1)
#         vbox.add_widget(btn2)


#         self.set_layout(vbox)
#         self.resize(500,500)
#         self.show()

#     @Slot()
#     def btn1_click(self):
#         self.label1.text = 'You clicked button 1'
    
#     @Slot()
#     def btn2_click(self):
#         self.label1.text = 'You clicked button 2'

# my_win = MyWindow()
# sys.exit(my_app.exec())

#   task 2


my_app = QApplication([])

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.color_dict = {
    "red": {
        "rgb": (255, 0, 0), "hex": "#FF0000"
    },
    "green": {
        "rgb": (0, 255, 0), "hex": "#00FF00"
    },
    "blue": {
        "rgb": (0, 0, 255), "hex": "#0000FF"
    }
}
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()


        label1 = QLabel("<h1>CST 205 Color Exchange!</h1>")
        label2 = QLabel("RGB: ")
        self.label3 = QLabel("")
        label4 = QLabel("Hex: ")
        self.label5 = QLabel("")


        self.my_combo_box = QComboBox()
        self.my_combo_box.add_items(self.color_dict)

        hbox.add_widget(label2)
        hbox.add_widget(self.label3)
        hbox.add_widget(label4)
        hbox.add_widget(self.label5)

        vbox.add_widget(label1)
        vbox.add_widget(self.my_combo_box)
        vbox.add_layout(hbox)

        self.my_combo_box.currentIndexChanged.connect(self.update_rgb)



        self.set_layout(vbox)
        self.resize(300, 300)
        self.window_title = "Color Picker"
        
        self.show()
    
    @Slot()
    def update_rgb(self):
        selected_color = self.my_combo_box.current_text
        rgb_value = self.color_dict[selected_color]["rgb"]
        hex_value = self.color_dict[selected_color]["hex"]

        self.label3.text = f'{rgb_value}'
        self.label5.text = f'{hex_value}'




my_win = MyWindow()
sys.exit(my_app.exec())
