import os.path as path

BASE_DIR = path.dirname(path.realpath(__file__))
IMAGES_DIR = path.join(BASE_DIR, "assets", "images")
SOUNDS_DIR = path.join(BASE_DIR, "assets", "sounds")
BACKGROUND_IMG_INIT = path.join(IMAGES_DIR, "background.png")
BACKGROUND_SIZE = (480, 852)
BACKGROUND_MUSIC = path.join(SOUNDS_DIR, "game_bg_music.wav")
