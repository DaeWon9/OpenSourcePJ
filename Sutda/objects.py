import pygame
from my_funtions import *
from variable import *

class Alert_Msg:
    def __init__(self, msg_text, window_width = 800, window_height = 450):
        self.msg_text = msg_text

        self.alert_msg_image = pygame.image.load("image\Alert_msg.png")
        self.alert_msg_image_width = self.alert_msg_image.get_rect().size[0]
        self.alert_msg_image_height = self.alert_msg_image.get_rect().size[1]
        self.alert_msg_image_x = window_width / 2 - self.alert_msg_image_width / 2
        self.alert_msg_image_y = window_height / 2 - self.alert_msg_image_height / 2

        self.alert_font = pygame.font.Font("D2Coding-Ver1.3.2-20180524-all.ttc", 16)
        self.alert_text = self.alert_font.render(msg_text, True, (0,0,0))
        self.alert_text_width = self.alert_font.size(msg_text)[0]
        self.alert_text_height = self.alert_font.size(msg_text)[1]
        self.alert_text_x = (2 * self.alert_msg_image_x + self.alert_msg_image_width) / 2 - self.alert_text_width / 2
        self.alert_text_y = (2 * self.alert_msg_image_y + self.alert_msg_image_height) / 2 - self.alert_text_height

    def draw(self, window):
        window.blit(self.alert_msg_image, (self.alert_msg_image_x, self.alert_msg_image_y))
        window.blit(self.alert_text, (self.alert_text_x, self.alert_text_y))


class Item:
    def __init__(self, item_name, item_price, item_image, item_effect):
        self.name = item_name
        self.item_price = item_price
        self.item_image = pygame.image.load(item_image)
        self.item_effect = item_effect
        self.item_size = self.item_image.get_rect().size
        self.item_width = self.item_size[0]
        self.item_height = self.item_size[1]

    def get_price(self):
        return self.item_price

    def item_draw(self, window, pos_x, pos_y):
        window.blit(self.item_image,(pos_x, pos_y))

    def item_draw_in_bag(self, window, magnification, bag_space):
        self.item_mid_pos = [[133,123],[250,123],[365,123],[133,222],[250,222],[365,222],[133,321],[250,321],[365,321]]
        self.item_new_width = self.item_width * magnification
        self.item_new_height = self.item_height * magnification
        self.item_pos_x = self.item_mid_pos[bag_space][0] - self.item_new_width/2
        self.item_pos_y = self.item_mid_pos[bag_space][1] - self.item_new_height/2
        self.item_inbag_image = pygame.transform.scale(self.item_image, (self.item_new_width, self.item_new_height))
        window.blit(self.item_inbag_image,(self.item_pos_x, self.item_pos_y))

    def item_draw_in_equip(self, window, magnification, equip_space):
        self.equip_mid_pos = [[516,400],[617,400],[718,400]]
        self.item_new_width = self.item_width * magnification
        self.item_new_height = self.item_height * magnification
        self.equip_pos_x = self.equip_mid_pos[equip_space][0] - self.item_new_width/2
        self.equip_pos_y = self.equip_mid_pos[equip_space][1] - self.item_new_height/2
        self.item_equip_image = pygame.transform.scale(self.item_image, (self.item_new_width, self.item_new_height))
        window.blit(self.item_equip_image,(self.equip_pos_x, self.equip_pos_y))

    def check_button_draw(self, window, text, window_width = 800, window_height = 450):
        self.text = pygame.font.Font("D2Coding-Ver1.3.2-20180524-all.ttc", 24).render(text, True, (0,0,0))
        self.name_text = pygame.font.Font("D2Coding-Ver1.3.2-20180524-all.ttc", 16).render(self.name, True, (0,0,0))
        self.name_text_width = pygame.font.Font("D2Coding-Ver1.3.2-20180524-all.ttc", 16).size(self.name)[0]
        self.name_text_height = pygame.font.Font("D2Coding-Ver1.3.2-20180524-all.ttc", 16).size(self.name)[1]
        self.name_text_x = (window_width / 2) - (self.name_text_width / 2)
        self.name_text_y = (window_height / 2) - (self.name_text_height / 2) + 10

        self.background_image = pygame.image.load("image\Select_button.png")
        self.b_image_width = self.background_image.get_rect().size[0]
        self.b_image_height = self.background_image.get_rect().size[1]
        self.b_x = (window_width / 2) - (self.b_image_width / 2)
        self.b_y = (window_height / 2) - (self.b_image_height / 2)

        self.item_x = (window_width / 2) - (self.item_new_width / 2)
        self.item_y = (window_height / 2) - (self.item_new_height / 2) - 17

        window.blit(self.background_image, (self.b_x, self.b_y))
        window.blit(self.text, (300, 150))
        window.blit(pygame.transform.scale(self.item_image, (self.item_new_width, self.item_new_height)),(self.item_x, self.item_y))
        window.blit(self.name_text, (self.name_text_x, self.name_text_y))
    
    def yes_button_in_locate(self, pos):
        if pos[0] > 260 and pos[0] < 370:
            if pos[1] > 262 and pos[1] < 310:
                return True        
        return False

    def no_button_in_locate(self, pos):
        if pos[0] > 420 and pos[0] < 532:
            if pos[1] > 262 and pos[1] < 310:
                return True           
        return False        

    def item_in_locate(self, pos):
        if pos[0] > self.item_pos_x and pos[0] < self.item_pos_x + self.item_new_width:
            if pos[1] > self.item_pos_y and pos[1] < self.item_pos_y + self.item_new_height:
                return True           
        return False

    def draw_sell_image(self, window, pos_x, pos_y, magnification, buyer):
        self.font = pygame.font.Font("D2Coding-Ver1.3.2-20180524-all.ttc", 14)
        
        self.name_text = self.font.render(self.name, True, (0,0,0))
        self.price_text = self.font.render(convert_money(self.item_price), True, (255,0,0))
        self.effect_text = self.font.render("효과:" + self.item_effect, True, (0,0,255))
        self.back_image = pygame.image.load("image\아이템판매.png")
        self.item_size = self.item_image.get_rect().size
        self.item_new_width = self.item_size[0] * magnification
        self.item_new_height = self.item_size[1] * magnification
        self.sell_image = pygame.transform.scale(self.item_image, (self.item_new_width, self.item_new_height))

        self.image_pos_x = pos_x + 42 - self.item_new_width / 2
        self.image_pos_y = pos_y + 23 - self.item_new_height / 2

        self.name_pos_x = pos_x + 92
        self.name_pos_y = pos_y + 6

        self.effect_pos_x = pos_x + 92
        self.effect_pos_y = pos_y + 23

        self.price_pos_x = pos_x + 227
        self.price_pos_y = pos_y + 16

        window.blit(self.back_image, (pos_x, pos_y))
        window.blit(self.sell_image,(self.image_pos_x, self.image_pos_y))
        window.blit(self.name_text, (self.name_pos_x, self.name_pos_y))
        window.blit(self.effect_text, (self.effect_pos_x, self.effect_pos_y))
        if (buyer == 1):
            window.blit(self.price_text, (self.price_pos_x, self.price_pos_y))
        else:
            window.blit(self.font.render("보유중", True, (0,0,0)), (self.price_pos_x, self.price_pos_y))

    def purchase(self, window, user_money):
        self.check_button_draw(window, "구매 하시겠습니까?")
        pygame.display.update() # display refresh
        click_check = True
        while(click_check):
            for event in pygame.event.get():
                check_pos = pygame.mouse.get_pos()
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if (self.yes_button_in_locate(check_pos)):
                        if (user_money >= self.get_price()):                                              
                            alert_purchase_completed.draw(window)
                            pygame.display.update() # display refresh
                            ok_check = True
                            while(ok_check):
                                for event in pygame.event.get():
                                    ok_pos = pygame.mouse.get_pos()
                                    if (event.type == pygame.MOUSEBUTTONDOWN):
                                        if (pos_check(ok_pos, 350, 259, 450, 299)):
                                            user_money = user_money - self.get_price()
                                            click_check = False
                                            return True, user_money
                        else:
                            alert_lack_of_money.draw(window)
                            pygame.display.update() # display refresh
                            ok_check = True
                            while(ok_check):
                                for event in pygame.event.get():
                                    ok_pos = pygame.mouse.get_pos()
                                    if (event.type == pygame.MOUSEBUTTONDOWN):
                                        if (pos_check(ok_pos, 350, 259, 450, 299)):
                                            ok_check = False
                                            click_check = False
                                            return False, user_money
                    if (self.no_button_in_locate(check_pos)):
                        click_check = False    
                        return False, user_money

    def equip(self, window):
        info_check = True
        while(info_check):
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if (self.item_in_locate(pos) == False):
                    info_check = False
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    self.check_button_draw(window, "장착 하시겠습니까?")
                    pygame.display.update() # display refresh
                    click_check = True
                    while(click_check):
                        for event in pygame.event.get():
                            pos = pygame.mouse.get_pos()
                            if (event.type == pygame.MOUSEBUTTONDOWN):
                                if (self.yes_button_in_locate(pos)):                                              
                                    return True
                                if (green_canvas.no_button_in_locate(pos)):
                                    return False


class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.button_image = pygame.image.load(self.image)
        self.x = x
        self.y = y
        self.width = self.button_image.get_rect().size[0]
        self.height = self.button_image.get_rect().size[1]
    
    def draw(self, window): #draw funtion
        window.blit(self.button_image, (self.x, self.y))
     
    def in_locate(self, pos): # [0] -> x좌표 // [1] -> y좌표
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True           
        return False

    def check_button_draw(self, window, text, window_width = 800, window_height = 450):
        self.text = pygame.font.Font("D2Coding-Ver1.3.2-20180524-all.ttc", 24).render(text, True, (0,0,0))
        self.background_image = pygame.image.load("image\Select_button.png")
        self.b_image_width = self.background_image.get_rect().size[0]
        self.b_image_height = self.background_image.get_rect().size[1]
        self.b_x = (window_width / 2) - (self.b_image_width / 2)
        self.b_y = (window_height / 2) - (self.b_image_height / 2)

        window.blit(self.background_image, (self.b_x, self.b_y))
        window.blit(self.text, (300, 190))
    
    def yes_button_in_locate(self, pos):
        if pos[0] > 260 and pos[0] < 370:
            if pos[1] > 262 and pos[1] < 310:
                return True        
        return False

    def no_button_in_locate(self, pos):
        if pos[0] > 420 and pos[0] < 532:
            if pos[1] > 262 and pos[1] < 310:
                return True           
        return False       



########################### create object ########################################
# alert_msg
alert_purchase_completed = Alert_Msg("구매완료!!")
alert_save_completed = Alert_Msg("저장완료!!")
alert_lack_of_money = Alert_Msg("보유금액이 부족합니다.")
alert_lack_of_find_money = Alert_Msg("보관금액이 부족합니다.")
#backbround image
main_background = pygame.image.load("image\Main_background.jpg") 
nick_background = pygame.image.load("image\닉_background.jpg")
move_map_background = pygame.image.load("image\Move_Main_background.jpg")
sutda_map_background = pygame.image.load("image\Sutda_Map_Background.jpg")
lose_map_background = pygame.image.load("image\You_lose.jpg")
win_map_background = pygame.image.load("image\You_win.jpg")
bag_background = pygame.image.load("image\Bag_background.png")
bag_table = pygame.image.load("image\가방틀.png")    
equip = pygame.image.load("image\Equip.png")



# computer character image
apeach_image = pygame.image.load("image\\Apeach.png")
muzi_image = pygame.image.load("image\\Muzi.png")
tube_image = pygame.image.load("image\\Tube.png")
neo_image = pygame.image.load("image\\Neo.png")
jayg_image = pygame.image.load("image\\JayG.png")
frodo_image = pygame.image.load("image\\Frodo.png")

#button
start_button = Button(492, 310, "image\Start.png")
explain_button = Button(492, 367, "image\Explain.png")

backstage_button = Button(770, 1, "image\Backstage.png")
continue_start_button = Button(100, 140, "image\이어하기.png")
new_start_button = Button(100, 200, "image\새로하기.png")

bag_button = Button(725, -1, "image\가방.png")
save_info_button = Button(685, 1, "image\저장하기.png")

Apeach = Button(250, 270, "image\\Apeach.png")
Neo = Button(470, 320, "image\\Neo.png")
SafeBox = Button(600, 300, "image\\SafeBox.png")

die_button = Button(79, 405, "image\Die.png")
call_button = Button(79 + 129, 405, "image\Call.png")
quater_button = Button(79 + 129*2, 405, "image\Quater.png")
half_button = Button(79 + 129*3, 405, "image\Half.png")
족보_button = Button(633, 421, "image\족보.png")
game_start_button = Button(613, 324, "image\Game_start.png")

#image
coin_1 = pygame.image.load("image\Coin1.png")
coin_2 = pygame.image.load("image\Coin2.png")
coin_3 = pygame.image.load("image\Coin3.png")
coin_4 = pygame.image.load("image\Coin4.png")
first_turn = pygame.image.load("image\선1.png")
combination_table_image = pygame.image.load("image\Combination_table.png")

green_canvas_info = pygame.image.load("image\Green_canvas_info.png")
blue_canvas_info = pygame.image.load("image\Blue_canvas_info.png")
red_canvas_info = pygame.image.load("image\Red_canvas_info.png")
green_fluoroscope_info = pygame.image.load("image\Green_fluoroscope_info.png")
blue_fluoroscope_info = pygame.image.load("image\Blue_fluoroscope_info.png")
red_fluoroscope_info = pygame.image.load("image\Red_fluoroscope_info.png")


#item
green_fluoroscope = Item("초록투시경", 10000000, "image\투시경_초록.png", "투시확률 5%")
blue_fluoroscope = Item("파란투시경", 1000000000, "image\투시경_파랑.png", "투시확률 15%")
red_fluoroscope = Item("빨간투시경", 100000000000, "image\투시경_빨강.png", "투시확률 30%")

green_canvas = Item("초록신발", 500000, "image\신발_초록.png", "이동속도 + 10")
blue_canvas = Item("파란신발", 5000000, "image\신발_파랑.png", "이동속도 + 20")
red_canvas = Item("빨간신발", 500000000, "image\신발_빨강.png", "이동속도 + 30")