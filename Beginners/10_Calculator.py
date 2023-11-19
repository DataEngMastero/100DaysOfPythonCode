logo = '''
|  _________________  |
| | My Calculator.  | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

'''

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

operations = {
    '+' : add, 
    '-' : subtract,
    '*' : multiply,
    '/' : divide
}

def calculator():
    first_number = float(input("What's the first number : "))
    for op in operations:
        print(op)

    should_continue = True

    while should_continue: 
        operation = input("Pick an operation : ")
        second_number = float(input("What's the second number : "))

        answer = operations[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {answer}")

        continue_cal = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit : ")
        if continue_cal == 'y':
            first_number = answer
        else:
            should_continue = False
            calculator()



calculator()