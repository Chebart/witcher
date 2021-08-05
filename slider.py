'''
Created on 27 июн. 2020 г.

@author: Артем
'''

import pygame

class Slider():
    def __init__(self,ai_settings,screen,x,y,width,height):
        #Инициализирует атрибуты слайдера
        # Initialize slider attributes
        self.screen = screen
        self.x = x
        self.y = y
        
        # Назначение размеров и свойств кнопок
        # Size and properties of sliders
        self.width,self.height = width,height
        self.button_color = (200,200,200)      
        
        # Построение объекта rect кнопки
        # Build the rect 
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        
       
    def draw_slider(self,screen):
        # Отображение ползунка
        # Draw the slider
        pygame.draw.rect(screen,(200,200,200),self.rect)
        