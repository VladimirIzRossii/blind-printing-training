import pygame

pygame.font.init()
screen = pygame.display.set_mode((1600, 900))
font = pygame.font.Font('font/YandexSansDisplay-Light.ttf', 25)
text = font.render("You win!", True, (255, 255, 255))
text_rect = text.get_rect(center=(1600/2, 900/2))
while True:
    screen.blit(text, text_rect)
    pygame.display.flip()
