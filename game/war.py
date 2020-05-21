import sys
import pygame
import constants as const

from time import sleep
from game.plane import HeroPlane, EnemyPlaneSmall


class PlaneWar(object):
    """
    Plane War class
    """
    # set the frame
    frame = 0
    game_status = None
    hero_plane = None
    enemy_small_plane_group = pygame.sprite.Group()
    enemy_planes_group = pygame.sprite.Group()

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(const.CAPTION)  # set caption
        self.screen = pygame.display.set_mode(const.BACKGROUND_SIZE)

        # background stuff
        self.bg_img = pygame.image.load(const.BACKGROUND_IMG_INIT)
        self.bg_over_img = pygame.image.load(const.BACKGROUND_IMG_OVER)
        self.game_title = pygame.image.load(const.GAME_TITLE)
        self.game_title_position = int((self.bg_img.get_width() - self.game_title.get_width()) / 2), int(
            self.bg_img.get_height() / 2 -
            self.game_title.get_height())
        self.game_start_btn = pygame.image.load(const.GAME_START_BTN)
        self.game_start_btn_position = int((self.bg_img.get_width() - self.game_start_btn.get_width()) / 2), int(
            self.bg_img.get_height() / 2 + self.game_start_btn.get_height(
            ))

        self.set_background_music()

        # set the game status to initial
        self.game_status = const.Status.INIT


    @classmethod
    def set_background_music(cls):
        # background music
        pygame.mixer.music.load(const.BACKGROUND_MUSIC)
        pygame.mixer_music.set_volume(const.BACKGROUND_MUSIC_VOL)
        pygame.mixer_music.play(-1)

    def add_hero_plane(self, speed):
        """
        set hero plane with the speed
        :param speed: the speed of the hero plane
        """
        self.hero_plane = HeroPlane(self.screen, speed)

    def add_enemy_small_plane_group(self, num, speed):
        """
        add some small enemy plane
        :param num: the number of small plane to be added
        :param speed: the speed of the small plane
        """
        for i in range(num):
            e_s_plane = EnemyPlaneSmall(self.screen, speed)
            e_s_plane.add(self.enemy_small_plane_group, self.enemy_planes_group)

    def bind_event(self):
        """
        bind the event of the game
        """
        for event in pygame.event.get():

            # quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_status is const.Status.INIT:
                    self.game_status = const.Status.START
            elif event.type == pygame.KEYDOWN:
                if self.game_status is const.Status.START:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.hero_plane.move_up()
                    if event.key == pygame.K_x or event.key == pygame.K_DOWN:
                        self.hero_plane.move_down()
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.hero_plane.move_left()
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.hero_plane.move_right()
                    if event.key == pygame.K_SPACE:
                        self.hero_plane.shoot()

    def set_fps(self, fps):
        """
        set the frame per second
        :param fps: frame per second
        """
        pygame.time.Clock().tick(fps)
        self.frame += 1
        if self.frame > fps:
            self.frame = 0

    def run_plane_war(self):
        # initial plane instance with speed
        self.add_hero_plane(const.HERO_PLANE_SPEED)
        self.add_enemy_small_plane_group(const.ENEMY_PLANE_SMALL_NUM, const.ENEMY_PLANE_SMALL_SPEED)
        while True:
            self.set_fps(60)
            self.bind_event()
            # draw background img
            self.screen.blit(self.bg_img, self.bg_img.get_rect())

            if self.game_status is const.Status.INIT:
                self.screen.blit(self.game_title, self.game_title_position)
                self.screen.blit(self.game_start_btn, self.game_start_btn_position)
            elif self.game_status is const.Status.START:
                self.hero_plane.update(self)
                # get bullets
                self.hero_plane.bullets.update(self)
                # enemy_small_plane_group.update()
                self.enemy_small_plane_group.update()
            elif self.game_status is const.Status.FINISH:
                sleep(1)
                self.screen.blit(self.bg_over_img, self.bg_over_img.get_rect())

            pygame.display.flip()
