'''
Created on 14 июн. 2020 г.

@author: Артем
'''
import pygame
from main_menu import *

# Отслеживание событий клавиатуры и мыши
# Check keyboard and mouse events
def check_events(ai_settings,screen,play_button,new_game_button,load_button,
                        settings_button,exit_button,logo,back_button,
                        audio_settings_button,video_settings_button,
                        language_settings_button,keys_settings_button,
                        game_process_settings_button,
                        interface_settings_button,
                        general_settings_button,
                        yes_button,no_button,
                        difficulty1_button,difficulty2_button,
                        difficulty3_button,difficulty4_button,
                        start_game_button,slider,
                        arrow_left1,arrow_right1,
                        arrow_left2,arrow_right2,
                        arrow_left3,arrow_right3,
                        arrow_left4,arrow_right4,
                        arrow_left5,arrow_right5,
                        arrow_left6,arrow_right6,
                        arrow_left7,arrow_right7,
                        arrow_left8,arrow_right8,
                        sound1,sound2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            button_clicked = True
            scroll = False
            # ЛКМ
            # LMB
            if event.button == 1:
                
                if not ai_settings.game_active:        
                    
                    if ai_settings.game_menu_active:
                        
                        # Первый уровень меню настроек
                        # First level of options menu
                        if ai_settings.game_menu_settings_lvl1_active:             
                            if ai_settings.last_button == "settings":
                                check_audio_settings_game_menu(ai_settings,screen,audio_settings_button,logo,button_clicked,False,sound1,sound2)
                                check_video_settings_game_menu(ai_settings,screen,video_settings_button,logo,button_clicked,False,sound1,sound2)
                                check_language_settings_game_menu(ai_settings,screen,language_settings_button,logo,button_clicked,False,sound1,sound2)
                                check_keys_settings_game_menu(ai_settings,screen,keys_settings_button,slider,logo,button_clicked,False,sound1,sound2)
                                check_game_process_settings_game_menu(ai_settings,screen,slider,game_process_settings_button,logo,button_clicked,False,sound1,sound2)
                            
                            elif ai_settings.last_button == "new_game":
                                check_load_game_yes_button(ai_settings,yes_button,no_button,button_clicked,sound1,sound2)
                                check_load_game_no_button(ai_settings,no_button,yes_button,button_clicked,sound1,sound2)
                                check_load_game_difficulty1_button(ai_settings,screen,difficulty1_button,difficulty2_button,difficulty3_button,difficulty4_button,button_clicked,sound1,sound2)
                                check_load_game_difficulty2_button(ai_settings,screen,difficulty1_button,difficulty2_button,difficulty3_button,difficulty4_button,button_clicked,sound1,sound2)
                                check_load_game_difficulty3_button(ai_settings,screen,difficulty1_button,difficulty2_button,difficulty3_button,difficulty4_button,button_clicked,sound1,sound2)
                                check_load_game_difficulty4_button(ai_settings,screen,difficulty1_button,difficulty2_button,difficulty3_button,difficulty4_button,button_clicked,sound1,sound2)                         
                                check_load_game_start_game_button(ai_settings,start_game_button,difficulty1_button,difficulty2_button,difficulty3_button,difficulty4_button,yes_button,no_button,button_clicked,sound1,sound2)
                        # Второй уровень меню настроек
                        # Second level of options menu
                        if ai_settings.game_menu_settings_lvl2_active:
                            if ai_settings.last_button == "language":
                                check_language(ai_settings,arrow_left1,arrow_right1,button_clicked)
                                check_voice_language(ai_settings,arrow_left2,arrow_right2,button_clicked)
                                check_subtitles_language(ai_settings,arrow_left3,arrow_right3,button_clicked)
                            
                            elif ai_settings.last_button == "game_process":
                                check_advices(ai_settings,button_clicked)
                                check_death_blow(ai_settings,button_clicked)
                                check_witcher_vision(ai_settings,button_clicked)
                                check_auto_save(ai_settings,arrow_left4,arrow_right4,button_clicked)
                                check_upgrade_enemy_level(ai_settings,button_clicked)
                                check_upgrade_enemy_level_gwent(ai_settings,arrow_left8,arrow_right8,button_clicked)
                                
                        # Третий уровень меню настроек
                        # Third level of options menu
                        if ai_settings.game_menu_settings_lvl3_active:
                            check_interface_settings(ai_settings,screen,interface_settings_button,slider,logo,button_clicked,False,sound1,sound2)
                            check_general_settings(ai_settings,screen,general_settings_button,logo,button_clicked,False,sound1,sound2)
                    
                        # Четвертый уровень меню настроек
                        # Fourth level of options menu
                        if ai_settings.game_menu_settings_lvl4_active:
                            if ai_settings.last_button == "general_settings":
                                check_FPS(ai_settings,arrow_left5,arrow_right5,button_clicked)
                                check_count_NPC(ai_settings,arrow_left6,arrow_right6,button_clicked)
                                check_count_plants(ai_settings,arrow_left7,arrow_right7,button_clicked)
                            elif ai_settings.last_button == "interface_settings":
                                check_interface(ai_settings,button_clicked)
                                check_action_log(ai_settings,button_clicked)
                                check_mini_map(ai_settings,button_clicked)
                                check_hidden_places(ai_settings,button_clicked)
                                check_explored_places(ai_settings,button_clicked)
                                check_active_task(ai_settings,button_clicked)
                                check_active_effect(ai_settings,button_clicked)
                                check_air(ai_settings,button_clicked)
                                check_damaged_things(ai_settings,button_clicked)
                                check_boss_hp(ai_settings,button_clicked)
                                check_enemy_hp(ai_settings,button_clicked)
                                check_herbs_labels(ai_settings,button_clicked)
                                check_boat_hp(ai_settings,button_clicked)
                                check_horse_anxiety(ai_settings,button_clicked)
                                check_horse_energy(ai_settings,button_clicked)
                        
                        check_back_button(ai_settings,back_button,button_clicked,sound1,sound2)
            
                    else:
                        # Нулевой уровень меню настроек
                        # Zero level of options menu
                        check_play_button(ai_settings,play_button,button_clicked,sound1,sound2)
                        check_new_game_button(ai_settings,screen,new_game_button,difficulty1_button,difficulty2_button,difficulty3_button,difficulty4_button,
                                              yes_button,no_button,logo,button_clicked,False,sound1,sound2)
                        check_load_button(ai_settings,screen,load_button,slider,logo,button_clicked,False,sound1,sound2)
                        check_settings_button(ai_settings,screen,settings_button,logo,button_clicked,False,sound1,sound2)
                        check_exit_button(exit_button,button_clicked,sound1)
            
            # Прокручивание колесика вверх
            # Scroll up
            elif event.button == 4:
                
                if ai_settings.game_menu_settings_lvl1_active:                            
                    if ai_settings.last_button == "load_game":
                        scroll = 'up'
                        check_load_game_slider(ai_settings,slider,scroll)
                
                if ai_settings.game_menu_settings_lvl2_active:
                    if ai_settings.last_button == "keys":
                        scroll = 'up'
                        check_keys_slider(ai_settings,slider,scroll)
                    elif ai_settings.last_button == "game_process":
                        scroll = 'up'
                        check_gameplay_slider(ai_settings,slider,scroll)
                        arrow_left8.rect.y+=ai_settings.slider_move/10
                        arrow_right8.rect.y+=ai_settings.slider_move/10
                
                if ai_settings.game_menu_settings_lvl4_active:
                    if ai_settings.last_button == "interface_settings":
                        scroll = 'up'
                        check_interface_settings_slider(ai_settings,slider,scroll)
            
            # Прокручивание колесика вниз
            # Scroll down
            elif event.button == 5:
                
                if ai_settings.game_menu_settings_lvl1_active:               
                    if ai_settings.last_button == "load_game":
                        scroll = 'down'
                        check_load_game_slider(ai_settings,slider,scroll)
                
                if ai_settings.game_menu_settings_lvl2_active:
                    if ai_settings.last_button == "keys":
                        scroll = 'down'
                        check_keys_slider(ai_settings,slider,scroll)
                    if ai_settings.last_button == "game_process":
                        scroll = 'down'
                        check_gameplay_slider(ai_settings,slider,scroll)
                        arrow_left8.rect.y+=ai_settings.slider_move/10
                        arrow_right8.rect.y+=ai_settings.slider_move/10
                
                if ai_settings.game_menu_settings_lvl4_active:
                    if ai_settings.last_button == "interface_settings":
                        scroll = 'down'
                        check_interface_settings_slider(ai_settings,slider,scroll)
            
        button_clicked = False
# Функция обновления экрана
# Redraw the screen
def update_screen(ai_settings,screen,main_menu_animation,logo,play_button,new_game_button,
                load_button,settings_button,exit_button,back_button,
                audio_settings_button,video_settings_button,
                language_settings_button,keys_settings_button,
                game_process_settings_button,
                interface_settings_button,
                general_settings_button,
                yes_button,no_button,
                difficulty1_button,difficulty2_button,
                difficulty3_button,difficulty4_button,
                start_game_button,slider,slider1,
                slider2,slider3,
                arrow_left1,arrow_right1,
                arrow_left2,arrow_right2,
                arrow_left3,arrow_right3,
                arrow_left4,arrow_right4,
                arrow_left5,arrow_right5,
                arrow_left6,arrow_right6,
                arrow_left7,arrow_right7,
                arrow_left8,arrow_right8,
                sound,sounds,main_menu1):
    
    change_text_language(ai_settings,play_button,new_game_button,load_button,
                        settings_button,exit_button,back_button,
                        audio_settings_button,video_settings_button,language_settings_button,
                        keys_settings_button,game_process_settings_button,
                        interface_settings_button,general_settings_button,
                        yes_button,no_button,difficulty1_button,difficulty2_button,
                        difficulty3_button,difficulty4_button,start_game_button)
    
    # Панель главного меню
    # Main menu bar
    if not ai_settings.game_active and not ai_settings.game_menu_active:
        screen.blit(main_menu_animation.get_sprite(),(0,0))
        main_menu_animation.update(60)
        
        pygame.draw.rect(screen,(30,30,30),(100,0,400,1080))
        screen.blit(logo,(100,80))
        
        # Отрисовка и проверка(рамка) кнопки "Играть"
        # Draw and check the "Play" button
        check_play_button(ai_settings,play_button,None,sound)
        play_button.draw_button(screen)
        
        # Отрисовка и проверка(рамка) кнопки "Новая игра"
        # Draw and check the "New game" button
        check_new_game_button(ai_settings,screen,new_game_button,difficulty1_button,difficulty2_button,difficulty3_button,difficulty4_button,yes_button,no_button,
                                logo,None,None,sound)
        new_game_button.draw_button(screen)
        
        # Отрисовка и проверка(рамка) кнопки "Загрузка"
        # Draw and check the "Load game" button
        check_load_button(ai_settings,screen,load_button,slider,logo,None,None,sound)
        load_button.draw_button(screen)
        
        # Отрисовка и проверка(рамка) кнопки "Настройки"
        # Draw and check the "Options" button
        check_settings_button(ai_settings,screen,settings_button,logo,None,None,sound)
        settings_button.draw_button(screen)
        
        # Отрисовка и проверка(рамка) кнопки "Выход из игры"
        # Draw and check the "Exit" button
        check_exit_button(exit_button,None,sound)
        exit_button.draw_button(screen)
        
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)
            
    # Если открыты что-нибудь из меню настроек
    # if options menu is active
    if not ai_settings.game_active and ai_settings.game_menu_active:
        
        # Четвертый уровень меню настроек
        # Fourth level of options menu
        if ai_settings.game_menu_settings_lvl4_active:
            
            if ai_settings.last_button == "general_settings":
                draw_general_settings_game_menu(ai_settings,screen,logo,True)
                draw_FPS(ai_settings,arrow_left5,arrow_right5,screen)
                draw_count_NPC(ai_settings,arrow_left6,arrow_right6,screen)
                draw_count_plants(ai_settings,arrow_left7,arrow_right7,screen)
            elif ai_settings.last_button == "interface_settings":
                draw_interface_settings_game_menu(ai_settings,screen,logo,True)
                draw_interface_settings(ai_settings,screen)
                # Отрисовка полосок
                # Draw bars
                draw_interface(ai_settings,screen)
                draw_action_log(ai_settings,screen)
                draw_mini_map(ai_settings,screen)
                draw_hidden_places(ai_settings,screen)
                draw_explored_places(ai_settings,screen)
                draw_active_task(ai_settings,screen)
                draw_active_effect(ai_settings,screen)
                draw_air(ai_settings,screen)
                draw_damaged_things(ai_settings,screen)
                draw_boss_hp(ai_settings,screen)
                draw_enemy_hp(ai_settings,screen)
                draw_herbs_labels(ai_settings,screen)
                draw_boat_hp(ai_settings,screen)
                draw_horse_anxiety(ai_settings,screen)
                draw_horse_energy(ai_settings,screen)
                
                draw_slider(screen)
                check_interface_settings_slider(ai_settings,slider,False)
                slider.draw_slider(screen)
                
        # Третий уровень меню настроек
        # Third level of options menu      
        elif ai_settings.game_menu_settings_lvl3_active:
            
            screen.blit(main_menu_animation.get_sprite(),(0,0))
            main_menu_animation.update(60)
            
            draw_video_settings_game_menu(ai_settings,screen,logo,True)
            
            check_interface_settings(ai_settings,screen,interface_settings_button,None,logo,False,False,sound,None)
            interface_settings_button.draw_button(screen)
                
            check_general_settings(ai_settings,screen,general_settings_button,logo,False,False,sound,None)
            general_settings_button.draw_button(screen)
            
        # Второй уровень меню настроек
        # Second level of options menu
        elif ai_settings.game_menu_settings_lvl2_active:
            # Проверка, какую кнопку нажали
            # Check which button has pressed
            if ai_settings.last_button == "audio":
                draw_audio_settings_game_menu(ai_settings,screen,logo,True)
                
                draw_music_volume_button(ai_settings,screen)
                set_music_volume(ai_settings,slider1)
                slider1.draw_slider(screen)
                
                draw_sound_volume_button(ai_settings,screen)
                set_sound_volume(ai_settings,sounds,slider2)
                slider2.draw_slider(screen)
                
                draw_voice_volume_button(ai_settings,screen)
                set_voice_volume(ai_settings,slider3)
                slider3.draw_slider(screen)
                
            elif ai_settings.last_button == "video":
                ai_settings.game_menu_settings_lvl2_active = False
                ai_settings.game_menu_settings_lvl3_active = True
                
            elif ai_settings.last_button == "language":     
                draw_language_settings_game_menu(ai_settings,screen,logo,True)
                draw_language(ai_settings,screen,arrow_left1,arrow_right1)
                draw_voice_language(ai_settings,screen,arrow_left2,arrow_right2)
                draw_subtitles_language(ai_settings,screen,arrow_left3,arrow_right3)    

            elif ai_settings.last_button == "keys":
                draw_keys_settings_game_menu(ai_settings,screen,logo,True)
                draw_slider(screen)
                check_keys_slider(ai_settings,slider,False)
                slider.draw_slider(screen)
            elif ai_settings.last_button == "game_process":
                check_gameplay_slider(ai_settings,slider,False)
                draw_game_process_settings_game_menu(ai_settings,screen,logo,True)
                draw_advices(ai_settings,screen)
                draw_death_blow(ai_settings,screen)
                draw_witcher_vision(ai_settings,screen)
                draw_auto_save(ai_settings,arrow_left4,arrow_right4,screen)
                draw_upgrade_enemy_level(ai_settings,screen)
                draw_upgrade_enemy_level_gwent(ai_settings,arrow_left8,arrow_right8,screen) 
                draw_slider(screen)
                slider.draw_slider(screen)
            
        # Первый уровень меню настроек
        # First level of options menu  
        elif ai_settings.game_menu_settings_lvl1_active:      
            if ai_settings.last_button == "new_game":              
                draw_new_game_menu(ai_settings,screen,logo,True)
                
                check_load_game_yes_button(ai_settings,yes_button,no_button,None,sound)
                yes_button.draw_button(screen)
                
                check_load_game_no_button(ai_settings,no_button,yes_button,None,sound)
                no_button.draw_button(screen)
                
                check_load_game_difficulty1_button(ai_settings,screen,difficulty1_button,difficulty2_button,difficulty3_button,difficulty4_button,None,sound)
                difficulty1_button.draw_button(screen)
                
                check_load_game_difficulty2_button(ai_settings,screen,difficulty1_button,difficulty2_button,difficulty3_button,difficulty4_button,None,sound)
                difficulty2_button.draw_button(screen)
                
                check_load_game_difficulty3_button(ai_settings,screen,difficulty1_button,difficulty2_button,difficulty3_button,difficulty4_button,None,sound)
                difficulty3_button.draw_button(screen)
                
                check_load_game_difficulty4_button(ai_settings,screen,difficulty1_button,difficulty2_button,difficulty3_button,difficulty4_button,None,sound)        
                difficulty4_button.draw_button(screen)
                
                check_load_game_start_game_button(ai_settings,start_game_button,difficulty1_button,difficulty2_button,difficulty3_button,difficulty4_button,yes_button,no_button,None,sound)
                start_game_button.draw_button(screen)
                
            elif ai_settings.last_button == "load_game":
                draw_load_game_menu(ai_settings,screen,logo,True)
                check_load_game_slider(ai_settings,slider,False)
                slider.draw_slider(screen)
                draw_slider(screen)
            else:
                screen.blit(main_menu_animation.get_sprite(),(0,0))
                main_menu_animation.update(60)
                       
                draw_settings_game_menu(ai_settings,screen,logo,True)
            
            
                check_audio_settings_game_menu(ai_settings,screen,audio_settings_button,logo,None,None,sound,None)
                audio_settings_button.draw_button(screen)
            
                check_video_settings_game_menu(ai_settings,screen,video_settings_button,logo,None,None,sound,None)
                video_settings_button.draw_button(screen)
            
                check_language_settings_game_menu(ai_settings,screen,language_settings_button,logo,None,None,sound,None)
                language_settings_button.draw_button(screen)
            
                check_keys_settings_game_menu(ai_settings,screen,keys_settings_button,None,logo,None,None,sound,None)
                keys_settings_button.draw_button(screen)
            
                check_game_process_settings_game_menu(ai_settings,screen,slider,game_process_settings_button,logo,None,None,sound,None)
                game_process_settings_button.draw_button(screen)
                    
        # Отрисовка кнопки "Назад"
        # Draw "Back" button
        check_back_button(ai_settings,back_button,False,sound,None)
        back_button.draw_button(screen)
        
        
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)
            
    # Начало игры 
    # The start of the game 
    if ai_settings.game_active:
        screen.blit(main_menu1,(0,0))
        pygame.mixer.music.stop()
       
    #Отображение последнего прорисованного экрана
    #Display the last frame
    pygame.display.flip()
    