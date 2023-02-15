from art import logo
from os import system

def add(n1, n2):
    return n1+n2

def substract(n1,n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


operations = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide
}

def calculator(): #RECURSION
    system("cls")
    print(logo)
    
    num1 = float(input("What is the first number?: "))
    for sign in operations.keys():
        print(sign)
    should_continue = True

    while should_continue:
        operation_symbol = input("\nPick an operation form the lines above: ")
        num2 = float(input("What is the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculting with {answer}, or 'n' to start a new calculation: ").lower().strip() == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
            
calculator()
            
