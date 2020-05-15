import sys, pygame
import constants as const


# entry method
def main():
    pygame.init()

    # Background surface
    screen = pygame.display.set_mode(const.BACKGROUND_SIZE)
    pygame.display.set_caption("Flight War")  # set caption
    bg_img = pygame.image.load(const.BACKGROUND_IMG_INIT)

    # background music
    bg_sound = pygame.mixer.Sound(const.BACKGROUND_MUSIC)


    while True:
        for event in pygame.event.get():

            # quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # draw background img
        screen.blit(bg_img, bg_img.get_rect())
        pygame.mixer.Sound.play(bg_sound, -1)
        pygame.mixer.Sound.set_volume(bg_sound, 0.5)

        # display the imges to the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
