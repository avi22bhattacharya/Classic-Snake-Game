import random
import pygame
pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width,height))
bg_col = (0,139,0)
game_over = False
direction = 0
snake = []
fps = 25
fpsClock = pygame.time.Clock()
snake_width = 30
snake_height = 30
foodx = 400
foody = 300
const = [10]
r = 10
vel = 10
initialx = 500
initialy = 200
snake_mouth = [initialx,initialy]
snake.append(snake_mouth)
for i in range(5,30,5):
    snake.append([initialx + i, initialy])

def move(list, dir):
    if direction == 1:
        snake.pop(len(snake)-1)
        snake.insert(0, [snake[0][0] - vel, snake[0][1]])
    elif direction == 2:
        snake.pop(len(snake) - 1)
        snake.insert(0, [snake[0][0] + vel, snake[0][1]])
    elif direction == 3:
        snake.pop(len(snake) - 1)
        snake.insert(0, [snake[0][0], snake[0][1] - vel])
    elif direction == 4:
        snake.pop(len(snake) - 1)
        snake.insert(0, [snake[0][0], snake[0][1] + vel])
def eat():
    global foodx, foody
    if ((snake[0][0] + snake_width/2 - foodx)**2 + (snake[0][1] + snake_height/2- foody)**2)**0.5 <= 10:
        if direction == 1:
            temp = [snake[-1][0] + snake_width,snake[-1][1]]
            snake.append(temp)
        elif direction == 2:
            temp = [snake[-1][0] - snake_width, snake[-1][1]]
            snake.append(temp)
        elif direction == 3:
            temp = [snake[-1][0], snake[-1][1] - snake_height]
            snake.append(temp)
        elif direction == 4:
            temp = [snake[-1][0], snake[-1][1] + snake_height]
            snake.append(temp)
        foodx = random.randint(50,750)
        foody = random.randint(50,550)
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 1
            if event.key == pygame.K_RIGHT:
                direction = 2
            if event.key == pygame.K_UP:
                direction = 3
            if event.key == pygame.K_DOWN:
                direction = 4

    screen.fill(bg_col)
    pygame.draw.circle(screen, (139,0,0), (foodx,foody), r)
    for i in range(len(snake)):
        pygame.draw.rect(screen,(0,0,0), [snake[i][0],snake[i][1], snake_width, snake_height])
    move(snake, direction)
    if snake[0][0] <= 0 or snake[0][0] >= width or snake[0][1] <= 0 or snake[0][1] >= height:
        game_over = True
    eat()
    pygame.display.update()
    fpsClock.tick(fps)

pygame.quit()