import random 
from replit import clear

logo = """
                           .------.
        .------.           |A .   |
        |A_  _ |    .------; / \  |
        |( \/ )|-----. _   |(_,_) |
        | \  / | /\  |( )  |  I  A|
        |  \/ A|/  \ |_x_) |------'
        `-----+'\  / | Y  A|
              |  \/ A|-----'    
              `------'
"""


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def calculate_winner(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, Opponent has blackjack"
    elif user_score == 0:
        return "Win with a blackjack"
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."

def play_game():
    is_game_ended = False
    user_cards = random.sample(cards, 2)
    computer_cards =  random.sample(cards, 2)
    while not is_game_ended:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, Current Score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_ended = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass : ").lower()
            if another_card == 'y':
                user_cards.append(random.choice(cards))
            else:
                is_game_ended = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = calculate_score(computer_cards)      

    print(f"    Your final hand is {user_cards}, final_score = {user_score}")
    print(f"    Computer's final hand is {computer_cards}, final_score = {computer_score}")
    print(calculate_winner(user_score,computer_score))

while input("Do you want to play a game of blackjack ? Type 'y' for yes, 'n' for no  ? ") == "y":
    clear()
    play_game()