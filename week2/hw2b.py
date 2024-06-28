"""
*** HW 2: Median Filter ***
Name: Jacob Bello
Course: CST 205
Date: 6/15/24
Week: 2
"""
from PIL import Image
from glob import glob

img_list = []
def load_images(location, type):
    for image in glob(f'{location}/*.{type}'):
        img_list.append(Image.open(image))

# Task 1 - Code for my_median() function
def my_median(int_list):
    int_list.sort()
    median = len(int_list) // 2
    
    return int_list[median]
# Task 2
load_images(r'C:\Users\jacob\cst_205\week2\hw_images\task2_images', 'png')
print(img_list)


# Task 3
# load_images('task3_images', 'png')
# Code to perform median filter and generate new image.