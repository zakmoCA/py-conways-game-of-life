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

# event loop to init/run game logic
def main():
    running = True
    
    positions = set()
    positions.add((10,10)) # will add tuple to positions set which we want, instead of two 10s individually
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill(GREY)            
        draw_grid(positions)
        pygame.display.update() # run this whenever i want to reflect logic that changes state to the GUI
                
    
def draw_grid(positions):
    # won't tell me pixel position but col x row position in the grid
    # translate the col x row position to the pixel position then draw it
    for position in positions:
        col, row = position
        # in pygame we always draw from top left corner
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE)) 
        # *top_left: the prefixed * unpacks its tuple so tat they're passed as individual args
  
    for row in range(GRID_HEIGHT):
          pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))
    
    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))
    
    
if __name__ == "__main__":
    main()
