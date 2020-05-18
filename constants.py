import os.path as path
from enum import IntEnum


class Status(IntEnum):
    INIT = 0
    START = 1
    FINISH = 2


BASE_DIR = path.dirname(path.realpath(__file__))
IMAGES_DIR = path.join(BASE_DIR, "assets", "images")
SOUNDS_DIR = path.join(BASE_DIR, "assets", "sounds")
BACKGROUND_IMG_INIT = path.join(IMAGES_DIR, "background.png")
BACKGROUND_SIZE = (480, 852)
BACKGROUND_MUSIC = path.join(SOUNDS_DIR, "game_bg_music.wav")
GAME_TITLE = path.join(IMAGES_DIR, "game_title.png")
GAME_START_BTN = path.join(IMAGES_DIR, "game_start.png")

OUR_PLANE_IMAGE_LIST = [path.join(IMAGES_DIR, "hero1.png"),
                        path.join(IMAGES_DIR,"hero2.png")]

OUR_PLANE_DESTROY_LIST = [path.join(IMAGES_DIR, "hero_broken_n1.png"),
                          path.join(IMAGES_DIR, "hero_broken_n2.png"),
                          path.join(IMAGES_DIR, "hero_broken_n3.png"),
                          path.join(IMAGES_DIR, "hero_broken_n4.png"),]
