import pygame
import math
from datetime import datetime


pygame.init()


WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")


clock_face = pygame.image.load("clock.png")
min_hand = pygame.image.load("min_hand.png")
sec_hand = pygame.image.load("sec_hand.png")


clock_face = pygame.transform.scale(clock_face, (WIDTH, HEIGHT))
min_hand = pygame.transform.scale(min_hand, (200, 200)) 
sec_hand = pygame.transform.scale(sec_hand, (150, 150))  


center = (WIDTH // 2, HEIGHT // 2)


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    
    min_angle = -minutes * 6
    sec_angle = -seconds * 6  

    
    screen.fill((255, 255, 255))
    screen.blit(clock_face, (0, 0))

    
    rotated_min = pygame.transform.rotate(min_hand, min_angle)
    rotated_sec = pygame.transform.rotate(sec_hand, sec_angle)

    
    min_rect = rotated_min.get_rect(center=center)
    sec_rect = rotated_sec.get_rect(center=center)


    screen.blit(rotated_min, min_rect.topleft)
    screen.blit(rotated_sec, sec_rect.topleft)

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
