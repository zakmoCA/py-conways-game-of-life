import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

# pygame methods: display, time, draw, event, quit, QUIT, MOUSEBUTTONDOWN, mouse
# KEYDOWN, K_SPACE, K_c, K_g

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

# pygame requires event loop for calling core logic
def main():
    running = True
    
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
    
if __name__ = "__main__":
    main()