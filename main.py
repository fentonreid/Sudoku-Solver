import pygame_menu
import pygame
import sudokuSolver

# this menu file was written using the examples for pygame_menu "https://pygame-menu.readthedocs.io/en/latest/"

difficulty = "Easy"

pygame.init()
surface = pygame.display.set_mode((500, 500))
icon = pygame.image.load("sudokuIcon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Sudoku Solver")


def setDifficulty(selected, value):
    global difficulty
    difficulty = value


def run():
    sudokuSolver.run(difficulty)


menu = pygame_menu.Menu(height=500, width=500, theme=pygame_menu.themes.THEME_DARK, title='Sudoku Solver')
menu.add_button('Play', run)
menu.add_selector("Sudoku difficulty: ", [("Very Easy", "V.Easy"), ("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard"), ("Very Hard", "V.Hard")], onchange=setDifficulty)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)