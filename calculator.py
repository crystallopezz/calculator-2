"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
while True: 
    equation = input(">")
    acceptable_operands = ["+","-","*","/","square","cube","pow","mod"]
    tokenized_equation = equation.split(" ")
    if tokenized_equation[0] == "q":
        quit()
    else:
        if tokenized_equation[0] == "+":
            print(add(float(tokenized_equation[1]),float(tokenized_equation[2])))
        if tokenized_equation[0] == "-":
            print(subtract(float(tokenized_equation[1]),float(tokenized_equation[2])))
        if tokenized_equation[0] == "*":
            print(multiply(float(tokenized_equation[1]),float(tokenized_equation[2])))
        if tokenized_equation[0] == "/":
            print(divide(float(tokenized_equation[1]),float(tokenized_equation[2])))
        if tokenized_equation[0] == "square":
            print(square(float(tokenized_equation[1])))
        if tokenized_equation[0] == "cube":
            print(cube(float(tokenized_equation[1])))
        if tokenized_equation[0] == "pow":
            print(power(float(tokenized_equation[1]),float(tokenized_equation[2])))
        if tokenized_equation[0] == "mod":
            print(mod(float(tokenized_equation[1]),float(tokenized_equation[2])))