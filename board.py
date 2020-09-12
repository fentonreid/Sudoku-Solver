import pygame
import random
from square import square

class board():
    def __init__(self, window):
        self.window = window
        self.grid = [[]]

    def createBoard(self, width, height):
        row = []
        x = 0
        y = 0
        width /= 9
        height /= 9

        for i in range (0, 9):
            for j in range (0, 9):
                s = square(x, y, width, height, (0,0,0), self.window)
                s.text = str(1)
                s.createRect()
                s.updateLabel()
                row.append(s)
                x += 55
            x = 0
            y += 55

            self.grid.append(row)
