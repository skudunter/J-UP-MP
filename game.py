import pygame
from player import Player
from platformSpawner import PlatformSpawner
from gameManager import GameManager
import os
import sys


def restartProgram():
    python = sys.executable
    os.execl(python, python, *sys.argv)


# pygame setup
pygame.init()

# global vars
screenWidth = pygame.display.Info().current_w
screenHeight = pygame.display.Info().current_h

screen = pygame.display.set_mode((screenWidth, screenHeight-60))
clock = pygame.time.Clock()
pygame.display.set_caption("J-UP-MP")

# Game objects
gameManager = GameManager()
background = pygame.image.load('Assets/background.png').convert()
background = pygame.transform.scale(background, (screenWidth, screenHeight-60))
player = Player(screenWidth/2, screenHeight/1.8, screenWidth, screenHeight)
platform_spawner = PlatformSpawner(10, screenWidth, screenHeight)
platform_spawner.spawn_platforms()

while gameManager.getGameOver():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameManager.running = False

    screen.blit(background, (0, 0))
    gameManager.checkIfGameOver(player, screenHeight)
    # RENDER YOUR GAME HERE
    player.check_collision(platform_spawner.platforms)
    platform_spawner.display(screen)
    player.display(screen)
    pygame.display.flip()

    dt = clock.tick(60) / 1000
    player.move(dt)
# restartProgram()
# pygame.quit()
