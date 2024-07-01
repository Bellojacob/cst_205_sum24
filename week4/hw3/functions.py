from PIL import Image
from image_info import image_info

# write function for sepia, negative, grayscale, thumbnail, none

def negative(img_path):
    img = Image.open(img_path)

    negative_list = [(255-p[0], 255-p[1], 255-p[2])
                           for p in img.getdata()]
    img.putdata(negative_list)
    img.show()

# negative(r"C:\Users\jacob\cst_205\coursework\week4\hw3\hw3_images\2152601472_55fb809919_c.jpg")

def grayscale(img_path):
    img = Image.open(img_path)

    new_list = [ ( (a[0]+a[1]+a[2])//3, ) * 3
                   for a in img.getdata() ]
    img.putdata(new_list)
    img.show()

# grayscale(r"C:\Users\jacob\cst_205\coursework\week4\hw3\hw3_images\2152601472_55fb809919_c.jpg")

def sepia(img_path):
    img = Image.open(img_path)
    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            img.putpixel((x, y), (min(tr, 255), min(tg, 255), min(tb, 255)))

    img.show()
    return img


# sepia(r"C:\Users\jacob\cst_205\coursework\week4\hw3\hw3_images\2152601472_55fb809919_c.jpg")

def thumbnail(img_path):
    img = Image.open(img_path)
    width, height = img.width//2, img.height//2
    my_trgt = Image.new('RGB', (img.width//2, img.height//2))

    target_x = 0
    for source_x in range(0,img.width,2):
        target_y = 0
        for source_y in range(0,img.height,2):
            p = img.getpixel((source_x,source_y))
            my_trgt.putpixel((target_x,target_y), p)
            target_y += 1
        target_x += 1
    
    my_trgt.show()

# thumbnail(r"C:\Users\jacob\cst_205\coursework\week4\hw3\hw3_images\2152601472_55fb809919_c.jpg")

    
def none_show(img_path):
    img = Image.open(img_path)
    img.show()

# none_show((r"C:\Users\jacob\cst_205\coursework\week4\hw3\hw3_images\2152601472_55fb809919_c.jpg"))
    
def my_search(keyword):
    keyword = keyword.lower()
    matches = {}
    # look for matching id's

    for x in range(len(image_info)):
        count = 0
        if image_info[x]["id"] == keyword:
            count += 1
            print(f'Found {keyword}, Times:{count}')
            

        for tag in image_info[x]["tags"]:    
            if tag.lower() == keyword.lower():
                count += 1
                print(f'Found {tag} : {image_info[x]["id"]}, Times: {count}')
                
        
        if count > 0:
            matches[image_info[x]["id"]] = count
        
    print(matches)

    best_match = max(matches, key=matches.get)
    print(f'{best_match} has the highest number of matches: {matches[best_match]}')
    return best_match

def image_transform(i, img_path):
    if i == 0:
        none_show(img_path)
    elif i == 1:
        negative(img_path)
    elif i == 2:
        grayscale(img_path)
    elif i == 3:
        thumbnail(img_path)
    elif i == 4:
        sepia(img_path)
    
        
            
                



