"""CLI application for a prefix-notation calculator."""
from functools import reduce

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    try:

        # assign varitable to the input string

        user_equation = input("enter your equation > ")
    
        # assign a v ariable to the split fucntion
        # use split fucntion with a deliminator to tokenize a string into a list
        user_equation = user_equation.split(" ")

        # the first item in the list is what you will do to the second two items in the list

        if user_equation[0] == "q":
            print("Done")
            break

        elif user_equation[0] == "+":
            # len == 3
            # 2 args have to be numbers
            if len(user_equation) == 3:
                print(add(float(user_equation[1]), float(user_equation[2])))
            
        elif user_equation[0] == "-":
            print(subtract(float(user_equation[1]), float(user_equation[2])))

        elif user_equation[0] == "*":
            print(multiply(float(user_equation[1]), float(user_equation[2])))

        elif user_equation[0] == "/":
            print(divide(float(user_equation[1]), float(user_equation[2])))

        elif user_equation[0] == "square":
            print(square(float(user_equation[1])))

        elif user_equation[0] == "cube":
            print(cube(float(user_equation[1])))

        elif user_equation[0] == "power":
            print(pow(float(user_equation[1]), float(user_equation[2])))

        elif user_equation[0] == "mod":
            print(mod(float(user_equation[1]), float(user_equation[2])))

    except(ValueError):
        print("Please enter only integers using the correct format")
