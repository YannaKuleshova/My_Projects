#########################
#Author: Kuleshova Yana
#Date: 27/11/2021
#Task: HW_7_Pygame
#########################

import pygame
run = True
width = 400 # ширина игрового окна
height = 100 # высота игрового окна
pygame.init()
screen = pygame.display.set_mode ((width, height))
pygame.display.set_caption("My Game")
font = pygame.font.SysFont(None, 48)
text = font.reder('Welcome to pygame', True, (255.255,255))
screen.blit(text,((width - text.get_width())) // 2, (height - text.get_height()))
pygame.display.flip()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT\
        or event.type == pygame.MOUSEBUTTONUP\
        or event.type == pygame.KEYUP:
            run = False