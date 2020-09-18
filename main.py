import pygame_menu
import pygame
from sudokuSolver import run

# this menu file was written using the examples for pygame_menu "https://pygame-menu.readthedocs.io/en/latest/"

difficulty = "Easy"

pygame.init()
surface = pygame.display.set_mode((500, 500))
icon = pygame.image.load("sudokuIcon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Sudoku Solver")


def setDifficulty(selected, value):
    """
    From the slider get the difficulty the user choose and update the global variable to reflect this

    :param selected: the slider option we are currently on
    :param value: the value associated with the selected option
    :return: None
    """
    global difficulty
    difficulty = value

def instructions():

    menu = pygame_menu.Menu(height=500, width=500, theme=pygame_menu.themes.THEME_DARK, title='Instructions')

    instruction = "Click on a square to select it                   " \
                  "Type the number into the square                      " \
                  "Press SPACE to start backtracking " \
                  "----------------------------------------"\

    menu.add_label(instruction, max_char=-1, font_size=25)
    menu.add_button('Play', mainrun)
    menu.mainloop(surface)


def mainrun():
    """
    Run sudokuSolver.py inputting the difficulty the user choose
    :return: None
    """
    run(difficulty)

# Build our menu
menu = pygame_menu.Menu(height=500, width=500, theme=pygame_menu.themes.THEME_DARK, title='Sudoku Solver')
menu.add_button('Play', mainrun)
menu.add_selector("Sudoku difficulty: ", [("Very Easy", "V.Easy"), ("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard"), ("Very Hard", "V.Hard")], onchange=setDifficulty)
menu.add_button("Instructions", instructions)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)