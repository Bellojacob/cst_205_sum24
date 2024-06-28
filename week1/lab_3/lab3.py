# task 1
color_dictionary = {
    "green" : (0, 255, 0),
    "blue" : (0, 0, 255),
    "magenta" : (255, 0, 255),
    
}

# task 2
print("The red channel of magenta is", color_dictionary["magenta"][0])
print("The green channel of magenta is", color_dictionary["magenta"][1])
print("The green channel of green is", color_dictionary["green"][1])
print("\n")

# task 3
tineye_sample = {
    "status": "ok",
    "error": [],
    "method": "extract_collection_colors",
    "result": [
        {
            "color": (141,125,83),
            "weight": 76.37,
            "name": "Clay Creek",
            "rank": 1,
            "class": "Grey"
        },
        {
            "color": (35,22,19),
            "weight": 23.63,
            "name": "Seal Brown",
            "rank": 2,
            "class": "Black"
        }
    ]
}



print("The red channel of Clay Creek is", tineye_sample["result"][0]["color"][0])
print("The blue channel of Seal Brown is", tineye_sample["result"][1]["color"][1])
print("\n")

# task 4
def enterColors():
    red = input("Enter red: ")
    green = input("Enter green: ")
    blue = input("Enter blue: ")
    return f'Thank you, your RGB color is ({red}, {green}, {blue})'
print(enterColors())
print("\n")

#task 5
def getUserInput(myTuple):
    print(f'The red channel intensity is: {myTuple[0]}')
    print(f'The green channel intensity is: {myTuple[1]}')
    print(f'The blue channel intensity is: {myTuple[2]}')
    

getUserInput((22,33,55))
print("\n")

#task 6
def convert_rgb_to_hex(tuple2):
    hex_color = "#"
    for i in tuple2:
        hex_color += str(hex(i))[2:]
    return hex_color

print(convert_rgb_to_hex((145, 240, 210)))
print("\n")

#task 7
def convert_hex_to_rgb(hex):
        
    if hex.startswith('#'):
        hex = hex[1:]

    r = int(hex[0:2], 16)
    g = int(hex[2:4], 16)
    b = int(hex[4:6], 16)

    return (r, g, b)

print(convert_hex_to_rgb("#91F0D2"))
