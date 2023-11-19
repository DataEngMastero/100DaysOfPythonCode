# Revisit Her code - Different Logic
logo = '''
     ____  ____   ____    ____  ____ _____     ____  _ _____  _   _  ____ _____ 
    / (__`| ===| / () \  (_ (_`| ===|| () )   / (__`| || ()_)| |_| || ===|| () )
    \____)|____|/__/\__\.__)__)|____||_|\_\   \____)|_||_|   |_| |_||____||_|\_\\
'''
print(logo)

def text_generator(command, msg, shift):
    new_msg = ""
    for letter in msg:
        ascii_code = ord(letter)
        if command == 'encode':
            new_msg += chr(ascii_code + shift)
        else:
            new_msg += chr(ascii_code - shift)

    print(f"Heres the result : {new_msg}.")

end_program = False
while not end_program:
    commad = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    msg = input("Type your message: \n")
    shift = input("Type the shift number: \n")
    text_generator(commad, msg, int(shift))
    continue_program = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if continue_program == 'no':
        end_program = True
