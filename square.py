from const import *

class Square:

    def __init__(self, row, col, piece=None, texture=None, texture_rect =None):
        self.row = row
        self.col = col
        self.texture = texture
        self.occupied = False
        self.texture_rect = texture_rect

