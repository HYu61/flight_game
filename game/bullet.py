import pygame
import constants as const



class Bullet(pygame.sprite.Sprite):
    """
    the class of the bullet
    """
    # the image of the bullet
    bullet_image_src = None
    # the sound of the bullet
    bullet_sound_src = None
    # the status of the bullet, True is active False is deactivate
    active = True

    def __init__(self, screen, plane, speed):
        super().__init__()
        # self._bullet_image_list = []
        self.image = pygame.image.load(self.bullet_image_src)
        self.screen = screen
        self.speed = speed
        self.plane = plane

        if self.bullet_sound_src:
            self.sound = pygame.mixer.Sound(self.bullet_sound_src)

        # self.load_src()

        # position
        # self.rect = self._bullet_image_list[0].get_rect()
        self.rect = self.image.get_rect()
        # self.rect.centerx = plane.rect.centerx
        # self.rect.top = plane.rect.top

    def update(self, *args):
        pass


class HeroPlaneBullet(Bullet):
    # the image of the bullet
    bullet_image_src = const.HERO_BULLET_IMAGE
    # the sound of the bullet
    bullet_sound_src = const.BULLET_SOUND

    def __init__(self, screen, plane, speed=const.HERO_PLANE_BULLET_SPEED):
        super().__init__(screen, plane, speed)
        # sound effect
        pygame.mixer.Sound.play(self.sound)
        pygame.mixer.Sound.set_volume(self.sound, const.BULLET_SOUND_VOL)
        # bullet position
        self.rect.centerx = plane.rect.centerx
        self.rect.top = plane.rect.top

    def update(self, war):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.remove(self.plane.bullets)
        self.screen.blit(self.image, self.rect)
        result = pygame.sprite.spritecollide(self, war.enemy_planes_group, False)
        for r in result:
            # kill the bullet
            self.kill()
            # the small plane crash down
            r.crash_down()
            war.result.score += const.ENEMY_PLANE_SMALL_POINT


