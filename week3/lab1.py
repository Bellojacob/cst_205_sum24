"""
Jacob Bello
CST 205
6/19/2024
Week 3
***    Lab — Collage, Chroma Key   ***
"""
from PIL import Image
from colorthief import ColorThief
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

#   task 1 - Collage

#   Ex blank canvas
im = Image.new("RGB", (1000,800), "white")
# im.show()



# function to create a canvas and paste a image onto it
def copy_image(your_image):
   my_src = Image.open(your_image)
   w,h = my_src.width * 3 , my_src.height * 3
   my_trgt = Image.new('RGB', (w,h), 'salmon')

   target_x = 200
   for source_x in range(my_src.width):
       target_y = 200
       for source_y in range(my_src.height):
           p = my_src.getpixel((source_x, source_y))
           my_trgt.putpixel((target_x, target_y), p)
           target_y += 1
       target_x += 1

   # I wasn't sure if I was supposed to call the method again, I didn't think so because
   # it would create a new canvas everytime, so instead I added onto the method/function
   # to open my images and shrink them(task 2) and put them in particular locations 
   my_src2 = Image.open("images/flowers.jpg")
   my_src3 = Image.open("images/iceland.jpg")

    # Img 2 paste
   target_x2 = 1200
   for source_x2 in range(my_src2.width):
       target_y2 = 800
       for source_y2 in range(my_src2.height):
           p = my_src2.getpixel((source_x2, source_y2))
           my_trgt.putpixel((target_x2, target_y2), p)
           target_y2 += 1
       target_x2 += 1

    # Img 3 paste
   target_x3 = 3000
   for source_x3 in range(my_src3.width):
       target_y3 = 2500
       for source_y3 in range(my_src3.height):
           p = my_src3.getpixel((source_x3, source_y3))
           my_trgt.putpixel((target_x3, target_y3), p)
           target_y3 += 1
       target_x3 += 1

   my_trgt.show()
   my_trgt.save("images/task1.png")

# task 2 Collage, cont.

# very similar to task 1 however and we are shrinking and moving the images
def copy_image(your_image):
   my_src = Image.open(your_image)
   # make my canvas 3 times as big as my image
   w,h = my_src.width * 3 , my_src.height * 3
   my_trgt = Image.new('RGB', (w,h), 'salmon')

    # set x and y locations for images
   target_x = 200
   for source_x in range(my_src.width):
       target_y = 200
       for source_y in range(my_src.height):
           p = my_src.getpixel((source_x, source_y))
           my_trgt.putpixel((target_x, target_y), p)
           target_y += 1
       target_x += 1
    
   my_src2 = Image.open("images/flowers.jpg")
   my_src3 = Image.open("images/iceland.jpg")

   target_x2 = 4500
   # we are going to shrink the image by only copying every 2 pixels instead of 
   # every pixel
   for source_x2 in range(0, my_src2.width, 2):
       target_y2 = 200
       for source_y2 in range(0, my_src2.height, 2):
           p = my_src2.getpixel((source_x2, source_y2))
           my_trgt.putpixel((target_x2, target_y2), p)
           target_y2 += 1
       target_x2 += 1

   target_x3 = 1000
   for source_x3 in range(my_src3.width):
       target_y3 = 3750
       for source_y3 in range(my_src3.height):
           p = my_src3.getpixel((source_x3, source_y3))
           my_trgt.putpixel((target_x3, target_y3), p)
           target_y3 += 1
       target_x3 += 1
   my_trgt.show()
   my_trgt.save("images/task1.png")
   my_trgt.save("images/task2.png")



copy_image("images/walkway.jpg")

#   task 3

# We are going to use color distance and chromakey to determine dominant pixel,
# and replace the background like a green screen
def color_distance(c1, c2):
    return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2) ** 0.5

def chromakey(src_path, bg_path, refp):
    src = Image.open(src_path)
    bg = Image.open(bg_path)

    
    color_thief = ColorThief(src_path)  
    dominant_color = color_thief.get_color(quality=1)
    print(f"Dominant Color: {dominant_color}")
    
    
    refp = dominant_color
    bg = bg.resize(src.size)

    for x in range(src.width):
        for y in range(src.height):
            cur_pixel = src.getpixel((x, y))

            if color_distance(cur_pixel, refp) < 150:
                src.putpixel((x, y), bg.getpixel((x, y)))

    return src


output_img = chromakey(r"C:\Users\jacob\cst_205\week3\images\iceland.jpg", r"C:\Users\jacob\cst_205\week3\images\flowers.jpg", 0)
output_img.save(r"C:\Users\jacob\cst_205\week3\images\task3.png")