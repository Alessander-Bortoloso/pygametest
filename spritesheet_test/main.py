import pygame
import sys
from player import Player

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_img = pygame.image.load('Walk.png').convert_alpha()

BG = (50, 50, 50)
BLACK = (0, 0, 0)

run = True

def get_image(sheet, frame, width, height, scale, colour):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (0, (frame * 16), width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(colour)
    return image

last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 0
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player('Walk.png', 4, (0, 0), all_sprites)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    delta_time = clock.tick() / 1000

    screen.fill(BG)
    all_sprites.draw(screen)
    all_sprites.update(delta_time)

    #current_time = pygame.time.get_ticks()
    #if current_time - last_update >= animation_cooldown:
    #    frame += 1
    #    if frame > 3:
    #        frame = 0
    #    last_update = current_time

    #frame_0 = get_image(sprite_sheet_img, frame, 16, 16, 3, BLACK)
    #screen.blit(frame_0, (0, 0))

    pygame.display.update()

pygame.quit()
