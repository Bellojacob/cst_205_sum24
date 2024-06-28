from PIL import Image
from pprint import pprint

with open ('monaLisa.txt', 'r') as file:
    mona_Str = file.read()

line_list = mona_Str.split('\n')

h = len(line_list)
w = len(line_list[0].split('\t'))

print(w,h)

mona_lisa = Image.new('L', (w,h))

for y, line in enumerate (mona_Str.split('\n')):
    for x, val in enumerate (line.split('\t')):
        #pass
        print((x,y))
        mona_lisa.putpixel((x,y), int(val))
        #print(int(val))

mona_lisa.show()
mona_lisa.save('jacob_bello_mona_lisa.png')
