'''
Created on 16 июн. 2020 г.

@author: Артем
'''
import pygame

class Button():
    def __init__(self,ai_settings,screen,msg,x,y):
        #Инициализирует атрибуты кнопки
        # Initialize button attributes
        self.screen = screen
        self.x = x
        self.y = y
        
        # Назначение размеров и свойств кнопок
        # Size and properties of buttons
        self.width,self.height = 400,100
        self.button_color = (30,30,30)
        self.text_color = (83,87,87)
        self.font = pygame.font.SysFont('AlundraText',48)
        
        # Находится ли мышка на кнопке(отрисовывает рамку)
        # Mouse on button?(draw the frame)
        self.frame = False
        self.active = False
        
        # Чтобы звук постоянно не проигрывался, когда навели мышку на кнопку
        # Counter of played sounds
        self.sound_count = 0
        
        # Построение объекта rect кнопки
        # Build the rect 
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        
        # Сообщение кнопки
        # Button message
        self.msg = msg
        self.prep_msg(msg)
    
    # Преобразует msg в прямоугольник и выравнивает текст по центру
    # Build the rect of message 
    def prep_msg(self,msg):
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    # Отображение пустой кнопки и вывод сообщения
    # Draw an empty button and output the msg 
    def draw_button(self,screen):
        if self.active:
            self.button_color = (100,100,100)
            self.screen.fill(self.button_color,self.rect)
            self.text_color = (220,220,220)
        else:
            self.button_color = (30,30,30)
            if self.frame:
                self.screen.fill(self.button_color,self.rect)
                pygame.draw.rect(screen,(210,210,210),(self.x,self.y,self.width,self.height),1)
                self.text_color = (220,220,220)
            else:
                self.screen.fill(self.button_color,self.rect)
                self.text_color = (83,87,87)
            
        self.screen.blit(self.msg_image,self.msg_image_rect)