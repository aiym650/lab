import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen settings
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
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Font and Clock
font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()

# Snake start position and direction
snake = [(5, 5), (4, 5), (3, 5)]
direction = (1, 0)  # Right

# Game stats
score = 0
level = 1
speed = 10  # Starting speed

# Function to generate random food position not on the snake
def get_random_food_position(snake):
    while True:
        pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
        if pos not in snake:
            return pos

# Food structure: (position, weight, time_to_live)
def create_food(snake):
    pos = get_random_food_position(snake)
    weight = random.choice([1, 2, 3])
    timer = 180  # time before food disappears (~3 seconds at 60 FPS)
    return [pos, weight, timer]

# Create first food
food = create_food(snake)

# Game loop
running = True
while running:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Change direction with arrow keys
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    # Move snake: calculate new head
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Collision with walls or self
    if (
        head in snake or
        head[0] < 0 or head[0] >= COLS or
        head[1] < 0 or head[1] >= ROWS
    ):
        print("Game Over!")
        pygame.time.delay(1000)
        pygame.quit()
        sys.exit()

    # Add new head
    snake.insert(0, head)

    # Check if food is eaten
    if head == food[0]:
        score += food[1]  # Add food weight to score

        # Increase level and speed every 4 points
        if score % 4 == 0:
            level += 1
            speed += 2

        food = create_food(snake)  # Generate new food
    else:
        snake.pop()  # Remove tail if not eaten

        # Decrease food timer
        food[2] -= 1
        if food[2] <= 0:
            food = create_food(snake)  # Replace expired food

    # Clear screen
    screen.fill(BLACK)

    # Draw food with color based on weight
    food_color = {1: YELLOW, 2: ORANGE, 3: RED}[food[1]]
    food_rect = pygame.Rect(food[0][0]*CELL_SIZE, food[0][1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, food_color, food_rect)

    # Draw snake
    for i, block in enumerate(snake):
        x = block[0] * CELL_SIZE
        y = block[1] * CELL_SIZE
        rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        color = GREEN if i == 0 else DARK_GREEN
        pygame.draw.rect(screen, color, rect)

    # Draw score and level
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 120, 10))

    # Update display
    pygame.display.flip()

# Quit the game
pygame.quit()
