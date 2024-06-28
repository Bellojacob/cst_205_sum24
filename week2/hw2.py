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
    

#   task 1: my_median()

# ex_list = [2, 4, 6, 237, 1]

def my_median(int_list):
    int_list.sort()
    median = len(int_list) // 2
    
    return int_list[median]

# print(my_median(ex_list))

# print(f"The length of the list is {len(ex_list)}")
# print(f"{len(ex_list)} // 2 = {len(ex_list)//2}")

#   task 2: Median RGB values
def task2():
    load_images(r"C:\Users\jacob\cst_205\week2\hw_images\task2_images", "png")

    width, height = img_list[0].size 
    
    red = []
    green = []
    blue = []

    for img in img_list:
        img_data = list(img.getdata())
        for p in img_data:
            red.append(p[0])
            green.append(p[1])
            blue.append(p[2])
        
    
    # print(f"list1 {red}")
    # print(f"list2 {green}")
    # print(f"list3 {blue}")

    red_median = my_median(red)
    green_median = my_median(green)
    blue_median = my_median(blue)

    median_rgb = (red_median, green_median, blue_median)
    median_rgb_data = [median_rgb] * (width * height)

    median_image = Image.new("RGB", (width, height))
    median_image.putdata(median_rgb_data)

    median_image.save("task2.png")
    
    median_image.show()



#   task 3
def task3():
    load_images(r"C:\Users\jacob\cst_205\week2\hw_images\task3_images","png")
    
    width, height = img_list[0].size 
    
    result = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            reds = [img.getpixel((x,y))[0] for img in img_list]
            greens = [img.getpixel((x,y))[1] for img in img_list]
            blues = [img.getpixel((x,y))[2] for img in img_list]

            red_median = my_median(reds)
            greens_median = my_median(greens)
            blue_median = my_median(blues)

            result.putpixel((x,y), (red_median, greens_median, blue_median))
            # DO NOT PUT result.show() HERE, WILL OPEN 1000 IMGS AND CRASH COMPUTER

    result.save("task3.png")
    result.show()

# one function has to be commented out otherwise that scaling becomes weird
# due to the fact that we have one img_list, basically it appends values from 
# each set of images to the list and break things

task2()
#task3()
