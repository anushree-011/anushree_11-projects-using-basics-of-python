import random 
from replit import clear
from art import logo
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score>21 and computer_score>21:
        return "You went over. You lose"
    if user_score==computer_score:
        return "Draw"
    elif user_score==0:
        return "win with a blackjack"
    elif computer_score==0:
        return "you lost , opponent has blackjack"
    elif user_score>21:
        return "You went over . you lose"
    elif computer_score>21:
        return "opponent went over . you win"
    elif user_score>computer_score:
        return "You win"
    else:
        return "you lost"
    
def play_game():
    print(logo)
    user_card=[]
    computer_card=[]
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    get_card=True
    while(get_card):
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)
        print(f"Your cards: {user_card},current score:{user_score}")
        print(f"Computer's first card:{computer_card[0]}")

        if user_score==0 and computer_score==0 or user_score>21:
            get_card=False
        else:
            deal=input("Type 'y' to get another card , type 'n' to pass")
            if deal=="y":
                user_card.append(deal_card())
            else:
                get_card=False

    while computer_score!=0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)
    print(f"   Your final hand: {user_card}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()


    
 

