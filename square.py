import pygame

class square():
    def __init__(self, x, y, width, height, colour, window):
        """
        Initialise the square class

        :param x: x-value of the square on the board
        :param y: y-value of the square on the board
        :param width: width of the pygame window
        :param height: height of the pygame window
        :param colour: colour to set the square and text
        :param window: pygame window
        """
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
        """
        Draw a rectangle onto the pygame window

        :return: None
        """
        pygame.draw.rect(self.window, self.colour, (self.x,self.y,self.width,self.height), 1)

    def createLine(self, start, end):
        """
        Draw grid lines onto the sudoku board

        :param start: (x,y) coord to start drawing
        :param end: (x,y) coordinate to stop drawing
        :return: None
        """
        pygame.draw.line(self.window, self.colour, start, end, 5)

    def updateLabel(self):
        """
        Draw the label onto the screen, excluding all 0 values (this equates to a None value)
        :return: None
        """
        if self.text != "0":
            label = pygame.font.SysFont("comicsans", 40).render(self.text, 1, (0,0,0))
            self.window.blit(label, (self.x + 20, self.y+15))