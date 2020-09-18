import pygame
import random
from time import sleep
import tkinter as tk
from tkinter import ttk

from board import board


def run(diff):
    """
    Runs the sudoku board game after start is pressed from the main.py file

    :param diff: the difficulty the user wants the sudoku game to be
    :return: None
    """

    pygame.init()

    difficulty = diff
    screenshotTaken = False

    # setup the pygame window
    width = 500
    height = 500

    # add an icon and title
    window = pygame.display.set_mode((width, height))
    icon = pygame.image.load("sudokuIcon.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Sudoku Solver")

    # setup the clock
    clock = pygame.time.Clock()
    initialTime = pygame.time.get_ticks()

    def placeable(grid, row, column, number):
        """
        checks if the user chosen number is valid in the specified row and column of the sudoku board

        :param grid: the 2d array that contains all the information on the sudoku board
        :param row: row integer
        :param column: column integer
        :param number: number the user choose to place on the board
        :return: true if placeable on the board else false
        """
        numberSet = set()
        # get all numbers in a row
        for i in range(9):
            numberSet.add(int(grid[row][i].text))

        # get all numbers in a column
        for i in range(9):
            numberSet.add(int(grid[i][column].text))

        # checking the box the row, column is present in
        for i in range(3):
            for j in range(3):
                numberSet.add(int(grid[i + (row - row % 3)][j + (column - column % 3)].text))

        # return if the number is present in the set
        return number not in numberSet

    def getEmpty(grid):
        """
        Returns the location of the empty space as a tuple of size 2 {row, column} or None if no empties found

        :param grid: the 2d array that contains all the information on the sudoku board
        :return: Location of the empty space or None if no empties
        """
        for i in grid:
            for j in i:
                if grid[j.row][j.column].text == "0":
                    return j.row, j.column

        return None

    def createSudokuBoard():
        """
        Returns a solveable sudoku board with a certain number of empty tiles based on the difficulty the user choose

        :return: a sudoku board with numbers filled in based on user chosen difficulty
        """
        numberToGenerate = 0

        # defining a number of numbers to generate from the users input of difficulty
        if difficulty == "V.Easy":
            numberToGenerate = 45
        elif difficulty == "Easy":
            numberToGenerate = 40
        elif difficulty == "Medium":
            numberToGenerate = 35
        elif difficulty == "Hard":
            numberToGenerate = 30
        elif difficulty == "V.Hard":
            numberToGenerate = 25

        # generate a nine-by-nine grid of 0's
        grid = board(window)
        grid.initialBoard()

        # need to add to the top-right box, 9 random values
        topRightList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(topRightList)

        # allocating a random digit to the top right box
        topRightBox = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

        for x, (i, j) in enumerate(topRightBox):
            grid.grid[i][j].text = str(topRightList[x])

        # BACKTRACK TO SOLVE
        backtrackSolver(grid.grid)

        # Now we remove from the grid until we reach the difficulty specified
        for i in range(81 - numberToGenerate):
            row = random.randint(0, 8)
            column = random.randint(0, 8)

            while grid.grid[row][column].text == "0":
                row = random.randint(0, 8)
                column = random.randint(0, 8)

            grid.grid[row][column].text = "0"

        return grid.grid

    def backtrackSolver(grid):
        """
        Recursively place a 1 to 9 in an empty square until the board is completed

        :param grid: the 2d array that contains all the information on the sudoku board
        :return: True or false
        """
        # function that checks whether there are still empty tiles
        getEmptyLocation = getEmpty(grid)
        if getEmptyLocation is None:
            return True
        else:
            row, column = getEmptyLocation

        for i in range(9):
            if placeable(grid, row, column, i + 1):
                grid[row][column].text = str(i + 1)

                if backtrackSolver(grid):
                    return True

        grid[row][column].text = "0"
        return False

    premade = createSudokuBoard()

    completedBoard = board(window)
    completedBoard.createBoard(width, height, premade)

    if not backtrackSolver(completedBoard.grid):
        pygame.quit()

    grid = board(window)
    grid.createBoard(width, height, premade, completedBoard.grid)
    keyPressed = 0
    wrong = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: keyPressed = 1
                if event.key == pygame.K_2: keyPressed = 2
                if event.key == pygame.K_3: keyPressed = 3
                if event.key == pygame.K_4: keyPressed = 4
                if event.key == pygame.K_5: keyPressed = 5
                if event.key == pygame.K_6: keyPressed = 6
                if event.key == pygame.K_7: keyPressed = 7
                if event.key == pygame.K_8: keyPressed = 8
                if event.key == pygame.K_9: keyPressed = 9
                if event.key == pygame.K_SPACE: backtrackSolver(grid.grid)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()  # tuple (x,y)
                grid.hover = (int(mousePos[1] / (width / 9)), int(mousePos[0] / (height / 9)))

        # if the user has clicked on a square and pressed a key
        if keyPressed != 0 and grid.hover is not None and grid.grid[grid.hover[0]][grid.hover[1]].changeable:
            # change the value if the number the user choose is valid and it must also match the actual answer generated by the algorithm
            if placeable(grid.grid, grid.hover[0], grid.hover[1], keyPressed) and keyPressed == int(
                    grid.grid[grid.hover[0]][grid.hover[1]].answer):
                grid.updateText(grid.hover[0], grid.hover[1], str(keyPressed))
                grid.grid[grid.hover[0]][grid.hover[1]].changeable = False
            else:
                wrong += 1

            keyPressed = 0

        # check for win condition and display information in a popup
        getEmptyLocation = getEmpty(grid.grid)
        if getEmptyLocation is None:
            grid.redrawBoard()
            pygame.display.update()

            endScreen = tk.Tk()
            endScreen.title("Board filled")
            endScreen.geometry("300x300")
            endScreen.configure(background="cyan")
            ttk.Label(endScreen, background="cyan", font=('Helvetica', 18, 'bold'),
                      text="Sudoku board complete: \n\n -You took " + str(
                          (pygame.time.get_ticks() - initialTime) // 1000) + "s \n" + " -You made " + str(
                          wrong) + " mistake(s)").pack()

            def screenshot():
                """Allows the user to save the board
                """
                # take a screenshot of the completed board
                pygame.image.save(window, "board.png")
                sleep(3)
                endScreen.destroy()

            running = False

            a = ttk.Button(endScreen, text="Take a screenshot", command=screenshot).pack()
            ttk.Button(endScreen, text="Close game", command= endScreen.destroy).pack()
            endScreen.mainloop()

        # clear the screen each frame
        window.fill((255, 255, 255))

        # draw the number of wrong guesses the user has
        wrongLabel = pygame.font.SysFont("comicsans", 25).render("Wrong: " + str(wrong), 1, (0, 0, 0))
        window.blit(wrongLabel, (405, 0))

        # draw the time elapsed onto the screen
        time = pygame.font.SysFont("comicsans", 25).render(
            "Time: " + (str((pygame.time.get_ticks() - initialTime) // 1000) + "s"), 1, (0, 0, 0))
        window.blit(time, (10, 0))

        # redraw the board with the latest information
        grid.redrawBoard()
        pygame.display.update()

        # force the program to run at 60 fps
        clock.tick(60)

    # close pygame
    pygame.quit()