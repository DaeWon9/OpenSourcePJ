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