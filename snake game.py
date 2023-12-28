import pygame
import sys 
import random

#initialize pygame
pygame.init()

#Constants
WIDTH, HEIGHT = 600,400
GRID_SIZE =20
FPS = 10

# COLORS
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0, 255,0)
RED = (255,0,0)

# SNAKE CLASS
class Snake:
    def __init__(self):
        self.body = [(100,100),(90,100),(80,100)]
        self.direction = 'RIGHT'
    def move(self, food_position):
        head = self.body[0]
        x,y = head

        if self.direction == 'UP':
            y -= GRID_SIZE
        elif self.direction == 'DOWN':
            y += GRID_SIZE
        elif self.direction == 'RIGHT':
            x+= GRID_SIZE
        elif self.direction == 'LEFT':
            x-= GRID_SIZE
        
        self.body.insert(0,(x,y))

        if head == food.position:
            return True
        else:
            self.body.pop()
            return False
    def change_direction(self, new_direction):
        if new_direction == 'UP' and not self.direction == 'DOWN':
            self.direction = 'UP'
        elif new_direction == 'DOWN' and not self.direction == 'UP':
            self.direction = 'DOWN'
        elif new_direction == 'RIGHT' and not self.direction == 'LEFT':
            self.direction = 'RIGHT'
        elif new_direction == 'LEFT' and not self.direction == 'RIGHT':
            self.direction = 'LEFT'
    def check_collision(self):
        head = self.body[0]
        if(
            head[0]<0
            or head[0]>= WIDTH
            or head[1]<0
            or head[1]>= HEIGHT
            or head in self.body[1:]
        ):
            return True
        return False
    def get_head_position(self):
        return self.body[0]
    def get_body(self):
        return self.body
    
    # FOOD CLASS
class Food:
    def __init__(self):
        self.position = (0,0)
        self.randomize_position()
    def randomize_position(self):
        x = random.randint(0, (WIDTH - GRID_SIZE)// GRID_SIZE)*GRID_SIZE
        y = random.randint(0, (HEIGHT - GRID_SIZE)// GRID_SIZE)*GRID_SIZE
        self.position=(x,y)
    def get_position(self):
        return self.position
# Pygame setup
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('SNAKE GAME')
clock = pygame.time.Clock()

snake = Snake()
food = Food()

#  Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction('UP')
            elif event.key == pygame.K_DOWN:
                snake.change_direction('DOWN')
            elif event.key == pygame.K_LEFT:
                snake.change_direction('LEFT')
            elif event.key == pygame.K_RIGHT:
                snake.change_direction('RIGHT')
    food_eaten = snake.move(food.get_position())
    # Check for collisions
    if snake.check_collision():
        pygame.quit()
        sys.exit()
    if food_eaten:
        food.randomize_position()
    screen.fill(BLACK)
    for segment in snake.get_body():
        pygame.draw.rect(screen, GREEN,(segment[0], segment[1], GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, RED, (food.get_position()[0], food.get_position()[1], GRID_SIZE, GRID_SIZE))
    pygame.display.flip()
    clock.tick(FPS)

        

