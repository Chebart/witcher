'''
Created on 4 июл. 2020 г.

@author: Артем
'''
import pygame
import sys
        
# Проверка нажатия кнопки "Играть"
# "Play" button click test
def check_play_button(ai_settings,play_button,button_clicked=False,sound1=None,sound2=None):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button = play_button.rect.collidepoint(mouse_x,mouse_y)
        
    if button_clicked and mouse_on_button:
        sound2.play()
        ai_settings.game_active = True
    else:
        if mouse_on_button:
            play_button.frame = True
            play_button.prep_msg(play_button.msg)
        
            if play_button.sound_count < 1:
                sound1.play()
                play_button.sound_count += 1
        else:
            play_button.frame = False
            play_button.prep_msg(play_button.msg)
            play_button.sound_count = 0


# Проверка нажатия кнопки "Новая игра"
# "New game" button click test
def check_new_game_button(ai_settings,screen,new_game_button,difficulty1_button,difficulty2_button,difficulty3_button,difficulty4_button,
                          yes_button,no_button,logo=None,button_clicked=False,draw_menu=False,sound1=None,sound2=None):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button = new_game_button.rect.collidepoint(mouse_x,mouse_y)

    if button_clicked and mouse_on_button:
        difficulty1_button.active=False
        difficulty2_button.active=False
        difficulty3_button.active=False
        difficulty4_button.active=False
        yes_button.active = False
        no_button.active = False
        sound2.play()
        draw_menu = True
        ai_settings.slider_move = 0
    else:
        if mouse_on_button:
            new_game_button.frame = True
            new_game_button.prep_msg(new_game_button.msg)
        
            if new_game_button.sound_count < 1:
                sound1.play()
                new_game_button.sound_count += 1
        else:
            new_game_button.frame = False
            new_game_button.prep_msg(new_game_button.msg)
            new_game_button.sound_count = 0
            
    draw_new_game_menu(ai_settings,screen,logo,draw_menu)

# Отрисовка меню Новой игры
# Draw "New game" button menu
def draw_new_game_menu(ai_settings,screen,logo=None,draw_menu=False):
    
    if draw_menu:
        ai_settings.game_menu_active = True
        ai_settings.game_menu_settings_lvl1_active = True
        ai_settings.last_button = "new_game"
        
        screen.fill((30,30,30))
        
        pygame.draw.rect(screen,(35,35,35),(590,240,1200,755))
        pygame.draw.rect(screen,(40,40,40),(590,240,1200,755),3)

        pygame.draw.line(screen,(40,40,40),[590,618],[1790,618],3)
        
        font = pygame.font.SysFont('AlundraText',52)
        if ai_settings.selected_language==0:
            text = font.render("Уровень сложности",True,(220,220,220))
            screen.blit(text,(1000,270))
            
            text = font.render("Пройти обучение",True,(220,220,220))
            screen.blit(text,(1000,650))
        else:
            text = font.render("Difficulty level",True,(220,220,220))
            screen.blit(text,(1030,270))
          
            text = font.render("Show tutorial",True,(220,220,220))
            screen.blit(text,(1035,650))           

    
        screen.blit(logo,(100,80))

# Проверка нажатия кнопки "Да"
# "yes" button click test
def check_load_game_yes_button(ai_settings,yes_button,no_button,button_clicked=False,sound1=None,sound2=None):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button = yes_button.rect.collidepoint(mouse_x,mouse_y)
    
    if button_clicked and mouse_on_button:
        yes_button.active = True
        no_button.active = False
        yes_button.prep_msg(yes_button.msg)
        no_button.prep_msg(no_button.msg)
        sound2.play()
        ai_settings.show_tutorial='yes'
    else:
        if mouse_on_button:
            yes_button.frame = True
            yes_button.prep_msg(yes_button.msg)
        
            if yes_button.sound_count < 1:
                sound1.play()
                yes_button.sound_count += 1
            
        else:
            yes_button.frame = False
            yes_button.prep_msg(yes_button.msg)
            yes_button.sound_count = 0
            
# Проверка нажатия кнопки "нет"
# "no" button click test   
def check_load_game_no_button(ai_settings,no_button,yes_button,button_clicked=False,sound1=None,sound2=None):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button = no_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and mouse_on_button:
        no_button.active = True
        yes_button.active = False
        no_button.prep_msg(no_button.msg)
        yes_button.prep_msg(yes_button.msg)
        sound2.play()
        ai_settings.show_tutorial='no'
    else:
        if mouse_on_button:
            no_button.frame = True
            no_button.prep_msg(no_button.msg)
        
            if no_button.sound_count < 1:
                sound1.play()
                no_button.sound_count += 1
            
        else:
            no_button.frame = False
            no_button.prep_msg(no_button.msg)
            no_button.sound_count = 0
    
# Проверка нажатия кнопки 1сложности
# "Just the story" button click test
def check_load_game_difficulty1_button(ai_settings,screen,difficulty1_button,difficulty2_button,difficulty3_button,difficulty4_button,
                                        button_clicked=False,sound1=None,sound2=None):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button = difficulty1_button.rect.collidepoint(mouse_x,mouse_y)
    
    if button_clicked and mouse_on_button:
        difficulty1_button.active = True
        difficulty2_button.active = False
        difficulty3_button.active = False
        difficulty4_button.active = False
        
        difficulty1_button.prep_msg(difficulty1_button.msg)
        difficulty2_button.prep_msg(difficulty2_button.msg)
        difficulty3_button.prep_msg(difficulty3_button.msg)
        difficulty4_button.prep_msg(difficulty4_button.msg)
        
        sound2.play()
        ai_settings.selected_difficulty = 0
    else:
        if mouse_on_button:
            difficulty1_button.frame = True
            difficulty1_button.prep_msg(difficulty1_button.msg)
        
            if difficulty1_button.sound_count < 1:
                sound1.play()
                difficulty1_button.sound_count += 1
            font = pygame.font.SysFont('AlundraText',33)
            if ai_settings.selected_language==0:
                text = font.render('Для тех,кто не хочет',True,(220,220,220))
                screen.blit(text,(155,790))

                text = font.render('отвлекаться на врагов',True,(220,220,220))
                screen.blit(text,(135,840))
            else:
                text = font.render('Enjoy a smooth ride',True,(220,220,220))
                screen.blit(text,(165,790))

                text = font.render('through the world',True,(220,220,220))
                screen.blit(text,(175,840))
            
        else:
            difficulty1_button.frame = False
            difficulty1_button.prep_msg(difficulty1_button.msg)
            difficulty1_button.sound_count = 0

# Проверка нажатия кнопки 2сложности
# "Story and sword" button click test      
def check_load_game_difficulty2_button(ai_settings,screen,difficulty1_button,difficulty2_button,difficulty3_button,difficulty4_button,
                                       button_clicked=False,sound1=None,sound2=None):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button = difficulty2_button.rect.collidepoint(mouse_x,mouse_y)
    
    if button_clicked and mouse_on_button:
        difficulty2_button.active = True
        difficulty1_button.active = False
        difficulty3_button.active = False
        difficulty4_button.active = False
        
        difficulty2_button.prep_msg(difficulty2_button.msg)
        difficulty1_button.prep_msg(difficulty1_button.msg)
        difficulty3_button.prep_msg(difficulty3_button.msg)
        difficulty4_button.prep_msg(difficulty4_button.msg)
        
        sound2.play()
        ai_settings.selected_difficulty = 1
    else:
        if mouse_on_button:
            difficulty2_button.frame = True
            difficulty2_button.prep_msg(difficulty2_button.msg)
        
            if difficulty2_button.sound_count < 1:
                sound1.play()
                difficulty2_button.sound_count += 1
            font = pygame.font.SysFont('AlundraText',33)
            if ai_settings.selected_language==0: 
                text = font.render('Для тех,кто не любит',True,(220,220,220))
                screen.blit(text,(155,790))
                text = font.render('простых решений',True,(220,220,220))
                screen.blit(text,(175,840))
            else:
                text = font.render('You`re happy',True,(220,220,220))
                screen.blit(text,(205,790))
                text = font.render('to be challenged',True,(220,220,220))
                screen.blit(text,(188,840))  
            
        else:
            difficulty2_button.frame = False
            difficulty2_button.prep_msg(difficulty2_button.msg)
            difficulty2_button.sound_count = 0
    
# Проверка нажатия кнопки 3сложности
# "Blood and bones" button click test    
def check_load_game_difficulty3_button(ai_settings,screen,difficulty1_button,difficulty2_button,difficulty3_button,difficulty4_button,
                                       button_clicked=False,sound1=None,sound2=None):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button = difficulty3_button.rect.collidepoint(mouse_x,mouse_y)
    
    if button_clicked and mouse_on_button:
        difficulty3_button.active = True
        difficulty1_button.active = False
        difficulty2_button.active = False
        difficulty4_button.active = False
        
        difficulty3_button.prep_msg(difficulty3_button.msg)
        difficulty1_button.prep_msg(difficulty1_button.msg)
        difficulty2_button.prep_msg(difficulty2_button.msg)
        difficulty4_button.prep_msg(difficulty4_button.msg)
        
        sound2.play()
        ai_settings.selected_difficulty = 2
    else:
        if mouse_on_button:
            difficulty3_button.frame = True
            difficulty3_button.prep_msg(difficulty3_button.msg)
        
            if difficulty3_button.sound_count < 1:
                sound1.play()
                difficulty3_button.sound_count += 1
            font = pygame.font.SysFont('AlundraText',33)
            if ai_settings.selected_language==0: 
                text = font.render('Для закаленных',True,(220,220,220))
                screen.blit(text,(185,790))
                text = font.render('в боях игроков',True,(220,220,220))
                screen.blit(text,(195,840))
            else:
                text = font.render('You`re a seasoned',True,(220,220,220))
                screen.blit(text,(175,790))
                text = font.render('demanding gamer',True,(220,220,220))
                screen.blit(text,(175,840))
            
        else:
            difficulty3_button.frame = False
            difficulty3_button.prep_msg(difficulty3_button.msg)
            difficulty3_button.sound_count = 0

# Проверка нажатия кнопки 4сложности
# "Death march" button click test 
def check_load_game_difficulty4_button(ai_settings,screen,difficulty1_button,difficulty2_button,difficulty3_button,difficulty4_button,
                                       button_clicked=False,sound1=None,sound2=None):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button = difficulty4_button.rect.collidepoint(mouse_x,mouse_y)
    
    if button_clicked and mouse_on_button:
        difficulty4_button.active = True
        difficulty1_button.active = False
        difficulty2_button.active = False
        difficulty3_button.active = False
        
        difficulty4_button.prep_msg(difficulty4_button.msg)
        difficulty1_button.prep_msg(difficulty1_button.msg)
        difficulty2_button.prep_msg(difficulty2_button.msg)
        difficulty3_button.prep_msg(difficulty3_button.msg)
        
        sound2.play()
        ai_settings.selected_difficulty = 3
    else:
        if mouse_on_button:
            difficulty4_button.frame = True
            difficulty4_button.prep_msg(difficulty4_button.msg)
        
            if difficulty4_button.sound_count < 1:
                sound1.play()
                difficulty4_button.sound_count += 1
            font = pygame.font.SysFont('AlundraText',33)
            if ai_settings.selected_language==0: 
                text = font.render('Для настоящих',True,(220,220,220))
                screen.blit(text,(185,790))
                text = font.render('безумцев',True,(220,220,220))
                screen.blit(text,(225,840))
            else:
                text = font.render('You`re truly insane',True,(220,220,220))
                screen.blit(text,(175,790))
                text = font.render('and loving it',True,(220,220,220))
                screen.blit(text,(215,840))
            
        else:
            difficulty4_button.frame = False
            difficulty4_button.prep_msg(difficulty4_button.msg)
            difficulty4_button.sound_count = 0
            
# Проверка нажатия кнопки старта игры
# Start game button click test 
def check_load_game_start_game_button(ai_settings,start_game_button,difficulty1_button,difficulty2_button,difficulty3_button,
                                      difficulty4_button,yes_button,no_button,button_clicked=False,sound1=None,sound2=None):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button = start_game_button.rect.collidepoint(mouse_x,mouse_y)
    
    if button_clicked and mouse_on_button and (difficulty1_button.active or difficulty2_button.active or \
            difficulty3_button.active or difficulty4_button.active) and (yes_button.active or no_button.active):
        
        sound2.play()
        ai_settings.game_active = True
    else:
        if mouse_on_button:
            start_game_button.frame = True
            start_game_button.prep_msg(start_game_button.msg)
        
            if start_game_button.sound_count < 1:
                sound1.play()
                start_game_button.sound_count += 1
            
        else:
            start_game_button.frame = False
            start_game_button.prep_msg(start_game_button.msg)
            start_game_button.sound_count = 0
        
#---------------------------------------------------------------------------
# Меню загрузки
# Load game menu
def check_load_button(ai_settings,screen,load_button,slider,logo=None,button_clicked=False,draw_menu=False,sound1=None,sound2=None):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button = load_button.rect.collidepoint(mouse_x,mouse_y)
   
    if button_clicked and mouse_on_button:
        sound2.play()
        draw_menu = True
        ai_settings.slider_move = 0
        slider.rect.top = 243
    else:
        if mouse_on_button:
            load_button.frame = True
            load_button.prep_msg(load_button.msg)
        
            if load_button.sound_count < 1:
                sound1.play()
                load_button.sound_count += 1
        else:
            load_button.frame = False
            load_button.prep_msg(load_button.msg)
            load_button.sound_count = 0

    draw_load_game_menu(ai_settings,screen,logo,draw_menu)

# Отрисовка меню загрузки
# Draw load game menu
def draw_load_game_menu(ai_settings,screen,logo,draw_menu=False):
    
    if draw_menu:
        ai_settings.game_menu_active = True
        ai_settings.game_menu_settings_lvl1_active = True
        ai_settings.last_button = "load_game"
        
        screen.fill((30,30,30))
        
        pygame.draw.rect(screen,(35,35,35),(590,240,1200,755))
        pygame.draw.rect(screen,(40,40,40),(590,240,1200,755),3)
        
        pygame.draw.line(screen,(15,15,15),[595,390+ai_settings.slider_move],[1790,390+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,540+ai_settings.slider_move],[1790,540+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,690+ai_settings.slider_move],[1790,690+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,840+ai_settings.slider_move],[1790,840+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,990+ai_settings.slider_move],[1790,990+ai_settings.slider_move],1)
    
        pygame.draw.line(screen,(15,15,15),[595,1140+ai_settings.slider_move],[1790,1140+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,1290+ai_settings.slider_move],[1790,1290+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,1440+ai_settings.slider_move],[1790,1440+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,1590+ai_settings.slider_move],[1790,1590+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,1740+ai_settings.slider_move],[1790,1740+ai_settings.slider_move],1)
        
        screen.blit(logo,(100,80))
        
# Создаем и проверяем слайдер(меню загрузок)
# Make and check slider(load game menu)
def check_load_game_slider(ai_settings,slider,scroll):
    
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_on_slider = slider.rect.collidepoint(mouse_x,mouse_y)
    
         
    if slider.rect.top > 242 and slider.rect.bottom < 990:
            
            if scroll == 'up':
                slider.rect.centery -= 10
                ai_settings.slider_move += 11.9

            elif scroll == 'down':
                slider.rect.centery += 10
                ai_settings.slider_move -= 11.9
                
            else:   
                if mouse_pressed[0] and mouse_on_slider:
                
                    if slider.rect.centery < mouse_y:
                        ai_settings.slider_move -= ((mouse_y - slider.rect.centery)*1.18)
                    elif slider.rect.centery > mouse_y:
                        ai_settings.slider_move += ((slider.rect.centery - mouse_y)*1.18)
                
                    slider.rect.centery = mouse_y
            
            
    if slider.rect.top <= 242:
        slider.rect.top = 243
        
    if slider.rect.bottom >= 990:
        slider.rect.bottom = 989
            
    if slider.rect.top <= 295:
        ai_settings.slider_move = 0
            
    if slider.rect.bottom >= 989:
        ai_settings.slider_move = -750


#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
# Меню настроек
# Options menu
def check_settings_button(ai_settings,screen,settings_button,logo=None,button_clicked=False,draw_menu=False,sound1=None,sound2=None):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button = settings_button.rect.collidepoint(mouse_x,mouse_y)

    if button_clicked and mouse_on_button:
        sound2.play()
        draw_menu = True
    else:
        if mouse_on_button:
            settings_button.frame = True
            settings_button.prep_msg(settings_button.msg)
        
            if settings_button.sound_count < 1:
                sound1.play()
                settings_button.sound_count += 1
        else:
            settings_button.frame = False
            settings_button.prep_msg(settings_button.msg)
            settings_button.sound_count = 0
            
    draw_settings_game_menu(ai_settings,screen,logo,draw_menu)
    
# Отрисовка меню настроек
# Draw options menu
def draw_settings_game_menu(ai_settings,screen,logo,draw_menu=False):
    
    if draw_menu:
        ai_settings.game_menu_active = True
        ai_settings.game_menu_settings_lvl1_active = True
        ai_settings.last_button = "settings"
        
        pygame.draw.rect(screen,(30,30,30),(100,0,400,1080))
        screen.blit(logo,(100,80))

      
#---------------------------------------------------------------------------
# Аудио
# Audio
def check_audio_settings_game_menu(ai_settings,screen,audio_settings_button,logo=None,button_clicked=False,draw_menu=False,sound1=None,sound2=None):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button = audio_settings_button.rect.collidepoint(mouse_x,mouse_y)
      
    if button_clicked and mouse_on_button:
        sound2.play()
        draw_menu = True
    else:
        if mouse_on_button:
            audio_settings_button.frame = True
            audio_settings_button.prep_msg(audio_settings_button.msg)
        
            if audio_settings_button.sound_count < 1:
                sound1.play()
                audio_settings_button.sound_count += 1
        else:
            audio_settings_button.frame = False
            audio_settings_button.prep_msg(audio_settings_button.msg)
            audio_settings_button.sound_count = 0
            
    draw_audio_settings_game_menu(ai_settings,screen,logo,draw_menu)
    
# Отрисовка настроек звука
# Draw audio options   
def draw_audio_settings_game_menu(ai_settings,screen,logo,draw_menu=False):
    
    if draw_menu:
        ai_settings.game_menu_settings_lvl2_active = True
        ai_settings.last_button = "audio"
        ai_settings.game_menu_settings_lvl1_active = False
        
        screen.fill((30,30,30))
        
        pygame.draw.rect(screen,(35,35,35),(590,240,1200,455))
        pygame.draw.rect(screen,(40,40,40),(590,240,1200,455),3)
        
        # Делаем рамочки
        pygame.draw.line(screen,(15,15,15),[595,390],[1790,390],1)
        pygame.draw.line(screen,(15,15,15),[595,540],[1790,540],1)
        pygame.draw.line(screen,(15,15,15),[595,690],[1790,690],1)
        
        
        
        screen.blit(logo,(100,80))
         
# Ползунок для музыки
# Music slider
def set_music_volume(ai_settings,slider):  
    
    # Проверка координат мыши
    # Check mouse coordinates
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_on_slider = slider.rect.collidepoint(mouse_x,mouse_y)
    
    if mouse_pressed[0] and mouse_on_slider:
        
        if slider.rect.left > 1290 and slider.rect.right < 1690:
                
            ai_settings.music_volume = (slider.rect.centerx - 1290)/4
            slider.rect.centerx = mouse_x
            
            
        if slider.rect.left <= 1292:
            ai_settings.music_volume = 0
            slider.rect.left = 1293
        
        if slider.rect.right >= 1688:
            ai_settings.music_volume = 100
            slider.rect.right = 1686
            
    pygame.mixer.music.set_volume(ai_settings.music_volume/100)
        
# Отрисовка настроек музыки
# Draw sound options
def draw_music_volume_button(ai_settings,screen):
    
    font = pygame.font.SysFont('AlundraText',58)
    if ai_settings.selected_language==0:
        text = font.render('Музыка',True,(220,220,220))
        screen.blit(text,(680,285))
    else:
        text = font.render('Music',True,(220,220,220))
        screen.blit(text,(680,285))       
    
    font1 = pygame.font.SysFont('AlundraText',38)
    text1 = font1.render(str(int(ai_settings.music_volume)),True,(220,220,220))
    screen.blit(text1,(1230,302))

    
    pygame.draw.rect(screen,(150,150,150),(1290,305,400,30))                
    pygame.draw.rect(screen,(20,20,20),(1290,300,400,35),4)


# Ползунок для звуков
# Sound slider
def set_sound_volume(ai_settings,sounds,slider):  
        
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_on_slider = slider.rect.collidepoint(mouse_x,mouse_y)
    
    if mouse_pressed[0] and mouse_on_slider:
        
        if slider.rect.left > 1290 and slider.rect.right < 1690:
                
            ai_settings.sound_volume = (slider.rect.centerx - 1290)/4
            slider.rect.centerx = mouse_x
            
            
        if slider.rect.left <= 1292:
            ai_settings.sound_volume = 0
            slider.rect.left = 1293
        
        if slider.rect.right >= 1688:
            ai_settings.sound_volume = 100
            slider.rect.right = 1687

    for sound in sounds:   
        sound.set_volume(ai_settings.sound_volume/100)
        
# Отрисовка настроек звука
# Draw sound options
def draw_sound_volume_button(ai_settings,screen):
    
    font = pygame.font.SysFont('AlundraText',58)
    if ai_settings.selected_language==0:
        text = font.render('Звуки',True,(220,220,220))
        screen.blit(text,(680,435))
    else:
        text = font.render('Sounds',True,(220,220,220))
        screen.blit(text,(680,435))
    
    font1 = pygame.font.SysFont('AlundraText',38)
    text1 = font1.render(str(int(ai_settings.sound_volume)),True,(220,220,220))
    screen.blit(text1,(1230,452))

    
    pygame.draw.rect(screen,(150,150,150),(1290,455,400,30))
    pygame.draw.rect(screen,(20,20,20),(1290,450,400,35),4)
    

# Ползунок для закадрового голоса
# Voice slider
def set_voice_volume(ai_settings,slider):  
    
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_on_slider = slider.rect.collidepoint(mouse_x,mouse_y)
    
    if mouse_pressed[0] and mouse_on_slider:
        
        if slider.rect.left > 1290 and slider.rect.right < 1690:
                
            ai_settings.voice_volume = (slider.rect.centerx - 1290)/4
            slider.rect.centerx = mouse_x
            
            
        if slider.rect.left <= 1292:
            ai_settings.voice_volume = 0
            slider.rect.left = 1293
        
        if slider.rect.right >= 1688:
            ai_settings.voice_volume = 100
            slider.rect.right = 1687
        
# Отрисовка настроек закадрового голоса
# Draw Voice options
def draw_voice_volume_button(ai_settings,screen):
    
    font = pygame.font.SysFont('AlundraText',58)
    if ai_settings.selected_language==0:
        text = font.render('Голос',True,(220,220,220))
        screen.blit(text,(680,585))
    else:
        text = font.render('Voice',True,(220,220,220))
        screen.blit(text,(680,585))
    
    font1 = pygame.font.SysFont('AlundraText',38)
    text1 = font1.render(str(int(ai_settings.voice_volume)),True,(220,220,220))
    screen.blit(text1,(1230,602))

    pygame.draw.rect(screen,(150,150,150),(1290,605,400,30))
    pygame.draw.rect(screen,(20,20,20),(1290,600,400,35),4)  

#---------------------------------------------------------------------------
# Привязки клавиш
# Key bindings
def check_keys_settings_game_menu(ai_settings,screen,keys_settings_button,slider=None,logo=None,button_clicked=False,draw_menu=False,sound1=None,sound2=None):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button = keys_settings_button.rect.collidepoint(mouse_x,mouse_y)
        
    if button_clicked and mouse_on_button:
        sound2.play()
        draw_menu = True
        ai_settings.slider_move = 0
        slider.rect.top = 243
    else:
        if mouse_on_button:
            keys_settings_button.frame = True
            keys_settings_button.prep_msg(keys_settings_button.msg)
        
            if keys_settings_button.sound_count < 1:
                sound1.play()
                keys_settings_button.sound_count += 1
        else:
            keys_settings_button.frame = False
            keys_settings_button.prep_msg(keys_settings_button.msg)
            keys_settings_button.sound_count = 0
            
    draw_keys_settings_game_menu(ai_settings,screen,logo,draw_menu)
    
# Отрисовка меню привязки клавиш
# Draw key bindings menu
def draw_keys_settings_game_menu(ai_settings,screen,logo,draw_menu=False):
    
    if draw_menu:
        ai_settings.game_menu_settings_lvl2_active = True
        ai_settings.last_button = "keys"
        ai_settings.game_menu_settings_lvl1_active = False
        
        screen.fill((30,30,30))
        
        pygame.draw.rect(screen,(35,35,35),(590,240,1200,755))
        pygame.draw.rect(screen,(40,40,40),(590,240,1200,755),3)
        
        pygame.draw.line(screen,(15,15,15),[595,390+ai_settings.slider_move],[1790,390+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,540+ai_settings.slider_move],[1790,540+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,690+ai_settings.slider_move],[1790,690+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,840+ai_settings.slider_move],[1790,840+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,990+ai_settings.slider_move],[1790,990+ai_settings.slider_move],1)
        
        pygame.draw.line(screen,(15,15,15),[595,1140+ai_settings.slider_move],[1790,1140+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,1290+ai_settings.slider_move],[1790,1290+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,1440+ai_settings.slider_move],[1790,1440+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,1590+ai_settings.slider_move],[1790,1590+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,1740+ai_settings.slider_move],[1790,1740+ai_settings.slider_move],1)
        
        pygame.draw.line(screen,(15,15,15),[595,1890+ai_settings.slider_move],[1790,1890+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,2040+ai_settings.slider_move],[1790,2040+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,2190+ai_settings.slider_move],[1790,2190+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,2340+ai_settings.slider_move],[1790,2340+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,2490+ai_settings.slider_move],[1790,2490+ai_settings.slider_move],1)
        
        pygame.draw.line(screen,(15,15,15),[595,2640+ai_settings.slider_move],[1790,2640+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,2790+ai_settings.slider_move],[1790,2790+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,2940+ai_settings.slider_move],[1790,2940+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,3090+ai_settings.slider_move],[1790,3090+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,3240+ai_settings.slider_move],[1790,3240+ai_settings.slider_move],1)
        
        pygame.draw.line(screen,(15,15,15),[595,3390+ai_settings.slider_move],[1790,3390+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,3540+ai_settings.slider_move],[1790,3540+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,3690+ai_settings.slider_move],[1790,3690+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,3840+ai_settings.slider_move],[1790,3840+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,3990+ai_settings.slider_move],[1790,3990+ai_settings.slider_move],1)
        
        pygame.draw.line(screen,(15,15,15),[595,4140+ai_settings.slider_move],[1790,4140+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,4290+ai_settings.slider_move],[1790,4290+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,4440+ai_settings.slider_move],[1790,4440+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,4590+ai_settings.slider_move],[1790,4590+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,4740+ai_settings.slider_move],[1790,4740+ai_settings.slider_move],1)
        
        pygame.draw.line(screen,(15,15,15),[595,4890+ai_settings.slider_move],[1790,4890+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,5040+ai_settings.slider_move],[1790,5040+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,5190+ai_settings.slider_move],[1790,5190+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,5340+ai_settings.slider_move],[1790,5340+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,5490+ai_settings.slider_move],[1790,5490+ai_settings.slider_move],1)
        
        pygame.draw.line(screen,(15,15,15),[595,5640+ai_settings.slider_move],[1790,5640+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,5790+ai_settings.slider_move],[1790,5790+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,5940+ai_settings.slider_move],[1790,5940+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,6090+ai_settings.slider_move],[1790,6090+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,6240+ai_settings.slider_move],[1790,6240+ai_settings.slider_move],1)
        
        pygame.draw.line(screen,(15,15,15),[595,6390+ai_settings.slider_move],[1790,6390+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,6540+ai_settings.slider_move],[1790,6540+ai_settings.slider_move],1)
        
        
        if ai_settings.selected_language==0:
            # Описание кнопок
            # Key names
            font = pygame.font.SysFont('AlundraText',48)
            
            text = font.render("Движение вперёд",True,(220,220,220))
            screen.blit(text,(685,302+ai_settings.slider_move))
            text = font.render("Движение влево",True,(220,220,220))
            screen.blit(text,(685,452+ai_settings.slider_move))
            text = font.render("Движение назад",True,(220,220,220))
            screen.blit(text,(685,602+ai_settings.slider_move))
            text = font.render("Движение вправо",True,(220,220,220))
            screen.blit(text,(685,752+ai_settings.slider_move))
            text = font.render("Взаимодействие",True,(220,220,220))
            screen.blit(text,(685,902+ai_settings.slider_move))
        
            text = font.render("Ускориться",True,(220,220,220))
            screen.blit(text,(685,1052+ai_settings.slider_move))
            text = font.render("Переключиться на шаг",True,(220,220,220))
            screen.blit(text,(685,1202+ai_settings.slider_move))
            text = font.render("Прыгнуть",True,(220,220,220))
            screen.blit(text,(685,1352+ai_settings.slider_move))
            text = font.render("Изменить тип атаки",True,(220,220,220))
            screen.blit(text,(685,1502+ai_settings.slider_move))
            text = font.render("Быстрая атака",True,(220,220,220))
            screen.blit(text,(685,1652+ai_settings.slider_move))
        
            text = font.render("Мощная атака",True,(220,220,220))
            screen.blit(text,(685,1802+ai_settings.slider_move))
            text = font.render("Ведьмачье чутье",True,(220,220,220))
            screen.blit(text,(685,1952+ai_settings.slider_move))
            text = font.render("Блок",True,(220,220,220))
            screen.blit(text,(685,2102+ai_settings.slider_move))
            text = font.render("Наложить знак",True,(220,220,220))
            screen.blit(text,(685,2252+ai_settings.slider_move))
            text = font.render("Переключиться между знаками",True,(220,220,220))
            screen.blit(text,(685,2402+ai_settings.slider_move))
        
            text = font.render("Предмет в быстром доступе",True,(220,220,220))
            screen.blit(text,(685,2552+ai_settings.slider_move))
            text = font.render("Уклониться",True,(220,220,220))
            screen.blit(text,(685,2702+ai_settings.slider_move))
            text = font.render("Кувырок",True,(220,220,220))
            screen.blit(text,(685,2852+ai_settings.slider_move))
            text = font.render("Подозвать лошадь",True,(220,220,220))
            screen.blit(text,(685,3002+ai_settings.slider_move))
            text = font.render("Скакать карьером/В галоп",True,(220,220,220))
            screen.blit(text,(685,3152+ai_settings.slider_move))
        
            text = font.render("Спешиться",True,(220,220,220))
            screen.blit(text,(685,3302+ai_settings.slider_move))
            text = font.render("Вынырнуть",True,(220,220,220))
            screen.blit(text,(685,3452+ai_settings.slider_move))
            text = font.render("Нырнуть",True,(220,220,220))
            screen.blit(text,(685,3602+ai_settings.slider_move))
            text = font.render("Меню быстрого доступа",True,(220,220,220))
            screen.blit(text,(685,3752+ai_settings.slider_move))
            text = font.render("Эликсиры и еда 1",True,(220,220,220))
            screen.blit(text,(685,3902+ai_settings.slider_move))
        
            text = font.render("Эликсиры и еда 2",True,(220,220,220))
            screen.blit(text,(685,4052+ai_settings.slider_move))
            text = font.render("Эликсиры и еда 3",True,(220,220,220))
            screen.blit(text,(685,4202+ai_settings.slider_move))
            text = font.render("Эликсиры и еда 4",True,(220,220,220))
            screen.blit(text,(685,4352+ai_settings.slider_move))
            text = font.render("Обнажить стальной меч",True,(220,220,220))
            screen.blit(text,(685,4502+ai_settings.slider_move))
            text = font.render("Обнажить серябряный меч",True,(220,220,220))
            screen.blit(text,(685,4652+ai_settings.slider_move))
        
            text = font.render("Сменить задачу",True,(220,220,220))
            screen.blit(text,(685,4802+ai_settings.slider_move))
            text = font.render("Персонаж",True,(220,220,220))
            screen.blit(text,(685,4952+ai_settings.slider_move))
            text = font.render("Рюкзак",True,(220,220,220))
            screen.blit(text,(685,5102+ai_settings.slider_move))
            text = font.render("Карта",True,(220,220,220))
            screen.blit(text,(685,5252+ai_settings.slider_move))
            text = font.render("Задания",True,(220,220,220))
            screen.blit(text,(685,5402+ai_settings.slider_move))
        
            text = font.render("Медитация",True,(220,220,220))
            screen.blit(text,(685,5552+ai_settings.slider_move))
            text = font.render("Алхимия",True,(220,220,220))
            screen.blit(text,(685,5702+ai_settings.slider_move))
            text = font.render("Ремесло",True,(220,220,220))
            screen.blit(text,(685,5852+ai_settings.slider_move))
            text = font.render("Бестиарий",True,(220,220,220))
            screen.blit(text,(685,6002+ai_settings.slider_move))
            text = font.render("Глоссарий",True,(220,220,220))
            screen.blit(text,(685,6152+ai_settings.slider_move))
        
            text = font.render("Колода для игры в гвинт",True,(220,220,220))
            screen.blit(text,(685,6302+ai_settings.slider_move))
            text = font.render("Быстрое сохранение",True,(220,220,220))
            screen.blit(text,(685,6452+ai_settings.slider_move))
        
        
            # Сами кнопки
            font = pygame.font.SysFont('AlundraText',68)
            font1 = pygame.font.SysFont('AlundraText',48)
        
            text = font.render("W",True,(220,220,220))
            screen.blit(text,(1535,300+ai_settings.slider_move))
            text = font.render("A",True,(220,220,220))
            screen.blit(text,(1535,450+ai_settings.slider_move))
            text = font.render("S",True,(220,220,220))
            screen.blit(text,(1535,600+ai_settings.slider_move))
            text = font.render("D",True,(220,220,220))
            screen.blit(text,(1535,750+ai_settings.slider_move))
            text = font.render("E",True,(220,220,220))
            screen.blit(text,(1535,900+ai_settings.slider_move))
        
            text = font1.render("Левый Shift",True,(220,220,220))
            screen.blit(text,(1420,1050+ai_settings.slider_move))
            text = font1.render("Левый Control",True,(220,220,220))
            screen.blit(text,(1405,1200+ai_settings.slider_move))
            text = font1.render("Пробел",True,(220,220,220))
            screen.blit(text,(1480,1350+ai_settings.slider_move))
            text = font1.render("Левый Shift",True,(220,220,220))
            screen.blit(text,(1420,1500+ai_settings.slider_move))
            text = font1.render("ЛКМ",True,(220,220,220))
            screen.blit(text,(1500,1650+ai_settings.slider_move))
        
            text = font1.render("Левый Shift + ЛКМ",True,(220,220,220))
            screen.blit(text,(1360,1800+ai_settings.slider_move))
            text = font1.render("ПКМ",True,(220,220,220))
            screen.blit(text,(1500,1950+ai_settings.slider_move))
            text = font1.render("ПКМ",True,(220,220,220))
            screen.blit(text,(1500,2100+ai_settings.slider_move))
            text = font1.render("Q",True,(220,220,220))
            screen.blit(text,(1535,2250+ai_settings.slider_move))
            text = font1.render("Tab",True,(220,220,220))
            screen.blit(text,(1510,2400+ai_settings.slider_move))
        
            text = font1.render("Средняя кнопка мыши",True,(220,220,220))
            screen.blit(text,(1320,2550+ai_settings.slider_move))
            text = font1.render("Alt",True,(220,220,220))
            screen.blit(text,(1510,2700+ai_settings.slider_move))
            text = font1.render("Пробел",True,(220,220,220))
            screen.blit(text,(1480,2850+ai_settings.slider_move))
            text = font1.render("X",True,(220,220,220))
            screen.blit(text,(1535,3000+ai_settings.slider_move))
            text = font1.render("Левый Shift",True,(220,220,220))
            screen.blit(text,(1420,3150+ai_settings.slider_move))
        
            text = font1.render("E",True,(220,220,220))
            screen.blit(text,(1535,3300+ai_settings.slider_move))
            text = font1.render("Пробел",True,(220,220,220))
            screen.blit(text,(1480,3450+ai_settings.slider_move))
            text = font1.render("C",True,(220,220,220))
            screen.blit(text,(1535,3600+ai_settings.slider_move))
            text = font1.render("Tab",True,(220,220,220))
            screen.blit(text,(1510,3750+ai_settings.slider_move))
            text = font1.render("R",True,(220,220,220))
            screen.blit(text,(1535,3900+ai_settings.slider_move))   
        
            text = font1.render("F",True,(220,220,220))
            screen.blit(text,(1535,4050+ai_settings.slider_move))
            text = font1.render("T",True,(220,220,220))
            screen.blit(text,(1535,4200+ai_settings.slider_move))
            text = font1.render("Y",True,(220,220,220))
            screen.blit(text,(1535,4350+ai_settings.slider_move))
            text = font1.render("1",True,(220,220,220))
            screen.blit(text,(1535,4500+ai_settings.slider_move))
            text = font1.render("2",True,(220,220,220))
            screen.blit(text,(1535,4650+ai_settings.slider_move))
        
            text = font1.render("V",True,(220,220,220))
            screen.blit(text,(1535,4800+ai_settings.slider_move))
            text = font1.render("K",True,(220,220,220))
            screen.blit(text,(1535,4950+ai_settings.slider_move))
            text = font1.render("I",True,(220,220,220))
            screen.blit(text,(1535,5100+ai_settings.slider_move))
            text = font1.render("M",True,(220,220,220))
            screen.blit(text,(1535,5250+ai_settings.slider_move))
            text = font1.render("J",True,(220,220,220))
            screen.blit(text,(1535,5400+ai_settings.slider_move))
            
            text = font1.render("N",True,(220,220,220))
            screen.blit(text,(1535,5550+ai_settings.slider_move))
            text = font1.render("L",True,(220,220,220))
            screen.blit(text,(1535,5700+ai_settings.slider_move))
            text = font1.render("O",True,(220,220,220))
            screen.blit(text,(1535,5850+ai_settings.slider_move))
            text = font1.render("B",True,(220,220,220))
            screen.blit(text,(1535,6000+ai_settings.slider_move))
            text = font1.render("G",True,(220,220,220))
            screen.blit(text,(1535,6150+ai_settings.slider_move)) 
        
            text = font1.render("H",True,(220,220,220))
            screen.blit(text,(1535,6300+ai_settings.slider_move))
            text = font1.render("F5",True,(220,220,220))
            screen.blit(text,(1535,6450+ai_settings.slider_move))
            
        else:
            # Описание кнопок
            # Key names
            font = pygame.font.SysFont('AlundraText',48)
            
            text = font.render("Movement up",True,(220,220,220))
            screen.blit(text,(685,302+ai_settings.slider_move))
            text = font.render("Movement left",True,(220,220,220))
            screen.blit(text,(685,452+ai_settings.slider_move))
            text = font.render("Movement down",True,(220,220,220))
            screen.blit(text,(685,602+ai_settings.slider_move))
            text = font.render("Movement right",True,(220,220,220))
            screen.blit(text,(685,752+ai_settings.slider_move))
            text = font.render("Interact",True,(220,220,220))
            screen.blit(text,(685,902+ai_settings.slider_move))
            text = font.render("Sprint",True,(220,220,220))
            screen.blit(text,(685,1052+ai_settings.slider_move))
            text = font.render("Toggle walk/run",True,(220,220,220))
            screen.blit(text,(685,1202+ai_settings.slider_move))
            text = font.render("Jump",True,(220,220,220))
            screen.blit(text,(685,1352+ai_settings.slider_move))
            text = font.render("Modify attack type",True,(220,220,220))
            screen.blit(text,(685,1502+ai_settings.slider_move))
            text = font.render("Fast attack",True,(220,220,220))
            screen.blit(text,(685,1652+ai_settings.slider_move))
            text = font.render("Strong attack",True,(220,220,220))
            screen.blit(text,(685,1802+ai_settings.slider_move))
            text = font.render("Use witcher senses",True,(220,220,220))
            screen.blit(text,(685,1952+ai_settings.slider_move))
            text = font.render("Parry",True,(220,220,220))
            screen.blit(text,(685,2102+ai_settings.slider_move))
            text = font.render("Cast signs",True,(220,220,220))
            screen.blit(text,(685,2252+ai_settings.slider_move))
            text = font.render("Toggle between signs",True,(220,220,220))
            screen.blit(text,(685,2402+ai_settings.slider_move))
            text = font.render("Use quick access item",True,(220,220,220))
            screen.blit(text,(685,2552+ai_settings.slider_move))
            text = font.render("Dodge",True,(220,220,220))
            screen.blit(text,(685,2702+ai_settings.slider_move))
            text = font.render("Roll",True,(220,220,220))
            screen.blit(text,(685,2852+ai_settings.slider_move))
            text = font.render("Call horse",True,(220,220,220))
            screen.blit(text,(685,3002+ai_settings.slider_move))
            text = font.render("Galop/Canter",True,(220,220,220))
            screen.blit(text,(685,3152+ai_settings.slider_move))
            text = font.render("Dismount",True,(220,220,220))
            screen.blit(text,(685,3302+ai_settings.slider_move))
            text = font.render("Surface",True,(220,220,220))
            screen.blit(text,(685,3452+ai_settings.slider_move))
            text = font.render("Dive",True,(220,220,220))
            screen.blit(text,(685,3602+ai_settings.slider_move))
            text = font.render("Quick access menu",True,(220,220,220))
            screen.blit(text,(685,3752+ai_settings.slider_move))
            text = font.render("Consumables slot 1",True,(220,220,220))
            screen.blit(text,(685,3902+ai_settings.slider_move))
            text = font.render("Consumables slot 2",True,(220,220,220))
            screen.blit(text,(685,4052+ai_settings.slider_move))
            text = font.render("Consumables slot 3",True,(220,220,220))
            screen.blit(text,(685,4202+ai_settings.slider_move))
            text = font.render("Consumables slot 4",True,(220,220,220))
            screen.blit(text,(685,4352+ai_settings.slider_move))
            text = font.render("Draw steel sword",True,(220,220,220))
            screen.blit(text,(685,4502+ai_settings.slider_move))
            text = font.render("Draw silver sword",True,(220,220,220))
            screen.blit(text,(685,4652+ai_settings.slider_move))
            text = font.render("Change objective",True,(220,220,220))
            screen.blit(text,(685,4802+ai_settings.slider_move))
            text = font.render("Character panel",True,(220,220,220))
            screen.blit(text,(685,4952+ai_settings.slider_move))
            text = font.render("Inventory panel",True,(220,220,220))
            screen.blit(text,(685,5102+ai_settings.slider_move))
            text = font.render("Map",True,(220,220,220))
            screen.blit(text,(685,5252+ai_settings.slider_move))
            text = font.render("Quests panel",True,(220,220,220))
            screen.blit(text,(685,5402+ai_settings.slider_move))
            text = font.render("Meditation",True,(220,220,220))
            screen.blit(text,(685,5552+ai_settings.slider_move))
            text = font.render("Alchemy",True,(220,220,220))
            screen.blit(text,(685,5702+ai_settings.slider_move))
            text = font.render("Crafting",True,(220,220,220))
            screen.blit(text,(685,5852+ai_settings.slider_move))
            text = font.render("Bestiary",True,(220,220,220))
            screen.blit(text,(685,6002+ai_settings.slider_move))
            text = font.render("Glossary panel",True,(220,220,220))
            screen.blit(text,(685,6152+ai_settings.slider_move))
            text = font.render("Gwent deck",True,(220,220,220))
            screen.blit(text,(685,6302+ai_settings.slider_move))
            text = font.render("Quick save",True,(220,220,220))
            screen.blit(text,(685,6452+ai_settings.slider_move))
        
            # Сами кнопки
            # Buttons
            font = pygame.font.SysFont('AlundraText',68)
            font1 = pygame.font.SysFont('AlundraText',48)
        
            text = font.render("W",True,(220,220,220))
            screen.blit(text,(1535,300+ai_settings.slider_move))
            text = font.render("A",True,(220,220,220))
            screen.blit(text,(1535,450+ai_settings.slider_move))
            text = font.render("S",True,(220,220,220))
            screen.blit(text,(1535,600+ai_settings.slider_move))
            text = font.render("D",True,(220,220,220))
            screen.blit(text,(1535,750+ai_settings.slider_move))
            text = font.render("E",True,(220,220,220))
            screen.blit(text,(1535,900+ai_settings.slider_move))
        
            text = font1.render("Left Shift",True,(220,220,220))
            screen.blit(text,(1460,1050+ai_settings.slider_move))
            text = font1.render("Left Control",True,(220,220,220))
            screen.blit(text,(1435,1200+ai_settings.slider_move))
            text = font1.render("Space",True,(220,220,220))
            screen.blit(text,(1490,1350+ai_settings.slider_move))
            text = font1.render("Left Shift",True,(220,220,220))
            screen.blit(text,(1460,1500+ai_settings.slider_move))
            text = font1.render("LMB",True,(220,220,220))
            screen.blit(text,(1510,1650+ai_settings.slider_move))
        
            text = font1.render("Left Shift + LMB",True,(220,220,220))
            screen.blit(text,(1375,1800+ai_settings.slider_move))
            text = font1.render("RMB",True,(220,220,220))
            screen.blit(text,(1510,1950+ai_settings.slider_move))
            text = font1.render("RMB",True,(220,220,220))
            screen.blit(text,(1510,2100+ai_settings.slider_move))
            text = font1.render("Q",True,(220,220,220))
            screen.blit(text,(1535,2250+ai_settings.slider_move))
            text = font1.render("Tab",True,(220,220,220))
            screen.blit(text,(1510,2400+ai_settings.slider_move))
        
            text = font1.render("MMB",True,(220,220,220))
            screen.blit(text,(1510,2550+ai_settings.slider_move))
            text = font1.render("Alt",True,(220,220,220))
            screen.blit(text,(1510,2700+ai_settings.slider_move))
            text = font1.render("Space",True,(220,220,220))
            screen.blit(text,(1490,2850+ai_settings.slider_move))
            text = font1.render("X",True,(220,220,220))
            screen.blit(text,(1535,3000+ai_settings.slider_move))
            text = font1.render("Left Shift",True,(220,220,220))
            screen.blit(text,(1460,3150+ai_settings.slider_move))
        
            text = font1.render("E",True,(220,220,220))
            screen.blit(text,(1535,3300+ai_settings.slider_move))
            text = font1.render("Space",True,(220,220,220))
            screen.blit(text,(1490,3450+ai_settings.slider_move))
            text = font1.render("C",True,(220,220,220))
            screen.blit(text,(1535,3600+ai_settings.slider_move))
            text = font1.render("Tab",True,(220,220,220))
            screen.blit(text,(1510,3750+ai_settings.slider_move))
            text = font1.render("R",True,(220,220,220))
            screen.blit(text,(1535,3900+ai_settings.slider_move))   
        
            text = font1.render("F",True,(220,220,220))
            screen.blit(text,(1535,4050+ai_settings.slider_move))
            text = font1.render("T",True,(220,220,220))
            screen.blit(text,(1535,4200+ai_settings.slider_move))
            text = font1.render("Y",True,(220,220,220))
            screen.blit(text,(1535,4350+ai_settings.slider_move))
            text = font1.render("1",True,(220,220,220))
            screen.blit(text,(1535,4500+ai_settings.slider_move))
            text = font1.render("2",True,(220,220,220))
            screen.blit(text,(1535,4650+ai_settings.slider_move))
        
            text = font1.render("V",True,(220,220,220))
            screen.blit(text,(1535,4800+ai_settings.slider_move))
            text = font1.render("K",True,(220,220,220))
            screen.blit(text,(1535,4950+ai_settings.slider_move))
            text = font1.render("I",True,(220,220,220))
            screen.blit(text,(1535,5100+ai_settings.slider_move))
            text = font1.render("M",True,(220,220,220))
            screen.blit(text,(1535,5250+ai_settings.slider_move))
            text = font1.render("J",True,(220,220,220))
            screen.blit(text,(1535,5400+ai_settings.slider_move))
        
            text = font1.render("N",True,(220,220,220))
            screen.blit(text,(1535,5550+ai_settings.slider_move))
            text = font1.render("L",True,(220,220,220))
            screen.blit(text,(1535,5700+ai_settings.slider_move))
            text = font1.render("O",True,(220,220,220))
            screen.blit(text,(1535,5850+ai_settings.slider_move))
            text = font1.render("B",True,(220,220,220))
            screen.blit(text,(1535,6000+ai_settings.slider_move))
            text = font1.render("G",True,(220,220,220))
            screen.blit(text,(1535,6150+ai_settings.slider_move)) 
        
            text = font1.render("H",True,(220,220,220))
            screen.blit(text,(1535,6300+ai_settings.slider_move))
            text = font1.render("F5",True,(220,220,220))
            screen.blit(text,(1525,6450+ai_settings.slider_move))
        
        screen.blit(logo,(100,80))
        
# Создаем и проверяем слайдер привязки клавиш
# Make and check key bindings slider
def check_keys_slider(ai_settings,slider,scroll):
    
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_on_slider = slider.rect.collidepoint(mouse_x,mouse_y)
    
    if slider.rect.top > 242 and slider.rect.bottom < 990:
            
            if scroll == 'up':
                slider.rect.centery -= 10
                ai_settings.slider_move += 87

            elif scroll == 'down':
                slider.rect.centery += 10
                ai_settings.slider_move -= 87
            else:
                
                if mouse_pressed[0] and mouse_on_slider:
                
                    if slider.rect.centery < mouse_y:
                        ai_settings.slider_move -= ((mouse_y - slider.rect.centery)*8.7)
                    elif slider.rect.centery > mouse_y:
                        ai_settings.slider_move += ((slider.rect.centery - mouse_y)*8.7)
                
                    slider.rect.centery = mouse_y
            
            
    if slider.rect.top <= 242:
        slider.rect.top = 243
        
    if slider.rect.bottom >= 990:
        slider.rect.bottom = 989
            
    if slider.rect.top <= 295:
        ai_settings.slider_move = 0
            
    if slider.rect.bottom >= 989:
        ai_settings.slider_move = -5550
            
        
def draw_slider(screen):
    pygame.draw.rect(screen,(15,15,15),(1795,240,27,755),5)
    pygame.draw.rect(screen,(30,30,30),(590,0,1390,240))
    pygame.draw.rect(screen,(30,30,30),(590,995,1390,85))

        
#---------------------------------------------------------------------------
# Игровой процесс
# Gameplay
def check_game_process_settings_game_menu(ai_settings,screen,slider,game_process_settings_button,logo=None,button_clicked=False,
                                          draw_menu=False,sound1=None,sound2=None):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button = game_process_settings_button.rect.collidepoint(mouse_x,mouse_y)
    
    if button_clicked and mouse_on_button:
        sound2.play()
        draw_menu = True
        ai_settings.slider_move = 0
        slider.rect.top = 243
    else:
        if mouse_on_button:
            game_process_settings_button.frame = True
            game_process_settings_button.prep_msg(game_process_settings_button.msg)
        
            if game_process_settings_button.sound_count < 1:
                sound1.play()
                game_process_settings_button.sound_count += 1
        else:
            game_process_settings_button.frame = False
            game_process_settings_button.prep_msg(game_process_settings_button.msg)
            game_process_settings_button.sound_count = 0
            
    draw_game_process_settings_game_menu(ai_settings,screen,logo,draw_menu)

# Отрисовка меню игровой процесс
# Draw gameplay menu
def draw_game_process_settings_game_menu(ai_settings,screen,logo,draw_menu=False):
    
    if draw_menu:
        ai_settings.game_menu_settings_lvl2_active = True
        ai_settings.last_button = "game_process"
        ai_settings.game_menu_settings_lvl1_active = False
        
        screen.fill((30,30,30))
        
        pygame.draw.rect(screen,(35,35,35),(590,240,1200,755))
        pygame.draw.rect(screen,(40,40,40),(590,240,1200,755),3)
        pygame.draw.line(screen,(15,15,15),[595,390+ai_settings.slider_move],[1790,390+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,540+ai_settings.slider_move],[1790,540+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,690+ai_settings.slider_move],[1790,690+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,840+ai_settings.slider_move],[1790,840+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,990+ai_settings.slider_move],[1790,990+ai_settings.slider_move],1)
        pygame.draw.line(screen,(15,15,15),[595,1140+ai_settings.slider_move],[1790,1140+ai_settings.slider_move],1)
        
        
        screen.blit(logo,(100,80))        
        
        
# Кнопка "Подсказки"
# Button 'advices'
def check_advices(ai_settings,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    if mouse_x > 1500 and mouse_x < 1700 and mouse_y > (304+ai_settings.slider_move) and mouse_y < (334+ai_settings.slider_move) and button_clicked:
        
        if ai_settings.advices:
            ai_settings.advices = False
        else:
            ai_settings.advices = True
        
# Отрисовка кнопки "Подсказки"
# Draw button 'advices'      
def draw_advices(ai_settings,screen):
    font = pygame.font.SysFont('AlundraText',43)
    
    if ai_settings.selected_language==0:
        text = font.render("Подсказки",True,(220,220,220))
        screen.blit(text,(650,288+ai_settings.slider_move))
    else:
        text = font.render("Advices",True,(220,220,220))
        screen.blit(text,(650,288+ai_settings.slider_move))
    
    pygame.draw.rect(screen,(15,15,15),(1526,301+ai_settings.slider_move,206,36),4)
    pygame.draw.rect(screen,(150,150,150),(1530,304+ai_settings.slider_move,200,30))
    
    if ai_settings.selected_language==0:
        text = font.render("Вкл",True,(220,220,220))
        text1 = font.render("Выкл",True,(220,220,220))
    else:
        text = font.render("On",True,(220,220,220))
        text1 = font.render("Off",True,(220,220,220))  
    
    if ai_settings.advices:
        pygame.draw.rect(screen,(230,230,230),(1630,304+ai_settings.slider_move,99,30))
        screen.blit(text,(1405,299+ai_settings.slider_move))
    else:
        pygame.draw.rect(screen,(230,230,230),(1530,304+ai_settings.slider_move,99,30))
        screen.blit(text1,(1405,299+ai_settings.slider_move))
        
# Кнопка "Автоматические добивающие удары"
# Button "automatic finishers"
def check_death_blow(ai_settings,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    if mouse_x > 1500 and mouse_x < 1700 and mouse_y > (454+ai_settings.slider_move) and mouse_y < (484+ai_settings.slider_move) and button_clicked:
        
        if ai_settings.death_blow:
            ai_settings.death_blow = False
        else:
            ai_settings.death_blow = True
        
# Отрисовка кнопки "Автоматические добивающие удары"
# Draw button "automatic finishers"       
def draw_death_blow(ai_settings,screen):
    font = pygame.font.SysFont('AlundraText',43) 
    
    if ai_settings.selected_language==0:
        text = font.render("Автоматические добивающие удары",True,(220,220,220))
        screen.blit(text,(650,449+ai_settings.slider_move))
    else:
        text = font.render("Automatic finishers",True,(220,220,220))
        screen.blit(text,(650,449+ai_settings.slider_move))
    
    pygame.draw.rect(screen,(15,15,15),(1526,451+ai_settings.slider_move,206,36),4)
    pygame.draw.rect(screen,(150,150,150),(1530,454+ai_settings.slider_move,200,30))
    
    if ai_settings.selected_language==0:
        text = font.render("Вкл",True,(220,220,220))
        text1 = font.render("Выкл",True,(220,220,220))
    else:
        text = font.render("On",True,(220,220,220))
        text1 = font.render("Off",True,(220,220,220))  
    
    if ai_settings.death_blow:
        pygame.draw.rect(screen,(230,230,230),(1630,454+ai_settings.slider_move,99,30))
        screen.blit(text,(1405,449+ai_settings.slider_move))
    else:
        pygame.draw.rect(screen,(230,230,230),(1530,454+ai_settings.slider_move,99,30))
        screen.blit(text1,(1405,449+ai_settings.slider_move))       

# Кнопка "Ведьмачье чутье без эффекта рыбьего глаза"
# Button "Turn off witcher senses fish-eye effect"
def check_witcher_vision(ai_settings,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    if mouse_x > 1500 and mouse_x < 1700 and mouse_y > (604+ai_settings.slider_move) and mouse_y < (634+ai_settings.slider_move) and button_clicked:
        
        if ai_settings.witcher_vision:
            ai_settings.witcher_vision = False
        else:
            ai_settings.witcher_vision = True
        
# Отрисовка кнопки "Ведьмачье чутье без эффекта рыбьего глаза"
# Draw button "Turn off witcher senses fish-eye effect"        
def draw_witcher_vision(ai_settings,screen):
    
    font = pygame.font.SysFont('AlundraText',43) 
    if ai_settings.selected_language==0:
        text = font.render('Отключить эффект "рыбьего глаза"',True,(220,220,220))
        screen.blit(text,(650,599+ai_settings.slider_move))
    else:
        text = font.render('Turn off fish-eye effect',True,(220,220,220))
        screen.blit(text,(650,599+ai_settings.slider_move))
    
    pygame.draw.rect(screen,(15,15,15),(1526,601+ai_settings.slider_move,206,36),4)
    pygame.draw.rect(screen,(150,150,150),(1530,604+ai_settings.slider_move,200,30))
    
    if ai_settings.selected_language==0:
        text = font.render("Вкл",True,(220,220,220))
        text1 = font.render("Выкл",True,(220,220,220))
    else:
        text = font.render("On",True,(220,220,220))
        text1 = font.render("Off",True,(220,220,220))  
    
    if ai_settings.witcher_vision:
        pygame.draw.rect(screen,(230,230,230),(1630,604+ai_settings.slider_move,99,30))
        screen.blit(text,(1405,599+ai_settings.slider_move))
    else:
        pygame.draw.rect(screen,(230,230,230),(1530,604+ai_settings.slider_move,99,30))
        screen.blit(text1,(1405,599+ai_settings.slider_move))


# Кнопка "Автосохранение"
# Button "Quicksave"
def check_auto_save(ai_settings,arrow_left,arrow_right,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button1 = arrow_left.rect.collidepoint(mouse_x,mouse_y)
    mouse_on_button2 = arrow_right.rect.collidepoint(mouse_x,mouse_y)
    
    if mouse_on_button1 and button_clicked and ai_settings.auto_save > 1:
        ai_settings.auto_save -= 1
    
    elif mouse_on_button2 and button_clicked and ai_settings.auto_save < 20:
        ai_settings.auto_save += 1
        
# Отрисовка кнопки "Автосохранение"
# Draw button "Quicksave"        
def draw_auto_save(ai_settings,arrow_left,arrow_right,screen):
    
    font = pygame.font.SysFont('AlundraText',43) 
    if ai_settings.selected_language==0:
        text = font.render('Быстрое сохранение(мин)',True,(220,220,220))
        screen.blit(text,(650,749+ai_settings.slider_move))
    else:
        text = font.render('Quicksave(min)',True,(220,220,220))
        screen.blit(text,(650,749+ai_settings.slider_move))
    
    font = pygame.font.SysFont('AlundraText',58)
        
    text = font.render(str(ai_settings.auto_save),True,(220,220,220))
    
    if ai_settings.auto_save < 10:
        screen.blit(text,(1560,739+ai_settings.slider_move))
    else:
        screen.blit(text,(1552,739+ai_settings.slider_move))
      
    if ai_settings.auto_save == 1:
        arrow_right.rect.y = 745+ai_settings.slider_move
        arrow_right.render(screen)
    elif ai_settings.auto_save == 20:
        arrow_left.rect.y = 745+ai_settings.slider_move
        arrow_left.render(screen)
    else:
        arrow_right.rect.y = 745+ai_settings.slider_move
        arrow_left.rect.y = 745+ai_settings.slider_move
        arrow_left.render(screen)
        arrow_right.render(screen)
               
        
# Кнопка "Повышение уровня противника"
# Button "Enemy upscaling"
def check_upgrade_enemy_level(ai_settings,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    if mouse_x > 1500 and mouse_x < 1700 and mouse_y > (904+ai_settings.slider_move) and mouse_y < (934+ai_settings.slider_move) and button_clicked:
        
        if ai_settings.upgrade_enemy_level:
            ai_settings.upgrade_enemy_level = False
        else:
            ai_settings.upgrade_enemy_level = True
        
# Отрисовка кнопки "Повышение уровня противника"
# Draw button "Enemy upscaling"        
def draw_upgrade_enemy_level(ai_settings,screen):

    font = pygame.font.SysFont('AlundraText',43)    
    if ai_settings.selected_language==0:
        text = font.render('Повышение уровня противников',True,(220,220,220))
        screen.blit(text,(650,899+ai_settings.slider_move))
    else:
        text = font.render('Enemy upscaling',True,(220,220,220))
        screen.blit(text,(650,899+ai_settings.slider_move))
    
    pygame.draw.rect(screen,(15,15,15),(1526,901+ai_settings.slider_move,206,36),4)
    pygame.draw.rect(screen,(150,150,150),(1530,904+ai_settings.slider_move,200,30))
    
    if ai_settings.selected_language==0:
        text = font.render("Вкл",True,(220,220,220))
        text1 = font.render("Выкл",True,(220,220,220))
    else:
        text = font.render("On",True,(220,220,220))
        text1 = font.render("Off",True,(220,220,220))  
    
    if ai_settings.upgrade_enemy_level:
        pygame.draw.rect(screen,(230,230,230),(1630,904+ai_settings.slider_move,99,30))
        screen.blit(text,(1405,899+ai_settings.slider_move))
    else:
        pygame.draw.rect(screen,(230,230,230),(1530,904+ai_settings.slider_move,99,30))
        screen.blit(text1,(1405,899+ai_settings.slider_move))
        
        
# Кнопка "Уровень сложности гвинт"
# Button "Difficulty level gwent"
def check_upgrade_enemy_level_gwent(ai_settings,arrow_left,arrow_right,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button1 = arrow_left.rect.collidepoint(mouse_x,mouse_y)
    mouse_on_button2 = arrow_right.rect.collidepoint(mouse_x,mouse_y)
    
    if mouse_on_button1 and button_clicked and ai_settings.selected_level_gwent > 0:
        ai_settings.selected_level_gwent -= 1
    
    elif mouse_on_button2 and button_clicked and (ai_settings.selected_level_gwent+1) < len(ai_settings.upgrade_enemy_level_gwent):
        ai_settings.selected_level_gwent += 1
        
        
def draw_upgrade_enemy_level_gwent(ai_settings,arrow_left,arrow_right,screen):
    font = pygame.font.SysFont('AlundraText',43)  
    if ai_settings.selected_language==0:
        text = font.render('Уровень сложности гвинта',True,(220,220,220))
        screen.blit(text,(650,1049+ai_settings.slider_move))
    else:
        text = font.render('Difficulty level gwent',True,(220,220,220))
        screen.blit(text,(650,1049+ai_settings.slider_move))
    
    font = pygame.font.SysFont('AlundraText',58)
    
    if ai_settings.selected_language==0:  
        text = font.render(str(ai_settings.upgrade_enemy_level_gwent_rus[ai_settings.selected_level_gwent]),True,(220,220,220))
        
        if ai_settings.selected_level_gwent == 1:
            screen.blit(text,(1505,1029+ai_settings.slider_move))
        elif ai_settings.selected_level_gwent == 2:
            screen.blit(text,(1505,1029+ai_settings.slider_move))
        else:
            screen.blit(text,(1515,1029+ai_settings.slider_move))
    else:
        text = font.render(str(ai_settings.upgrade_enemy_level_gwent[ai_settings.selected_level_gwent]),True,(220,220,220))
        
        if ai_settings.selected_level_gwent == 1:
            screen.blit(text,(1500,1029+ai_settings.slider_move))
        else:
            screen.blit(text,(1530,1029+ai_settings.slider_move))

         
    if ai_settings.selected_level_gwent == 0:
        arrow_right.rect.y = 1045+ai_settings.slider_move
        arrow_right.render(screen)
    elif (ai_settings.selected_level_gwent+1) == len(ai_settings.upgrade_enemy_level_gwent):
        arrow_left.rect.y = 1045+ai_settings.slider_move
        arrow_left.render(screen)
    else:
        arrow_right.rect.y = 1045+ai_settings.slider_move
        arrow_left.rect.y = 1045+ai_settings.slider_move
        arrow_left.render(screen)
        arrow_right.render(screen)
        
# Создаем и проверяем слайдер
# Make and check slider
def check_gameplay_slider(ai_settings,slider,scroll):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_on_slider = slider.rect.collidepoint(mouse_x,mouse_y)
     
    if slider.rect.top > 242 and slider.rect.bottom < 990:
            
            if scroll == 'up':
                slider.rect.centery -= 99
                ai_settings.slider_move += 22

            elif scroll == 'down':
                slider.rect.centery += 99
                ai_settings.slider_move -= 22
            else:
                
                if mouse_pressed[0] and mouse_on_slider:
                
                    if slider.rect.centery < mouse_y:
                        ai_settings.slider_move -= ((mouse_y - slider.rect.centery)*3.5)
                    elif slider.rect.centery > mouse_y:
                        ai_settings.slider_move += ((slider.rect.centery - mouse_y)*3.5)
                
                    slider.rect.centery = mouse_y
            
            
    if slider.rect.top <= 242:
        slider.rect.top = 243
        
    if slider.rect.bottom >= 990:
        slider.rect.bottom = 989
            
    if slider.rect.top <= 295:
        ai_settings.slider_move = 0
            
    if slider.rect.bottom >= 989:
        ai_settings.slider_move = -150
            
#----------------------------------------------------------     
# Видео
# Video
def check_video_settings_game_menu(ai_settings,screen,video_settings_button,logo=None,button_clicked=False,draw_menu=False,sound1=None,sound2=None):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button = video_settings_button.rect.collidepoint(mouse_x,mouse_y)

    if button_clicked and mouse_on_button:
        sound2.play()
        draw_menu = True
    else:
        if mouse_on_button:
            video_settings_button.frame = True
            video_settings_button.prep_msg(video_settings_button.msg)
        
            if video_settings_button.sound_count < 1:
                sound1.play()
                video_settings_button.sound_count += 1
        else:
            video_settings_button.frame = False
            video_settings_button.prep_msg(video_settings_button.msg)
            video_settings_button.sound_count = 0

    draw_video_settings_game_menu(ai_settings,screen,logo,draw_menu)

# Отрисовка меню видео настроек
# Draw video options menu
def draw_video_settings_game_menu(ai_settings,screen,logo,draw_menu=False):
    
    if draw_menu:
        ai_settings.game_menu_settings_lvl2_active = True
        ai_settings.last_button = "video"
        ai_settings.game_menu_settings_lvl1_active = False
        
        
        pygame.draw.rect(screen,(30,30,30),(100,0,400,1080))
        screen.blit(logo,(100,80))
  
#----------------------------------------------------------------------------------        
# Меню интерфейса
# Interface options menu
def check_interface_settings(ai_settings,screen,interface_settings_button,slider=None,logo=None,button_clicked=False,draw_menu=False,sound1=False,sound2=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button = interface_settings_button.rect.collidepoint(mouse_x,mouse_y)

    if button_clicked and mouse_on_button:
        sound2.play()
        draw_menu = True
        ai_settings.slider_move = 0
        slider.rect.top = 243
    else:
        if mouse_on_button:
            interface_settings_button.frame = True
            interface_settings_button.prep_msg(interface_settings_button.msg)
        
            if interface_settings_button.sound_count < 1:
                sound1.play()
                interface_settings_button.sound_count += 1
        else:
            interface_settings_button.frame = False
            interface_settings_button.prep_msg(interface_settings_button.msg)
            interface_settings_button.sound_count = 0
            
    draw_interface_settings_game_menu(ai_settings,screen,logo,draw_menu)
    
# Настройки интерфейса
# Interface options   
def draw_interface_settings_game_menu(ai_settings,screen,logo,draw_menu=False):
    
    if draw_menu:
        ai_settings.game_menu_settings_lvl4_active = True
        ai_settings.last_button = "interface_settings"
        ai_settings.game_menu_settings_lvl3_active = False
        
        screen.fill((30,30,30))
        
        pygame.draw.rect(screen,(35,35,35),(590,240,1200,755))
        pygame.draw.rect(screen,(40,40,40),(590,240,1200,755),3)
               
        
        screen.blit(logo,(100,80))
        
# Отрисовка настроек интерфейса
# Draw interface options     
def draw_interface_settings(ai_settings,screen):
    pygame.draw.line(screen,(15,15,15),[595,390+ai_settings.slider_move],[1790,390+ai_settings.slider_move],1)
    pygame.draw.line(screen,(15,15,15),[595,540+ai_settings.slider_move],[1790,540+ai_settings.slider_move],1)
    pygame.draw.line(screen,(15,15,15),[595,690+ai_settings.slider_move],[1790,690+ai_settings.slider_move],1)
    pygame.draw.line(screen,(15,15,15),[595,840+ai_settings.slider_move],[1790,840+ai_settings.slider_move],1)
    pygame.draw.line(screen,(15,15,15),[595,990+ai_settings.slider_move],[1790,990+ai_settings.slider_move],1)
    
    pygame.draw.line(screen,(15,15,15),[595,1140+ai_settings.slider_move],[1790,1140+ai_settings.slider_move],1)
    pygame.draw.line(screen,(15,15,15),[595,1290+ai_settings.slider_move],[1790,1290+ai_settings.slider_move],1)
    pygame.draw.line(screen,(15,15,15),[595,1440+ai_settings.slider_move],[1790,1440+ai_settings.slider_move],1)
    pygame.draw.line(screen,(15,15,15),[595,1590+ai_settings.slider_move],[1790,1590+ai_settings.slider_move],1)
    pygame.draw.line(screen,(15,15,15),[595,1740+ai_settings.slider_move],[1790,1740+ai_settings.slider_move],1)
    
    pygame.draw.line(screen,(15,15,15),[595,1890+ai_settings.slider_move],[1790,1890+ai_settings.slider_move],1)
    pygame.draw.line(screen,(15,15,15),[595,2040+ai_settings.slider_move],[1790,2040+ai_settings.slider_move],1)
    pygame.draw.line(screen,(15,15,15),[595,2190+ai_settings.slider_move],[1790,2190+ai_settings.slider_move],1)
    pygame.draw.line(screen,(15,15,15),[595,2340+ai_settings.slider_move],[1790,2340+ai_settings.slider_move],1)
    pygame.draw.line(screen,(15,15,15),[595,2490+ai_settings.slider_move],[1790,2490+ai_settings.slider_move],1)
    
    font = pygame.font.SysFont('AlundraText',48)  
    
    if ai_settings.selected_language==0:
        text = font.render("Интерфейс",True,(220,220,220))
        screen.blit(text,(685,302+ai_settings.slider_move))
        text = font.render("Журнал действий",True,(220,220,220))
        screen.blit(text,(685,452+ai_settings.slider_move))
        text = font.render("Мини-карта",True,(220,220,220))
        screen.blit(text,(685,602+ai_settings.slider_move))
        text = font.render("Неоткрытые места на карте",True,(220,220,220))
        screen.blit(text,(685,752+ai_settings.slider_move))
        text = font.render("Исследованные точки на карте",True,(220,220,220))
        screen.blit(text,(685,902+ai_settings.slider_move))
    
        text = font.render("Показывать активные задания",True,(220,220,220))
        screen.blit(text,(685,1052+ai_settings.slider_move))
        text = font.render("Действующие эффекты",True,(220,220,220))
        screen.blit(text,(685,1202+ai_settings.slider_move))
        text = font.render("Шкала воздуха",True,(220,220,220))
        screen.blit(text,(685,1352+ai_settings.slider_move))
        text = font.render("Поврежденные предметы",True,(220,220,220))
        screen.blit(text,(685,1502+ai_settings.slider_move))
        text = font.render("Шкала босса",True,(220,220,220))
        screen.blit(text,(685,1652+ai_settings.slider_move))
    
        text = font.render("Шкала противника",True,(220,220,220))
        screen.blit(text,(685,1802+ai_settings.slider_move))
        text = font.render("Названия трав",True,(220,220,220))
        screen.blit(text,(685,1952+ai_settings.slider_move))
        text = font.render("Прочность лодки",True,(220,220,220))
        screen.blit(text,(685,2102+ai_settings.slider_move))
        text = font.render("Тревога лошади",True,(220,220,220))
        screen.blit(text,(685,2252+ai_settings.slider_move))
        text = font.render("Энергия лошади",True,(220,220,220))
        screen.blit(text,(685,2402+ai_settings.slider_move))
    else:
        text = font.render("Interface",True,(220,220,220))
        screen.blit(text,(685,302+ai_settings.slider_move))
        text = font.render("Action log",True,(220,220,220))
        screen.blit(text,(685,452+ai_settings.slider_move))
        text = font.render("Minimap",True,(220,220,220))
        screen.blit(text,(685,602+ai_settings.slider_move))
        text = font.render("Undiscovered POIs on minimap",True,(220,220,220))
        screen.blit(text,(685,752+ai_settings.slider_move))
        text = font.render("Completed POIs on minimap",True,(220,220,220))
        screen.blit(text,(685,902+ai_settings.slider_move))
        text = font.render("Active quests",True,(220,220,220))
        screen.blit(text,(685,1052+ai_settings.slider_move))
        text = font.render("Display current buffs",True,(220,220,220))
        screen.blit(text,(685,1202+ai_settings.slider_move))
        text = font.render("Breath remaining bar",True,(220,220,220))
        screen.blit(text,(685,1352+ai_settings.slider_move))
        text = font.render("Damaged items",True,(220,220,220))
        screen.blit(text,(685,1502+ai_settings.slider_move))
        text = font.render("Boss health bar",True,(220,220,220))
        screen.blit(text,(685,1652+ai_settings.slider_move))
        text = font.render("Enemy health bar",True,(220,220,220))
        screen.blit(text,(685,1802+ai_settings.slider_move))
        text = font.render("Herb names",True,(220,220,220))
        screen.blit(text,(685,1952+ai_settings.slider_move))
        text = font.render("Boat durablity",True,(220,220,220))
        screen.blit(text,(685,2102+ai_settings.slider_move))
        text = font.render("Horse fear bar",True,(220,220,220))
        screen.blit(text,(685,2252+ai_settings.slider_move))
        text = font.render("Horse stamina bar",True,(220,220,220))
        screen.blit(text,(685,2402+ai_settings.slider_move))
    
# Создаем и проверяем слайдер
# Make and check slider
def check_interface_settings_slider(ai_settings,slider,scroll):  
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_on_slider = slider.rect.collidepoint(mouse_x,mouse_y)
    
    if slider.rect.top > 242 and slider.rect.bottom < 990:
            
            if scroll == 'up':
                slider.rect.centery -= 10
                ai_settings.slider_move += 23

            elif scroll == 'down':
                slider.rect.centery += 10
                ai_settings.slider_move -= 23
            else:
                
                if mouse_pressed[0] and mouse_on_slider:
                
                    if slider.rect.centery < mouse_y:
                        ai_settings.slider_move -= ((mouse_y - slider.rect.centery)*2.3)
                    elif slider.rect.centery > mouse_y:
                        ai_settings.slider_move += ((slider.rect.centery - mouse_y)*2.3)
                
                    slider.rect.centery = mouse_y
            
            
    if slider.rect.top <= 242:
        slider.rect.top = 243
        
    if slider.rect.bottom >= 990:
        slider.rect.bottom = 989
            
    if slider.rect.top <= 295:
        ai_settings.slider_move = 0
            
    if slider.rect.bottom >= 989:
        ai_settings.slider_move = -1500
            

# Кнопка "Интерфейс"
# Button "Interface"
def check_interface(ai_settings,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    if mouse_x > 1500 and mouse_x < 1700 and mouse_y > (304+ai_settings.slider_move) and mouse_y < (334+ai_settings.slider_move) and button_clicked:
        
        if ai_settings.interface:
            ai_settings.interface = False
        else:
            ai_settings.interface = True
        
# Отрисовка кнопки "Интерфейс"
# Draw button "Interface"      
def draw_interface(ai_settings,screen):
    
    font = pygame.font.SysFont('AlundraText',48) 
       
    pygame.draw.rect(screen,(15,15,15),(1526,304+ai_settings.slider_move,206,36),4)
    pygame.draw.rect(screen,(150,150,150),(1530,307+ai_settings.slider_move,200,30))
    
    if ai_settings.selected_language==0:
        text = font.render("Вкл",True,(220,220,220))
        text1 = font.render("Выкл",True,(220,220,220))
    else:
        text = font.render("On",True,(220,220,220))
        text1 = font.render("Off",True,(220,220,220))
    
    if ai_settings.interface:
        pygame.draw.rect(screen,(230,230,230),(1630,307+ai_settings.slider_move,99,30))
        screen.blit(text,(1405,302+ai_settings.slider_move))
    else:
        pygame.draw.rect(screen,(230,230,230),(1530,307+ai_settings.slider_move,99,30))
        screen.blit(text1,(1405,302+ai_settings.slider_move))
        

# Кнопка "Журнал действий"
# Button "Action log"
def check_action_log(ai_settings,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    if mouse_x > 1500 and mouse_x < 1700 and mouse_y > (454+ai_settings.slider_move) and mouse_y < (484+ai_settings.slider_move) and button_clicked:
        
        if ai_settings.action_log:
            ai_settings.action_log = False
        else:
            ai_settings.action_log = True
        
# Отрисовка кнопки "Журнал действий"
# Draw button "Action log"
def draw_action_log(ai_settings,screen):
    
    font = pygame.font.SysFont('AlundraText',48) 
       
    pygame.draw.rect(screen,(15,15,15),(1526,454+ai_settings.slider_move,206,36),4)
    pygame.draw.rect(screen,(150,150,150),(1530,457+ai_settings.slider_move,200,30))
    
    if ai_settings.selected_language==0:
        text = font.render("Вкл",True,(220,220,220))
        text1 = font.render("Выкл",True,(220,220,220))
    else:
        text = font.render("On",True,(220,220,220))
        text1 = font.render("Off",True,(220,220,220))
    
    if ai_settings.action_log:
        pygame.draw.rect(screen,(230,230,230),(1630,457+ai_settings.slider_move,99,30))
        screen.blit(text,(1405,452+ai_settings.slider_move))
    else:
        pygame.draw.rect(screen,(230,230,230),(1530,457+ai_settings.slider_move,99,30))
        screen.blit(text1,(1405,452+ai_settings.slider_move))
        
# Кнопка "Миникарта"
# Button "Minimap"
def check_mini_map(ai_settings,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    if mouse_x > 1500 and mouse_x < 1700 and mouse_y > (604+ai_settings.slider_move) and mouse_y < (634+ai_settings.slider_move) and button_clicked:
        
        if ai_settings.mini_map:
            ai_settings.mini_map = False
        else:
            ai_settings.mini_map = True
            
# Отрисовка кнопки "Миникарта"
# Draw button "Minimap"   
def draw_mini_map(ai_settings,screen):
    
    font = pygame.font.SysFont('AlundraText',48) 
       
    pygame.draw.rect(screen,(15,15,15),(1526,604+ai_settings.slider_move,206,36),4)
    pygame.draw.rect(screen,(150,150,150),(1530,607+ai_settings.slider_move,200,30))
    
    if ai_settings.selected_language==0:
        text = font.render("Вкл",True,(220,220,220))
        text1 = font.render("Выкл",True,(220,220,220))
    else:
        text = font.render("On",True,(220,220,220))
        text1 = font.render("Off",True,(220,220,220))
    
    if ai_settings.mini_map:
        pygame.draw.rect(screen,(230,230,230),(1630,607+ai_settings.slider_move,99,30))
        screen.blit(text,(1405,602+ai_settings.slider_move))
    else:
        pygame.draw.rect(screen,(230,230,230),(1530,607+ai_settings.slider_move,99,30))
        screen.blit(text1,(1405,602+ai_settings.slider_move))
        
        
# Кнопка "Скрытые места"
# Button "hidden_places"
def check_hidden_places(ai_settings,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    if mouse_x > 1500 and mouse_x < 1700 and mouse_y > (754+ai_settings.slider_move) and mouse_y < (784+ai_settings.slider_move) and button_clicked:
        
        if ai_settings.hidden_places:
            ai_settings.hidden_places = False
        else:
            ai_settings.hidden_places = True
        
# Отрисовка кнопки "Скрытые места"
# Draw button "hidden_places"     
def draw_hidden_places(ai_settings,screen):
    
    font = pygame.font.SysFont('AlundraText',48) 
       
    pygame.draw.rect(screen,(15,15,15),(1526,754+ai_settings.slider_move,206,36),4)
    pygame.draw.rect(screen,(150,150,150),(1530,757+ai_settings.slider_move,200,30))
    
    if ai_settings.selected_language==0:
        text = font.render("Вкл",True,(220,220,220))
        text1 = font.render("Выкл",True,(220,220,220))
    else:
        text = font.render("On",True,(220,220,220))
        text1 = font.render("Off",True,(220,220,220))
    
    if ai_settings.hidden_places:
        pygame.draw.rect(screen,(230,230,230),(1630,757+ai_settings.slider_move,99,30))
        screen.blit(text,(1405,752+ai_settings.slider_move))
    else:
        pygame.draw.rect(screen,(230,230,230),(1530,757+ai_settings.slider_move,99,30))
        screen.blit(text1,(1405,752+ai_settings.slider_move))
        
        
# Кнопка "Исследованные точки"
# Button "explored_places"  
def check_explored_places(ai_settings,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    if mouse_x > 1500 and mouse_x < 1700 and mouse_y > (904+ai_settings.slider_move) and mouse_y < (934+ai_settings.slider_move) and button_clicked:
        
        if ai_settings.explored_places:
            ai_settings.explored_places = False
        else:
            ai_settings.explored_places = True
        
# Отрисовка кнопки "Исследованные точки"
# Draw button "explored_places"   
def draw_explored_places(ai_settings,screen):
    
    font = pygame.font.SysFont('AlundraText',48) 
       
    pygame.draw.rect(screen,(15,15,15),(1526,904+ai_settings.slider_move,206,36),4)
    pygame.draw.rect(screen,(150,150,150),(1530,907+ai_settings.slider_move,200,30))
    
    if ai_settings.selected_language==0:
        text = font.render("Вкл",True,(220,220,220))
        text1 = font.render("Выкл",True,(220,220,220))
    else:
        text = font.render("On",True,(220,220,220))
        text1 = font.render("Off",True,(220,220,220))
    
    if ai_settings.explored_places:
        pygame.draw.rect(screen,(230,230,230),(1630,907+ai_settings.slider_move,99,30))
        screen.blit(text,(1405,902+ai_settings.slider_move))
    else:
        pygame.draw.rect(screen,(230,230,230),(1530,907+ai_settings.slider_move,99,30))
        screen.blit(text1,(1405,902+ai_settings.slider_move))
    
# Кнопка "Показывать активные задания"
# Button "active_task" 
def check_active_task(ai_settings,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    if mouse_x > 1500 and mouse_x < 1700 and mouse_y > (1054+ai_settings.slider_move) and mouse_y < (1084+ai_settings.slider_move) and button_clicked:
        
        if ai_settings.active_task:
            ai_settings.active_task = False
        else:
            ai_settings.active_task = True
        
# Отрисовка кнопки "Показывать активные задания"
# Draw button "active_task"          
def draw_active_task(ai_settings,screen):
    
    font = pygame.font.SysFont('AlundraText',48) 
       
    pygame.draw.rect(screen,(15,15,15),(1526,1054+ai_settings.slider_move,206,36),4)
    pygame.draw.rect(screen,(150,150,150),(1530,1057+ai_settings.slider_move,200,30))
    
    if ai_settings.selected_language==0:
        text = font.render("Вкл",True,(220,220,220))
        text1 = font.render("Выкл",True,(220,220,220))
    else:
        text = font.render("On",True,(220,220,220))
        text1 = font.render("Off",True,(220,220,220))
    
    if ai_settings.active_task:
        pygame.draw.rect(screen,(230,230,230),(1630,1057+ai_settings.slider_move,99,30))
        screen.blit(text,(1405,1052+ai_settings.slider_move))
    else:
        pygame.draw.rect(screen,(230,230,230),(1530,1057+ai_settings.slider_move,99,30))
        screen.blit(text1,(1405,1052+ai_settings.slider_move))
        
        
# Кнопка "Показывать действующие эффекты"
# Button "active_effect" 
def check_active_effect(ai_settings,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    if mouse_x > 1500 and mouse_x < 1700 and mouse_y > (1204+ai_settings.slider_move) and mouse_y < (1234+ai_settings.slider_move) and button_clicked:
        
        if ai_settings.active_effect:
            ai_settings.active_effect = False
        else:
            ai_settings.active_effect = True
        
# Отрисовка кнопки "Показывать действующие эффекты"
# Draw button "active_effect"     
def draw_active_effect(ai_settings,screen):
    
    font = pygame.font.SysFont('AlundraText',48) 
       
    pygame.draw.rect(screen,(15,15,15),(1526,1204+ai_settings.slider_move,206,36),4)
    pygame.draw.rect(screen,(150,150,150),(1530,1207+ai_settings.slider_move,200,30))
    
    if ai_settings.selected_language==0:
        text = font.render("Вкл",True,(220,220,220))
        text1 = font.render("Выкл",True,(220,220,220))
    else:
        text = font.render("On",True,(220,220,220))
        text1 = font.render("Off",True,(220,220,220))
    
    if ai_settings.active_effect:
        pygame.draw.rect(screen,(230,230,230),(1630,1207+ai_settings.slider_move,99,30))
        screen.blit(text,(1405,1202+ai_settings.slider_move))
    else:
        pygame.draw.rect(screen,(230,230,230),(1530,1207+ai_settings.slider_move,99,30))
        screen.blit(text1,(1405,1202+ai_settings.slider_move))
        
        
# Кнопка "Шкала воздуха"
# Button "air_bar" 
def check_air(ai_settings,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    if mouse_x > 1500 and mouse_x < 1700 and mouse_y > (1354+ai_settings.slider_move) and mouse_y < (1384+ai_settings.slider_move) and button_clicked:
        
        if ai_settings.air:
            ai_settings.air = False
        else:
            ai_settings.air = True
        
# Отрисовка кнопки "Шкала воздуха"
# Draw button "air_bar"       
def draw_air(ai_settings,screen):
    
    font = pygame.font.SysFont('AlundraText',48) 
       
    pygame.draw.rect(screen,(15,15,15),(1526,1354+ai_settings.slider_move,206,36),4)
    pygame.draw.rect(screen,(150,150,150),(1530,1357+ai_settings.slider_move,200,30))
    
    if ai_settings.selected_language==0:
        text = font.render("Вкл",True,(220,220,220))
        text1 = font.render("Выкл",True,(220,220,220))
    else:
        text = font.render("On",True,(220,220,220))
        text1 = font.render("Off",True,(220,220,220))
    
    if ai_settings.air:
        pygame.draw.rect(screen,(230,230,230),(1630,1357+ai_settings.slider_move,99,30))
        screen.blit(text,(1405,1352+ai_settings.slider_move))
    else:
        pygame.draw.rect(screen,(230,230,230),(1530,1357+ai_settings.slider_move,99,30))
        screen.blit(text1,(1405,1352+ai_settings.slider_move))  
        
# Кнопка "Поврежденые предметы"
# Button "damaged_things" 
def check_damaged_things(ai_settings,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    if mouse_x > 1500 and mouse_x < 1700 and mouse_y > (1504+ai_settings.slider_move) and mouse_y < (1534+ai_settings.slider_move) and button_clicked:
        
        if ai_settings.damaged_things:
            ai_settings.damaged_things = False
        else:
            ai_settings.damaged_things = True
        
# Отрисовка кнопки "Поврежденые предметы"
# Draw button "damaged_things"      
def draw_damaged_things(ai_settings,screen):
    font = pygame.font.SysFont('AlundraText',48) 
       
    pygame.draw.rect(screen,(15,15,15),(1526,1504+ai_settings.slider_move,206,36),4)
    pygame.draw.rect(screen,(150,150,150),(1530,1507+ai_settings.slider_move,200,30))
    
    if ai_settings.selected_language==0:
        text = font.render("Вкл",True,(220,220,220))
        text1 = font.render("Выкл",True,(220,220,220))
    else:
        text = font.render("On",True,(220,220,220))
        text1 = font.render("Off",True,(220,220,220))
    
    if ai_settings.damaged_things:
        pygame.draw.rect(screen,(230,230,230),(1630,1507+ai_settings.slider_move,99,30))
        screen.blit(text,(1405,1502+ai_settings.slider_move))
    else:
        pygame.draw.rect(screen,(230,230,230),(1530,1507+ai_settings.slider_move,99,30))
        screen.blit(text1,(1405,1502+ai_settings.slider_move))
        
# Кнопка "Шкала босса"
# Button "boss_hp" 
def check_boss_hp(ai_settings,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    if mouse_x > 1500 and mouse_x < 1700 and mouse_y > (1654+ai_settings.slider_move) and mouse_y < (1684+ai_settings.slider_move) and button_clicked:
        
        if ai_settings.boss_hp:
            ai_settings.boss_hp = False
        else:
            ai_settings.boss_hp = True
        
# Отрисовка кнопки "Шкала босса"
# Draw button "boss_hp"   
def draw_boss_hp(ai_settings,screen):
    
    font = pygame.font.SysFont('AlundraText',48) 
       
    pygame.draw.rect(screen,(15,15,15),(1526,1654+ai_settings.slider_move,206,36),4)
    pygame.draw.rect(screen,(150,150,150),(1530,1657+ai_settings.slider_move,200,30))
    
    if ai_settings.selected_language==0:
        text = font.render("Вкл",True,(220,220,220))
        text1 = font.render("Выкл",True,(220,220,220))
    else:
        text = font.render("On",True,(220,220,220))
        text1 = font.render("Off",True,(220,220,220))
    
    if ai_settings.boss_hp:
        pygame.draw.rect(screen,(230,230,230),(1630,1657+ai_settings.slider_move,99,30))
        screen.blit(text,(1405,1652+ai_settings.slider_move))
    else:
        pygame.draw.rect(screen,(230,230,230),(1530,1657+ai_settings.slider_move,99,30))
        screen.blit(text1,(1405,1652+ai_settings.slider_move))
        
# Кнопка "Шкала противника"
# Button "enemy_hp" 
def check_enemy_hp(ai_settings,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    if mouse_x > 1500 and mouse_x < 1700 and mouse_y > (1804+ai_settings.slider_move) and mouse_y < (1834+ai_settings.slider_move) and button_clicked:
        
        if ai_settings.enemy_hp:
            ai_settings.enemy_hp = False
        else:
            ai_settings.enemy_hp = True
        
# Отрисовка кнопки "Шкала противника"
# Draw button "enemy_hp"          
def draw_enemy_hp(ai_settings,screen):
    
    font = pygame.font.SysFont('AlundraText',48) 
       
    pygame.draw.rect(screen,(15,15,15),(1526,1804+ai_settings.slider_move,206,36),4)
    pygame.draw.rect(screen,(150,150,150),(1530,1807+ai_settings.slider_move,200,30))
    
    if ai_settings.selected_language==0:
        text = font.render("Вкл",True,(220,220,220))
        text1 = font.render("Выкл",True,(220,220,220))
    else:
        text = font.render("On",True,(220,220,220))
        text1 = font.render("Off",True,(220,220,220))
    
    if ai_settings.enemy_hp:
        pygame.draw.rect(screen,(230,230,230),(1630,1807+ai_settings.slider_move,99,30))
        screen.blit(text,(1405,1802+ai_settings.slider_move))
    else:
        pygame.draw.rect(screen,(230,230,230),(1530,1807+ai_settings.slider_move,99,30))
        screen.blit(text1,(1405,1802+ai_settings.slider_move))  
        
# Кнопка "Названия трав"
# Button "herbs_labels" 
def check_herbs_labels(ai_settings,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    if mouse_x > 1500 and mouse_x < 1700 and mouse_y > (1954+ai_settings.slider_move) and mouse_y < (1984+ai_settings.slider_move) and button_clicked:
        
        if ai_settings.herbs_labels:
            ai_settings.herbs_labels = False
        else:
            ai_settings.herbs_labels = True
        
# Отрисовка кнопки "Названия трав"
# Draw button "herbs_labels"      
def draw_herbs_labels(ai_settings,screen):
    font = pygame.font.SysFont('AlundraText',48) 
       
    pygame.draw.rect(screen,(15,15,15),(1526,1954+ai_settings.slider_move,206,36),4)
    pygame.draw.rect(screen,(150,150,150),(1530,1957+ai_settings.slider_move,200,30))
    
    if ai_settings.selected_language==0:
        text = font.render("Вкл",True,(220,220,220))
        text1 = font.render("Выкл",True,(220,220,220))
    else:
        text = font.render("On",True,(220,220,220))
        text1 = font.render("Off",True,(220,220,220))
    
    if ai_settings.herbs_labels:
        pygame.draw.rect(screen,(230,230,230),(1630,1957+ai_settings.slider_move,99,30))
        screen.blit(text,(1405,1952+ai_settings.slider_move))
    else:
        pygame.draw.rect(screen,(230,230,230),(1530,1957+ai_settings.slider_move,99,30))
        screen.blit(text1,(1405,1952+ai_settings.slider_move))
        

# Кнопка "Прочность лодки"
# Button "boat_hp" 
def check_boat_hp(ai_settings,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    if mouse_x > 1500 and mouse_x < 1700 and mouse_y > (2104+ai_settings.slider_move) and mouse_y < (2134+ai_settings.slider_move) and button_clicked:
        
        if ai_settings.boat_hp:
            ai_settings.boat_hp = False
        else:
            ai_settings.boat_hp = True
        
# Отрисовка кнопки "Прочность лодки"
# Draw button "boat_hp"      
def draw_boat_hp(ai_settings,screen):
    font = pygame.font.SysFont('AlundraText',48) 
       
    pygame.draw.rect(screen,(15,15,15),(1526,2104+ai_settings.slider_move,206,36),4)
    pygame.draw.rect(screen,(150,150,150),(1530,2107+ai_settings.slider_move,200,30))
    
    if ai_settings.selected_language==0:
        text = font.render("Вкл",True,(220,220,220))
        text1 = font.render("Выкл",True,(220,220,220))
    else:
        text = font.render("On",True,(220,220,220))
        text1 = font.render("Off",True,(220,220,220))
    
    if ai_settings.boat_hp:
        pygame.draw.rect(screen,(230,230,230),(1630,2107+ai_settings.slider_move,99,30))
        screen.blit(text,(1405,2102+ai_settings.slider_move))
    else:
        pygame.draw.rect(screen,(230,230,230),(1530,2107+ai_settings.slider_move,99,30))
        screen.blit(text1,(1405,2102+ai_settings.slider_move))
        
        
# Кнопка "Тревога лошади"
# Button "horse_anxiety" 
def check_horse_anxiety(ai_settings,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    if mouse_x > 1500 and mouse_x < 1700 and mouse_y > (2254+ai_settings.slider_move) and mouse_y < (2284+ai_settings.slider_move) and button_clicked:
        
        if ai_settings.horse_anxiety:
            ai_settings.horse_anxiety = False
        else:
            ai_settings.horse_anxiety = True
        
# Отрисовка кнопки "Тревога лошади"
# Draw button "horse_anxiety"          
def draw_horse_anxiety(ai_settings,screen):
    font = pygame.font.SysFont('AlundraText',48) 
       
    pygame.draw.rect(screen,(15,15,15),(1526,2254+ai_settings.slider_move,206,36),4)
    pygame.draw.rect(screen,(150,150,150),(1530,2257+ai_settings.slider_move,200,30))
    
    if ai_settings.selected_language==0:
        text = font.render("Вкл",True,(220,220,220))
        text1 = font.render("Выкл",True,(220,220,220))
    else:
        text = font.render("On",True,(220,220,220))
        text1 = font.render("Off",True,(220,220,220))
    
    if ai_settings.horse_anxiety:
        pygame.draw.rect(screen,(230,230,230),(1630,2257+ai_settings.slider_move,99,30))
        screen.blit(text,(1405,2252+ai_settings.slider_move))
    else:
        pygame.draw.rect(screen,(230,230,230),(1530,2257+ai_settings.slider_move,99,30))
        screen.blit(text1,(1405,2252+ai_settings.slider_move))
        
        
# Кнопка "Энергия лошади"
# Button "horse_energy" 
def check_horse_energy(ai_settings,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    
    if mouse_x > 1500 and mouse_x < 1700 and mouse_y > (2404+ai_settings.slider_move) and mouse_y < (2434+ai_settings.slider_move) and button_clicked:
        
        if ai_settings.horse_energy:
            ai_settings.horse_energy = False
        else:
            ai_settings.horse_energy = True
        
# Отрисовка кнопки "Энергия лошади"
# Draw button "horse_energy"        
def draw_horse_energy(ai_settings,screen):
    font = pygame.font.SysFont('AlundraText',48) 
       
    pygame.draw.rect(screen,(15,15,15),(1526,2404+ai_settings.slider_move,206,36),4)
    pygame.draw.rect(screen,(150,150,150),(1530,2407+ai_settings.slider_move,200,30))
    
    if ai_settings.selected_language==0:
        text = font.render("Вкл",True,(220,220,220))
        text1 = font.render("Выкл",True,(220,220,220))
    else:
        text = font.render("On",True,(220,220,220))
        text1 = font.render("Off",True,(220,220,220))
    
    if ai_settings.horse_energy:
        pygame.draw.rect(screen,(230,230,230),(1630,2407+ai_settings.slider_move,99,30))
        screen.blit(text,(1405,2402+ai_settings.slider_move))
    else:
        pygame.draw.rect(screen,(230,230,230),(1530,2407+ai_settings.slider_move,99,30))
        screen.blit(text1,(1405,2402+ai_settings.slider_move))
  
        
#---------------------------------------------------------------------------------------------------------    
# Общие настройки
# Graphics
def check_general_settings(ai_settings,screen,general_settings_button,logo=None,button_clicked=False,draw_menu=False,sound1=False,sound2=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button = general_settings_button.rect.collidepoint(mouse_x,mouse_y)

    if button_clicked and mouse_on_button:
        sound2.play()
        draw_menu = True
    else:
        if mouse_on_button:
            general_settings_button.frame = True
            general_settings_button.prep_msg(general_settings_button.msg)
        
            if general_settings_button.sound_count < 1:
                sound1.play()
                general_settings_button.sound_count += 1
        else:
            general_settings_button.frame = False
            general_settings_button.prep_msg(general_settings_button.msg)
            general_settings_button.sound_count = 0
            
    draw_general_settings_game_menu(ai_settings,screen,logo,draw_menu)
    
# Отрисовка меню общих настроек
# Draw button general_settings menu 
def draw_general_settings_game_menu(ai_settings,screen,logo,draw_menu=False):
    
    if draw_menu:
        ai_settings.game_menu_settings_lvl4_active = True
        ai_settings.last_button = "general_settings"
        ai_settings.game_menu_settings_lvl3_active = False
        
        screen.fill((30,30,30))
        
        pygame.draw.rect(screen,(35,35,35),(590,240,1200,455))
        pygame.draw.rect(screen,(40,40,40),(590,240,1200,455),3)
        pygame.draw.line(screen,(15,15,15),[595,390],[1790,390],1)
        pygame.draw.line(screen,(15,15,15),[595,540],[1790,540],1)
        pygame.draw.line(screen,(15,15,15),[595,690],[1790,690],1)
        
        
        screen.blit(logo,(100,80))
        
# Количество кадров в секунду
# FPS
def check_FPS(ai_settings,arrow_left,arrow_right,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button1 = arrow_left.rect.collidepoint(mouse_x,mouse_y)
    mouse_on_button2 = arrow_right.rect.collidepoint(mouse_x,mouse_y)
    
    if mouse_on_button1 and button_clicked and ai_settings.FPS > 30:
        ai_settings.FPS -= 30
    
    elif mouse_on_button2 and button_clicked and ai_settings.FPS < 60:
        ai_settings.FPS += 30
        
# Отрисовка кнопки FPS
# Draw FPS button   
def draw_FPS(ai_settings,arrow_left,arrow_right,screen):
    font = pygame.font.SysFont('AlundraText',43) 
    text = font.render('FPS',True,(220,220,220))
    screen.blit(text,(640,294))
    
    font = pygame.font.SysFont('AlundraText',58)
        
    text = font.render(str(ai_settings.FPS),True,(220,220,220))
    
    screen.blit(text,(1557,294))
      
    if ai_settings.FPS == 30:
        arrow_right.render(screen)
    elif ai_settings.FPS == 60:
        arrow_left.render(screen)
    else:
        arrow_left.render(screen)
        arrow_right.render(screen)
        
        
# Количество персонажей
# Count NPC
def check_count_NPC(ai_settings,arrow_left,arrow_right,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button1 = arrow_left.rect.collidepoint(mouse_x,mouse_y)
    mouse_on_button2 = arrow_right.rect.collidepoint(mouse_x,mouse_y)
    
    if mouse_on_button1 and button_clicked and ai_settings.selected_count_NPC > 0:
        ai_settings.selected_count_NPC -= 1
    
    elif mouse_on_button2 and button_clicked and (ai_settings.selected_count_NPC+1) < len(ai_settings.count_NPC):
        ai_settings.selected_count_NPC += 1
        
# Отрисовка кнопки count NPC
# Draw count NPC button       
def draw_count_NPC(ai_settings,arrow_left,arrow_right,screen):
    
    font = pygame.font.SysFont('AlundraText',43)
    if ai_settings.selected_language==0:
        text = font.render('Количество NPC',True,(220,220,220))
    else:
        text = font.render('Count NPC',True,(220,220,220))
    screen.blit(text,(640,444))
    
    font = pygame.font.SysFont('AlundraText',58)
    
    if ai_settings.selected_language==0:
        text = font.render(str(ai_settings.count_NPC_rus[ai_settings.selected_count_NPC]),True,(220,220,220))

        if ai_settings.selected_count_NPC == 0:
            screen.blit(text,(1520,441))
        elif ai_settings.selected_count_NPC == 2:
            screen.blit(text,(1510,441))
        else:
            screen.blit(text,(1510,441))
            
    else:
        text = font.render(str(ai_settings.count_NPC[ai_settings.selected_count_NPC]),True,(220,220,220))
    
        if ai_settings.selected_count_NPC == 0 or ai_settings.selected_count_NPC == 2:
            screen.blit(text,(1535,441))
        else:
            screen.blit(text,(1490,441))
         
    if ai_settings.selected_count_NPC == 0:
        arrow_right.render(screen)
    elif (ai_settings.selected_count_NPC+1) == len(ai_settings.count_NPC):
        arrow_left.render(screen)
    else:
        arrow_left.render(screen)
        arrow_right.render(screen)
        
        
# Количество растительности
# Count plants
def check_count_plants(ai_settings,arrow_left,arrow_right,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button1 = arrow_left.rect.collidepoint(mouse_x,mouse_y)
    mouse_on_button2 = arrow_right.rect.collidepoint(mouse_x,mouse_y)
    
    if mouse_on_button1 and button_clicked and ai_settings.selected_count_plants > 0:
        ai_settings.selected_count_plants -= 1
    
    elif mouse_on_button2 and button_clicked and (ai_settings.selected_count_plants+1) < len(ai_settings.count_plants):
        ai_settings.selected_count_plants += 1
        
# Отрисовка кнопки count plants
# Draw count plants button   
def draw_count_plants(ai_settings,arrow_left,arrow_right,screen):
    
    font = pygame.font.SysFont('AlundraText',43) 
    if ai_settings.selected_language==0:
        text = font.render('Количество растительности',True,(220,220,220))
    else:
        text = font.render('Count plants',True,(220,220,220))
    screen.blit(text,(640,594))
    
    font = pygame.font.SysFont('AlundraText',58)

    if ai_settings.selected_language==0:
        text = font.render(str(ai_settings.count_plants_rus[ai_settings.selected_count_plants]),True,(220,220,220))
        if ai_settings.selected_count_plants == 0:
            screen.blit(text,(1520,591))
        elif ai_settings.selected_count_plants == 2:
            screen.blit(text,(1510,591))
        else:
            screen.blit(text,(1510,591))
    else:
        text = font.render(str(ai_settings.count_plants[ai_settings.selected_count_plants]),True,(220,220,220))
        if ai_settings.selected_count_plants == 0 or ai_settings.selected_count_plants == 2:
            screen.blit(text,(1535,591))
        else:
            screen.blit(text,(1490,591))
         
    if ai_settings.selected_count_plants == 0:
        arrow_right.render(screen)
    elif (ai_settings.selected_count_plants+1) == len(ai_settings.count_plants):
        arrow_left.render(screen)
    else:
        arrow_left.render(screen)
        arrow_right.render(screen)
#------------------------------------------------------------------    
def change_text_language(ai_settings,play_button,new_game_button,load_button,
                        settings_button,exit_button,back_button,
                        audio_settings_button,video_settings_button,language_settings_button,
                        keys_settings_button,game_process_settings_button,
                        interface_settings_button,general_settings_button,
                        yes_button,no_button,difficulty1_button,difficulty2_button,
                        difficulty3_button,difficulty4_button,start_game_button):
    
    
    if ai_settings.selected_language == 0:
        play_button.msg="Играть"
        new_game_button.msg='Новая игра'
        load_button.msg='Загрузить игру'
        settings_button.msg='Настройки'
        exit_button.msg='Выход'
        back_button.msg='Назад'
        audio_settings_button.msg="Аудио"
        video_settings_button.msg='Видео'
        language_settings_button.msg='Локализация'
        keys_settings_button.msg='Привязки клавиш'
        game_process_settings_button.msg='Игровой процесс'
        interface_settings_button.msg='Интерфейс'
        general_settings_button.msg='Общие'
        yes_button.msg='Да'
        no_button.msg='Нет'
        difficulty1_button.msg='Только сюжет'
        difficulty2_button.msg='Сюжет и драки'
        difficulty3_button.msg='Боль и страдания'
        difficulty4_button.msg='На смерть'
        start_game_button.msg='Начать'
        
    elif ai_settings.selected_language == 1:
        play_button.msg='Play'
        new_game_button.msg='New game'
        load_button.msg='Load game'
        settings_button.msg='Options'
        exit_button.msg='Exit'
        back_button.msg='Back'
        audio_settings_button.msg='Audio'
        video_settings_button.msg='Video'
        language_settings_button.msg='Language'
        keys_settings_button.msg='Key bindings'
        game_process_settings_button.msg='Gameplay'
        interface_settings_button.msg='Interface'
        general_settings_button.msg='Graphics'
        yes_button.msg='Yes'
        no_button.msg='No'
        difficulty1_button.msg='Just the story'
        difficulty2_button.msg='Story and sword'
        difficulty3_button.msg='Blood and bones'
        difficulty4_button.msg='Death march'
        start_game_button.msg='Start'

# Язык
# Language
def check_language_settings_game_menu(ai_settings,screen,language_settings_button,logo=None,button_clicked=False,draw_menu=False,sound1=None,sound2=None):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button = language_settings_button.rect.collidepoint(mouse_x,mouse_y)
    
    if button_clicked and mouse_on_button:
        sound2.play()
        draw_menu = True
    else:
        if mouse_on_button:
            language_settings_button.frame = True
            language_settings_button.prep_msg(language_settings_button.msg)
        
            if language_settings_button.sound_count < 1:
                sound1.play()
                language_settings_button.sound_count += 1
        else:
            language_settings_button.frame = False
            language_settings_button.prep_msg(language_settings_button.msg)
            language_settings_button.sound_count = 0
            
    draw_language_settings_game_menu(ai_settings,screen,logo,draw_menu)
    
# Отрисовка меню локализации
# Draw language menu   
def draw_language_settings_game_menu(ai_settings,screen,logo,draw_menu=False):
    
    if draw_menu:
        ai_settings.game_menu_settings_lvl2_active = True
        ai_settings.last_button = "language"
        ai_settings.game_menu_settings_lvl1_active = False
        
        screen.fill((30,30,30))
        
        pygame.draw.rect(screen,(35,35,35),(590,240,1200,455))
        pygame.draw.rect(screen,(40,40,40),(590,240,1200,455),3)
        pygame.draw.line(screen,(15,15,15),[595,390],[1790,390],1)
        pygame.draw.line(screen,(15,15,15),[595,540],[1790,540],1)
        pygame.draw.line(screen,(15,15,15),[595,690],[1790,690],1)
        
        font = pygame.font.SysFont('AlundraText',58)
        
        if ai_settings.selected_language==0:
            text = font.render('Язык',True,(220,220,220))
            screen.blit(text,(700,285))
            
            text = font.render('Голос',True,(220,220,220))
            screen.blit(text,(700,435))
            
            text = font.render('Субтитры',True,(220,220,220))
            screen.blit(text,(700,585))        
        else:
            text = font.render('Language',True,(220,220,220))
            screen.blit(text,(700,285))
            
            text = font.render('Voice',True,(220,220,220))
            screen.blit(text,(700,435))
            
            text = font.render('Subtitles',True,(220,220,220))
            screen.blit(text,(700,585))   
        screen.blit(logo,(100,80))

#----------------------------------------------------------        
# Проверка языка
# Сheck language
def check_language(ai_settings,arrow_left,arrow_right,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button1 = arrow_left.rect.collidepoint(mouse_x,mouse_y)
    mouse_on_button2 = arrow_right.rect.collidepoint(mouse_x,mouse_y)
    
    if mouse_on_button1 and button_clicked and ai_settings.selected_language==1:
        ai_settings.selected_language = 0
    
    elif mouse_on_button2 and button_clicked and (ai_settings.selected_language+1) < len(ai_settings.languages):
        ai_settings.selected_language = 1
            
# Отрисовка кнопки язык
# Draw language button  
def draw_language(ai_settings,screen,arrow_left,arrow_right):
    
    font = pygame.font.SysFont('AlundraText',58)
        
    text = font.render(str(ai_settings.languages[ai_settings.selected_language]),True,(220,220,220))
    
    if (ai_settings.selected_language+1) == len(ai_settings.languages):
        screen.blit(text,(1490,290))
    else:
        screen.blit(text,(1470,290))
    
    
    if ai_settings.selected_language == 0:
        arrow_right.render(screen)
    elif (ai_settings.selected_language+1) == len(ai_settings.languages):
        arrow_left.render(screen)
    else:
        arrow_left.render(screen)
        arrow_right.render(screen)
        

#----------------------------------------------------------        
# Проверка языка озвучки
# Сheck voice language   
def check_voice_language(ai_settings,arrow_left,arrow_right,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button1 = arrow_left.rect.collidepoint(mouse_x,mouse_y)
    mouse_on_button2 = arrow_right.rect.collidepoint(mouse_x,mouse_y)
    
    if mouse_on_button1 and button_clicked and ai_settings.selected_voice_language > 0:
        ai_settings.selected_voice_language -= 1
    
    elif mouse_on_button2 and button_clicked and (ai_settings.selected_voice_language+1) < len(ai_settings.languages):
        ai_settings.selected_voice_language += 1
    
# Отрисовка кнопки голос
# Draw voice language button 
def draw_voice_language(ai_settings,screen,arrow_left,arrow_right):
    font = pygame.font.SysFont('AlundraText',58)
        
    text = font.render(str(ai_settings.languages[ai_settings.selected_voice_language]),True,(220,220,220))
    
    if (ai_settings.selected_voice_language+1) == len(ai_settings.languages):
        screen.blit(text,(1490,440))
    else:
        screen.blit(text,(1470,440))
     
    if ai_settings.selected_voice_language == 0:
        arrow_right.render(screen)
    elif (ai_settings.selected_voice_language+1) == len(ai_settings.languages):
        arrow_left.render(screen)
    else:
        arrow_left.render(screen)
        arrow_right.render(screen)
        

#----------------------------------------------------------        
# Проверка языка субтитров
# Сheck subtitles language     
def check_subtitles_language(ai_settings,arrow_left,arrow_right,button_clicked=False):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button1 = arrow_left.rect.collidepoint(mouse_x,mouse_y)
    mouse_on_button2 = arrow_right.rect.collidepoint(mouse_x,mouse_y)
    
    if mouse_on_button1 and button_clicked and ai_settings.selected_subtitles_language > 0:
        ai_settings.selected_subtitles_language -= 1
    
    elif mouse_on_button2 and button_clicked and (ai_settings.selected_subtitles_language+1) < len(ai_settings.languages):
        ai_settings.selected_subtitles_language += 1
    
# Отрисовка кнопки язык субтитров
# Draw subtitles language button   
def draw_subtitles_language(ai_settings,screen,arrow_left,arrow_right):
    font = pygame.font.SysFont('AlundraText',58)
        
    text = font.render(str(ai_settings.languages[ai_settings.selected_subtitles_language]),True,(220,220,220))
    
    if (ai_settings.selected_subtitles_language+1) == len(ai_settings.languages):
        screen.blit(text,(1490,590))
    else:
        screen.blit(text,(1470,590))
    
    if ai_settings.selected_subtitles_language == 0:
        arrow_right.render(screen)
    elif (ai_settings.selected_subtitles_language+1) == len(ai_settings.languages):
        arrow_left.render(screen)
    else:
        arrow_left.render(screen)
        arrow_right.render(screen)
    
# Проверка кнопки выхода из игры
# Check exit button  
#------------------------------------------------------------------------------------------------
def check_exit_button(exit_button,button_clicked=False,sound=None):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button = exit_button.rect.collidepoint(mouse_x,mouse_y)

    if button_clicked and mouse_on_button:
        sys.exit()
    else:
        if mouse_on_button:
            exit_button.frame = True
            exit_button.prep_msg(exit_button.msg)
        
            if exit_button.sound_count < 1:
                sound.play()
                exit_button.sound_count += 1
        else:
            exit_button.frame = False
            exit_button.prep_msg(exit_button.msg)
            exit_button.sound_count = 0

#---------------------------------------------------------------------------
# Проверка кнопки назад в разных меню
# Check back button  
def check_back_button(ai_settings,back_button,button_clicked=False,sound1=None,sound2=None):
    mouse_x,mouse_y = pygame.mouse.get_pos()
    mouse_on_button = back_button.rect.collidepoint(mouse_x,mouse_y)
    if mouse_on_button:
        back_button.frame = True
        back_button.prep_msg(back_button.msg)
        
        if back_button.sound_count < 1:
            sound1.play()
            back_button.sound_count += 1
    else:
        back_button.frame = False
        back_button.prep_msg(back_button.msg)
        back_button.sound_count = 0
    
    # Меняем позицию, когда глубоко заходим в настройки
    # Change positon when go to another level
    if ai_settings.game_menu_settings_lvl2_active or ai_settings.game_menu_settings_lvl3_active:
        back_button.y = 570
        back_button.rect = pygame.Rect(back_button.x,back_button.y,
                                    back_button.width,back_button.height)
        back_button.prep_msg(back_button.msg)
    elif ai_settings.game_menu_settings_lvl1_active and (ai_settings.last_button == "new_game" or ai_settings.last_button == "load_game"):
        back_button.y = 570
        back_button.rect = pygame.Rect(back_button.x,back_button.y,
                                    back_button.width,back_button.height)
        back_button.prep_msg(back_button.msg)
    else:
        back_button.y = 870
        back_button.rect = pygame.Rect(back_button.x,back_button.y,
                                    back_button.width,back_button.height)
        back_button.prep_msg(back_button.msg)
        
    if mouse_on_button and button_clicked:
        sound2.play()
        if ai_settings.game_menu_settings_lvl1_active and not ai_settings.game_menu_settings_lvl2_active:
            ai_settings.game_menu_settings_lvl1_active = False
        if ai_settings.game_menu_settings_lvl3_active:
            ai_settings.game_menu_settings_lvl3_active = False
            ai_settings.game_menu_settings_lvl2_active = True
        if ai_settings.game_menu_settings_lvl2_active:
            ai_settings.game_menu_settings_lvl2_active = False
            ai_settings.game_menu_settings_lvl1_active = True
        if ai_settings.game_menu_settings_lvl4_active:
            ai_settings.game_menu_settings_lvl4_active = False
            ai_settings.game_menu_settings_lvl3_active = True
        if ai_settings.game_menu_active and not ai_settings.game_menu_settings_lvl1_active and not ai_settings.game_menu_settings_lvl2_active:
            ai_settings.game_menu_active = False