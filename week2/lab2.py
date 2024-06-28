"""
*** Lab 2: Color Manipulation ***
Name: Jacob Bello
Course: CST 205
Date: 6/11/24
"""
 
from PIL import Image

# Open the original image
img = Image.open("images/lmp.jpg")

# Create the negative image
negative_list = [(255 - pixel[0], 255 - pixel[1], 255 - pixel[2]) for pixel in img.getdata()]
img.putdata(negative_list)
img.save("images/negative_car.jpg")

# Open the negative image
neg_img = Image.open("images/negative_car.jpg")
#   This one is pretty cool

# Create the double negative image
double_negative_list = [(255 - pixel[0], 255 - pixel[1], 255 - pixel[2]) for pixel in neg_img.getdata()]
neg_img.putdata(double_negative_list)
neg_img.save("images/double_negative.jpg")


#   task 2 : Sunset Filter


def sunset_filter(pic):
    img = Image.open(pic)
    my_list = []
    for p in img.getdata():
        my_list.append((p[0], p[1]//2, p[2]//2))

    img.putdata(my_list)
    # img.show()
    img.save("images/sunset_filter_img.jpg")

sunset_filter("images/lmp.jpg")

#   task 3

rgb_tuples = [
    (54,54,54),(204,82,122),(71,71,71),
    (232,22,93),(54,54,54),(168,167,167)
]

x = 2
y = 3
my_img = Image.new("RGB", (x,y))
my_img.putdata(rgb_tuples)
my_img.save("images/pixel_grid.png")


"""
My comments:
I was able to complete everything in the lab, although I spent about 2 hours probably on 
this lab, mainly because I was confused on task 3. Task 1 and 2 were straight forward from
the lecture, task 3 gave me some issues, but I believe I completed it correctly.
"""