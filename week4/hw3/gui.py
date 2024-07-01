import sys
from PySide6.QtWidgets import (QWidget, QApplication, QLabel, QPushButton,
                               QLineEdit, QVBoxLayout,QComboBox, QHBoxLayout)
from PySide6.QtCore import Qt, Slot
from __feature__ import snake_case, true_property
from PySide6.QtGui import QPixmap
from functions import sepia, negative, grayscale, thumbnail, none_show, my_search
from image_info import image_info

app = QApplication([])
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()

        # add widgets
        self.line_edit = QLineEdit()
        self.combo_box = QComboBox()
        self.combo_box.add_items(['Sepia', 'Negative', 'Grayscale', 'Thumbnail', 'None'])
        self.search_button = QPushButton('Search')
        self.result_label = QLabel()
        




        # Layout
        layout.add_widget(self.line_edit)
        layout.add_widget(self.combo_box)
        layout.add_widget(self.search_button)
        layout.add_widget(self.result_label)
        

        self.set_layout(layout)
        self.resize(500,500)

        # connection for button
        self.search_button.clicked.connect(self.search)


    @Slot()
    def search(self):
        
        search_term = self.line_edit.text
        # print(search_term)
        best_match = my_search(search_term)
        print(my_search(search_term))
        img_path = (r"C:\Users\jacob\cst_205\coursework\week4\hw3\hw3_images\\" + best_match + ".jpg")
        print(img_path)
        # transformation = self.combo_box.currentText()
        self.open_new_win(img_path)
    
    @Slot()
    def open_new_win(self, img_path):
        self.new_win = NewWindow(img_path)
        self.new_win.show()
        i = self.combo_box.current_index()
    
class NewWindow(QWidget):
    def __init__(self, img_path):
        super().__init__()

        label = QLabel()
        
        my_pixmap = QPixmap(img_path)
        label.pixmap = my_pixmap

        self.layout = QVBoxLayout()
        self.layout.add_widget(label)
        
        self.set_layout(self.layout)
        self.resize(500,500)
        


        


my_win = MyWindow()
my_win.show()
sys.exit(app.exec())