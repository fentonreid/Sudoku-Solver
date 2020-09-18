from square import square


class board():
    def __init__(self, window):
        """
        intialise the board class

        :param window: takes the main pygame screen
        """
        self.window = window
        self.grid = []
        self.hover = None

    def createBoard(self, width, height, premade, completedBoard=None):
        """
        Creates a sudoku game board and draws it to the window

        :param width: width of the window
        :param height: height of the window
        :param premade: a solved sudoku board stored in a 2d array
        :param completedBoard: a solved sudoku board
        :return: None
        """
        x = 2
        y = 20
        width = (width - 2) // 9
        height = (height - 20) // 9

        print(width, height)

        # create grid of squares
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
                x += width

            x = 2
            y += height
            self.grid.append(row)

    def initialBoard(self):
        """
        Used for the initial generation of the sudokuBoard

        :return: None
        """

        for i in range(9):
            row = []
            for j in range(9):
                s = square(0, 0, 0, 0, (0, 0, 0), self.window)
                s.row = i
                s.column = j
                row.append(s)
            self.grid.append(row)

    def updateText(self, row, column, text):
        """
        When a square's label is changed this updates the change to the window

        :param row: specific row in the 2d array
        :param column: specific column in the 2d array
        :param text: the new label the square should display
        :return: None
        """
        self.grid[row][column].text = text
        self.grid[row][column].updateLabel()

    def redrawBoard(self):
        """
        Draw the board, updating the labels and each square
        :return: None
        """
        for i in range(0, 9):
            for j in range(0, 9):
                self.grid[i][j].createRect()
                self.grid[i][j].updateLabel()


        # draw lines to the board
        self.grid[0][0].createLine((167, 21), (167, 496))
        self.grid[0][0].createLine((332, 21), (332, 496))

        self.grid[0][0].createLine((3, 179), (496, 179))
        self.grid[0][0].createLine((3, 338), (496, 338))
