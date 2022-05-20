import pygame

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
#backbround image
main_background = pygame.image.load("image\Main_background.jpg") 
nick_background = pygame.image.load("image\닉_background.jpg")
move_map_background = pygame.image.load("image\Move_Main_background.jpg")
sutda_map_background = pygame.image.load("image\Sutda_Map_Background.jpg")
lose_map_background = pygame.image.load("image\You_lose.jpg")
win_map_background = pygame.image.load("image\You_win.jpg")

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

die_button = Button(1, 400, "image\Die.png")
call_button = Button(161, 400, "image\Call.png")
quater_button = Button(321, 400, "image\Quater.png")
half_button = Button(481, 400, "image\Half.png")
족보_button = Button(641, 400, "image\족보.png")
game_start_button = Button(481, 345, "image\Game_start.png")

#image
coin_1 = pygame.image.load("image\Coin1.png")
coin_2 = pygame.image.load("image\Coin2.png")
coin_3 = pygame.image.load("image\Coin3.png")
coin_4 = pygame.image.load("image\Coin4.png")
first_turn = pygame.image.load("image\선1.png")
combination_table_image = pygame.image.load("image\Combination_table.png")