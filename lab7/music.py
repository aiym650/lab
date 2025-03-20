import pygame
import os

pygame.init()


screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Simple Music Player")


music_folder = "music"
tracks = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
current_track = 0

pygame.mixer.init()

def play_track(index):
    pygame.mixer.music.load(os.path.join(music_folder, tracks[index]))
    pygame.mixer.music.play()
    print(f"Now playing: {tracks[index]}")

running = True
is_playing = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                if not is_playing:
                    play_track(current_track)
                    is_playing = True
                else:
                    pygame.mixer.music.pause()
                    is_playing = False

            elif event.key == pygame.K_s: 
                pygame.mixer.music.stop()
                is_playing = False

            elif event.key == pygame.K_RIGHT:  
                current_track = (current_track + 1) % len(tracks)
                play_track(current_track)
                is_playing = True

            elif event.key == pygame.K_LEFT:  
                current_track = (current_track - 1) % len(tracks)
                play_track(current_track)
                is_playing = True

    screen.fill((30, 30, 30))
    pygame.display.flip()

pygame.quit()
