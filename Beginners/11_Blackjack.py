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

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def calculate_score(cards_list):
    score = 0
    for card in cards_list:
        if card in cards[:-4]: 
            score += int(card)
        elif card in cards[-4:-1]:
            score += 10
        elif score < 11 and card == 'A':
            score += 11
        else:
            score += 1
    
    return score

# Ask user if they want to play - TODO
while input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ") == 'y':
    # Print logo
    clear()
    print(logo)
        
    # Random Selection of 2 Cards and Calculate Score
    user_cards = random.sample(cards, 2)
    computer_cards =  random.sample(cards, 2)

    draw_card = True
    while draw_card:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Show User Cards and its core and Computer's first card
        print(f"Your cards: {user_cards}, Current Score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Ask User for Another-Pass
        another_card = input("Type 'y' to get another card, type 'n' to pass : ").lower()
        if another_card == 'n' or user_score > 21 or computer_score > 21:
            draw_card = False
        elif another_card == 'y':
            user_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))

            
    # Evaluate final score of User and Computer
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, Final Score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, Final Score : {computer_score}")

    # Declare Winner - TODO
    if user_score > 21:
        print("You went over. You lose!")
    elif computer_score > 21:
        print("Opponent went over. You winss!")
    elif user_score > computer_score:
        print('You wins!')
    else:
        print('Computer wins!')