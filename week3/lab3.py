"""
Jacob Bello
CST 205
6/19/2024
Week 3
***    Lab — Python OOP, Part 2   ***
"""

#   Task 1
class Song:
    def __init__(self, name, artist, genre, length, album):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.length = length
        self.album = album
    
    #   Task 2
    def __str__(self):
        return f"{self.name} is made by {self.artist} ({self.genre}, {self.length} seconds, {self.album})"
    
    #   Task 3
    def __eq__(self, song2):
        return self.name == song2.name and self.artist == song2.artist
    
song1 = Song("Porch Light", "Josh Meloy", "Country", 184, "Porch Light Single")
song2 = Song("Fast Car", "Luke Combs", "Country", 265, "Gettin' Old" )
print(song1)
print(song2)
print(song1 == song2)

#   Task 4
# QWidget