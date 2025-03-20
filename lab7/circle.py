import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

radius = 25
x, y = WIDTH // 2, HEIGHT // 2
speed = 20

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - radius > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + radius < WIDTH:
        x += speed
    if keys[pygame.K_UP] and y - radius > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + radius < HEIGHT:
        y += speed

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    pygame.display.update()
    clock.tick(30)

pygame.quit()

