import pygame

pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Suduku Solver")

# main game loop
# events
# game logic
# refresh the screen

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    window.fill((255,255,255))

    pygame.display.flip()

    clock.tick(60)