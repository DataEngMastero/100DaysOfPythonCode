import random

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ] 
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to the PyPassword Generator!")
letters_len = int(input("How many letters would you like in your password ?"))
symbols_len = int(input("How many symbols would you like ?"))
numbers_len = int(input("How many numbers would you like ?"))

passowrd = ""

# EASY LEVEL
# for i in range(1, letters_len + 1):
#     letter = random.randrange(0,len(alphabets))
#     passowrd += alphabets[letter]

# for i in range(1, numbers_len + 1):
#     number = random.randrange(0, len(numbers))
#     passowrd += numbers[number]

# for i in range(1, symbols_len + 1):
#     symbol = random.randrange(0, len(symbols))
#     passowrd += symbols[symbol]

# HARD PART
eligible_chars = numbers + alphabets + symbols
for i in range(1, letters_len + symbols_len + numbers_len + 1):
    pass_char = random.choice(eligible_chars)
    passowrd += pass_char

print(f"Here is your password : {passowrd}")