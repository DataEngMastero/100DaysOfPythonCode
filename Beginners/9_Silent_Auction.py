from replit import clear

logo = '''
    ___________
    \         /
     )_______(
     |"""""""|_.-._,.---------.,_.-._
     |       | | |               | | ''-.
     |       |_| |_             _| |_..-'
     |_______| '-' `'---------'` '-'
     )"""""""(
    /_________\\
    `'-------'`
   .-------------.
 /_______________\\
'''
print(logo)
print('Welcome to the secret auction program')

bidders_dict = {}
end_loop = False
while not end_loop:
    name = input("What is your name ?: ")
    bid_amt = int(input("What\'s your bid ?: "))
    bidders_dict[name] = bid_amt

    continue_loop = input("Are there any other bidders ? Type 'yes' or 'no'.")
    if continue_loop == 'no':
        end_loop = True
    clear()

winner_name = ""
winner_amt = 0
for bid in bidders_dict:
    if winner_amt < bidders_dict[bid]:
        winner_amt = bidders_dict[bid]
        winner_name = bid
    
print(f'The winner of the bidding is {winner_name} with amount ${winner_amt}.')

    

