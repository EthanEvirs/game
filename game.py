import pygame
import pygame.mixer

pygame.mixer.init(frequency=44100, channels=2)
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.zoom_factor = 600


camera = Camera()

sprite_sheet = pygame.image.load("player.png")
colorkey = (42, 83, 209)
sprite_sheet.set_colorkey(colorkey)


def get_image(sheet, width, height):
    image = pygame.Surface((width, height))
    image.blit(sheet, (0, 0))

    return image


frame_0 = get_image(sprite_sheet, 0, 0)


frames = [
    pygame.Rect(0, 0, 16, 24),  # frame1
    pygame.Rect(17, 0, 16, 25),  # frame2
    ##pygame.Rect(128, 0, 64, 64),  # frame3
    ##pygame.Rect(192, 0, 64, 64),  # frame4
]

up_down_frames = [
    pygame.Rect(80, 0, 26, 14),
    pygame.Rect(100, 0, 26, 14),
]

frame_index = 0

# Screen size
pygame.init()
screen_width = 1024
screen_height = 786
window_size = (screen_width, screen_height)

player_x = 2770
player_y = 650
player_speed = 0.5

player_x -= player_speed * camera.zoom_factor
player_y -= player_speed * camera.zoom_factor

player_speed = 0.15


fps = 60
elasped_time = 0

background_image = pygame.image.load("background.png")
background_rect = background_image.get_rect()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Movement test")

BG_COLOR = (50, 50, 50)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        frame_index = frame_index - 0.05
        frame_index = frame_index % len(frames)
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        frame_index = frame_index + 0.05
        frame_index = frame_index % len(frames)
        player_x += player_speed
    if keys[pygame.K_UP]:
        frame_index = frame_index - 0.05
        frame_index = frame_index % len(frames)
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        frame_index = frame_index + 0.05
        frame_index = frame_index % len(frames)
        player_y += player_speed

    camera.x = player_x - (window_size[0] // 2)
    camera.y = player_y - (window_size[1] // 2)

    # update background
    screen.fill(BG_COLOR)
    # display image
    screen.blit(background_image, background_rect.move(-camera.x, -camera.y))
    draw_x = player_x - camera.x
    draw_y = player_y - camera.y
    draw_width = frames[int(frame_index)].width * camera.zoom_factor
    draw_height = frames[int(frame_index)].height * camera.zoom_factor

    # sprite sheet
    screen.blit(sprite_sheet, (0, 0))
    # show frame image
    screen.blit(frame_0, (17, 0))

    screen.blit(
        sprite_sheet,
        (draw_x, draw_y, draw_width, draw_height),
        frames[int(frame_index)],
    )

    pygame.display.flip()

pygame.quit()
