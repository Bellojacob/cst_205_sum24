from PIL import Image

def sepia(img_path):
    img = Image.open(img_path)
    w,h = img.size
    pixels = img.load()

    for x in range(h):
        for y in range(w):
            r,g,b = img.getpixel((x,y))

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            if tr > 255:
                tr = 255
            if tg > 255:
                tg = 255
            if tb > 255:
                tb = 255

            pixels[x, y] = (tr, tg, tb)
    
    img.show()
    return img

sepia(r"C:\Users\jacob\cst_205\coursework\week4\hw3\hw3_images\2152601472_55fb809919_c.jpg")

    