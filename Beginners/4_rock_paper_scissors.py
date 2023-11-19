import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Welcome to Rock, Paper and Scissors Game.")
print("Type what you choose. 0 => Rock, 1 => Paper, 2 => Scissors")
user_choice = int(input())

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)

print("\n\nComputer chooses: ")
computer_choice = random.randint(0,1)
print(computer_choice)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

# Rules of Game
if(user_choice == computer_choice):
    print("Draw")
elif(user_choice == 1 and computer_choice == 0):
    print("You win!")
elif(user_choice == 0 and computer_choice == 1):
    print("Computer wins!")

elif(user_choice == 0 and computer_choice == 2):
    print("You win!")
elif(user_choice == 2 and computer_choice == 0):
    print("Computer wins!")

elif(user_choice == 2 and computer_choice == 1):
    print("You win!")
elif(user_choice == 1 and computer_choice == 2):
    print("Computer wins!")