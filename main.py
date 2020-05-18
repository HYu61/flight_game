import sys, pygame
import constants as const

# entry method
from game.plane import OurPlane


def main():
    pygame.init()

    # Background surface
    screen = pygame.display.set_mode(const.BACKGROUND_SIZE)
    pygame.display.set_caption("Flight War")  # set caption

    # background music
    bg_sound = pygame.mixer.Sound(const.BACKGROUND_MUSIC)
    # bg_music = pygame.mixer.music.load(const.BACKGROUND_MUSIC)

    bg_img = pygame.image.load(const.BACKGROUND_IMG_INIT)
    game_title = pygame.image.load(const.GAME_TITLE)
    game_title_position = int((bg_img.get_width() - game_title.get_width()) / 2), int(bg_img.get_height() / 2 -
                                                                                      game_title.get_height())

    game_start_btn = pygame.image.load(const.GAME_START_BTN)
    game_start_btn_position = int((bg_img.get_width() - game_start_btn.get_width()) / 2), int(
        bg_img.get_height() / 2 + game_start_btn.get_height(
        ))
    game_status = const.Status.INIT

    frame = 0
    clock = pygame.time.Clock()
    our_plane = OurPlane(screen, 50)
    # our_plane.get_init_position()
    while True:
        clock.tick(60)
        frame += 1
        if frame > 60:
            frame = 0


        for event in pygame.event.get():

            # quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game_status is const.Status.INIT:
                    game_status = const.Status.START
            elif event.type == pygame.KEYDOWN:
                if game_status is const.Status.START:
                    if event.key == pygame.K_w or event.key ==pygame.K_UP:
                        our_plane.move_up()
                    if event.key == pygame.K_x or event.key == pygame.K_DOWN:
                        our_plane.move_down()
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        our_plane.move_left()
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        our_plane.move_right()


        # draw background img
        screen.blit(bg_img, bg_img.get_rect())
        pygame.mixer.Sound.play(bg_sound, -1)
        pygame.mixer.Sound.set_volume(bg_sound, 0.5)
        # pygame.mixer.music.play(-1)

        if game_status is const.Status.INIT:
            screen.blit(game_title, game_title_position)
            screen.blit(game_start_btn, game_start_btn_position)
        elif game_status is const.Status.START:

            # our_plane.blit_me()
            our_plane.update(frame)
        # display the imges to the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
