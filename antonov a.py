import pygame
import random

# Инициализация
pygame.init()

# Цвета
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Размер окна
width = 800
height = 600

# Инициализируем окно
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Переменные
block_size = 20 # Размер змейки и еды
snake_speed = 15

clock = pygame.time.Clock()

# Змейка
snake_block = []
snake_length = 1 #размер начальной змейки
snake_head = [width // 2, height // 2]
direction = 'RIGHT'

# Еда
food_pos = [random.randrange(1, width // block_size) * block_size,
            random.randrange(1, height // block_size) * block_size]


# Функция отрисовки змейки
def draw_snake(snake_block):
    for block in snake_block:
        pygame.draw.rect(win, black, [block[0], block[1], block_size, block_size])


# Главный цикл игры
running = True
while running:
    win.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                direction = 'RIGHT'
            elif event.key == pygame.K_UP:
                direction = 'UP'
            elif event.key == pygame.K_DOWN:
                direction = 'DOWN'
# передвижение
    if direction == 'UP':
        snake_head[1] -= block_size
    elif direction == 'DOWN':
        snake_head[1] += block_size
    elif direction == 'LEFT':
        snake_head[0] -= block_size
    elif direction == 'RIGHT':
        snake_head[0] += block_size

    if snake_head[0] == food_pos[0] and snake_head[1] == food_pos[1]:
        snake_length += 1
        food_pos = [random.randrange(1, width // block_size) * block_size,
                    random.randrange(1, height // block_size) * block_size]

    snake_block.append(list(snake_head))
    if len(snake_block) > snake_length:
        del snake_block[0]

    for block in snake_block[:-1]:
        if block == snake_head:
            running = False

    draw_snake(snake_block)

    pygame.draw.rect(win, red, [food_pos[0], food_pos[1], block_size, block_size])

    pygame.display.update()

    clock.tick(snake_speed)

# Закрытие окна
pygame.quit()