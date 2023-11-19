# https://ascii.co.uk/art/treasure
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('Welcome to Treasure Island')
print('Your mission is to find the treasure.')
direction =  input("You're at the cross road. Where do you want to go ? Type 'left' or 'right'.")

if direction == "left":
    activity = input("You come to a lake. There is an island in the midle of the lake. Type 'wait' or 'swim'.")
    if activity == "wait":
        house = input("You arrived at island unharmed. There is a house with 3 doors. Which color do you choose ? Type red, yellow or blue.")
        if house == 'blue':
            print("Entered room full of beasts. GAME OVER!")
        elif house == 'red':
            print("Ambushed by flying knives. GAME OVER!")
        else:
            print("You found the treasure. You win!")
    else:
        print("There are crocodiles in water. GAME OVER!")
else:
    print("Fell of the edge. GAME OVER!")


