import pygame
from objects import *

pygame.init()
window_width = 800
window_height = 450
window = pygame.display.set_mode((window_width, window_height)) #set display size
pygame.display.set_caption("섯다!") #title
game_font = pygame.font.Font("D2Coding-Ver1.3.2-20180524-all.ttc", 16) # create font


if (__name__ == "__main__"): # main 함수임
    entire_loop = True
    start_menu = True
    mode_select_menu = False
    explain_menu = False
    info_menu = False

    while(entire_loop): # entire loop
        while(start_menu):
            window.blit(main_background, (0,-60)) # main_background draw
            #start_button.draw(window)
            #explain_button.draw(window)
            #info_button.draw(window)
            pygame.display.update() # display refresh

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if (event.type == pygame.QUIT): #quit event
                    entire_loop = False
                    start_menu = False
                if (event.type == pygame.MOUSEBUTTONDOWN): 
                    if (start_button.in_locate(pos)): # game_start button click down
                        #mode_select_menu = True
                        #start_menu = False
                        pass
                    if (explain_button.in_locate(pos)): # explain button click down
                        #explain_menu = True
                        #start_menu = False
                        pass
                    if (info_button.in_locate(pos)): # info_button click down
                        #info_menu = True
                        #start_menu = False
                        pass