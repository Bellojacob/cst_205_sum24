"""
Jacob Bello
CST 205
6/20/2024
Week 3
***    Lab — Qt 1   ***
"""
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from __feature__ import snake_case, true_property
#   Task 1: See Image

#   Task 2
#   QGraphicsBlurEffect
#   This widget provides a blur effect and can be altered
#   to change the hint and radius of the blur.


#   Task 3
my_app = QApplication([])



class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        
        label = QLabel("Jacob Bello")
        # Can't figure out how to show it
        
"""
I could not figure out how to get my label to show
"""

        

my_window = MyWindow()

sys.exit(my_app.exec())