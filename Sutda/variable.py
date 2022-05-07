import pygame
####################################  pygame initialization  ###############################
pygame.init()
window_width = 800
window_height = 450
window = pygame.display.set_mode((window_width, window_height)) #set display size
pygame.display.set_caption("섯다!") #title
game_font = pygame.font.Font("D2Coding-Ver1.3.2-20180524-all.ttc", 16) # create font

############################################################################################
window_frame = 100
character_speed = 0.05
coin_speed = 0
user_name = "테스트유저"
com_name = ""
user_bet_result_text = ""
com_bet_result_text = ""
user_bet_value = -1
hand_out_delay = 300
betting_delay = 300

user_money = 0
com_money = 0
pan_money = 0
bet_money = 0
call_money = 0
save_money = 0
find_money = 0
coin_money = 0

coin_y_pos = window_height
combination_table = 0
result = 0
turn = 0 # 0: user 1 : computer
first_bet = 0
compare_cnt = 0
user_die = 0
com_die = 0
rand_card = [0,0,0,0]
user_card = [0,0]
com_card = [0,0]

#character
character = pygame.image.load("image\Character.png")
character_size = character.get_rect().size # get character size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = 0
character_y_pos = window_height - character_height
move_x = 0
move_y = 0

#time
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks() # get start tick
fps = clock.tick(window_frame) #frame set

#input text
eng_chars = "abcdefghijklmnopqrstuvwxyz"
text_font = pygame.font.Font("D2Coding-Ver1.3.2-20180524-all.ttc", 32)
input_first_text = text_font.render("닉네임을 입력하세요.", True, (255,255,255))
input_text = ""
input_box = pygame.Rect(230, 70, 340, 52)
color_inactive = pygame.Color("lightskyblue3")
color_active = pygame.Color("orangered4")
color = color_inactive
active = False
done = False