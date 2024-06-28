from PIL import Image, ImageDraw
import random

# Generate a dark 8-bit color
my_color = random.randint(0, 150)

#Enter name here
my_name = "Jacob Bello"

img = Image.new('L', (200,200), color= my_color)

my_text = ImageDraw.Draw(img)
my_text.text((30,30), my_name, fill=255)

img.save(r"C:\Users\jacob\cst_205\hw_1\task4.png")