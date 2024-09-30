def add():
    x = input("what is the 1st number?\n>")
    x= int(x)
    y = input("what is the 2nd number?\n>")
    y = int(y)
    print(str(x) + " + " + str(y) + " = " + str(x + y)) #states the problem then solves it
def subtract():
    x = input("what is the 1st number?\n>")
    x= int(x)
    y = input("what is the 2nd number?\n>")
    y = int(y)
    print(str(x) + " - " + str(y) + " = " + str(x - y)) #states the problem then solves it
def multiply():
    x = input("what is the 1st number?\n>")
    x= int(x)
    y = input("what is the 2nd number?\n>")
    y = int(y)
    print(str(x) + " * " + str(y) + " = " + str(x * y)) #states the problem then solves it
def divide():
    x = input("what is the 1st number?\n>")
    x= int(x)
    y = input("what is the 2nd number?\n>")
    y = int(y)
    print(str(x) + " / " + str(y) + " / " + str(x / y)) #states the problem then solves it

add()
subtract()
multiply()
divide()