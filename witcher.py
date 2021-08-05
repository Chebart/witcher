'''
Created on 13 июн. 2020 г.

@author: Артем
'''

import pygame
from pygame.locals import *
from settings import Settings
from objects_main_menu import *
from button import Button
from animation import Animation
from button import Button
from slider import Slider
from design_objects import Sprite
import game_functions as gf


def run_game():
    #инициализирует игру и создаёт объект экрана
    #initialize the game and create the window
    
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                    ai_settings.screen_height),
                    pygame.FULLSCREEN | 
                    pygame.HWSURFACE | 
                    pygame.DOUBLEBUF)
    
    pygame.display.set_caption("The witcher3")
    
    # Музыка и звуки
    # Music and sounds
    sounds = []
    pygame.mixer.music.load('Main_Menu.mp3')
    main_menu_sound1 = pygame.mixer.Sound("main_menu_sound1.wav")
    main_menu_sound2 = pygame.mixer.Sound("main_menu_sound2.wav")

    sounds.append(main_menu_sound1)
    sounds.append(main_menu_sound2)
    
    # Анимация для главного меню
    # Main menu animation
    main_menu_animation = []
    add_animation(main_menu_animation)
    MAIN_MENU = Animation(main_menu_animation,950)
    
    #---------------------------------------------------------
    # Создаем кнопки для главного меню
    # Create buttons for main menu
    
    # кнопка "Играть"
    # "Play" button
    play_button = Button(ai_settings,screen,"Play",100,370)
    # кнопка "Новая игра"
    # "New game" button
    new_game_button = Button(ai_settings,screen,"New game",100,470)
    # кнопка "Загрузка"
    # "Load game" button
    load_button = Button(ai_settings,screen,"Load game",100,570)
    # кнопка "Настройки"
    # "Options" button
    settings_button = Button(ai_settings,screen,"Options",100,670)
    # кнопка "Выход из игры"
    # "Exit" button
    exit_button = Button(ai_settings,screen,"Exit",100,770)
    # кнопка "Звук"
    # "Audio" button
    audio_settings_button = Button(ai_settings,screen,"Audio",100,370)
    # кнопка "Привязка клавиш"
    # "Key bindings" button
    keys_settings_button = Button(ai_settings,screen,"Key bindings",100,470)
    # кнопка "Игровой процесс"
    # "Gameplay" button
    game_process_settings_button = Button(ai_settings,screen,"Gameplay",100,570)
    # кнопка "Видео"
    # "Video" button
    video_settings_button = Button(ai_settings,screen,"Video",100,670)
    # кнопка "Интерфейс"
    # "Interface" button
    interface_settings_button = Button(ai_settings,screen,"Interface",100,370)
    # кнопка "Качество графики"
    # "Graphics" button
    general_settings_button = Button(ai_settings,screen,"Graphics",100,470)
    # кнопка "Локализация"
    # "Language" button
    language_settings_button = Button(ai_settings,screen,"Language",100,770)
    # кнопка "Назад"
    # "Back" button
    back_button = Button(ai_settings,screen,"Back",100,870)
    # кнопка "Да"(Новая игра)
    # "Yes" button(New game)
    yes_button = Button(ai_settings,screen,"Yes",630,770)
    # кнопка "Нет"(Новая игра)
    # "No" button(New game)
    no_button = Button(ai_settings,screen,"No",1350,770)
    # кнопка 1 сложности(Новая игра)
    # First difficulty level button(New game)
    difficulty1_button = Button(ai_settings,screen,"Just the story",630,350)
    # кнопка 2 сложности(Новая игра)
    # Second difficulty level button(New game)
    difficulty2_button = Button(ai_settings,screen,"Story and sword",630,480)
    # кнопка 3 сложности(Новая игра)
    # Third difficulty level button(New game)
    difficulty3_button = Button(ai_settings,screen,"Blood and bones",1350,350)
    # кнопка 4 сложности(Новая игра)
    # Fourth difficulty level button(New game)
    difficulty4_button = Button(ai_settings,screen,"Death march",1350,480)
    # кнопка запуска новой игры(Новая игра)
    # Start new game button(New game)
    start_game_button = Button(ai_settings,screen,"Start",100,470)
    
    #-----------------------------------------------------
    # Специальные интерактивные объекты для настроек
    # Special interactive objects for options
    
    # Создаем слайдеры(вверх,вниз)
    # Make sliders(up,down)
    slider = Slider(ai_settings,screen,1799,243,19,60)
    # Создаем слайдеры(вправо,влево)
    # Make sliders(left,right)
    slider1 = Slider(ai_settings,screen,1292+int(ai_settings.music_volume)*3.96,306,60,27)
    slider2 = Slider(ai_settings,screen,1292+int(ai_settings.sound_volume)*3.96,456,60,27)
    slider3 = Slider(ai_settings,screen,1292+int(ai_settings.music_volume)*3.96,606,60,27)
    
    # Стрелки 
    # Arrows
    #1
    arrow_right1 = Sprite(1700,303,"arrow_right.png")
    arrow_left1 = Sprite(1420,303,"arrow_left.png")
    
    #2
    arrow_right2 = Sprite(1700,453,"arrow_right.png")
    arrow_left2 = Sprite(1420,453,"arrow_left.png")
    
    #3
    arrow_right3 = Sprite(1700,603,"arrow_right.png")
    arrow_left3 = Sprite(1420,603,"arrow_left.png")
    
    #4 
    arrow_right4 = Sprite(1640,749,"arrow_right.png")
    arrow_left4 = Sprite(1485,749,"arrow_left.png")
    
    #5
    arrow_right5 = Sprite(1645,304,"arrow_right.png")
    arrow_left5 = Sprite(1490,304,"arrow_left.png")
    
    #6
    arrow_right6 = Sprite(1695,454,"arrow_right.png")
    arrow_left6 = Sprite(1440,454,"arrow_left.png")
    
    #7
    arrow_right7 = Sprite(1695,604,"arrow_right.png")
    arrow_left7 = Sprite(1440,604,"arrow_left.png")
    
    #8
    arrow_right8 = Sprite(1695,1054,"arrow_right.png")
    arrow_left8 = Sprite(1440,1054,"arrow_left.png")
    
    gf.set_music_volume(ai_settings,slider1)
    gf.set_sound_volume(ai_settings,sounds,slider2)
    
    #запуск основного цикла
    #main cycle
    while True:
        
        # Отслеживание событий клавиатуры и мыши
        # Check input events
        gf.check_events(ai_settings,screen,play_button,new_game_button,load_button,
                        settings_button,exit_button,logo,back_button,
                        audio_settings_button,video_settings_button,language_settings_button,
                        keys_settings_button,game_process_settings_button,
                        interface_settings_button,general_settings_button,
                        yes_button,no_button,difficulty1_button,difficulty2_button,
                        difficulty3_button,difficulty4_button,start_game_button,
                        slider,arrow_left1,arrow_right1,arrow_left2,arrow_right2,
                        arrow_left3,arrow_right3,arrow_left4,arrow_right4,
                        arrow_left5,arrow_right5,arrow_left6,arrow_right6,
                        arrow_left7,arrow_right7,arrow_left8,arrow_right8,
                        main_menu_sound1, main_menu_sound2)
        
        # При каждом проходе цикла перерисовывается экран
        # Redraw the screen
        gf.update_screen(ai_settings,screen,MAIN_MENU,logo,play_button,new_game_button,load_button,settings_button,
                        exit_button,back_button,audio_settings_button,video_settings_button,
                        language_settings_button,keys_settings_button,
                        game_process_settings_button,interface_settings_button,
                        general_settings_button,
                        yes_button,no_button,
                        difficulty1_button,difficulty2_button,
                        difficulty3_button,difficulty4_button,
                        start_game_button,slider,slider1,
                        slider2,slider3,arrow_left1,arrow_right1,
                        arrow_left2,arrow_right2,arrow_left3,arrow_right3,
                        arrow_left4,arrow_right4,arrow_left5,arrow_right5,
                        arrow_left6,arrow_right6,arrow_left7,arrow_right7,
                        arrow_left8,arrow_right8,main_menu_sound1,sounds,
                        main_menu_animation[0])

run_game()
