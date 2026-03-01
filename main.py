import time
from colorama import init, Fore, Style
init() # for colorama colors working in windows

from art import logo

def add(n1, n2):
    """function created to adds two numbers"""
    return n1 + n2

def subtraction(n1, n2):
    """function created to subtracts two numbers"""
    return n1 - n2

def multiplication(n1, n2):
    """function created to multiplicate two numbers"""
    return n1 * n2

def division(n1, n2):
    """function created to divide two numbers"""
    return n1 / n2

oper = ["+", "-", "*", "/"]
n = True  # variable for first number (a) input if
W = True  # variable for main loop working

while W: # boolean for main loop working
    print(logo)
    if n:
        while True:
            try:
                a = float(input("What's the first number: "))
                break
            except ValueError:
                print(Fore.RED + "You need to enter a number!" + Style.RESET_ALL)
                continue

    for klucz in oper:
        print(klucz)
    operation = input("Pick an operation: ")

    while True:
        if operation not in oper:
            print(Fore.RED + "You give a wrong operation symbol. Try again!!!" + Style.RESET_ALL)
            operation = input("Pick an operation: ")
            continue
        else:
            break

    while True:
        try:
            b = float(input("What's the next number?: "))
            break
        except ValueError:
            print(Fore.RED + "You need to enter a number!" + Style.RESET_ALL)
            continue
    if operation == "+":
        result = add(a,b)
    elif operation == "-":
        result = subtraction(a,b)
    elif operation == "*":
        result = multiplication(a,b)
    elif operation == "/":
        if b != 0:
            result = division(a,b)
        else:
             print(Fore.RED + "You can't division number by 0!" + Style.RESET_ALL)
             input("Press Enter to continue...")
             continue

    print(Fore.GREEN + f"{a} {operation} {b} = {result}" + Style.RESET_ALL)

    while True:
        con = input(f"Type 'y' to continue calculating with {Fore.GREEN}{result}{Style.RESET_ALL}, type 'n' to start a new calculation or 'e' to end program: ").lower()
        if con == 'y':
            n = False
            a = result
            break
        elif con == 'n':
            print("\n" * 20)
            n = True
            break
        elif con == 'e':
            print()
            for sec in range(3,-1,-1):
                print("Closing program - in " + Fore.RED + f"{sec}" + Style.RESET_ALL)
                time.sleep(1)
            print("\nGoodbye!")
            W = False
            break
        else:
            print(Fore.RED + "You write a wrong char. Try again!" + Style.RESET_ALL)