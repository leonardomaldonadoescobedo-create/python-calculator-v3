#---PYTHON-CALCULATOR-V3---

import math

def menu():
    
    print("=== PYTHON-CALCULATOR-V3 ===")
    print("")
    print("=== Basic Operations ===")
    
    options = [
        "1. Addition" ,
        "2. Subtraction" ,
        "3. Multiplication" ,
        "4. Division" , 
    ]
    
    for i in options:
        print(i)
    
def menu2():
    
    print("=== Other Operations ===")
    
    options = [
        "5. Percentage" ,
        "6. Power" ,
        "7. Modulo" ,
        "8. Square Root" , 
        "9. Factorial" ,
        "",
        "0. Exist" , 
    ]
    
    for i in options:
        print(i)
    
    print("========================")

def addiction(a, b):
    return a + b
    
def subtraction(a, b):
    return a - b
    
def multiplication(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("SYNTAX ERROR")
        
def percentage(a, b):
    try:
        return a * b / 100
    except ZeroDivisionError:
        print("SYNTAX ERROR")   
        
def power(a, b):
    return a ** b
    
def modulo(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        print("SYNTAX ERROR")
        
def square_root(a):
    return math.sqrt(a)
    
def factorial(a):
    counter = a = int(a)
    
    for i in range(1 , a):
        counter *= i
    
    return counter
        
while True:
    menu()
    menu2()
    
    try:
        option = int(input("Write an option:"))
        
        if option == 0:
            break
        
        a = float(input("Write a first number:"))
        
        if option == 8:
            answer = square_root(a)
            print("The answer is:" , answer)
        elif option == 9:
            answer = factorial(a)
            print("The answer is" , answer)
        else:
             b = float(input("Write a second number:"))
        
        if option == 1:
            answer = sum(a, b)
            print("The answer is:" , answer)
        elif option == 2:
            answer = subtraction(a, b)
            print("The answer is:" , answer)
        elif option == 3:
            answer = multiplication(a, b)
            print("The answer is:" , answer)
        elif option == 4:
            answer = division(a, b)
            print("The answer is:" , answer)
        elif option == 5:
            answer = percentage(a, b)
            print("The answer is:" , answer)
        elif option == 6:
            answer = power(a, b)
            print("The answer is:" , answer)
        elif option == 7:
            answer = modulo(a, b)
            print("The answer is:" , answer)
        else:
            print("That option doesn´t exist")
        
    except ValueError:
        print("SYNTAX ERROR")
