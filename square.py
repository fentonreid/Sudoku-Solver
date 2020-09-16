import pygame

class square():
    def __init__(self, x, y, width, height, colour, window):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.window = window
        self.text = "0"
        self.changeable = True
        self.row = None
        self.column = None
        self.answer = 0

    def createRect(self):
        pygame.draw.rect(self.window, self.colour, (self.x,self.y,self.width,self.height), 1)

    def createLine(self, start, end):
        pygame.draw.line(self.window, self.colour, start, end, 5)

    def updateLabel(self):
        if self.text != "0":
            label = pygame.font.SysFont("comicsans", 40).render(self.text, 1, (0,0,0))
            self.window.blit(label, (self.x, self.y))