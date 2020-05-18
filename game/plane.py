import pygame
import constants as const


class Plane(pygame.sprite.Sprite):
    """
    Basic class of plane
    """
    # the list image of plane
    plane_images = []
    # the list image og plane destroy
    destroy_images = []
    # the sound effect when plan crashed
    down_sound_src = None
    # the status of plane True is active, False is deactivate
    active = True
    # bullets of the plane
    bullets = pygame.sprite.Group()

    def __init__(self, screen, speed=None):
        super().__init__()
        self._plane_img_list = []
        self._destroy_img_list = []
        self._down_sound_effect = None
        self.load_src()
        self.screen = screen
        self.speed = speed or 10

        # get the image ract
        self.rect = self._plane_img_list[0].get_rect()

    def load_src(self):
        """
        load assets
        """
        # image for plane
        for img in self.plane_images:
            self._plane_img_list.append(pygame.image.load(img))

        # image for plane destroy
        for img in self.destroy_images:
            self._destroy_img_list.append(pygame.image.load(img))

        # the sound effect of destroy
        if self.down_sound_src:
            self.down_sound_src = pygame.mixer.Sound(self._down_sound_effect)

    @property
    def image(self):
        return self._plane_img_list

    def blit_me(self):
        self.screen.blit(self.image[0], self.rect)

    # plane move up
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
            self._down_sound_effect.play()

        # gif for crash down
        for img in self._destroy_img_list:
            self.screen.blit(img, self.rect)

        # set status to deactivate
        self.active = False


class OurPlane(Plane):
    """
    our plane
    """
    plane_images = const.OUR_PLANE_IMAGE_LIST
    destroy_images = const.OUR_PLANE_DESTROY_LIST
    down_sound_src = None

    def __init__(self, screen, speed=None):
        super().__init__(screen, speed)
        self.p_w, self.p_h = self.image[0].get_size()
        self.width, self.height = self.screen.get_size()
        self.init_position()

    def init_position(self):
        self.rect.left = (self.width - self.p_w) / 2
        self.rect.top = self.height / 2 + self.p_h

    def update(self, frame):

        if frame % 5 == 0:
            self.screen.blit(self.image[0], self.rect)
        else:
            self.screen.blit(self.image[1], self.rect)

    def move_up(self):
        super().move_up()
        self.rect.top = 0 if self.rect.top < 0 else self.rect.top

    def move_down(self):
        super(OurPlane, self).move_down()
        if self.rect.top > self.height - self.p_h:
            self.rect.top = self.height - self.p_h

    def move_left(self):
        super(OurPlane, self).move_left()
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        super().move_right()
        if self.rect.left > self.width - self.p_w:
            self.rect.left = self.width - self.p_w
