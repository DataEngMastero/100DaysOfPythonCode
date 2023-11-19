import Higher_Lower_Constants as hlc
import random
from replit import clear

def game_screen(option_A, option_B, score):
    print(hlc.higher_lower)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    print(f"Compare A : {option_A['name']}, {option_A['description']}, from {option_A['country']}")
    print(hlc.vs)
    print(f"Against A : {option_B['name']}, {option_B['description']}, from {option_B['country']}")

    print("----- FOR TESTING -----")
    print(option_A)
    print(option_B)

def check_answer(choice, option_A, option_B):
    if (choice == 'A' and option_A['followers'] > option_B['followers']) or (choice == 'B' and option_A['followers'] < option_B['followers']):
        return True
    else:
        return False


option_A = random.choice(hlc.game_data)
option_B = random.choice(hlc.game_data)
if option_A == option_B:
    option_B = random.choice(hlc.game_data)
    

end_game = False
score = 0
already_played = []

while not end_game:
    game_screen(option_A,option_B, score)
    choice = input("Who has more followers? Type 'A' or 'B' - ").upper()

    if check_answer(choice, option_A, option_B):
        score += 1
        if choice == 'A' :
            already_played.append(option_B['name'])
            
        else:
            already_played.append(option_A['name'])
            option_A = option_B

        
        option_B = random.choice(hlc.game_data)
        while option_B['name'] in already_played:
            print(option_B)
            option_B = random.choice(hlc.game_data)
    else:
        end_game = True

    clear()

print(hlc.higher_lower)
print(f"Sorry, that's wrong. Final score: {score}")