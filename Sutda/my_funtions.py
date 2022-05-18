import random

def pos_check(pos, target_x1, target_y1, target_x2, target_y2):
    if pos[0] > target_x1 and pos[0] < target_x2:
        if pos[1] > target_y1 and pos[1] < target_y2:
            return True          
    return False
def convert_money(money):
    money_경 = money // 10000000000000000
    c_money = money % 10000000000000000
    money_조 = c_money // 1000000000000
    c_money = money % 1000000000000
    money_억 = c_money // 100000000
    c_money = c_money % 100000000     
    money_만 = c_money // 10000
    money_냥 = c_money % 10000

    if (money_경 != 0):
        money_경_text = str(money_경) + "경"
    else:
        money_경_text = ""

    if (money_조 != 0):
        money_조_text = str(money_조) + "조"
    else:
        money_조_text = ""

    if (money_억 != 0):
        money_억_text = str(money_억) + "억"
    else:
        money_억_text = ""

    if (money_만 != 0):
        money_만_text = str(money_만) + "만"
    else:
        money_만_text = ""

    if (money_냥 != 0):
        money_냥_text = str(money_냥)
    else:
        money_냥_text = ""

    if (money <= 0):
        return "0냥"
    else:
        return money_경_text + money_조_text + money_억_text + money_만_text + money_냥_text + "냥"
def hand_out_card(user_card, com_card, turn):
    rand_card = random.sample(range(0,20),4)
    if (turn == 0): # user turn
        user_card[0] = rand_card[0]
        com_card[0] = rand_card[1]
        user_card[1] = rand_card[2]
        com_card[1] = rand_card[3]
    else: # computer turn
        com_card[0] = rand_card[0]
        user_card[0] = rand_card[1]
        com_card[1] = rand_card[2]
        user_card[1] = rand_card[3]
def decide_computer_auto_betting(com_card_value): # return 0 : die, return 1 : 콜, return 2 : 쿼터, return 3 : 하프
    if (com_card_value == 3181): # 38광땡 무조건 승리 
        rand_num = random.randint(0, 20) #0 ~ 19
        if (rand_num < 15): # 15/20 확률로
            return 3 # 하프
        elif (rand_num < 19): # 4/20 확률로
            return 2 # 쿼터
        else: # 1/20 확률로
            return 1 # call
    elif (com_card_value == 1181): # 18광땡 암행어사에 잡힙
        rand_num = random.randint(0, 20) #0 ~ 19
        if (rand_num < 13): # 13/20 확률로
            return 3 # 하프
        elif (rand_num < 18): # 5/20 확률로
            return 2 # 쿼터
        else: # 2/20 확률로
            return 1 # call
    elif (com_card_value == 1131): # 13광땡 암행어사에 잡힙
        rand_num = random.randint(0, 20) #0 ~ 19
        if (rand_num < 13): # 13/20 확률로
            return 3 # 하프
        elif (rand_num < 18): # 5/20 확률로
            return 2 # 쿼터
        else: # 2/20 확률로
            return 1 # call
    elif (com_card_value == 1001): # 3,7 땡잡이(1~9땡 상대로 승리)
        rand_num = random.randint(0, 20) #0 ~ 19
        if (rand_num < 10): # 10/20 확률로
            return 0 # die
        elif (rand_num < 14): # 4/20 확률로
            return 2 # 쿼터
        elif (rand_num < 16): # 2/20 확률로
            return 3 # 하프
        else: # 4/20 확률로
            return 1 # call
    elif (com_card_value == 2000): # 4,7 암행어사 (1,3 & 1,8 광땡 상대로 승리)
        rand_num = random.randint(0, 20) #0 ~ 19
        if (rand_num < 15): # 15/20 확률로
            return 0 # die
        elif (rand_num < 17): # 2/20 확률로
            return 2 # 쿼터
        elif (rand_num < 18): # 1/20 확률로
            return 3 # 하프
        else: # 2/20 확률로
            return 1 # call

    elif (com_card_value == 1000 or com_card_value == 101): # 멍텅구리구사 or 구사
        rand_num = random.randint(0, 20) #0 ~ 19
        if (rand_num < 10): # 10/20 확률로
            return 2 # 쿼터
        elif (rand_num < 15): # 5/20 확률로
            return 3 # 하프
        else: # 5/20 확률로
            return 1 # call

    elif (com_card_value >= 111 and com_card_value <= 1010): # 땡
        rand_num = random.randint(0, 20) #0 ~ 19
        if (rand_num < 10): # 10/20 확률로
            return 3 # 하프
        elif (rand_num < 17): # 7/20 확률로
            return 2 # 쿼터
        else: # 3/20 확률로
            return 1 # call
    
    elif (com_card_value >= 95 and com_card_value <= 100): # 그 외 조합 알리~세륙
        rand_num = random.randint(0, 20) #0 ~ 19
        if (rand_num < 8): # 8/20 확률	
            return 3 # 하프
        elif (rand_num < 15): # 7/20 확률로
            return 2 # 쿼터
        else: # 5/20 확률로
            return 1 # call

    elif (com_card_value >= 7 and com_card_value <= 9): # 갑오 ~ 7끗
        rand_num = random.randint(0, 20) #0 ~ 19
        if (rand_num < 5): # 5/20 확률로
            return 3 # 하프
        elif (rand_num < 12): # 7/20 확률로
            return 2 # 쿼터
        elif (rand_num < 14): # 2/20 확률로
            return 0 # die 
        else: # 5/20 확률로
            return 1 # call
    
    else: # 6끗 아래
        rand_num = random.randint(0, 20) #0 ~ 19
        if (rand_num < 2): # 2/20 확률로
            return 3 # 하프
        elif (rand_num < 4): # 2/20 확률로
            return 2 # 쿼터
        elif (rand_num < 16): # 12/20 확률로
            return 0 # die 
        else: # 4/20 확률로
            return 1 # call
def decide_user_auto_betting(user_card_value): # return 0 : die, return 1 : 콜, return 2 : 쿼터, return 3 : 하프
    if (user_card_value == 3181): # 38광땡 무조건 승리 
        rand_num = random.randint(0, 20) #0 ~ 19
        if (rand_num < 15): # 15/20 확률로
            return 3 # 하프
        elif (rand_num < 19): # 4/20 확률로
            return 2 # 쿼터
        else: # 1/20 확률로
            return 1 # call
    elif (user_card_value == 1181): # 18광땡 암행어사에 잡힙
        rand_num = random.randint(0, 20) #0 ~ 19
        if (rand_num < 13): # 13/20 확률로
            return 3 # 하프
        elif (rand_num < 18): # 5/20 확률로
            return 2 # 쿼터
        else: # 2/20 확률로
            return 1 # call
    elif (user_card_value == 1131): # 13광땡 암행어사에 잡힙
        rand_num = random.randint(0, 20) #0 ~ 19
        if (rand_num < 13): # 13/20 확률로
            return 3 # 하프
        elif (rand_num < 18): # 5/20 확률로
            return 2 # 쿼터
        else: # 2/20 확률로
            return 1 # call
    elif (user_card_value == 1001): # 3,7 땡잡이(1~9땡 상대로 승리)
        rand_num = random.randint(0, 20) #0 ~ 19
        if (rand_num < 10): # 10/20 확률로
            return 0 # die
        elif (rand_num < 14): # 4/20 확률로
            return 2 # 쿼터
        elif (rand_num < 16): # 2/20 확률로
            return 3 # 하프
        else: # 4/20 확률로
            return 1 # call
    elif (user_card_value == 2000): # 4,7 암행어사 (1,3 & 1,8 광땡 상대로 승리)
        rand_num = random.randint(0, 20) #0 ~ 19
        if (rand_num < 15): # 15/20 확률로
            return 0 # die
        elif (rand_num < 17): # 2/20 확률로
            return 2 # 쿼터
        elif (rand_num < 18): # 1/20 확률로
            return 3 # 하프
        else: # 2/20 확률로
            return 1 # call

    elif (user_card_value == 1000 or user_card_value == 101): # 멍텅구리구사 or 구사
        rand_num = random.randint(0, 20) #0 ~ 19
        if (rand_num < 10): # 10/20 확률로
            return 2 # 쿼터
        elif (rand_num < 15): # 5/20 확률로
            return 3 # 하프
        else: # 5/20 확률로
            return 1 # call

    elif (user_card_value >= 111 and user_card_value <= 1010): # 땡
        rand_num = random.randint(0, 20) #0 ~ 19
        if (rand_num < 10): # 10/20 확률로
            return 3 # 하프
        elif (rand_num < 17): # 7/20 확률로
            return 2 # 쿼터
        else: # 3/20 확률로
            return 1 # call
    
    elif (user_card_value >= 95 and user_card_value <= 100): # 그 외 조합 알리~세륙
        rand_num = random.randint(0, 20) #0 ~ 19
        if (rand_num < 8): # 8/20 확률	
            return 3 # 하프
        elif (rand_num < 15): # 7/20 확률로
            return 2 # 쿼터
        else: # 5/20 확률로
            return 1 # call

    elif (user_card_value >= 7 and user_card_value <= 9): # 갑오 ~ 7끗
        rand_num = random.randint(0, 20) #0 ~ 19
        if (rand_num < 5): # 5/20 확률로
            return 3 # 하프
        elif (rand_num < 12): # 7/20 확률로
            return 2 # 쿼터
        elif (rand_num < 14): # 2/20 확률로
            return 0 # die 
        else: # 5/20 확률로
            return 1 # call
    
    else: # 6끗 아래
        rand_num = random.randint(0, 20) #0 ~ 19
        if (rand_num < 2): # 2/20 확률로
            return 3 # 하프
        elif (rand_num < 4): # 2/20 확률로
            return 2 # 쿼터
        elif (rand_num < 16): # 12/20 확률로
            return 0 # die 
        else: # 4/20 확률로
            return 1 # call
def compare_card_class(com_class, my_class): # return 0 : I_win | return 1 : com_win | return 2 : draw & rematch
	if (com_class == 2000): # com : 4,7암행어사
		if (my_class == 1181 or my_class == 1131):
			return 1 #com_win
		elif (my_class > 1):
			return 0 #I_win
		elif (my_class < 1):
			return 1 # com_win
		else:
			return 2 # draw
	if (my_class == 2000): # my : 4,7암행어사
		if (com_class == 1181 or com_class == 1131):
			return 0 #I_win
		elif (com_class > 1):
			return 1 #com_win
		elif (com_class < 1):
			return 0 # I_win
		else:
			return 2 # draw
	if (com_class == 1001): # com : 3,7 땡잡이 | 1~9땡 상대로 승리
		if (my_class == 999 or my_class == 888 or my_class == 777 or my_class == 666 or my_class == 555 or my_class == 444 or my_class == 333 or my_class == 222 or my_class == 111):
			return 1 #com_win
		elif (my_class == 0):
			return 2 #draw
		else:
			return 0 #I_win
	if (my_class == 1001): # my : 3,7 땡잡이 | 1~9땡 상대로 승리
		if (com_class == 999 or com_class == 888 or com_class == 777 or com_class == 666 or com_class == 555 or com_class == 444 or com_class == 333 or com_class == 222 or com_class == 111):
			return 0 #I_win
		elif (com_class == 0):
			return 2 #draw
		else:
			return 1 #com_win
	if (com_class == 1000): #com : 멍텅구리 구사 | 9땡까지 재경기
		if (my_class == 1010 or my_class == 1131 or my_class == 1181 or my_class == 3181):
			return 0 #I_win
		else:
			return 2 #rematch
	if (my_class == 1000): #my : 멍텅구리 구사 | 9땡까지 재경기
		if (com_class == 1010 or com_class == 1131 or com_class == 1181 or com_class == 3181):
			return 1 #com_win
		else:
			return 2 #rematch
	if (com_class == 101): # com : 구사 | 알리까지 재경기
		if (my_class == 111 or my_class == 222 or my_class == 333 or my_class == 444 or my_class == 555 or my_class == 666 or my_class == 777 or my_class == 888 or my_class == 999 or my_class == 1010 or my_class == 1131 or my_class == 1181 or my_class == 3181):
			return 0 #I_win
		else:
			return 2 #rematch
	if (my_class == 101): # my : 구사 | 알리까지 재경기
		if (com_class == 111 or com_class == 222 or com_class == 333 or com_class == 444 or com_class == 555 or com_class == 666 or com_class == 777 or com_class == 888 or com_class == 999 or com_class == 1010 or com_class == 1131 or com_class == 1181 or com_class == 3181):
			return 1 #com_win
		else:
			return 2 #rematch

	if (my_class > com_class):
		return 0 #I_win
	if (com_class > my_class):
		return 1 #com_win
	if (my_class == com_class):
		return 2 #draw
def decide_fluoroscope_power(power_value):
    rand_num = random.randint(0,100)
    if (rand_num < power_value):
        return True


