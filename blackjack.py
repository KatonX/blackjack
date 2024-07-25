import random

title = """
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                  
"""

print(title)

class Cards:
    
    def __init__(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    def deal_card(self):
        card = random.choice(self.cards)
        return card

class BlackJack:
    
    def __init__(self):
        self.cards = Cards()
    
    def count_score(self, card):
        if sum(card) == 21 and len(card) == 2:
            return 0
        if 11 in card and sum(card) > 21:
            card.remove(11)
            card.append(1)
        return sum(card)
    
    @staticmethod
    def compare_score(user,comp):
        if user == comp:
            return "It's a draw"
        elif comp == 0:
            return "Computer Win"
        elif user == 0:
            return "User Win"
        elif user > 21:
            return "Computer Win"
        elif comp > 21:
            return "User Win"
        elif user > comp:
            return "User Win"
        else:
            return "Computer Win"
        
def play_game():

    user_card = []
    comp_card = []

    for i in range(2):
        card = Cards()
        user_card.append(card.deal_card())
        comp_card.append(card.deal_card())

    game_over = False

    while not game_over:
        game = BlackJack()
        user_score = game.count_score(user_card)
        comp_score = game.count_score(comp_card)
        
        print(f"Your card is {user_card}")
        print('-'*50)
        print(f"Comp card is {comp_card[0]}")
        
        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
            print("GAME OVER!!!")
        else:
            draw_card = input("Do you want to draw a card? Y or N\n").lower()
            if draw_card == 'y':
                user_card.append(card.deal_card())
                #print(f"your card is {user_card}")
            else:
                game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_card.append(card.deal_card())
        comp_score = game.count_score(comp_card)
        print(f"Computer Card: {comp_card}")
        
    print(f"Your score is: {user_score}")
    print(f"Computer score is: {comp_score}")
    print(BlackJack.compare_score(user_score, comp_score))

while input("do you want to play game? ").lower() == 'yes':
    play_game()
else:
    print("See you again!!")