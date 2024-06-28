"""
*** HW 2: Median Filter ***
Name: Jacob Bello
Course: CST 205
Date: 6/15/24
Week: 2
"""
from PIL import Image

#   task 1: my_median()

ex_list = [2, 4, 6, 237, 1]

def my_median(int_list):
    int_list.sort()
    median = (len(int_list)) // 2
    
    return int_list[median]

# print(my_median(ex_list))

# print(f"The length of the list is {len(ex_list)}")
# print(f"{len(ex_list)} // 2 = {len(ex_list)//2}")

#   task 2: Median RGB values

img1 = Image.open("hw_images/task2_images/img_1.png")
img2 = Image.open("hw_images/task2_images/img_2.png")
img3 = Image.open("hw_images/task2_images/img_3.png")

img1_data = list(img1.getdata())
img2_data = list(img2.getdata())
img3_data = list(img3.getdata())

# print(f"img 1 {img1_data}")
# print(f"img 2 {img2_data}")
# print(f"img 3 {img3_data}")

img1_list = []
for p in img1_data:
    median = my_median(list(p))
    img1_list.append(median)

img2_list = []
for p in img2_data:
    median = my_median(list(p))
    img2_list.append(median)

img3_list = []
for p in img3_data:
    median = my_median(list(p))
    img3_list.append(median)

new_img_data = []

for i in range(len(img1_list)):
    new_tuple = (img1_list[i], img2_list[i], img3_list[i])
    new_img_data.append(new_tuple)

print("\nNew data")
print(new_img_data)

img1.putdata(new_img_data)
img1.show()




