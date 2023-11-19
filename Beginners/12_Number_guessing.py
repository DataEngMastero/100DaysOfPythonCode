import random

def validate_guess(number, select_number):
    if number == select_number:
        return True 
    elif number > select_number:
        print("Too high")
        return False 
    else:
        print("Too low")
        return False


print('Welcome to Number Guessing Game!')
print("I'm thinking of number between 1 and 100.")
numbers = [i for i in range(1,101)]
difficulty_dict = {
    'easy': 10,
    'medium': 8,
    'hard': 5
}

select_number = random.choice(numbers)
difficulty = input("Choose a difficulty. Type 'easy', 'medium' or 'hard': ")
attempts_left = difficulty_dict[difficulty]

while attempts_left > 0:
    print(f"You have {attempts_left} attempts remaining to guess the number. ")
    guess = int(input("Make a guess : "))
    is_guess_correct = validate_guess(guess, select_number)
    attempts_left = attempts_left - 1
    
    if is_guess_correct:
        print('You got it')
        break 
    elif not is_guess_correct and attempts_left > 0:
        print("Guess again.")
    else:
        print("You ran out of guesses. You lose.")


