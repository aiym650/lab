import pygame
import random
import sys

# initialization
pygame.init()

# screen size
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Background music and sound
pygame.mixer.music.load("images/background.wav")
pygame.mixer.music.play(-1)
crash_sound = pygame.mixer.Sound("images/crash.wav")

# images
bg_img = pygame.image.load("images/AnimatedStreet.png")
player_img = pygame.image.load("images/Player.png")
enemy_img = pygame.image.load("images/Enemy.png")
coin_img_original = pygame.image.load("images/coin.png")
coin_img = pygame.transform.scale(coin_img_original, (30, 30))  # Монетаны кішірейту

# bg animation
bg_y1 = 0
bg_y2 = -HEIGHT
bg_speed = 5

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 80))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 5

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect(center=(random.randint(50, WIDTH - 50), -50))
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.center = (random.randint(50, WIDTH - 50), -50)

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect(center=(random.randint(30, WIDTH - 30), -30))

    def update(self):
        self.rect.y += 4
        if self.rect.top > HEIGHT:
            self.kill()

# Sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# Enemy 
enemy = Enemy()
all_sprites.add(enemy)
enemies.add(enemy)


coin_count = 0

# Coin timer
ADD_COIN = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_COIN, 1200)


running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == ADD_COIN:
            coin = Coin()
            all_sprites.add(coin)
            coins.add(coin)

    
    bg_y1 += bg_speed
    bg_y2 += bg_speed
    if bg_y1 >= HEIGHT:
        bg_y1 = -HEIGHT
    if bg_y2 >= HEIGHT:
        bg_y2 = -HEIGHT

    
    all_sprites.update()

    # Coin collection
    collected = pygame.sprite.spritecollide(player, coins, dokill=True)
    coin_count += len(collected)

    # crash
    if pygame.sprite.spritecollide(player, enemies, dokill=False):
        crash_sound.play()
        pygame.mixer.music.stop()
        print("Game Over!")
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    # Imaging
    screen.blit(bg_img, (0, bg_y1))
    screen.blit(bg_img, (0, bg_y2))
    all_sprites.draw(screen)

    # Number of coins
    coin_text = font.render(f"Coins: {coin_count}", True, (255, 255, 255))
    screen.blit(coin_text, (WIDTH - 120, 10))

    pygame.display.flip()

pygame.quit()
