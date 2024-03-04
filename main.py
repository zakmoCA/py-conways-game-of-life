import pygame
import random

# verbose commenting: for quick reference/reminder for pygame specifics, should i want to build more games with it

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
    playing = False
    
    positions = set()
    positions.add((10,10)) # will add tuple to positions set which we want, instead of two 10s individually
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # translate pixel position back to row x col position
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                pos = (col, row)
                
                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                      playing = not playing
                      
                if event.key == pygame.K_c:
                    positions = set()
                    playing = False
                    
                if event.key == pygame.K_r:
                    positions = gen(random.randrange(2, 5) * GRID_WIDTH)
                
        screen.fill(GREY)            
        draw_grid(positions)
        pygame.display.update() # run this whenever i want to reflect logic that changes state to the GUI
                
def gen(num):
    return set([(random.randrange(0, GRID_HEIGHT), random.randrange(0, GRID_WIDTH)) for _ in range(num)])
     # when generating random n based on grid/board dimensions in future use sets as above to -->
     # avoid generating duplicate positions
    
def adjust_grid(positions):
    pass
  
def get_neighbours(pos):
    pass

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
