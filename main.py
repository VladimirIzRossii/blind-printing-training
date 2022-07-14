import random
import os
import pygame
import math
import time

width = 1920
height = 1080
const = height / 45
fps = 60
keyboard_margin_left = 18.25 * const
keyboard_margin_top = 25 * const
keykup_size = 2.5 * const
keycap_range = 0.25 * const
pygame.init()
pygame.font.init()
# myfont = pygame.font.Font('MaredivRegular.ttf', round(1.5 * cellsize))
# myfont1 = pygame.font.Font('MaredivRegular.ttf', round(4 * cellsize))
screen = pygame.display.set_mode((width, height))
hubscreen = pygame.Surface((width / 2, height / 2))
# hubscreen.fill((50, 50, 50))
# if flscr:
#     monitor = pygame.display.set_mode((width1, height1), pygame.FULLSCREEN)
# else:
#     monitor = pygame.display.set_mode((width1, height1))

clock = pygame.time.Clock()
keyboard_recs = [pygame.Rect(keyboard_margin_left, keyboard_margin_top, keykup_size, keykup_size),
                 pygame.Rect((keykup_size + keycap_range) * 1 + keyboard_margin_left, keyboard_margin_top, keykup_size,
                             keykup_size),
                 pygame.Rect((keykup_size + keycap_range) * 2 + keyboard_margin_left, keyboard_margin_top, keykup_size,
                             keykup_size),
                 pygame.Rect((keykup_size + keycap_range) * 3 + keyboard_margin_left, keyboard_margin_top, keykup_size,
                             keykup_size),
                 pygame.Rect((keykup_size + keycap_range) * 4 + keyboard_margin_left, keyboard_margin_top, keykup_size,
                             keykup_size),
                 pygame.Rect((keykup_size + keycap_range) * 5 + keyboard_margin_left, keyboard_margin_top, keykup_size,
                             keykup_size),
                 pygame.Rect((keykup_size + keycap_range) * 6 + keyboard_margin_left, keyboard_margin_top, keykup_size,
                             keykup_size),
                 pygame.Rect((keykup_size + keycap_range) * 7 + keyboard_margin_left, keyboard_margin_top, keykup_size,
                             keykup_size),
                 pygame.Rect((keykup_size + keycap_range) * 8 + keyboard_margin_left, keyboard_margin_top, keykup_size,
                             keykup_size),
                 pygame.Rect((keykup_size + keycap_range) * 9 + keyboard_margin_left, keyboard_margin_top, keykup_size,
                             keykup_size),
                 pygame.Rect((keykup_size + keycap_range) * 10 + keyboard_margin_left, keyboard_margin_top, keykup_size,
                             keykup_size),
                 pygame.Rect((keykup_size + keycap_range) * 11 + keyboard_margin_left, keyboard_margin_top, keykup_size,
                             keykup_size),
                 pygame.Rect((keykup_size + keycap_range) * 12 + keyboard_margin_left, keyboard_margin_top, keykup_size,
                             keykup_size),
                 pygame.Rect((keykup_size + keycap_range) * 13 + keyboard_margin_left, keyboard_margin_top,
                             2 * keykup_size, keykup_size),

                 pygame.Rect(keyboard_margin_left, keyboard_margin_top + keycap_range + keykup_size,
                             1.5 * keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.5 * keykup_size + keycap_range,
                             keyboard_margin_top + keycap_range + keykup_size, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.5 * keykup_size + 2 * keycap_range + keykup_size,
                             keyboard_margin_top + keycap_range + keykup_size, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.5 * keykup_size + 3 * keycap_range + 2 * keykup_size,
                             keyboard_margin_top + keycap_range + keykup_size, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.5 * keykup_size + 4 * keycap_range + 3 * keykup_size,
                             keyboard_margin_top + keycap_range + keykup_size, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.5 * keykup_size + 5 * keycap_range + 4 * keykup_size,
                             keyboard_margin_top + keycap_range + keykup_size, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.5 * keykup_size + 6 * keycap_range + 5 * keykup_size,
                             keyboard_margin_top + keycap_range + keykup_size, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.5 * keykup_size + 7 * keycap_range + 6 * keykup_size,
                             keyboard_margin_top + keycap_range + keykup_size, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.5 * keykup_size + 8 * keycap_range + 7 * keykup_size,
                             keyboard_margin_top + keycap_range + keykup_size, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.5 * keykup_size + 9 * keycap_range + 8 * keykup_size,
                             keyboard_margin_top + keycap_range + keykup_size, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.5 * keykup_size + 10 * keycap_range + 9 * keykup_size,
                             keyboard_margin_top + keycap_range + keykup_size, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.5 * keykup_size + 11 * keycap_range + 10 * keykup_size,
                             keyboard_margin_top + keycap_range + keykup_size, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.5 * keykup_size + 12 * keycap_range + 11 * keykup_size,
                             keyboard_margin_top + keycap_range + keykup_size, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.5 * keykup_size + 13 * keycap_range + 12 * keykup_size,
                             keyboard_margin_top + keycap_range + keykup_size, 1.5 * keykup_size, keykup_size),

                 pygame.Rect(keyboard_margin_left, keyboard_margin_top + (keycap_range + keykup_size) * 2,
                             1.8 * keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.8 * keykup_size + keycap_range,
                             keyboard_margin_top + (keycap_range + keykup_size) * 2, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.8 * keykup_size + 2 * keycap_range + keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 2, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.8 * keykup_size + 3 * keycap_range + 2 * keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 2, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.8 * keykup_size + 4 * keycap_range + 3 * keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 2, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.8 * keykup_size + 5 * keycap_range + 4 * keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 2, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.8 * keykup_size + 6 * keycap_range + 5 * keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 2, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.8 * keykup_size + 7 * keycap_range + 6 * keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 2, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.8 * keykup_size + 8 * keycap_range + 7 * keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 2, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.8 * keykup_size + 9 * keycap_range + 8 * keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 2, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.8 * keykup_size + 10 * keycap_range + 9 * keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 2, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.8 * keykup_size + 11 * keycap_range + 10 * keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 2, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.8 * keykup_size + 12 * keycap_range + 11 * keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 2, 2.2 * keykup_size + keycap_range,
                             keykup_size),

                 pygame.Rect(keyboard_margin_left, keyboard_margin_top + (keycap_range + keykup_size) * 3,
                             2.6 * keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 2.6 * keykup_size + keycap_range,
                             keyboard_margin_top + (keycap_range + keykup_size) * 3, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 2.6 * keykup_size + 2 * keycap_range + keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 3, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 2.6 * keykup_size + 3 * keycap_range + 2 * keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 3, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 2.6 * keykup_size + 4 * keycap_range + 3 * keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 3, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 2.6 * keykup_size + 5 * keycap_range + 4 * keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 3, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 2.6 * keykup_size + 6 * keycap_range + 5 * keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 3, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 2.6 * keykup_size + 7 * keycap_range + 6 * keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 3, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 2.6 * keykup_size + 8 * keycap_range + 7 * keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 3, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 2.6 * keykup_size + 9 * keycap_range + 8 * keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 3, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 2.6 * keykup_size + 10 * keycap_range + 9 * keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 3, keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 2.6 * keykup_size + 11 * keycap_range + 10 * keykup_size,
                             keyboard_margin_top + (keycap_range + keykup_size) * 3, 2.6 * keykup_size, keykup_size),

                 pygame.Rect(keyboard_margin_left, keyboard_margin_top + (keycap_range + keykup_size) * 4,
                             1.2 * keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + 1.2 * keykup_size + keycap_range,
                             keyboard_margin_top + (keycap_range + keykup_size) * 4, 1.2 * keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + (1.2 * keykup_size + keycap_range) * 2,
                             keyboard_margin_top + (keycap_range + keykup_size) * 4, 1.2 * keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + (1.2 * keykup_size + keycap_range) * 3,
                             keyboard_margin_top + (keycap_range + keykup_size) * 4, 7 * keykup_size + 2 * keycap_range,
                             keykup_size),
                 pygame.Rect(keyboard_margin_left + (1.2 * keykup_size) * 3 + keycap_range * 4 + keykup_size * 7 + 2 *
                             keycap_range,
                             keyboard_margin_top + (keycap_range + keykup_size) * 4, 1.2 * keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + (1.2 * keykup_size) * 4 + keycap_range * 5 + keykup_size * 7 + 2 *
                             keycap_range,
                             keyboard_margin_top + (keycap_range + keykup_size) * 4, 1.2 * keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + (1.2 * keykup_size) * 5 + keycap_range * 6 + keykup_size * 7 + 2 *
                             keycap_range,
                             keyboard_margin_top + (keycap_range + keykup_size) * 4, 1.2 * keykup_size, keykup_size),
                 pygame.Rect(keyboard_margin_left + (1.2 * keykup_size) * 6 + keycap_range * 7 + keykup_size * 7 + 2 *
                             keycap_range,
                             keyboard_margin_top + (keycap_range + keykup_size) * 4, 1.2 * keykup_size, keykup_size),
                 ]


class Player:
    def __init__(self, money):
        self.money = money

    def money(self):
        return self.money


def print_keyboard(*key_pressed):
    key_pressed = key_pressed[0]
    # pygame.draw.rect(screen, (255, 255, 255), [50, 400, 1500, 450], 1)
    if key_pressed:
        for key in key_pressed:
            pygame.draw.rect(screen, (255, 255, 255), keyboard_recs[key - 1], 0, 5)
    for keycup in keyboard_recs:
        pygame.draw.rect(screen, (255, 255, 255), keycup, 1, 5)


# class CommonTower(Tower):
#     def fire(self):
#         if self.firerate <= 0:
#             addbullet(self.x, self.y, 6, self.color, self.damage, self.bullspeed, 0)
#             self.firerate = self.firespeed
#         else:
#             self.firerate -= 1 / fps
#
#     def draw(self):
#         outline_mask(greentow, (self.x - cellsize / 2, self.y - cellsize / 2))
#         window.blit(greentow, (self.x - cellsize / 2, self.y - cellsize / 2))
#         # pygame.draw.circle(window, self.color, [self.x, self.y], self.size)


# class QuadTower(Tower):
#     def fire(self):
#         if self.firerate <= 0:
#             for direction in range(4):
#                 addbullet(self.x, self.y, 6, self.color, self.damage, self.bullspeed, direction)
#             self.firerate = self.firespeed
#         else:
#             self.firerate -= 1 / fps
#
#     def draw(self):
#         outline_mask(yellowtow, (self.x - cellsize / 2, self.y - cellsize / 2))
#         window.blit(yellowtow, (self.x - cellsize / 2, self.y - cellsize / 2))


# class Bullet:
#     def __init__(self, x, y, size, color, damage, speed, direction):
#         self.x = x
#         self.y = y
#         self.size = size / sclsz1 * cellsize / 20
#         self.color = color
#         self.damage = damage
#         self.speed = speed * cellsize / 20 * 60 / clock.get_fps()
#         self.rect = pygame.Rect(x - size, y - size, size * 2, size * 2)
#         self.direction = direction
#
#     def move(self):
#         if self.direction == 0:
#             self.x += self.speed
#         if self.direction == 1:
#             self.x -= self.speed
#         if self.direction == 2:
#             self.y += self.speed
#         if self.direction == 3:
#             self.y -= self.speed
#         if self.direction == 4:
#             self.x += self.speed / math.sqrt(2)
#             self.y += self.speed / math.sqrt(2)
#         if self.direction == 5:
#             self.x += self.speed / math.sqrt(2)
#             self.y -= self.speed / math.sqrt(2)
#         if self.direction == 6:
#             self.x -= self.speed / math.sqrt(2)
#             self.y += self.speed / math.sqrt(2)
#         if self.direction == 7:
#             self.x -= self.speed / math.sqrt(2)
#             self.y -= self.speed / math.sqrt(2)
#         if self.direction == 8:
#             if meat:
#                 self.homingx = \
#                     (meat[0].x - self.x) / math.sqrt((meat[0].x - self.x) ** 2 + (meat[0].y - self.y) ** 2) * self.speed
#                 self.homingxy = \
#                     (meat[0].y - self.y) / math.sqrt((meat[0].x - self.x) ** 2 + (meat[0].y - self.y) ** 2) * self.speed
#                 self.x += self.homingx
#                 self.y += self.homingxy
#             else:
#                 self.x += self.homingx
#                 self.y += self.homingxy
#         self.rect = pygame.Rect(self.x - self.size, self.y - self.size, self.size * 2, self.size * 2)
#
#     def draw(self):
#         pygame.draw.circle(window, self.color, [self.x, self.y], self.size)
#         # pygame.draw.rect(window, (255, 0, 0), self.rect, 1)
#
#     def rng(self):
#         return self.x
#
#     def rect(self):
#         return self.rect
#
#     def damage(self):
#         return self.damage


# class Crosshair:
#     def __init__(self):
#         self.Cursor = cross
#         pygame.mouse.set_visible(False)
#
#     def render(self):
#         monitor.blit(self.Cursor, (pygame.mouse.get_pos()))


# def showfps():
#     if show:
#         cost = myfont.render(f'{clock.get_fps()}', False, 'white')
#         screen.blit(cost, (0, 0))


# def outline_mask(img, loc):
#     mask = pygame.mask.from_surface(img)
#     mask_outline = mask.outline()
#     n = 0
#     for point in mask_outline:
#         mask_outline[n] = (point[0] + loc[0], point[1] + loc[1])
#         n += 1
#     pygame.draw.polygon(window, (255, 255, 255), mask_outline, 3)
#
#
# def outline_mask1(img, loc):
#     mask = pygame.mask.from_surface(img)
#     mask_outline = mask.outline()
#     n = 0
#     for point in mask_outline:
#         mask_outline[n] = (point[0] + loc[0], point[1] + loc[1])
#         n += 1
#     pygame.draw.polygon(monitor, (255, 255, 255), mask_outline, 7)
#
#
# def outline_mask2(img, loc):
#     img = pygame.transform.scale(img, (5 * cellsize / 20, 5 * cellsize / 20))
#     mask = pygame.mask.from_surface(img)
#     mask_outline = mask.outline()
#     n = 0
#     for point in mask_outline:
#         mask_outline[n] = (point[0] + loc[0], point[1] + loc[1])
#         n += 1
#     pygame.draw.polygon(window, (255, 255, 255), mask_outline, 3)


def run():
    print_keyboard(key_presed)
    # overwidth()
    # if alive:
    #     global spawntime, inviztime, wawe, playerv, meatend
    #     for tower in towers:
    #         tower.draw()
    #         tower.fire()
    #     for drop in drops:
    #         drop.fly()
    #         drop.take()
    #         drop.draw()
    #         if drop.taked():
    #             drops.remove(drop)
    #             plr.money += 1
    #     for bullet in bullets:
    #         bullet.move()
    #         bullet.draw()
    #         if player.rect().colliderect(bullet.rect):
    #             player.hp -= 1
    #             bullets.remove(bullet)
    #             break
    #         for wall in walls:
    #             if wall.colliderect(bullet.rect):
    #                 bullets.remove(bullet)
    #                 break
    #     for meats in meat:
    #         meats.draw()
    #         meats.go()
    #         for bullet in bullets:
    #             if Bullet.rng(bullet) > width or bullet.x < 0:
    #                 bullets.remove(bullet)
    #             elif meats.rect.colliderect(bullet.rect):
    #                 meats.damage(bullet.damage)
    #                 bullets.remove(bullet)
    #         if not meats.check():
    #             if meats in meat:
    #                 for i in range(random.randint(3, 5)):
    #                     adddrop(meats.x, meats.y, meats.x, meats.y)
    #                 ch = random.randint(1, 10)
    #                 if ch == 5 or ch == 2:
    #                     adddrop(meats.x, meats.y, meats.x, meats.y, True)
    #                 explosions.append(e.Explosion(meats.x, meats.y))
    #                 meat.remove(meats)
    #         if inviztime > 500 and player.rect().colliderect(meats.rect):
    #             player.hp -= 1
    #             inviztime = 0
    #         else:
    #             inviztime += 1
    #     if len(meat) == 0 and wawe < 3:
    #         if spawntime > 300:
    #             for i in range(10 + wawe * 2):
    #                 if wawe == 0:
    #                     meatcreate(meatstrt[0] - 2 * i * cellsize, meatstrt[1], 50, 0.5, wawe + 10, 'red', False)
    #                 else:
    #                     meatcreate(meatstrt[0] - 2 * i * cellsize, meatstrt[1], wawe * 50, 0.6, wawe + 10, 'red', False)
    #             wawe += 1
    #             spawntime = 0
    #         else:
    #             spawntime += 1
    #     if len(meat) == 0 and (wawe >= 3 or wawe == 0):
    #         meatend = True
    #     else:
    #         meatend = False
    # else:
    #     for tower in towers:
    #         tower.draw()
    #     for drop in drops:
    #         drop.fly()
    #         drop.draw()
    #     for bullet in bullets:
    #         bullet.move()
    #         bullet.draw()
    #         if player.rect().colliderect(bullet.rect):
    #             player.hp -= 1
    #             bullets.remove(bullet)
    #             break
    #         for wall in walls:
    #             if wall.colliderect(bullet.rect):
    #                 bullets.remove(bullet)
    #                 break
    #     for meats in meat:
    #         meats.draw()
    #         for bullet in bullets:
    #             if Bullet.rng(bullet) > width or bullet.x < 0:
    #                 bullets.remove(bullet)
    #             elif meats.rect.colliderect(bullet.rect):
    #                 meats.damage(bullet.damage)
    #                 bullets.remove(bullet)


plr = Player(35)
# crosshair = Crosshair()
running = True
last_time = time.time()
key_presed = []

while running:
    # pygame.mouse.set_visible(False)
    # print(pygame.key.get_pressed()[pygame.K_w])
    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_q:
            #     key_presed = 16
            # if event.key == pygame.K_w:
            #     key_presed = 17
            # if event.key == pygame.K_e:
            #     key_presed = 18
            # if event.key == pygame.K_r:
            #     key_presed = 19
            # if event.key == pygame.K_t:
            #     key_presed = 20
            # if event.key == pygame.K_y:
            #     key_presed = 21
            # if event.key == pygame.K_u:
            #     key_presed = 22
            # if event.key == pygame.K_i:
            #     key_presed = 23
            # if event.key == pygame.K_o:
            #     key_presed = 24
            # if event.key == pygame.K_p:
            #     key_presed = 25
            # if event.key == pygame.K_LEFTBRACKET:
            #     key_presed = 26
            # if event.key == pygame.K_RIGHTBRACKET:
            #     key_presed = 27
            # if event.key == pygame.K_BACKSLASH:
            #     key_presed = 28
            # if event.key == pygame.K_a:
            #     key_presed = 30
            # if event.key == pygame.K_s:
            #     key_presed = 31
            # if event.key == pygame.K_d:
            #     key_presed = 32
            # if event.key == pygame.K_f:
            #     key_presed = 33
            # if event.key == pygame.K_g:
            #     key_presed = 34
            # if event.key == pygame.K_h:
            #     key_presed = 35
            # if event.key == pygame.K_j:
            #     key_presed = 36
            # if event.key == pygame.K_k:
            #     key_presed = 37
            # if event.key == pygame.K_l:
            #     key_presed = 38
            # if event.key == pygame.K_SEMICOLON:
            #     key_presed = 39
            # if event.key == pygame.K_QUOTEDBL:
            #     key_presed = 40
            # if event.key == pygame.K_z:
            #     key_presed = 43
            # if event.key == pygame.K_x:
            #     key_presed = 44
            # if event.key == pygame.K_c:
            #     key_presed = 45
            # if event.key == pygame.K_v:
            #     key_presed = 46
            # if event.key == pygame.K_b:
            #     key_presed = 47
            # if event.key == pygame.K_n:
            #     key_presed = 48
            # if event.key == pygame.K_m:
            #     key_presed = 49
            # if event.key == pygame.K_COMMA:
            #     key_presed = 50
            # if event.key == pygame.K_PERIOD:
            #     key_presed = 51
            # if event.key == pygame.K_SLASH:
            #     key_presed = 52
            # if event.key == pygame.K_SPACE:
            #     key_presed = 57
            if event.key == pygame.K_q:
                key_presed.append(16)
            if event.key == pygame.K_w:
                key_presed.append(17)
            if event.key == pygame.K_e:
                key_presed.append(18)
            if event.key == pygame.K_r:
                key_presed.append(19)
            if event.key == pygame.K_t:
                key_presed.append(20)
            if event.key == pygame.K_y:
                key_presed.append(21)
            if event.key == pygame.K_u:
                key_presed.append(22)
            if event.key == pygame.K_i:
                key_presed.append(23)
            if event.key == pygame.K_o:
                key_presed.append(24)
            if event.key == pygame.K_p:
                key_presed.append(25)
            if event.key == pygame.K_LEFTBRACKET:
                key_presed.append(26)
            if event.key == pygame.K_RIGHTBRACKET:
                key_presed.append(27)
            if event.key == pygame.K_BACKSLASH:
                key_presed.append(28)
            if event.key == pygame.K_a:
                key_presed.append(30)
            if event.key == pygame.K_s:
                key_presed.append(31)
            if event.key == pygame.K_d:
                key_presed.append(32)
            if event.key == pygame.K_f:
                key_presed.append(33)
            if event.key == pygame.K_g:
                key_presed.append(34)
            if event.key == pygame.K_h:
                key_presed.append(35)
            if event.key == pygame.K_j:
                key_presed.append(36)
            if event.key == pygame.K_k:
                key_presed.append(37)
            if event.key == pygame.K_l:
                key_presed.append(38)
            if event.key == pygame.K_SEMICOLON:
                key_presed.append(39)
            if event.key == pygame.K_QUOTEDBL:
                key_presed.append(40)
            if event.key == pygame.K_z:
                key_presed.append(43)
            if event.key == pygame.K_x:
                key_presed.append(44)
            if event.key == pygame.K_c:
                key_presed.append(45)
            if event.key == pygame.K_v:
                key_presed.append(46)
            if event.key == pygame.K_b:
                key_presed.append(47)
            if event.key == pygame.K_n:
                key_presed.append(48)
            if event.key == pygame.K_m:
                key_presed.append(49)
            if event.key == pygame.K_COMMA:
                key_presed.append(50)
            if event.key == pygame.K_PERIOD:
                key_presed.append(51)
            if event.key == pygame.K_SLASH:
                key_presed.append(52)
            if event.key == pygame.K_SPACE:
                key_presed.append(57)
        if event.type == pygame.KEYUP:
            # key_presed = 0
            if event.key == pygame.K_q:
                key_presed.remove(16)
            if event.key == pygame.K_w:
                key_presed.remove(17)
            if event.key == pygame.K_e:
                key_presed.remove(18)
            if event.key == pygame.K_r:
                key_presed.remove(19)
            if event.key == pygame.K_t:
                key_presed.remove(20)
            if event.key == pygame.K_y:
                key_presed.remove(21)
            if event.key == pygame.K_u:
                key_presed.remove(22)
            if event.key == pygame.K_i:
                key_presed.remove(23)
            if event.key == pygame.K_o:
                key_presed.remove(24)
            if event.key == pygame.K_p:
                key_presed.remove(25)
            if event.key == pygame.K_LEFTBRACKET:
                key_presed.remove(26)
            if event.key == pygame.K_RIGHTBRACKET:
                key_presed.remove(27)
            if event.key == pygame.K_BACKSLASH:
                key_presed.remove(28)
            if event.key == pygame.K_a:
                key_presed.remove(30)
            if event.key == pygame.K_s:
                key_presed.remove(31)
            if event.key == pygame.K_d:
                key_presed.remove(32)
            if event.key == pygame.K_f:
                key_presed.remove(33)
            if event.key == pygame.K_g:
                key_presed.remove(34)
            if event.key == pygame.K_h:
                key_presed.remove(35)
            if event.key == pygame.K_j:
                key_presed.remove(36)
            if event.key == pygame.K_k:
                key_presed.remove(37)
            if event.key == pygame.K_l:
                key_presed.remove(38)
            if event.key == pygame.K_SEMICOLON:
                key_presed.remove(39)
            if event.key == pygame.K_QUOTEDBL:
                key_presed.remove(40)
            if event.key == pygame.K_z:
                key_presed.remove(43)
            if event.key == pygame.K_x:
                key_presed.remove(44)
            if event.key == pygame.K_c:
                key_presed.remove(45)
            if event.key == pygame.K_v:
                key_presed.remove(46)
            if event.key == pygame.K_b:
                key_presed.remove(47)
            if event.key == pygame.K_n:
                key_presed.remove(48)
            if event.key == pygame.K_m:
                key_presed.remove(49)
            if event.key == pygame.K_COMMA:
                key_presed.remove(50)
            if event.key == pygame.K_PERIOD:
                key_presed.remove(51)
            if event.key == pygame.K_SLASH:
                key_presed.remove(52)
            if event.key == pygame.K_SPACE:
                key_presed.remove(57)
#                 moving_right = True
#             if event.key == pygame.K_a:
#                 moving_left = True
#             if event.key == pygame.K_w:
#                 moving_up = True
#             if event.key == pygame.K_s:
#                 moving_down = True
#             if event.key == pygame.K_1:
#                 towernum = 1
#             if event.key == pygame.K_2:
#                 towernum = 2
#             if event.key == pygame.K_3:
#                 towernum = 3
#             if event.key == pygame.K_4:
#                 towernum = 4
#             if event.key == pygame.K_F5:
#                 show = not show
#             if event.key == pygame.K_F11:
#                 fullscrn()
#             if event.key == pygame.K_ESCAPE:
#                 if towernum != 0:
#                     towernum = 0
#                 else:
#                     running = False
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_d:
#                 moving_right = False
#             if event.key == pygame.K_a:
#                 moving_left = False
#             if event.key == pygame.K_w:
#                 moving_up = False
#             if event.key == pygame.K_s:
#                 moving_down = False
#     crosshair.render()

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         run = False
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if event.button == 1:
        #             maketower(towernum)
        #             if getmpos()[0] >= 68 * cellsize:
        #                 towernum = uiswtch()
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_F5:
        #             show = not show
        #         if event.key == pygame.K_F11:
        #             fullscrn()
        #         if event.key == pygame.K_F1:
        #             if fps == 120:
        #                 fps = 60
        #             else:
        #                 fps = 120
        #         if event.key == pygame.K_d:
        #             moving_right = True
        #         if event.key == pygame.K_a:
        #             moving_left = True
        #         if event.key == pygame.K_w:
        #             moving_up = True
        #         if event.key == pygame.K_s:
        #             moving_down = True
        #         if event.key == pygame.K_1:
        #             towernum = 1
        #         if event.key == pygame.K_2:
        #             towernum = 2
        #         if event.key == pygame.K_3:
        #             towernum = 3
        #         if event.key == pygame.K_4:
        #             towernum = 4
        #         if event.key == pygame.K_ESCAPE:
        #             if towernum != 0:
        #                 towernum = 0
        #             else:
        #                 running = False
        #     if event.type == pygame.KEYUP:
        #         if event.key == pygame.K_d:
        #             moving_right = False
        #         if event.key == pygame.K_a:
        #             moving_left = False
        #         if event.key == pygame.K_w:
        #             moving_up = False
        #         if event.key == pygame.K_s:
        #             moving_down = False

    run()
    # showfps()
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
