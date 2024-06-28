"""
Jacob Bello
CST 205
6/19/2024
Week 3
***    Lab — Python OOP, Part 1   ***
"""

#   Task 1
# The class defintion for Pillow's image class begins on line 516

#   Task 2 - docstring
"""
This class represents an image object.  To create
:py:class:`~PIL.Image.Image` objects, use the appropriate factory
functions.  There's hardly ever any reason to call the Image constructor
directly.

* :py:func:`~PIL.Image.open`
* :py:func:`~PIL.Image.new`
* :py:func:`~PIL.Image.frombytes`
"""

#   Task 3
from PIL import Image
img = Image.open("images/flowers.jpg")
attributes = dir(img)
#   print(attributes)
#   'info'
"""
You can attach auxiliary information to an image using the info attribute.
This is a dictionary object.  How such information is handled when loading 
and saving image files is up to the file format handler 
(see the chapter on Image file formats). 
Most handlers add properties to the info attribute 
when loading an image, but ignore it when saving images.
"""

#   Task 4
class Song:

    def __init__(self, name, artist, genre, length, album):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.length = length
        self.album = album
    
    def __str__(self):
        return f"{self.name} is made by {self.genre} artist {self.artist}."
    

song1 = Song("Hurt", "Johnny Cash", "Country", 216, "American IV: The Man Comes Around")

print(song1)