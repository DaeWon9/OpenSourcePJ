import pygame
from my_funtions import *

class Card:
    image_card = ["image\Card_1.png", "image\Card_1_s.png", "image\Card_2.png", "image\Card_2_s.png", "image\Card_3.png", "image\Card_3_s.png", "image\Card_4.png", "image\Card_4_s.png", "image\Card_5.png", "image\Card_5_s.png", "image\Card_6.png", "image\Card_6_s.png", "image\Card_7.png", "image\Card_7_s.png", "image\Card_8.png", "image\Card_8_s.png", "image\Card_9.png", "image\Card_9_s.png", "image\Card_10.png", "image\Card_10_s.png", "image\Card_0.png"]
    card_ary = [ 1, 11, 2, 2, 3, 31, 4, 41, 5, 5, 6, 6, 7, 71, 8, 81, 9, 91, 10, 10 , 0]
    def __init__(self, index_num):
        self.index_num = index_num

    def get_card_value(self):
        self.value = self.card_ary[self.index_num]
        return self.value

    def load_card_info(self):
        self.image = pygame.image.load(self.image_card[self.index_num])
        self.width = self.image.get_rect().size[0]
        self.height = self.image.get_rect().size[1]
        #self.cd_text = game_font.render(str(self.get_card_value()), True, (0,0,255))

    def draw_image(self, window, pos_x, pos_y):
        window.blit(self.image,(pos_x, pos_y))

class Combination_Card(Card):
    def __init__(self, card_1_value, card_2_value):
        self.card_1_value = card_1_value
        self.card_2_value = card_2_value
    
    def get_card_class(self):
        self.card_1_class = self.card_1_value
        self.card_2_class = self.card_2_value

        if ((self.card_1_class == 31 and self.card_2_class == 81) or (self.card_1_class == 81 and self.card_2_class == 31)):
            return [3181, "38광땡"]
        elif ((self.card_1_class == 81 and self.card_2_class == 11) or (self.card_1_class == 11 and self.card_2_class == 81)):
            return [1181, "18광땡"]
        elif ((self.card_1_class == 31 and self.card_2_class == 11) or (self.card_1_class == 11 and self.card_2_class == 31)):
            return [1131, "13광땡"]

        elif (self.card_1_class == self.card_2_class): # 땡
            if (self.card_1_class == 10):
                return [1010,"장땡"]
            if (self.card_1_class == 6):
                return [666, "6땡"]
            if (self.card_1_class == 5):
                return [555, "5땡"]
            if (self.card_1_class == 2):
                return [222, "2땡"]

        elif ((self.card_1_class == 91 and self.card_2_class == 9) or (self.card_1_class == 9 and self.card_2_class == 91)):
            return [999, "9땡"]
        elif ((self.card_1_class == 81 and self.card_2_class == 8) or (self.card_1_class == 8 and self.card_2_class == 81)):
            return [888, "8땡"]
        elif ((self.card_1_class == 71 and self.card_2_class == 7) or (self.card_1_class == 7 and self.card_2_class == 71)):
            return [777, "7땡"]
        elif ((self.card_1_class == 41 and self.card_2_class == 4) or (self.card_1_class == 4 and self.card_2_class == 41)):
            return [444, "4땡"]
        elif ((self.card_1_class == 31 and self.card_2_class == 3) or (self.card_1_class == 3 and self.card_2_class == 31)):
            return [333, "3땡"]
        elif ((self.card_1_class == 11 and self.card_2_class == 1) or (self.card_1_class == 1 and self.card_2_class == 11)):
            return [111, "1땡"]

        elif ((self.card_1_class == 11 and self.card_2_class == 2) or (self.card_1_class == 2 and self.card_2_class == 11) or (self.card_1_class == 1 and self.card_2_class == 2) or (self.card_1_class == 2 and self.card_2_class == 1)):
            return [100, "알리"]
        elif ((self.card_1_class == 11 and self.card_2_class == 4) or (self.card_1_class == 4 and self.card_2_class == 11) or (self.card_1_class == 1 and self.card_2_class == 4) or (self.card_1_class == 4 and self.card_2_class == 1) or (self.card_1_class == 11 and self.card_2_class == 41) or (self.card_1_class == 41 and self.card_2_class == 11) or (self.card_1_class == 1 and self.card_2_class == 41) or (self.card_1_class == 41 and self.card_2_class == 1)):
            return [99, "독사"]
        elif ((self.card_1_class == 11 and self.card_2_class == 9) or (self.card_1_class == 9 and self.card_2_class == 11) or (self.card_1_class == 1 and self.card_2_class == 9) or (self.card_1_class == 9 and self.card_2_class == 1) or (self.card_1_class == 11 and self.card_2_class == 91) or (self.card_1_class == 91 and self.card_2_class == 11) or (self.card_1_class == 1 and self.card_2_class == 91) or (self.card_1_class == 91 and self.card_2_class == 1)):
            return [98, "구삥"]
        elif ((self.card_1_class == 11 and self.card_2_class == 10) or (self.card_1_class == 10 and self.card_2_class == 11) or (self.card_1_class == 1 and self.card_2_class == 10) or (self.card_1_class == 10 and self.card_2_class == 1)):
            return [97, "장삥"]
        elif ((self.card_1_class == 10 and self.card_2_class == 4) or (self.card_1_class == 4 and self.card_2_class == 10) or (self.card_1_class == 10 and self.card_2_class == 41) or (self.card_1_class == 41 and self.card_2_class == 10)):
            return [96, "장사"]
        elif ((self.card_1_class == 4 and self.card_2_class == 6) or (self.card_1_class == 6 and self.card_2_class == 4) or (self.card_1_class == 41 and self.card_2_class == 6) or (self.card_1_class == 6 and self.card_2_class == 41)):
            return [95, "세륙"]

        # 그외 특수 조합
        elif ((self.card_1_class == 41 and self.card_2_class == 71) or (self.card_1_class == 71 and self.card_2_class == 41)):
            return [2000, "4,7 암행어사 (1,3 & 1,8 광땡만 승리)"]

        elif ((self.card_1_class == 31 and self.card_2_class == 71) or (self.card_1_class == 71 and self.card_2_class == 31)):
            return [1001, "3,7 땡잡이 (1~9땡만 승리)"]

        elif ((self.card_1_class == 91 and self.card_2_class == 41) or (self.card_1_class == 41 and self.card_2_class == 91)):
            return [1000, "멍텅구리구사 (9땡까지 재경기)"]

        elif ((self.card_1_class == 9 and self.card_2_class == 4) or (self.card_1_class == 4 and self.card_2_class == 9) or (self.card_1_class == 91 and self.card_2_class == 4) or (self.card_1_class == 4 and self.card_2_class == 91) or (self.card_1_class == 9 and self.card_2_class == 41) or (self.card_1_class == 41 and self.card_2_class == 9)):
            return [101, "구사 (알리까지 재경기)"]

        # 끗 계산
        else:
            if (self.card_1_class > 10):
                self.card_1_class = int(self.card_1_class / 10)
            if (self.card_2_class > 10):
                self.card_2_class = int(self.card_2_class / 10)


            if ((self.card_1_class + self.card_2_class == 9) or (self.card_1_class + self.card_2_class == 19)):
                return [9, "갑오(9끗)"]
            if ((self.card_1_class + self.card_2_class == 8) or (self.card_1_class + self.card_2_class == 18)):
                return [8, "8끗"]
            if ((self.card_1_class + self.card_2_class == 7) or (self.card_1_class + self.card_2_class == 17)):
                return [7, "7끗"]
            if ((self.card_1_class + self.card_2_class == 6) or (self.card_1_class + self.card_2_class == 16)):
                return [6, "6끗"]
            if ((self.card_1_class + self.card_2_class == 5) or (self.card_1_class + self.card_2_class == 15)):
                return [5, "5끗"]
            if ((self.card_1_class + self.card_2_class == 4) or (self.card_1_class + self.card_2_class == 14)):
                return [4, "4끗"]
            if ((self.card_1_class + self.card_2_class == 3) or (self.card_1_class + self.card_2_class == 13)):
                return [3, "3끗"]
            if ((self.card_1_class + self.card_2_class == 2) or (self.card_1_class + self.card_2_class == 12)):
                return [2, "2끗"]
            if (self.card_1_class + self.card_2_class == 11):
                return [1, "1끗"]
            if (self.card_1_class + self.card_2_class == 10):
                return [0, "망통(0끗)"]
            else:
                return [999999999, "error"]

    def show_card_class(self, window, pos_x, pos_y):
        game_font = pygame.font.Font("D2Coding-Ver1.3.2-20180524-all.ttc", 13) # create font
        self.card_text = game_font.render(self.get_card_class()[1], True, (255,255,255))
        window.blit(self.card_text,(pos_x, pos_y))
