import time

import pygame
import sys

from enemy import Enemy
from Bullet import Bullet


def events(screen, gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.mright = True

            if event.key == pygame.K_a:
                gun.mleft = True

            if event.key == pygame.K_w:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False

            if event.key == pygame.K_a:
                gun.mleft = False


def update_display(bg_color, screen, stats, sc, gun, bullets, inos):
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.out_put()
    inos.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, inos, bullets):
    """обновляет позици пулек"""
    bullets.update()
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collision = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collision:
        for inos in collision.values():
            stats.score += 10 * len(inos)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_lifes()
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)


def gun_kill(stats, screen, sc, gun, inos, bullets):
    """столкновение пушки и пришельцев"""
    if stats.guns_life > 0:
        stats.guns_life -= 1
        sc.image_lifes()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def update_enemy(stats, screen, sc, gun, inos, bullets):
    """обновляет позицию пришельцев"""
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, sc, gun, inos, bullets)

    enemy_check(stats, screen, sc, gun, inos, bullets)


def enemy_check(stats, screen, sc, gun, inos, bullets):
    """добрались ли до края или нет"""
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, inos, bullets)
            break


def create_army(screen, inos):
    """создание армии пришельцев"""
    ino = Enemy(screen)
    ino_width = ino.rect.width
    ino_height = ino.rect.height
    number_ino_x = int((600 - (2 * ino_width)) / ino_width)
    number_ino_y = int((800 - 64 - (2 * ino_height)) / ino_height)

    for row_number in range((number_ino_y // 3 + 1)):

        for number_ino in range(number_ino_x):
            ino = Enemy(screen)
            ino.x = ino_width + (ino_width * number_ino)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)


def check_high_score(stats, sc):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('high_core.txt', 'w') as file:
            file.write(str(stats.high_score))
