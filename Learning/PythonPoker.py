import random


def drawing_cards():
    #获取手牌数字
    str_tool1 = '0123456789TJQKA'
    num1 =  [random.randint(2,13) for _ in range(5)]
    poker_number = [str_tool1[x] for x in num1]
    #获取手牌花色
    str_tool2 = '0SCDH'
    num2 = [random.randint(1,4) for _ in range(5)]
    poker_suit = [str_tool2[x] for x in num2]
    #生成手牌组合（列表）
    cards = [poker_number[x]+poker_suit[x] for x in range(5)]
    return cards


print(drawing_cards())