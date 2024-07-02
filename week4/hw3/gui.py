"""
NAME:   Jacob Bello
CLASS:  CST 205
DATE:   7/1/2024
DESCRIPTION: This program will launch a interactive GUI using PySide6, which allows the
users to enter an ID or tag and the program will search for an image from image_info.py, 
hw3_images, then it will allow the user to select an image transformation and see the result 
"""
import sys
from PySide6.QtWidgets import (QWidget, QApplication, QLabel, QPushButton,
                               QLineEdit, QVBoxLayout,QComboBox)
from PySide6.QtCore import Qt, Slot
from __feature__ import snake_case, true_property
from PySide6.QtGui import QPixmap
from functions import my_search, image_transform
from image_info import image_info


    # init opening gui
app = QApplication([])
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()

            # add widgets
        self.line_edit = QLineEdit()
        self.combo_box = QComboBox()
        self.combo_box.add_items(['None', 'Negative', 'Grayscale', 'Thumbnail', 'Sepia'])
        self.search_button = QPushButton('Search')
        self.result_label = QLabel()
        
            # Layout
        layout.add_widget(self.line_edit)
        layout.add_widget(self.combo_box)
        layout.add_widget(self.search_button)
        layout.add_widget(self.result_label)
        
            # set layout and size
        self.set_layout(layout)
        self.resize(500,500)

            # connection for button
        self.search_button.clicked.connect(self.search)


    @Slot()
    def search(self):
            # when button is pressed, save combo box index as i and whatever was entered into QLineEdit as search_term
        i = self.combo_box.current_index
        # print(i)
        search_term = self.line_edit.text
        # print(search_term)
            # print my search for debugging purposes
        print(my_search(search_term))
            # get img_path with is either an img or an error img from functions.py
        img_path = my_search(search_term)
            # print path for debugging
        print(img_path)
            # when button is pressed, open new window and pass current combo box index and img_path
        self.open_new_win(img_path, i)
    
    @Slot()
    def open_new_win(self, img_path, i):
            # continue to pass path and index
        self.new_win = NewWindow(img_path, i)
        self.new_win.show()
        
    
class NewWindow(QWidget):
    def __init__(self, img_path, i):
        super().__init__()
            # placeholder for img
        label = QLabel()
        
            # call image_transform from functions.py using current index and img_path which will decide what picture
            # appears and how or if any edits are done to it
        my_pixmap = QPixmap(image_transform(i, img_path))
        label.pixmap = my_pixmap

            # set layout and add label which contains QPixmap
        self.layout = QVBoxLayout()
        self.layout.add_widget(label)
        
            # set layout and size
        self.set_layout(self.layout)
        self.resize(500,500)
        


        


my_win = MyWindow()
my_win.show()
sys.exit(app.exec())