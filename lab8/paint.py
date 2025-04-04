import pygame
import sys

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

# Set up brush size
brush_size = 5
drawing = False
shape_mode = 'pen'  # 'pen', 'rectangle', 'circle', 'eraser'
brush_color = BLACK
previous_pos = None

# Create the screen surface
screen.fill(WHITE)

# Set up font for buttons and text
font = pygame.font.SysFont("Arial", 20)

# Function to create a button
def draw_button(x, y, width, height, color, text):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
    label = font.render(text, True, WHITE)
    screen.blit(label, (x + 10, y + 10))

# Function to check if mouse clicks a button
def is_button_clicked(x, y, width, height, mouse_pos):
    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
        return True
    return False

# Function to draw the color selection buttons
def draw_color_buttons():
    x_offset = 20
    y_offset = HEIGHT - 40
    button_width = 40
    button_height = 30
    for i, color in enumerate(colors):
        draw_button(x_offset + i * button_width, y_offset, button_width, button_height, color, "")
        # Highlight selected color
        if brush_color == color:
            pygame.draw.rect(screen, WHITE, pygame.Rect(x_offset + i * button_width + 5, y_offset + 5, button_width - 10, button_height - 10), 3)

# Draw shape mode buttons (Pen, Rectangle, Circle, Eraser)
def draw_shape_buttons():
    draw_button(20, HEIGHT - 100, 80, 30, BLACK, 'Pen')
    draw_button(120, HEIGHT - 100, 80, 30, RED, 'Rectangle')
    draw_button(220, HEIGHT - 100, 80, 30, GREEN, 'Circle')
    draw_button(320, HEIGHT - 100, 80, 30, BLUE, 'Eraser')

# Draw brush size buttons
def draw_size_buttons():
    draw_button(420, HEIGHT - 100, 80, 30, BLACK, '-')
    draw_button(520, HEIGHT - 100, 80, 30, BLACK, '+')

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()

                # Check if a color button is clicked
                x_offset = 20
                y_offset = HEIGHT - 40
                button_width = 40
                button_height = 30
                for i, color in enumerate(colors):
                    if is_button_clicked(x_offset + i * button_width, y_offset, button_width, button_height, mouse_pos):
                        brush_color = color
                        break

                # Check if a shape mode button is clicked
                if is_button_clicked(20, HEIGHT - 100, 80, 30, mouse_pos):
                    shape_mode = 'pen'
                elif is_button_clicked(120, HEIGHT - 100, 80, 30, mouse_pos):
                    shape_mode = 'rectangle'
                elif is_button_clicked(220, HEIGHT - 100, 80, 30, mouse_pos):
                    shape_mode = 'circle'
                elif is_button_clicked(320, HEIGHT - 100, 80, 30, mouse_pos):
                    shape_mode = 'eraser'

                # Check if size buttons are clicked
                if is_button_clicked(420, HEIGHT - 100, 80, 30, mouse_pos):
                    brush_size = max(1, brush_size - 1)  # Decrease size (min 1)
                elif is_button_clicked(520, HEIGHT - 100, 80, 30, mouse_pos):
                    brush_size += 1  # Increase size

                # Start drawing
                drawing = True
                previous_pos = mouse_pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                drawing = False
                previous_pos = None

        elif event.type == pygame.MOUSEMOTION:
            if drawing and shape_mode == 'pen':
                pygame.draw.line(screen, brush_color, previous_pos, event.pos, brush_size)
                previous_pos = event.pos

            elif drawing and shape_mode == 'rectangle':
                screen.fill(WHITE)  # Clear screen
                pygame.draw.rect(screen, brush_color, pygame.Rect(previous_pos, (event.pos[0] - previous_pos[0], event.pos[1] - previous_pos[1])))
                
            elif drawing and shape_mode == 'circle':
                screen.fill(WHITE)  # Clear screen
                radius = int(((event.pos[0] - previous_pos[0])**2 + (event.pos[1] - previous_pos[1])**2)**0.5)
                pygame.draw.circle(screen, brush_color, previous_pos, radius)

            elif drawing and shape_mode == 'eraser':
                pygame.draw.line(screen, WHITE, previous_pos, event.pos, brush_size)
                previous_pos = event.pos

    # Draw the interface buttons
    draw_color_buttons()
    draw_shape_buttons()
    draw_size_buttons()

    # Update screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
