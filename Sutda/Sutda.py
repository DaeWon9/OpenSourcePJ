import pygame
import random
from variable import *
from objects import *
from my_funtions import *

# text
game_font = pygame.font.Font("D2Coding-Ver1.3.2-20180524-all.ttc", 16) # create font
user_name_text = game_font.render(com_name, True, (255,255,255))
com_money_text = game_font.render(user_name, True, (255, 255 ,255))
com_name_text = game_font.render(convert_money(com_money), True, (255, 255, 255))
user_money_text = game_font.render(convert_money(user_money), True, (255, 255, 255))
bet_money_text = game_font.render(convert_money(bet_money), True, (255, 255, 255))
call_money_text = game_font.render(convert_money(call_money), True, (255, 255, 255))
coin_money_text = game_font.render("+" + convert_money(coin_money), True, (0, 0, 255))


if (__name__ == "__main__"): # main 함수임
    entire_loop = True
    start_menu = True
    mode_select_menu = False
    explain_menu = False
    move_map = False
    sutda_map = False

    while(entire_loop): # entire loop
        while(start_menu):
            window.blit(main_background, (0,0)) # main_background draw
            start_button.draw(window)
            explain_button.draw(window)
            #info_button.draw(window)
            pygame.display.update() # display refresh

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if (event.type == pygame.QUIT): #quit event
                    entire_loop = False
                    start_menu = False
                if (event.type == pygame.MOUSEBUTTONDOWN): 
                    if (start_button.in_locate(pos)): # game_start button click down
                        mode_select_menu = True
                        start_menu = False
                        pass
                    if (explain_button.in_locate(pos)): # explain button click down
                        #explain_menu = True
                        #start_menu = False
                        pass

        while(mode_select_menu):
            window.blit(nick_background, (0,0)) # nick_background draw
            backstage_button.draw(window)
            continue_start_button.draw(window)
            new_start_button.draw(window)
            pygame.display.update() # display refresh

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if (event.type == pygame.QUIT): #quit event
                    entire_loop = False
                    mode_select_menu = False                
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if (backstage_button.in_locate(pos)):
                        start_menu = True
                        mode_select_menu = False
                    if (continue_start_button.in_locate(pos)):
                        mode_select_menu = False
                        move_map = True
                    if (new_start_button.in_locate(pos)):
                        user_money = 1000000
                        save_money = 0
                        mode_select_menu = False
                        move_map = True
                        #nick_menu = True
        while(move_map):
            window.blit(move_map_background, (0,-150)) # move_map_background draw
            backstage_button.draw(window)
            bag_button.draw(window)
            save_info_button.draw(window)
            Neo.draw(window)
            Apeach.draw(window)
            SafeBox.draw(window)
            window.blit(character, (character_x_pos, character_y_pos))

            user_name_text = game_font.render("닉네임 : " + user_name, True, (0, 0 ,0))
            window.blit(user_name_text,(1, 1)) #user name
            if (coin_money == 0):
                user_money_text = game_font.render("보유금액 : " + convert_money(user_money), True, (0, 0, 0))
            else:
                user_money_text = game_font.render("보유금액 : " + convert_money(user_money) + " +" + convert_money(coin_money), True, (255, 180, 0))
            window.blit(user_money_text,(1, 20)) #user money
            user_speed_text = game_font.render("이동속도 : " + str(int(character_speed * 100)), True, (0, 0, 255))
            window.blit(user_speed_text,(1, 40)) #user speed
            pygame.display.update() # display refresh

            for event in pygame.event.get(): #event check
                pos = pygame.mouse.get_pos()
                if (event.type == pygame.QUIT): #quit event
                    entire_loop = False
                    move_map = False 

                if (event.type == pygame.KEYDOWN): #keydown event
                    if (event.key == pygame.K_LEFT):
                        move_x = move_x - character_speed
                    elif (event.key == pygame.K_RIGHT):
                        move_x = move_x + character_speed
                    elif (event.key == pygame.K_DOWN):
                        move_y = move_y + character_speed
                    elif (event.key == pygame.K_UP):
                        move_y = move_y - character_speed
                
                if (event.type == pygame.KEYUP): #keyup event
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                        move_x = 0
                    elif (event.key == pygame.K_DOWN or event.key == pygame.K_UP):
                        move_y = 0
                
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if (Apeach.in_locate(pos)): #Apeach 클릭시 게임시작
                        # sutda_map = True
                        # move_map = False
                        pass
                    if (backstage_button.in_locate(pos)): #뒤로가기버튼 클릭
                        start_menu = True
                        move_map = False

            character_x_pos = character_x_pos + (move_x * fps)
            character_y_pos = character_y_pos + (move_y * fps)


            if character_x_pos < 0: # character x좌표 조정 
                character_x_pos = 0
            elif character_x_pos > window_width - character_width:
                character_x_pos = window_width - character_width


            if character_y_pos < 310: # character y좌표 조정 
                character_y_pos = 310
            elif character_y_pos > window_height - character_width:
                character_y_pos = window_height - character_width

        while(sutda_map):
            pass
    