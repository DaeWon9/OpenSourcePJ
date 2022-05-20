import pygame
from card import *
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

def computer_betting(value): # value 0 : die, value 1 : 콜, value 2 : 쿼터, value 3 : 하프
    global com_die, com_money, bet_money, call_money, com_bet_result_text
    if (value == 0): # computer die
        com_die = 1
        return "die"
    if (value == 1): # call
        com_money = com_money - call_money
        bet_money = bet_money + call_money
        return "call"
    if (value == 2): # quater
        com_money = com_money - int(bet_money // 4)
        call_money = int(bet_money // 4)
        bet_money = bet_money + int(bet_money // 4)
        return "quater"
    if (value == 3): # half
        com_money = com_money - int(bet_money // 2)
        call_money = int(bet_money // 2)
        bet_money = bet_money + int(bet_money // 2)
        return "half"
def user_betting(value): # value 0 : die, value 1 : 콜, value 2 : 쿼터, value 3 : 하프
    global user_die, user_money, bet_money, call_money
    if (value == 0): # die
        user_die = 0
        return "die"
    if (value == 1): # call
        user_money = user_money - call_money
        bet_money = bet_money + call_money
        return "call"
    if (value == 2): # quater
        user_money = user_money - int(bet_money // 4)
        call_money = int(bet_money // 4)
        bet_money = bet_money + int(bet_money // 4)
        return "quater"
    if (value == 3): # half
        user_money = user_money - int(bet_money // 2)
        call_money = int(bet_money // 2)
        bet_money = bet_money + int(bet_money // 2)
        return "half"

def display_refresh():
    user_name_text = game_font.render(user_name, True, (255, 255 ,255))
    user_name_text_width = game_font.size(user_name)[0]
    com_name_text = game_font.render(com_name, True, (255,255,255))
    com_name_text_width = game_font.size(com_name)[0]
    com_money_text = game_font.render(convert_money(com_money), True, (255, 255, 255))
    user_money_text = game_font.render(convert_money(user_money), True, (255, 255, 255))
    bet_money_text = game_font.render(convert_money(bet_money), True, (255, 255, 255))
    call_money_text = game_font.render(convert_money(call_money), True, (255, 255, 255))
    window.blit(sutda_map_background, (0,0)) # background draw
    window.blit(user_name_text,(85 - user_name_text_width / 2, 360)) #user name
    window.blit(com_name_text,(85 - com_name_text_width / 2, 195))  #com name
    window.blit(first_turn, (first_turn_pos[0], first_turn_pos[1]))
    # character draw
    window.blit(character,(46,268))
    window.blit(apeach_image,(55,100))

    die_button.draw(window)
    call_button.draw(window)
    quater_button.draw(window)
    half_button.draw(window)
    족보_button.draw(window)
    game_start_button.draw(window)
    backstage_button.draw(window)
    user_card1.draw_image(window, 150, 265)
    user_card2.draw_image(window, 205, 265)
    com_card2.draw_image(window, 205,100)
    if (fluoroscope_power_value):
        com_card1.draw_image(window, 150,100)
        com_combination_card.show_card_class(window, 150,180)
    else:
        back_card.draw_image(window, 150,100)
    user_combination_card.show_card_class(window, 150, 345)
    window.blit(com_money_text,(130, 198))   # computer money
    window.blit(user_money_text,(130, 363)) #user money
    window.blit(bet_money_text,(500, 237)) #betting money
    window.blit(call_money_text,(500, 285)) #call money
    if(combination_table == 1):
        window.blit(combination_table_image, (645,50)) # combination_table show
    pygame.display.update() # display refresh

def before_start_display_refresh():
    # sutda_map_back ground draw
    window.blit(sutda_map_background, (0,0)) # background draw
    # refresh name and money info
    user_name_text = game_font.render(user_name, True, (255, 255 ,255))
    user_name_text_width = game_font.size(user_name)[0]
    com_name_text = game_font.render(com_name, True, (255,255,255))
    com_name_text_width = game_font.size(com_name)[0]
    com_money_text = game_font.render(convert_money(com_money), True, (255, 255, 255))
    user_money_text = game_font.render(convert_money(user_money), True, (255, 255, 255))
    bet_money_text = game_font.render(convert_money(bet_money), True, (255, 255, 255))
    call_money_text = game_font.render(convert_money(call_money), True, (255, 255, 255))
    # user and computer name draw
    window.blit(user_name_text,(85 - user_name_text_width / 2, 360)) #user name
    window.blit(com_name_text,(85 - com_name_text_width / 2, 195))  #com name
    # money info draw
    window.blit(com_money_text,(130, 198))   # computer money
    window.blit(user_money_text,(130, 363)) #user money
    window.blit(bet_money_text,(500, 237)) #betting money
    window.blit(call_money_text,(500, 285)) #call money
    # character draw
    window.blit(character,(46,268))
    window.blit(apeach_image,(55,100))

    # button draw    
    die_button.draw(window)
    call_button.draw(window)
    quater_button.draw(window)
    half_button.draw(window)
    족보_button.draw(window)
    game_start_button.draw(window)
    backstage_button.draw(window)
    if(combination_table == 1):
        window.blit(combination_table_image, (645,50)) # combination_table show
    pygame.display.update() # display refresh 

def decide_user_self_betting(): # return 0 : die, return 1 : 콜, return 2 : 쿼터, return 3 : 하프
    global user_bet_value, first_bet, combination_table, entire_loop, sutda_map
    do_bet = True
    while(do_bet):
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT: #quit event
                do_bet = False
                entire_loop = False
                sutda_map = False
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (die_button.in_locate(pos)):
                    do_bet = False
                    user_bet_value = 0 #die
                if (call_button.in_locate(pos)):
                    if (first_bet != 0):
                        do_bet = False
                        user_bet_value = 1 #call
                if (quater_button.in_locate(pos)):
                    if (first_bet != 0):
                        do_bet = False
                        user_bet_value = 2 #quater        
                if (half_button.in_locate(pos)):
                    do_bet = False
                    user_bet_value = 3 #half
                if (족보_button.in_locate(pos) and combination_table == 0):
                    combination_table = 1
                    display_refresh()
                    continue
                if (족보_button.in_locate(pos) and combination_table == 1):
                    combination_table = 0
                    display_refresh()
                    continue      



if (__name__ == "__main__"): # main 함수임
    entire_loop = True
    start_menu = True
    mode_select_menu = False
    explain_menu = False
    move_map = False
    sutda_map = False
    lose_map = False
    win_map = False


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
                        com_name = "어피치LV.1"
                        user_money = 1000000
                        com_money = 1000000
                        pan_money = 10000
                        sutda_map = True
                        move_map = False
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

        while(lose_map):
            window.blit(lose_map_background, (0,0)) # lose_map_background draw
            backstage_button.draw(window)  
            pygame.display.update() # display refresh

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if (event.type == pygame.QUIT): #quit event
                    entire_loop = False
                    lose_map = False                
                if (event.type == pygame.MOUSEBUTTONDOWN): # backstage_button click down
                    if (backstage_button.in_locate(pos)):
                        move_map = True
                        lose_map = False       

        while(win_map):
            window.blit(win_map_background, (0,0)) # win_map_background draw
            backstage_button.draw(window)  
            pygame.display.update() # display refresh

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if (event.type == pygame.QUIT): #quit event
                    entire_loop = False
                    win_map = False                
                if (event.type == pygame.MOUSEBUTTONDOWN): # backstage_button click down
                    if (backstage_button.in_locate(pos)):
                        move_map = True
                        win_map = False    

        while(sutda_map):
            before_start_display_refresh()
            if (com_money <= 0 and not result == 2): # computer 파산
                turn = 0
                com_die = 0 #com_die 초기화
                bet_money = 0
                call_money = 0
                compare_cnt = 0
                sutda_map = False
                win_map = True
                break
            if (user_money <= 0 and not result == 2): # user 파산
                user_money = 0
                turn = 1
                user_die = 0 #com_die 초기화
                bet_money = 0
                call_money = 0
                compare_cnt = 0
                sutda_map = False
                lose_map = True
                break
            # wait start button or backstage button
            starting = True
            while (starting):
                for event in pygame.event.get():
                    pos = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT: #quit event
                        starting = False
                        entire_loop = False
                        sutda_map = False
                    if (event.type == pygame.MOUSEBUTTONDOWN):
                        if (game_start_button.in_locate(pos)): # game_start_button click down
                            starting = False
                        if (backstage_button.in_locate(pos)): # backstage_button click down
                            starting = False
                            move_map = True
                            sutda_map = False
                        if (족보_button.in_locate(pos) and combination_table == 0):
                            combination_table = 1
                            before_start_display_refresh()
                            continue
                        if (족보_button.in_locate(pos) and combination_table == 1):
                            combination_table = 0
                            before_start_display_refresh()
                            continue
                
            if(sutda_map == False):
                break
            # draw & rematch -> 판돈계산 x
            if (result != 2): 
                bet_money = pan_money * 2
                user_money = user_money - pan_money 
                com_money = com_money - pan_money

            before_start_display_refresh()

            ######################### hand out card ###############################
            pygame.time.delay(500)
            hand_out_card(user_card, com_card, turn)
            back_card = Card(20)
            back_card.load_card_info()
            user_card1 = Card(user_card[0])
            user_card2 = Card(user_card[1])
            com_card1 = Card(com_card[0])
            com_card2 = Card(com_card[1])
            user_card1.load_card_info()
            user_card2.load_card_info()
            com_card1.load_card_info()
            com_card2.load_card_info()
            # distribute cards according to order
            if (turn == 0): #user turn
                first_turn_pos = [280, 255]
                window.blit(first_turn, (first_turn_pos[0], first_turn_pos[1]))
                user_card1.draw_image(window, 150, 265)
                pygame.display.update() # display refresh
                pygame.time.delay(hand_out_delay)
                back_card.draw_image(window, 150,100)
                pygame.display.update() # display refresh
                pygame.time.delay(hand_out_delay)
                user_card2.draw_image(window, 205, 265)
                pygame.display.update() # display refresh
                pygame.time.delay(hand_out_delay)
                com_card2.draw_image(window, 205,100)
                pygame.display.update() # display refresh
                pygame.time.delay(hand_out_delay)
            else: #computer turn   
                first_turn_pos = [280, 90]
                window.blit(first_turn, (first_turn_pos[0], first_turn_pos[1]))
                back_card.draw_image(window, 150,100)
                pygame.display.update() # display refresh
                pygame.time.delay(hand_out_delay)
                user_card1.draw_image(window, 150, 265)
                pygame.display.update() # display refresh
                pygame.time.delay(hand_out_delay)
                com_card2.draw_image(window, 205,100)
                pygame.display.update() # display refresh
                pygame.time.delay(hand_out_delay)
                user_card2.draw_image(window, 205, 265)
                pygame.display.update() # display refresh
                pygame.time.delay(hand_out_delay)

            #show card_class
            user_combination_card = Combination_Card(user_card1.get_card_value(), user_card2.get_card_value())
            com_combination_card = Combination_Card(com_card1.get_card_value(), com_card2.get_card_value())
            #com_combination_card.show_card_class(window, 150,180)
            user_combination_card.show_card_class(window, 150, 345)
            fluoroscope_power_value = False
            display_refresh()
            pygame.display.update() # display refresh

            ##################################betting##############################
            first_bet = 0
            user_bet_value = -1
            while(compare_cnt == 0 and com_die == 0 and user_die == 0):
                display_refresh()
                if (turn == 0): #user turn
                    decide_user_self_betting()
                    if (sutda_map == False):
                        break
                    user_bet_text = user_betting(user_bet_value)
                    if (first_bet == 0 and (user_bet_text == "call" or user_bet_text == "quater")): #첫 턴에 half or die 만 가능
                        continue
                    user_bet_result_text = game_font.render(user_bet_text, True, (255, 255, 255))
                    display_refresh()
                    window.blit(user_bet_result_text,(280, 315))
                    pygame.display.update() # display refresh    
                    
                    if (user_bet_text == "die"):
                        user_die = 1
                        result = 1
                    if (user_bet_text == "call"):
                        compare_cnt = 1

                    first_bet += 1
                    turn = 1
                    pygame.time.delay(betting_delay)
                    continue
                else: #computer turn
                    com_bet_text = computer_betting(decide_computer_auto_betting(com_combination_card.get_card_class()[0]))
                    if (first_bet == 0 and (com_bet_text == "call" or com_bet_text == "quater")): #첫 턴에 half or die 만 가능
                        continue
                    com_bet_result_text = game_font.render(com_bet_text, True, (255, 255, 255))
                    display_refresh()
                    window.blit(com_bet_result_text,(280, 150))
                    pygame.display.update() # display refresh    
                    if (com_bet_text == "die"):
                        com_die = 1
                        result = 0
                    if (com_bet_text == "call"):
                        compare_cnt = 1
                    first_bet += 1
                    turn = 0
                    pygame.time.delay(betting_delay)
                    continue
                
            if(compare_cnt == 1): # compare combination card class
                com_card1.draw_image(window, 150,100) #show computer card image
                com_card2.draw_image(window, 205,100)
                com_combination_card.show_card_class(window, 150,180)
                pygame.display.update() # display refresh
                pygame.time.delay(hand_out_delay)


                result = compare_card_class(com_combination_card.get_card_class()[0], user_combination_card.get_card_class()[0])
                if (result == 0):
                    result_text = game_font.render("********* " + user_name + " Win! **********", True, (255,255,255))
                    user_money = user_money + bet_money
                    turn = 0
                if (result == 1):
                    result_text = game_font.render("*********" + com_name + " Win! **********", True, (255,255,255))
                    com_money = com_money + bet_money
                    turn = 1
                if (result == 2):
                    result_text = game_font.render("********* Draw & Rematch! ********", True, (255,255,255))
                    window.blit(result_text,(30, 40))
                    compare_cnt = 0 #compare_cnt 초기화
                    call_money = 0
                    pygame.display.update() # display refresh
                    pygame.time.delay(1000)
                    continue
                window.blit(result_text,(30, 40))
                bet_money = 0
                call_money = 0
                compare_cnt = 0 #compare_cnt 초기화

            if (com_die == 1): #computer die
                result_text = game_font.render("********* " + user_name + " Win! **********", True, (255,255,255))
                window.blit(result_text,(30, 40))
                turn = 0
                com_die = 0 #com_die 초기화
                user_money = user_money + bet_money
                bet_money = 0
                call_money = 0
                
            if (user_die == 1): #user die
                result_text = game_font.render("*********" + com_name + " Win! **********", True, (255,255,255))
                window.blit(result_text,(30, 40))
                turn = 1
                user_die = 0 #user_die 초기화
                com_money = com_money + bet_money
                bet_money = 0
                call_money = 0

                
            pygame.display.update() # display refresh
            pygame.time.delay(1000)
    