import random
import os
import pygame
import math
import time

width = 1600
height = 900
const = height / 45
fps = 60
keyboard_margin_left = 18.25 * const
keyboard_margin_top = 25 * const
keykup_size = 2.5 * const
keycap_range = 0.25 * const
dark_color = (30, 30, 30)
bright_color = (230, 230, 230)
# background_color = dark_color
# keyboard_color = bright_color
# second_keyboard_color = dark_color
pygame.init()
pygame.font.init()
font = pygame.font.Font('font/YandexSansDisplay-Light.ttf', round(0.8 * const))
font1 = pygame.font.Font('font/YandexSansDisplay-Light.ttf', round(2.5 * const))
screen = pygame.display.set_mode((width, height))
click = False
layout = 'en'
resolution = '900p'
dark_theme = True
fullscreen = False
printed_text = ''
input_active = True
globalt = 0

keys_en = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'backspace', 'tab', 'Q', 'W', 'E', 'R',
           'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\', 'caps', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'",
           'enter', 'shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'shift', 'ctrl', 'win', 'alt', 'space',
           'alt', 'fn', 'some', 'ctrl']
keys_en_sh = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'backspace', 'tab', 'Q', 'W', 'E', 'R',
              'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|', 'caps', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':',
              '"', 'enter', 'shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?', 'shift', 'ctrl', 'win', 'alt',
              'space', 'alt', 'fn', 'some', 'ctrl']
keys_ru = ['Ё', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'backspace', 'tab', 'Й', 'Ц', 'У', 'К', 'Е',
           'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ', '\\', 'caps', 'Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж', 'Э',
           'enter', 'shift', 'Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю', '.', 'shift', 'ctrl', 'win', 'alt', 'space',
           'alt', 'fn', 'some', 'ctrl']
keys_ru_sh = ['Ё', '!', '"', '№', ';', '%', ':', '?', '*', '(', ')', '_', '+', 'backspace', 'tab', 'Й', 'Ц', 'У', 'К',
              'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ', '/', 'caps', 'Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж',
              'Э', 'enter', 'shift', 'Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю', ',', 'shift', 'ctrl', 'win', 'alt',
              'space', 'alt', 'fn', 'some', 'ctrl']
clock = pygame.time.Clock()


def upd():
    global keyboard_recs, screen, const, width, height, keyboard_margin_top, keyboard_margin_left, keykup_size, \
        keycap_range, font, font1, font2, tx, tx1, tx2, printed_text_rect
    const = height / 45
    keyboard_margin_left = 19.375 * const
    keyboard_margin_top = 25 * const
    keykup_size = 2.5 * const
    keycap_range = 0.25 * const
    tumbler_rect = pygame.Rect(10 * const * 1.05 + 60 * const * 0.8 + (11 * const * 1.05 - 11 * const),
                               11 * const * 1.05,
                               60 * const - 60 * const * 0.8 - const * 1.05 - (11 * const * 1.05 - 11 * const),
                               5 * const * 0.8)
    tx1 = tumbler_rect.right - 3.5 * const
    tx2 = tumbler_rect.left + 3.5 * const
    tx = tx1
    font = pygame.font.Font('font/YandexSansDisplay-Light.ttf', round(0.8 * const))
    font1 = pygame.font.Font('font/YandexSansDisplay-Light.ttf', round(2.5 * const))
    font2 = pygame.font.Font('font/YandexSansDisplay-Light.ttf', round(2.5 * const))
    if fullscreen:
        screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((width, height))
    keyboard_recs = [pygame.Rect(keyboard_margin_left, keyboard_margin_top, keykup_size, keykup_size),
                     pygame.Rect((keykup_size + keycap_range) * 1 + keyboard_margin_left, keyboard_margin_top,
                                 keykup_size,
                                 keykup_size),
                     pygame.Rect((keykup_size + keycap_range) * 2 + keyboard_margin_left, keyboard_margin_top,
                                 keykup_size,
                                 keykup_size),
                     pygame.Rect((keykup_size + keycap_range) * 3 + keyboard_margin_left, keyboard_margin_top,
                                 keykup_size,
                                 keykup_size),
                     pygame.Rect((keykup_size + keycap_range) * 4 + keyboard_margin_left, keyboard_margin_top,
                                 keykup_size,
                                 keykup_size),
                     pygame.Rect((keykup_size + keycap_range) * 5 + keyboard_margin_left, keyboard_margin_top,
                                 keykup_size,
                                 keykup_size),
                     pygame.Rect((keykup_size + keycap_range) * 6 + keyboard_margin_left, keyboard_margin_top,
                                 keykup_size,
                                 keykup_size),
                     pygame.Rect((keykup_size + keycap_range) * 7 + keyboard_margin_left, keyboard_margin_top,
                                 keykup_size,
                                 keykup_size),
                     pygame.Rect((keykup_size + keycap_range) * 8 + keyboard_margin_left, keyboard_margin_top,
                                 keykup_size,
                                 keykup_size),
                     pygame.Rect((keykup_size + keycap_range) * 9 + keyboard_margin_left, keyboard_margin_top,
                                 keykup_size,
                                 keykup_size),
                     pygame.Rect((keykup_size + keycap_range) * 10 + keyboard_margin_left, keyboard_margin_top,
                                 keykup_size,
                                 keykup_size),
                     pygame.Rect((keykup_size + keycap_range) * 11 + keyboard_margin_left, keyboard_margin_top,
                                 keykup_size,
                                 keykup_size),
                     pygame.Rect((keykup_size + keycap_range) * 12 + keyboard_margin_left, keyboard_margin_top,
                                 keykup_size,
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
                                 keyboard_margin_top + (keycap_range + keykup_size) * 2,
                                 2.2 * keykup_size + keycap_range,
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
                                 keyboard_margin_top + (keycap_range + keykup_size) * 3, 2.6 * keykup_size,
                                 keykup_size),

                     pygame.Rect(keyboard_margin_left, keyboard_margin_top + (keycap_range + keykup_size) * 4,
                                 1.2 * keykup_size, keykup_size),
                     pygame.Rect(keyboard_margin_left + 1.2 * keykup_size + keycap_range,
                                 keyboard_margin_top + (keycap_range + keykup_size) * 4, 1.2 * keykup_size,
                                 keykup_size),
                     pygame.Rect(keyboard_margin_left + (1.2 * keykup_size + keycap_range) * 2,
                                 keyboard_margin_top + (keycap_range + keykup_size) * 4, 1.2 * keykup_size,
                                 keykup_size),
                     pygame.Rect(keyboard_margin_left + (1.2 * keykup_size + keycap_range) * 3,
                                 keyboard_margin_top + (keycap_range + keykup_size) * 4,
                                 7 * keykup_size + 2 * keycap_range,
                                 keykup_size),
                     pygame.Rect(
                         keyboard_margin_left + (1.2 * keykup_size) * 3 + keycap_range * 4 + keykup_size * 7 + 2 *
                         keycap_range,
                         keyboard_margin_top + (keycap_range + keykup_size) * 4, 1.2 * keykup_size, keykup_size),
                     pygame.Rect(
                         keyboard_margin_left + (1.2 * keykup_size) * 4 + keycap_range * 5 + keykup_size * 7 + 2 *
                         keycap_range,
                         keyboard_margin_top + (keycap_range + keykup_size) * 4, 1.2 * keykup_size, keykup_size),
                     pygame.Rect(
                         keyboard_margin_left + (1.2 * keykup_size) * 5 + keycap_range * 6 + keykup_size * 7 + 2 *
                         keycap_range,
                         keyboard_margin_top + (keycap_range + keykup_size) * 4, 1.2 * keykup_size, keykup_size),
                     pygame.Rect(
                         keyboard_margin_left + (1.2 * keykup_size) * 6 + keycap_range * 7 + keykup_size * 7 + 2 *
                         keycap_range,
                         keyboard_margin_top + (keycap_range + keykup_size) * 4, 1.2 * keykup_size, keykup_size),
                     ]
    board_rect = pygame.Rect(keyboard_recs[0].left - keycap_range, keyboard_recs[0].top - keycap_range,
                             keyboard_recs[-1].right - keyboard_recs[0].left + 2 * keycap_range,
                             5 * keykup_size + keycap_range * 6)
    printed_text_rect = pygame.Rect(12 * const, 0,  width - 24 * const, board_rect.top)


upd()


class Player:
    def __init__(self, money):
        self.money = money

    def money(self):
        return self.money


def settings():
    global running, layout, dark_color, bright_color, dark_theme, resolution, screen, const, width, height, \
        keyboard_margin_top, keyboard_margin_left, keykup_size, keycap_range, fullscreen, tx
    setting = True
    click = False
    velocity = 180
    tvelocity = 360
    change_theme = False
    while setting:
        screen.fill(dark_color)
        settings_button = pygame.Rect(0.5 * const, 0.5 * const, 2 * const, 2 * const)
        pygame.draw.rect(screen, bright_color, settings_button, 1, int(const / 6))
        text = font.render('back', True, bright_color)
        text_rect = text.get_rect(center=settings_button.center)
        screen.blit(text, text_rect)

        rct = pygame.Rect(width / 2, 5 * const, 0, 0)
        text = font1.render('SETTINGS', True, bright_color)
        text_rect = text.get_rect(center=rct.center)
        screen.blit(text, text_rect)

        theme_button = pygame.Rect(10 * const, 11 * const, 60 * const, 5 * const)
        theme_text = pygame.Rect(10 * const * 1.05, 11 * const * 1.05, 60 * const * 0.8, 5 * const * 0.8)
        tumbler = pygame.Rect(10 * const * 1.05 + 60 * const * 0.8 + (11 * const * 1.05 - 11 * const) +
                              (60 * const - 60 * const * 0.8 - const * 1.05 - (11 * const * 1.05 - 11 * const)) * 0.2,
                              11 * const * 1.05 + 5 * const * 0.8 * 0.2,
                              (60 * const - 60 * const * 0.8 - const * 1.05 - (11 * const * 1.05 - 11 * const)) * 0.6,
                              5 * const * 0.8 * 0.6)
        tumbler1 = pygame.Rect(10 * const * 1.05 + 60 * const * 0.8 + (11 * const * 1.05 - 11 * const) +
                               (60 * const - 60 * const * 0.8 - const * 1.05 - (11 * const * 1.05 - 11 * const)) * 0.2,
                               11 * const * 1.05 + 5 * const * 0.8 * 0.2,
                               tx - (10 * const * 1.05 + 60 * const * 0.8 + (11 * const * 1.05 - 11 * const) +
                                     (60 * const - 60 * const * 0.8 - const * 1.05 - (
                                             11 * const * 1.05 - 11 * const)) * 0.2) + 0.25 * const + 1.25 * const,
                               5 * const * 0.8 * 0.6)
        pygame.draw.rect(screen, (150, 0, 0), tumbler, 0, int(1000 * const))
        pygame.draw.rect(screen, (0, 150, 0), tumbler1, 0, int(1000 * const))
        text = font1.render('Dark theme', True, bright_color)
        text_rect = text.get_rect(center=theme_text.center)
        screen.blit(text, (theme_text.left, text_rect[1]))
        # pygame.draw.rect(screen, bright_color, theme_button, 1)
        pygame.draw.circle(screen, (120, 120, 120), (tx, tumbler.centery),
                           1.5 * const, 0)

        layout_button = pygame.Rect(10 * const, 17.5 * const, 60 * const, 5 * const)
        layout_text = pygame.Rect(10 * const * 1.05, 17.5 * const * 1.03, 60 * const * 0.8, 5 * const * 0.8)
        language_rect = pygame.Rect(10 * const * 1.05 + 60 * const * 0.8 + (11 * const * 1.05 - 11 * const),
                                    17.5 * const * 1.03,
                                    60 * const - 60 * const * 0.8 - const * 1.05 - (11 * const * 1.05 - 11 * const),
                                    5 * const * 0.8)
        # pygame.draw.rect(screen, bright_color, layout_text, 1)
        pygame.draw.rect(screen, bright_color, language_rect, 1)
        text = font1.render('Layout', True, bright_color)
        text_rect = text.get_rect(center=layout_text.center)
        screen.blit(text, (layout_text.left, text_rect[1]))
        text = font1.render(layout.upper(), True, bright_color)
        text_rect = text.get_rect(center=language_rect.center)
        screen.blit(text, text_rect)
        # pygame.draw.rect(screen, bright_color, layout_button, 1)

        resolution_button = pygame.Rect(10 * const, 24 * const, 60 * const, 5 * const)
        resolution_text = pygame.Rect(10 * const * 1.05, 24 * const * 1.02, 60 * const * 0.8, 5 * const * 0.8)
        resolution_rect = pygame.Rect(10 * const * 1.05 + 60 * const * 0.8 + (11 * const * 1.05 - 11 * const),
                                      24 * const * 1.02,
                                      60 * const - 60 * const * 0.8 - const * 1.05 - (11 * const * 1.05 - 11 * const),
                                      5 * const * 0.8)
        # pygame.draw.rect(screen, bright_color, resolution_text, 1)
        pygame.draw.rect(screen, bright_color, resolution_rect, 1)
        text = font1.render('Resolution', True, bright_color)
        text_rect = text.get_rect(center=resolution_text.center)
        screen.blit(text, (layout_text.left, text_rect[1]))
        text = font1.render(resolution, True, bright_color)
        text_rect = text.get_rect(center=resolution_rect.center)
        screen.blit(text, text_rect)
        # pygame.draw.rect(screen, bright_color, resolution_button, 1)

        fullscreen_button = pygame.Rect(10 * const, 30.5 * const, 60 * const, 5 * const)
        theme_text = pygame.Rect(10 * const * 1.05, 30.5 * const * 1.015, 60 * const * 0.8, 5 * const * 0.8)
        tumbler_rect = pygame.Rect(10 * const * 1.05 + 60 * const * 0.8 + (11 * const * 1.05 - 11 * const),
                                   30.5 * const * 1.015,
                                   60 * const - 60 * const * 0.8 - const * 1.05 - (11 * const * 1.05 - 11 * const),
                                   5 * const * 0.8)
        tumbler1 = pygame.Rect(10 * const * 1.05 + 60 * const * 0.8 + (11 * const * 1.05 - 11 * const) +
                               (60 * const - 60 * const * 0.8 - const * 1.05 - (11 * const * 1.05 - 11 * const)) * 0.2,
                               (11 * const * 1.05 + 5 * const * 0.8 * 0.2) * 2.57,
                               (60 * const - 60 * const * 0.8 - const * 1.05 - (11 * const * 1.05 - 11 * const)) * 0.6,
                               5 * const * 0.8 * 0.6)
        if fullscreen:
            pygame.draw.rect(screen, (0, 150, 0), tumbler1, 0, int(1000 * const))
            pygame.draw.circle(screen, (120, 120, 120), (tumbler_rect.right - 3.5 * const, tumbler1.centery),
                               1.5 * const, 0)
        else:
            pygame.draw.rect(screen, (150, 0, 0), tumbler1, 0, int(1000 * const))
            pygame.draw.circle(screen, (120, 120, 120), (tumbler_rect.left + 3.5 * const, tumbler1.centery),
                               1.5 * const, 0)
        text = font1.render('Fullscreen', True, bright_color)
        text_rect = text.get_rect(center=theme_text.center)
        screen.blit(text, (theme_text.left, text_rect[1]))
        # pygame.draw.rect(screen, bright_color, fullscreen_button, 1)

        pygame.draw.line(screen, bright_color, (theme_button.left,
                                                theme_button.top - (layout_button.top - theme_button.bottom) / 2,),
                         (theme_button.right, theme_button.top - (layout_button.top - theme_button.bottom) / 2))
        pygame.draw.line(screen, bright_color, (theme_button.left,
                                                theme_button.bottom + (layout_button.top - theme_button.bottom) / 2,),
                         (theme_button.right, theme_button.bottom + (layout_button.top - theme_button.bottom) / 2))
        pygame.draw.line(screen, bright_color, (theme_button.left,
                                                layout_button.bottom + (layout_button.top - theme_button.bottom) / 2,),
                         (theme_button.right, layout_button.bottom + (layout_button.top - theme_button.bottom) / 2))
        pygame.draw.line(screen, bright_color, (theme_button.left,
                                                resolution_button.bottom +
                                                (layout_button.top - theme_button.bottom) / 2,),
                         (theme_button.right, resolution_button.bottom + (layout_button.top - theme_button.bottom) / 2))
        pygame.draw.line(screen, bright_color, (theme_button.left,
                                                fullscreen_button.bottom +
                                                (layout_button.top - theme_button.bottom) / 2,),
                         (theme_button.right, fullscreen_button.bottom + (layout_button.top - theme_button.bottom) / 2))

        if settings_button.collidepoint(pygame.mouse.get_pos()) and click:
            setting = False
        if layout_button.collidepoint(pygame.mouse.get_pos()) and click:
            if layout == 'en':
                layout = 'ru'
            elif layout == 'ru':
                layout = 'en'
            click = False
        if theme_button.collidepoint(pygame.mouse.get_pos()) and click:
            if dark_theme:
                dark_theme = False
            else:
                dark_theme = True
            # dark_color, bright_color = bright_color, dark_color
            click = False
            change_theme = True
        if fullscreen_button.collidepoint(pygame.mouse.get_pos()) and click:
            fullscreen = not fullscreen
            click = False
            upd()
        if resolution_button.collidepoint(pygame.mouse.get_pos()) and click:
            if resolution == '900p':
                resolution = '1080p'
                width, height = 1920, 1080
            elif resolution == '1080p':
                resolution = '720p'
                width, height = 1280, 720
            elif resolution == '720p':
                resolution = '900p'
                width, height = 1600, 900
            click = False
            upd()
        if change_theme:
            if dark_theme:
                if dark_color[0] > 30:
                    x = dark_color[0] - velocity / fps
                    dark_color = (x, x, x)
                    x = bright_color[0] + velocity / fps
                    bright_color = (x, x, x)
                if tx < tx1:
                    tx += tvelocity / fps
            else:
                if dark_color[0] < 230:
                    x = dark_color[0] + velocity / fps
                    dark_color = (x, x, x)
                    x = bright_color[0] - velocity / fps
                    bright_color = (x, x, x)
                if tx > tx2:
                    tx -= tvelocity / fps

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    setting = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False
            if event.type == pygame.QUIT:
                setting = False
                running = False
        pygame.display.update()
        clock.tick(fps)


def ui():
    global click
    settings_button = pygame.Rect(0.5 * const, 0.5 * const, 2 * const, 2 * const)
    pygame.draw.rect(screen, bright_color, settings_button, 1, int(const / 6))
    text = font.render('settings', True, bright_color)
    text_rect = text.get_rect(center=settings_button.center)
    screen.blit(text, text_rect)
    if settings_button.collidepoint(pygame.mouse.get_pos()) and click:
        click = False
        settings()


def print_keyboard(key_pressed):
    global board_rect
    # pygame.draw.rect(screen, (255, 255, 255), [50, 400, 1500, 450], 1)
    for keycup in keyboard_recs:
        pygame.draw.rect(screen, bright_color, keycup, 1, int(const / 6))
    if key_pressed:
        for key in key_pressed:
            pygame.draw.rect(screen, bright_color, keyboard_recs[key - 1], 0, int(const / 6))
    board_rect = pygame.Rect(keyboard_recs[0].left - keycap_range, keyboard_recs[0].top - keycap_range,
                             keyboard_recs[-1].right - keyboard_recs[0].left + 2 * keycap_range,
                             5 * keykup_size + keycap_range * 6)
    pygame.draw.rect(screen, bright_color, board_rect, 1)


def print_values(key_pressed):
    t = 0
    if layout == 'en':
        if 43 in key_pressed or 53 in key_pressed:
            keys = keys_en_sh
        else:
            keys = keys_en
    elif layout == 'ru':
        if 43 in key_pressed or 53 in key_pressed:
            keys = keys_ru_sh
        else:
            keys = keys_ru
    for keycup in keyboard_recs:
        text = font.render(keys[t], True, bright_color)
        text_rect = text.get_rect(center=keycup.center)
        screen.blit(text, text_rect)
        t += 1
    if key_pressed:
        for key in key_pressed:
            text = font.render(keys[key - 1], True, dark_color)
            text_rect = text.get_rect(center=keyboard_recs[key - 1].center)
            screen.blit(text, text_rect)


def print_text():
    global printed_text, globalt
    text_input = printed_text.split('\n')
    t = 0
    globalt += 1
    if globalt <= 50:
        text_input[-1] += '|'
    elif globalt == 100:
        globalt = 0
    for i in range(len(text_input)):
        x = int(len(text_input)) / 2 - i
        text = font2.render(text_input[i], True, bright_color)
        text_rect = text.get_rect(center=printed_text_rect.center)
        screen.blit(text, (printed_text_rect.left, text_rect[1] - x * (text_rect[1] - printed_text_rect.centery)))
        if text.get_rect().width >= printed_text_rect.width and text_input[i] == text_input[-1]:
            printed_text += '\n'
        t += 1
    pygame.draw.line(screen, bright_color, (printed_text_rect.left, printed_text_rect.centery),
                     (printed_text_rect.right, printed_text_rect.centery), 1)


def run():
    ui()
    print_keyboard(key_presed)
    print_values(key_presed)
    print_text()


# crosshair = Crosshair()
running = True
last_time = time.time()
key_presed = []

while running:
    # pygame.mouse.set_visible(False)
    screen.fill(dark_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                click = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKQUOTE:
                key_presed.append(1)
            if event.key == pygame.K_1:
                key_presed.append(2)
            if event.key == pygame.K_2:
                key_presed.append(3)
            if event.key == pygame.K_3:
                key_presed.append(4)
            if event.key == pygame.K_4:
                key_presed.append(5)
            if event.key == pygame.K_5:
                key_presed.append(6)
            if event.key == pygame.K_6:
                key_presed.append(7)
            if event.key == pygame.K_7:
                key_presed.append(8)
            if event.key == pygame.K_8:
                key_presed.append(9)
            if event.key == pygame.K_9:
                key_presed.append(10)
            if event.key == pygame.K_0:
                key_presed.append(11)
            if event.key == pygame.K_MINUS:
                key_presed.append(12)
            if event.key == pygame.K_EQUALS:
                key_presed.append(13)
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
            if event.key == pygame.K_QUOTE:
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
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                key_presed.append(42)
                key_presed.append(53)
            if event.key == pygame.K_BACKSPACE:
                key_presed.append(14)
                if printed_text[-1] != '\n':
                    printed_text = printed_text[:-1]
                else:
                    printed_text = printed_text[:-2]
            elif input_active:
                printed_text += event.unicode
        if event.type == pygame.KEYUP:
            # key_presed = 0
            if event.key == pygame.K_BACKQUOTE:
                key_presed.remove(1)
            if event.key == pygame.K_1:
                key_presed.remove(2)
            if event.key == pygame.K_2:
                key_presed.remove(3)
            if event.key == pygame.K_3:
                key_presed.remove(4)
            if event.key == pygame.K_4:
                key_presed.remove(5)
            if event.key == pygame.K_5:
                key_presed.remove(6)
            if event.key == pygame.K_6:
                key_presed.remove(7)
            if event.key == pygame.K_7:
                key_presed.remove(8)
            if event.key == pygame.K_8:
                key_presed.remove(9)
            if event.key == pygame.K_9:
                key_presed.remove(10)
            if event.key == pygame.K_0:
                key_presed.remove(11)
            if event.key == pygame.K_MINUS:
                key_presed.remove(12)
            if event.key == pygame.K_EQUALS:
                key_presed.remove(13)
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
            if event.key == pygame.K_QUOTE:
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
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                key_presed.remove(42)
                key_presed.remove(53)
            if event.key == pygame.K_BACKSPACE:
                key_presed.remove(14)

    run()
    # showfps()
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
