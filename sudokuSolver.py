import pygame
import random
from board import board

def run(diff):
    pygame.init()

    difficulty = diff
    width = 500
    height = 500

    window = pygame.display.set_mode((width, height))
    icon = pygame.image.load("sudokuIcon.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Sudoku Solver")

    clock = pygame.time.Clock()

    # checks if the user chosen number is valid in the specified row and column of the sudoku board
    def placeable(grid, row, column, number):
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
        for i in grid:
            for j in i:
                if grid[j.row][j.column].text == "0":
                    return j.row, j.column

        return None

    def createSudokuBoard():
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

        # OTHERWISE THIS WON'T WORK
        # NEED TO WRITE CODE TO FILL IN TOP-MID AND TOP-RIGHT BOXES
        # OTHERWISE THIS WON'T WORK

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
        # function that checks whether there are still empty tiles
        getEmptyLocation = getEmpty(grid)
        if getEmptyLocation is None:
            return True
        else:
            row, column = getEmptyLocation

        for i in range(9):
            if placeable(grid, row, column, i + 1):
                grid[row][column].text = str(i + 1)
                grid[row][column].colour = (0, 255, 0)

                if backtrackSolver(grid):
                    return True

        grid[row][column].text = "0"
        grid[row][column].colour = (255, 0, 0)
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

        # clear the screen each frame
        window.fill((255, 255, 255))

        # draw the number of wrong guesses the user has
        wrongLabel = pygame.font.SysFont("comicsans", 40).render("Wrong: " + str(wrong), 1, (0, 0, 0))
        window.blit(wrongLabel, (350, 0))

        # redraw the board with the latest information
        grid.redrawBoard()
        pygame.display.update()

        # force the program to run at 60 fps
        clock.tick(60)

    # close pygame
    pygame.quit()


run("Easy")

# thanks to icons8.com for the sudoku logo