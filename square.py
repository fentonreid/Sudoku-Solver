import pygame

class square():
    def __init__(self, x, y, width, height, colour, window):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.window = window
        self.text = ""

    def createRect(self):
        pygame.draw.rect(self.window, self.colour, (self.x,self.y,self.width,self.height), 1)

    def updateLabel(self):
        label = pygame.font.SysFont("comicsans", 40).render(self.text, 10, (0, 0, 0))
        self.window.blit(label, (self.x, self.y))