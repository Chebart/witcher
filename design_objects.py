'''
Created on 27 июн. 2020 г.

@author: Артем
'''
import pygame

# Класс спрайта
# Sprite class
class Sprite():
    def __init__(self,x,y,filename):
        self.bitmap = pygame.image.load(filename)
        self.bitmap = self.bitmap.convert_alpha()
        self.rect = self.bitmap.get_rect()
        self.rect.x = x
        self.rect.y = y
         
    def render(self,screen):       
        screen.blit(self.bitmap,(self.rect.x,self.rect.y))