"""
*** Lab 3: Grayscale, L*a*b* color ***
Name: Jacob Bello
Course: CST 205
Date: 6/13/24
Week: 2
"""
from PIL import Image
from colorthief import ColorThief
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import numpy

#  task 1
img = Image.open(r"C:\Users\jacob\cst_205\week2\images\paris.jpg")
# img.show()

new_list = [ (  (a[0]+a[1]+a[2])//3, ) * 3 for a in img.getdata()]

img.putdata(new_list)
img.save("images/paris_bw.jpg")
# img.show()

#   task 2

#   luminance method
img2 = Image.open(r"C:\Users\jacob\cst_205\week2\images\paris.jpg")
second_list = [((a[0]*299 + a[1]*587 + a[2]*114)//1000,) *3 for a in img2.getdata()]
img2.putdata(second_list)
img2.save("images/paris_luminance_method.jpg")
# img2.show()

# I like the average method better than the luminance method for my picture i chose, 
# I feel like it has more contrast, the luminance method doesn't look quite as good.

#   task 3

color_thief = ColorThief('images/paris.jpg')
dominant_color = color_thief.get_color(quality=1)
print(dominant_color)

img3 = Image.open("images/paris.jpg", "r")
pixels = list(img3.getdata())

w,h = img3.size
pixel_list = [(x,y,img3.getpixel((x,y))) for y in range(h) for x in range(w)]
# print(pixel_list)

counter = 0

for x in pixel_list:
    if dominant_color == x:
        counter += 1

print(f"We found your color {counter} times!")
# I never got my counter to work properly

#   task 4
def patch_asscalar(a):
  return a.item()
setattr(numpy, "asscalar", patch_asscalar)

color1_rgb = sRGBColor(176, 63, 81, True)
color2_rgb = sRGBColor(185, 77, 89, True)

color1_lab = convert_color(color1_rgb, LabColor)
color2_lab = convert_color(color2_rgb, LabColor)

delta_e = delta_e_cie2000(color1_lab, color2_lab)

print(f'The difference is {delta_e}.')

#   task 5
def color_distance(c1, c2):
    r_diff = (c1[0] - c2[0])**2
    g_diff = (c1[1] - c2[1])**2
    b_diff = (c1[2] - c2[2])**2
    return (r_diff + g_diff + b_diff)**(1/2)

distance = color_distance((176,63,81),(185,77,89))
print(f"The distance between Apple 1 and Apple 2 is", distance)

"""
I completed the lab, the only issue I had was on task 3 using colorthief, for some reason
I could not figure out how to count how many times that color was used. I tried many variations
but I did not get anything successful.

Other than that, I find these image manipulations interesting because I am into photography,
and I use Adobe products a lot, and I now have a greater appreciation for what they have created.
"""