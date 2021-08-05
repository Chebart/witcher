'''
Created on 4 июл. 2020 г.

@author: Артем
'''
import pygame

# Текстура логотипа
# Logo texture
logo = pygame.image.load("logo.png")

# Текстуры для анимации
# Textures for animation
def add_animation(animation):
    for i in range(1,33):
        img = pygame.image.load("main_menu"+str(i)+".png")
        animation.append(img)
