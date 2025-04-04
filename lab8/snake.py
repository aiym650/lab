import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Font for score and level
font = pygame.font.SysFont("Arial", 24)

# Game clock
clock = pygame.time.Clock()


# Function to generate random food position not overlapping the snake
def get_random_food(snake):
    while True:
        pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
        if pos not in snake:
            return pos


# Initial snake body (list of grid positions)
snake = [(5, 5), (4, 5), (3, 5)]
direction = (1, 0)  # Starting direction: right
food = get_random_food(snake)

score = 0
level = 1
speed = 10  # Initial speed (frames per second)

# Game loop
running = True
while running:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle keyboard input to change snake direction
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    # Calculate new head position
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Check for collisions with walls or self
    if (
        head in snake or
        head[0] < 0 or head[0] >= COLS or
        head[1] < 0 or head[1] >= ROWS
    ):
        print("Game Over!")
        pygame.time.delay(1000)
        pygame.quit()
        sys.exit()

    # Add new head position to the snake
    snake.insert(0, head)

    # If food is eaten
    if head == food:
        score += 1
        food = get_random_food(snake)

        # Increase level and speed every 4 points
        if score % 4 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()  # Remove tail if no food eaten

    # Clear screen
    screen.fill(BLACK)

    # Draw food
    food_rect = pygame.Rect(food[0]*CELL_SIZE, food[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, RED, food_rect)

    # Draw snake
    for i, block in enumerate(snake):
        x = block[0] * CELL_SIZE
        y = block[1] * CELL_SIZE
        rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        color = GREEN if i == 0 else DARK_GREEN  # Head is brighter
        pygame.draw.rect(screen, color, rect)

    # Draw score and level
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 120, 10))

    # Update screen
    pygame.display.flip()

# Quit game
pygame.quit()
