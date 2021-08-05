'''
Created on 13 июн. 2020 г.

@author: Артем
'''
from ctypes import *


class Settings():
    # Все основные настройки игры
    # All main settings of the game
    def __init__(self):
        #Параметры экрана
        # Window settings
        self.screen_width = windll.user32.GetSystemMetrics(0)
        self.screen_height = windll.user32.GetSystemMetrics(1)
        self.bg_color = (230,230,230)
        self.game_active = False
        
        # Основные параметры новой игры
        # Main new game settings
        self.difficulty = ['Just the story','Story and sword','Blood and broken bones','Death march']
        self.selected_difficulty = 1
        self.show_tutorial = ''
        
        # Параметры, связанные с игровым процессом
        # Gameplay settings
        self.advices = True
        self.death_blow = True
        self.witcher_vision = True
        self.auto_save = 10
        self.upgrade_enemy_level = True
        self.upgrade_enemy_level_gwent = ["easy","normal","hard"]
        self.upgrade_enemy_level_gwent_rus = ["легко","средне","сложно"]
        self.selected_level_gwent = 1
        
        # Параметры, связанные с настройками интерфейса
        # Interface settings
        self.interface = True
        self.action_log = True
        self.mini_map = True
        self.hidden_places = True
        self.explored_places = True
        self.active_task = True
        self.active_effect = True
        self.air = True
        self.damaged_things = True
        self.boss_hp = True
        self.enemy_hp = True
        self.herbs_labels = True
        self.boat_hp = True
        self.horse_anxiety = True
        self.horse_energy = True
        
        # Параметры, связанные с общими настройками
        # Graphics settings
        self.FPS = 60
        self.count_NPC = ["Low","Medium","High"]
        self.count_NPC_rus = ["Мало","Средне","Много"]
        self.count_plants = ["Low","Medium","High"]
        self.count_plants_rus = ["Мало","Средне","Много"]
        self.selected_count_NPC = 1
        self.selected_count_plants = 1
        
        # Параметры, связанные с языком,озвучкой,субтитрами
        # Language settings
        self.languages = ["Русский","English"]
        self.selected_language = 1
        self.selected_voice_language = 1
        self.selected_subtitles_language = 1
        
        # Параметры, связанные с музыкой,звуками и тд (аудио)
        # Audio settings
        self.music_volume = 50
        self.sound_volume = 25
        self.voice_volume = 60
        
        # Параметры, связанные с игровым меню и его кнопками
        # Main menu settings
        self.game_menu_active = False
        self.game_menu_settings_lvl1_active = False
        self.game_menu_settings_lvl2_active = False
        self.game_menu_settings_lvl3_active = False
        self.game_menu_settings_lvl4_active = False
        self.last_button = None
        
        # Параметры для слайдера (x и у)
        # Slider parametres
        self.slider_y = 243
        self.slider_move = 0

        #self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        pass
        
    def increase_speed(self):
        pass