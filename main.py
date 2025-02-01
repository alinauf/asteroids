import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()  # display update
        clock = pygame.time.Clock()
        dt = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dt = clock.tick(60)
                return
                # pygame.quit()
                # sys.exit()

    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
