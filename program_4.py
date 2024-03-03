# Create a function with variable length of arguments. Write a program to create function func1() to accept a variable length of arguments and print the

def function1(*args):
    for arg in args:
        print("arguments:", arg)

function1(20, 40, 60)

function1(80, 100)