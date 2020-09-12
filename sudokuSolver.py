import pygame
from square import square
from board import  board

pygame.init()
width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku Solver")

clock = pygame.time.Clock()

grid = board(window)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    window.fill((255,255,255))
    grid.createBoard(width, height)

    pygame.display.update()

    clock.tick(60)