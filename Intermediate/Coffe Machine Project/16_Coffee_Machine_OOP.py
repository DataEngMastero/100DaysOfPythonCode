from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

continue_machine = True
while continue_machine:
    menu_items = menu.get_items()
    user_choice = input(f"What would you like ?  {menu_items} : ")
    if user_choice == "off":
        continue_machine = False 
        break
    elif user_choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(user_choice)
        if isinstance(coffee, MenuItem) and coffee.name == user_choice:
            if coffee_machine.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
                    coffee_machine.make_coffee(coffee)                
        else:
            print(coffee)


