import random
from replit import clear
from Hangman_Constants import stages, word_list, hangman

print(hangman)

word_list = ['valueable', 'recitation', 'quite', 'professor']
choice_word = random.choice(word_list)
print('Pssst, the solution is ', choice_word)


word_length = len(choice_word)
answer_word = []
for letter in range(word_length):
    answer_word.append("_")

end_of_game = False
lives = 6
while not end_of_game:
    guess = input('Guess a letter: ').lower()
    clear()
    word_found = False
    for position in range(word_length):
        if choice_word[position] == guess:
            answer_word[position] = choice_word[position]
            word_found = True 

    
    if not word_found:
        lives -= 1
            
    print(''.join(answer_word))

    if lives == 0:
        end_of_game = True
        print('You Lose')

    if '_' not in answer_word:
        end_of_game = True
        print('You Win!')

    print(stages[lives])