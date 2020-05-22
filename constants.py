import os.path as path
from enum import IntEnum


class Status(IntEnum):
    INIT = 0
    START = 1
    FINISH = 2


# dir path
BASE_DIR = path.dirname(path.realpath(__file__))
IMAGES_DIR = path.join(BASE_DIR, "assets", "images")
SOUNDS_DIR = path.join(BASE_DIR, "assets", "sounds")
RESULT_FILE = path.join(BASE_DIR, "store", "result.txt")
FONT_COLOR_PLAYING = (111, 158, 232)
FONT_COLOR_RESULT = (181,22,22)
DISPLAY_FONT_SIZE = 40
HIGHEST_FONT_SIZE = 80
RESULT_FONT_SIZE = 100
CAPTION = "Plane War"
# background size, images and other related stuff
BACKGROUND_SIZE = (480, 852)
BACKGROUND_IMG_INIT = path.join(IMAGES_DIR, "background.png")
BACKGROUND_IMG_OVER = path.join(IMAGES_DIR, "game_over.png")
BACKGROUND_MUSIC = path.join(SOUNDS_DIR, "game_bg_music.mp3")
BACKGROUND_MUSIC_VOL = 0.8
GAME_TITLE = path.join(IMAGES_DIR, "game_title.png")
GAME_START_BTN = path.join(IMAGES_DIR, "game_start.png")

# hero plane images
HERO_PLANE_IMAGE_LIST = [path.join(IMAGES_DIR, "hero1.png"),
                         path.join(IMAGES_DIR, "hero2.png")]

HERO_PLANE_DESTROY_LIST = [path.join(IMAGES_DIR, "hero_broken_n1.png"),
                           path.join(IMAGES_DIR, "hero_broken_n2.png"),
                           path.join(IMAGES_DIR, "hero_broken_n3.png"),
                           path.join(IMAGES_DIR, "hero_broken_n4.png"), ]

HERO_PLANE_SPEED = 10
HERO_PLANE_BULLET_SPEED = 15

HERO_PLANE_DESTROY_SOUND = path.join(SOUNDS_DIR, "game_over.wav")

# bullet related stuff
HERO_BULLET_IMAGE = path.join(IMAGES_DIR, "bullet1.png")
BULLET_SOUND = path.join(SOUNDS_DIR, "bullet.wav")
BULLET_SOUND_VOL = 0.5

# enemy plane
ENEMY_PLANE_SMALL_IMAGE = [path.join(IMAGES_DIR, "enemy1.png")]
ENEMY_PLANE_SMALL_DESTROY_IMAGE = [path.join(IMAGES_DIR, "enemy1_down1.png"),
                                   path.join(IMAGES_DIR, "enemy1_down2.png"),
                                   path.join(IMAGES_DIR, "enemy1_down3.png"),
                                   path.join(IMAGES_DIR, "enemy1_down4.png")]
ENEMY_PLANE_SMALL_SPEED = 5
ENEMY_PLANE_SMALL_NUM = 5

ENEMY_PLANE_SMALL_DOWN_SOUND = path.join(SOUNDS_DIR, "enemy1_down.wav")
ENEMY_PLANE_SMALL_POINT = 10
