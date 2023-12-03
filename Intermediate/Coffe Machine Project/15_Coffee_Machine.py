menu_list = {
    "espresso" : {
        "water" : 50,
        "coffee" : 18,
        "money" : 1.50
    },
    "latte" : {
        "water" : 200,
        "coffee" : 24,
        "milk" : 150,
        "money" : 2.50,
    },
    "cappuccino" : {
        "water" : 250,
        "coffee" : 24,
        "milk" : 100,
        "money" : 3.00
    }
}

machine_resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
    "money" : 2.5
}

coins_values = {
    "quarter" : 0.25,
    "dime" : 0.10,
    "nickle" : 0.05,
    "penny" : 0.01
}

def show_report():
    return f"""
    Water : {machine_resources['water']}ml
    Milk : {machine_resources['milk']}ml
    Coffee : {machine_resources['coffee']}g
    Money : ${machine_resources['money']}
    """

def check_resources(user_choice):
    required_resources = menu_list[user_choice]

    for resource, value in machine_resources.items():
        if resource != 'money' and resource in required_resources and required_resources[resource] > value:
            print(f"Sorry there is not enough {resource}.")
            return False
        
    return True

def process_coins(user_choice, quarters, nickles, dimes, pennies):
    coffee_cost = menu_list[user_choice]['money']
    total_coins = round(quarters * coins_values['quarter'] + nickles * coins_values['nickle'] \
        + dimes * coins_values['dime'] + pennies * coins_values['penny' ], 2)
    
    print(f"Coffee Cost - {coffee_cost} and Total Counts - {total_coins}")
    if total_coins < coffee_cost:
        print(f"Sorry that's not enough money. Money Refunded")
        return False
    elif total_coins > coffee_cost:
        change = round(total_coins - coffee_cost,2)
        print(f"Here is ${change} in change.")
    
    machine_resources['money'] += total_coins
    machine_resources['water'] -= menu_list[user_choice]['water']
    machine_resources['coffee'] -= menu_list[user_choice]['coffee']
    if 'milk' in menu_list[user_choice]:
        machine_resources['milk'] -= menu_list[user_choice]['milk']

    return True

while True:
    user_choice = input("What would you like ? (espresso/latte/cappuccino) ")
    if user_choice == "off":
        break
    elif user_choice == "report":
        print(show_report())
    elif user_choice in ['espresso', 'latte', 'cappuccino']:
        if check_resources(user_choice):
            # Process Coins 
            quarters = int(input("How many quarters ? "))
            dimes = int(input("How many dimes ? "))
            nickles = int(input("How many nickles ? "))
            pennies = int(input("How many pennies ? "))
            if process_coins(user_choice, quarters, nickles, dimes, pennies):
                print(f"Here's your {user_choice}. Enjoy!")
    
             
    
