import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint with Buttons")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
colors = [BLACK, RED, GREEN, BLUE]

# Brush settings
brush_size = 5
drawing = False
shape_mode = 'pen'
brush_color = BLACK
previous_pos = None
start_pos = None

# Fill screen white
screen.fill(WHITE)

# Font for UI
font = pygame.font.SysFont("Arial", 20)

# Draw a button
def draw_button(x, y, width, height, color, text):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
    label = font.render(text, True, WHITE)
    screen.blit(label, (x + 5, y + 5))

# Detect button click
def is_button_clicked(x, y, width, height, mouse_pos):
    return x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height

# Draw color selection buttons
def draw_color_buttons():
    x_offset = 20
    y_offset = HEIGHT - 40
    button_width = 40
    for i, color in enumerate(colors):
        draw_button(x_offset + i * button_width, y_offset, button_width, 30, color, "")
        if brush_color == color:
            pygame.draw.rect(screen, WHITE, (x_offset + i * button_width + 5, y_offset + 5, 30, 20), 2)

# Draw shape tool buttons
def draw_shape_buttons():
    labels = ['Pen', 'Rectangle', 'Circle', 'Square', 'R-Triangle', 'E-Triangle', 'Rhombus', 'Eraser']
    for i, label in enumerate(labels):
        draw_button(20 + i * 90, HEIGHT - 100, 80, 30, BLACK, label)

# Draw brush size buttons
def draw_size_buttons():
    draw_button(750, HEIGHT - 100, 20, 30, BLACK, '-')
    draw_button(750, HEIGHT - 60, 20, 30, BLACK, '+')

# Drawing helper functions
def draw_square(start, end, color):
    side = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
    pygame.draw.rect(screen, color, (start[0], start[1], side, side), 0)

def draw_right_triangle(start, end, color):
    points = [start, (end[0], start[1]), end]
    pygame.draw.polygon(screen, color, points, 0)

def draw_equilateral_triangle(start, end, color):
    side = abs(end[0] - start[0])
    height = (math.sqrt(3) / 2) * side
    points = [start, (start[0] + side, start[1]), (start[0] + side / 2, start[1] - height)]
    pygame.draw.polygon(screen, color, points, 0)

def draw_rhombus(start, end, color):
    mid_x = (start[0] + end[0]) // 2
    mid_y = (start[1] + end[1]) // 2
    dx = abs(end[0] - start[0]) // 2
    dy = abs(end[1] - start[1]) // 2
    points = [(mid_x, start[1]), (end[0], mid_y), (mid_x, end[1]), (start[0], mid_y)]
    pygame.draw.polygon(screen, color, points, 0)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                start_pos = mouse_pos

                # Check color buttons
                for i, color in enumerate(colors):
                    if is_button_clicked(20 + i * 40, HEIGHT - 40, 40, 30, mouse_pos):
                        brush_color = color

                # Shape buttons
                modes = ['pen', 'rectangle', 'circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus', 'eraser']
                for i, mode in enumerate(modes):
                    if is_button_clicked(20 + i * 90, HEIGHT - 100, 80, 30, mouse_pos):
                        shape_mode = mode

                # Brush size buttons
                if is_button_clicked(750, HEIGHT - 100, 20, 30, mouse_pos):
                    brush_size = max(1, brush_size - 1)
                elif is_button_clicked(750, HEIGHT - 60, 20, 30, mouse_pos):
                    brush_size += 1

                drawing = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_pos = pygame.mouse.get_pos()

                # Draw shapes based on mode
                if shape_mode == 'rectangle':
                    pygame.draw.rect(screen, brush_color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])), 0)
                elif shape_mode == 'circle':
                    radius = int(math.hypot(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    pygame.draw.circle(screen, brush_color, start_pos, radius, 0)
                elif shape_mode == 'square':
                    draw_square(start_pos, end_pos, brush_color)
                elif shape_mode == 'right_triangle':
                    draw_right_triangle(start_pos, end_pos, brush_color)
                elif shape_mode == 'equilateral_triangle':
                    draw_equilateral_triangle(start_pos, end_pos, brush_color)
                elif shape_mode == 'rhombus':
                    draw_rhombus(start_pos, end_pos, brush_color)

        elif event.type == pygame.MOUSEMOTION and drawing:
            if shape_mode == 'pen':
                pygame.draw.line(screen, brush_color, previous_pos or start_pos, event.pos, brush_size)
                previous_pos = event.pos
            elif shape_mode == 'eraser':
                pygame.draw.line(screen, WHITE, previous_pos or start_pos, event.pos, brush_size)
                previous_pos = event.pos

    draw_color_buttons()
    draw_shape_buttons()
    draw_size_buttons()
    pygame.display.flip()

pygame.quit()
sys.exit()


