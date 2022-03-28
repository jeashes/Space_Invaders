import pygame
from gun import Gun
import controls
from pygame.sprite import Group
from stats import Stats
import time
from scores import Scores


def run():
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_caption('Space Invaders')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game is True:
            gun.update_gun()
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_display(bg_color, screen, stats, sc, gun, bullets, inos)
            controls.update_enemy(stats, screen, sc, gun, inos, bullets)


run()
