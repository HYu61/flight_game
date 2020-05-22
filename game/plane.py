import pygame
import constants as const
from .bullet import HeroPlaneBullet
import random


class Plane(pygame.sprite.Sprite):
    """
    Basic class of plane
    """
    # the list image of plane
    plane_images_src = []
    # the list image og plane destroy
    destroy_images_src = []
    # the sound effect when plan crashed
    down_sound_src = None
    # the status of plane True is active, False is deactivate
    active = True
    # bullets of the plane
    bullets = pygame.sprite.Group()

    def __init__(self, screen, speed=None):
        """
        constructor
        :param screen: the surface object of the game
        :param speed: the speed of the plane
        """
        super().__init__()
        self._plane_img_list = []
        self._destroy_img_list = []
        self._down_sound_effect = None
        self.load_src()
        self.screen = screen
        self.speed = speed or 10

        # get the image ract
        self.rect = self._plane_img_list[0].get_rect()

        # the width and height of the screen
        self.width, self.height = self.screen.get_size()
        # the width and height of the plane
        self.p_w, self.p_h = self.image[0].get_size()
        # set the initial position
        self.init_position()

    def load_src(self):
        """
        load image and sound resource
        """
        # image for plane
        for img in self.plane_images_src:
            self._plane_img_list.append(pygame.image.load(img))

        # image for plane destroy
        for img in self.destroy_images_src:
            self._destroy_img_list.append(pygame.image.load(img))

        # the sound effect of destroy
        if self.down_sound_src:
            self._down_sound_effect = pygame.mixer.Sound(self.down_sound_src)

    @property
    def image(self):
        return self._plane_img_list

    def blit_me(self):
        """
        draw the plane on the screen
        """
        self.screen.blit(self.image[0], self.rect)

    def init_position(self):
        pass

    # plane move action
    def move_up(self):
        self.rect.top -= self.speed

    def move_down(self):
        self.rect.top += self.speed

    def move_left(self):
        self.rect.left -= self.speed

    def move_right(self):
        self.rect.left += self.speed

    def crash_down(self):
        # sound effect
        if self._down_sound_effect:
            # self._down_sound_effect.play()
            pygame.mixer.Sound.play(self._down_sound_effect)

        # gif for crash down
        for img in self._destroy_img_list:
            self.screen.blit(img, self.rect)

        # set status to deactivate
        self.active = False

    def shoot(self):
        """
        plane shoot the bullet
        """
        bullet = None
        if isinstance(self, HeroPlane):
            bullet = HeroPlaneBullet(self.screen, self)
        self.bullets.add(bullet)


class HeroPlane(Plane):
    """
    hero plane
    """
    plane_images_src = const.HERO_PLANE_IMAGE_LIST
    destroy_images_src = const.HERO_PLANE_DESTROY_LIST
    down_sound_src = const.HERO_PLANE_DESTROY_SOUND

    def __init__(self, screen, speed=None):
        super().__init__(screen, speed)

    def init_position(self):
        """
        set the initial position of the hero plane
        """
        self.rect.left = (self.width - self.p_w) / 2
        self.rect.top = self.height / 2 + self.p_h

    def update(self, war):
        if war.frame % 5 == 0:
            self.screen.blit(self.image[0], self.rect)
        else:
            self.screen.blit(self.image[1], self.rect)
        self.auto_move(war.key_down)
        is_collided = pygame.sprite.spritecollide(self, war.enemy_planes_group, False,
                                                  pygame.sprite.collide_rect_ratio(0.88))
        if is_collided:
            # set the status of the game to finishe
            war.game_status = const.Status.FINISH
            # empty all enemy planes
            war.enemy_planes_group.empty()
            war.enemy_small_plane_group.empty()
            self.bullets.empty()
            # the hero plane is crashed
            self.crash_down()

            # set the score record
            war.result.set_highest_score()



    def auto_move(self, key):
        """
        according the value of the key move automatically
        :param key: the value of the former key
        """
        if key == pygame.K_w or key == pygame.K_UP:
            self.move_up()
        if key == pygame.K_s or key == pygame.K_DOWN:
            self.move_down()
        if key == pygame.K_a or key == pygame.K_LEFT:
            self.move_left()
        if key == pygame.K_d or key == pygame.K_RIGHT:
            self.move_right()

    def move_up(self):
        super().move_up()
        self.rect.top = 0 if self.rect.top < 0 else self.rect.top

    def move_down(self):
        super(HeroPlane, self).move_down()
        if self.rect.top > self.height - self.p_h:
            self.rect.top = self.height - self.p_h

    def move_left(self):
        super(HeroPlane, self).move_left()
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        super().move_right()
        if self.rect.left > self.width - self.p_w:
            self.rect.left = self.width - self.p_w


class EnemyPlaneSmall(Plane):
    """
    Small enemy plane
    """
    # the list image of plane
    plane_images_src = const.ENEMY_PLANE_SMALL_IMAGE
    # the list image og plane destroy
    destroy_images_src = const.ENEMY_PLANE_SMALL_DESTROY_IMAGE
    # the sound effect when plan crashed
    down_sound_src = const.ENEMY_PLANE_SMALL_DOWN_SOUND

    def __init__(self, screen, speed=const.ENEMY_PLANE_SMALL_SPEED):
        super().__init__(screen, speed)

    def init_position(self):
        """
        set the position randomly according to the num of the small plane
        :return:
        """
        self.rect.left = random.randint(0, self.width - self.p_w)
        self.rect.top = random.randint(-1 * const.ENEMY_PLANE_SMALL_NUM * self.p_h, -1 * self.p_h)

    def update(self, *args):
        super().move_down()
        self.blit_me()
        if self.rect.top > self.height:
            self.active = False
            self.reset()

    def reset(self):
        self.active = True
        self.init_position()

    def crash_down(self):
        super().crash_down()
        self.reset()
