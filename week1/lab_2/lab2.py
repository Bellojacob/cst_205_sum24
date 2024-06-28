print("Enter RGB color values")
user_input_1 = input("Enter RGB color value, seperate by comma: ")
#print(user_input)
split = user_input_1.split(',')
rgb = (int(split[0]), int(split[1]), int(split[2]))
#print(rgb)
print("Red = " + str(rgb[0]))
print("Green = " + str(rgb[1]))
print("Blue = " + str(rgb[2]))



if (rgb[0] > rgb[1] and rgb[0] > rgb[2]):
    print("Red is the dominant color")
elif (rgb[1] > rgb[0] and rgb[1] > rgb[2]):
    print("Green is the dominant color")
elif (rgb[2] > rgb[0] and rgb[2] > rgb[1]):
    print("Blue is the dominant color")
    
elif (rgb[0] == rgb[1]):
    print("The color is a shade of yellow")
elif (rgb[0] == rgb[2]):
    print("The color is a shade of purple")
elif (rgb[1] == rgb[2]):
    print("The color is a shade of cyan")
