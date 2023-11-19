print("Welcome to the tip calculator.")
total_bill = input("What was the total bill ? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
people_count = input("How many people to split the bill? ")

bill_plus_tip = float(total_bill) + (float(total_bill) * float(tip_percentage))/100
bill_amt_per_person = round(bill_plus_tip/int(people_count),2)

print(f"Each person should pay: ${bill_amt_per_person}")
