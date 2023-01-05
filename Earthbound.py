import pygame
import spritesheet

pygame.mixer.init(frequency=44100, channels=2)
pygame.mixer.music.load("music2.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.zoom_factor = 600


camera = Camera()

player_x = 1470
player_y = 450
player_speed = 0.15

fps = 60

background_image = pygame.image.load("twoson.png")
background_rect = background_image.get_rect()

pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
WINDOW_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("EarthBound")

background_image = pygame.image.load("twoson.png").convert()

sprite_sheet_image = pygame.image.load("player.png").convert_alpha()
sprite_sheet = spritesheet.Spritesheet(sprite_sheet_image)

BG = (50, 50, 50)
LIGHTBLUE = (42, 83, 209)

# create animation list
animation_list = []
animation_steps = [2, 4, 2, 2, 2, 2, 2, 2, 2, 1]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 400
frame = 0
step_counter = 0

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 17, 24, 1, LIGHTBLUE))
        step_counter += 1
    animation_list.append(temp_img_list)


run = True
while run:

    # update background
    screen.fill(BG)

    screen.blit(background_image, background_rect.move(-camera.x, -camera.y))

    screen.blit(
        animation_list[action][frame], (player_x - camera.x, player_y - camera.y)
    )

    # update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    # show frame image (leave for testing to see if frames are updating)
    screen.blit(animation_list[action][frame], (0, 0))

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    camera.x = player_x - (WINDOW_SIZE[0] // 2)
    camera.y = player_y - (WINDOW_SIZE[1] // 2)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN and action > 0:
            action -= 1
            frame = 0
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN and action > len(animation_list) - 1:
            action += 1
            frame = 0

    pygame.display.update()

pygame.quit()
