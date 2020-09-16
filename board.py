from square import square

class board():
    def __init__(self, window):
        self.window = window
        self.grid = []
        self.hover = None

    def createBoard(self, width, height, premade, completedBoard=None):
        x = 0
        y = 0
        width /= 9
        height /= 9

        for i in range(9):
            row = []
            for j in range(9):
                # draw square and set row and column
                s = square(x, y, width, height, (0, 0, 0), self.window)
                s.row = i
                s.column = j

                if int(premade[i][j].text) != 0:
                    s.text = premade[i][j].text
                    s.changeable = False
                else:
                    s.changeable = True
                    if completedBoard is not None:
                        s.answer = completedBoard[i][j].text

                s.createRect()

                s.updateLabel()
                row.append(s)
                x += 55

            x = 0
            y += 55
            self.grid.append(row)

    # used for the initial generation of the sudokuBoard
    def initialBoard(self):
        x = 0
        y = 0
        width = 0
        height = 0

        for i in range(9):
            row = []
            for j in range(9):
                s = square(x, y, width, height, (255,255,255), self.window)
                s.row = i
                s.column = j
                row.append(s)
            self.grid.append(row)

    def updateText(self, row, column, text):
        self.grid[row][column].colour = (255, 0, 0)
        self.grid[row][column].text = text
        self.grid[row][column].updateLabel()

    def redrawBoard(self):
        for i in range(0, 9):
            for j in range(0, 9):
                self.grid[i][j].createRect()
                self.grid[i][j].updateLabel()