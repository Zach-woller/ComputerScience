trys = 0
real_password = "PAssWord"
entered_password = ""

while real_password != entered_password:
    entered_password = input("Please enter your password\n>")
    if entered_password == real_password:
        print("ACCESS GRANTED")
    else:
        trys += 1
        print("ACCESS DENIED")
        print("renter password")
        print(str(trys) + " try")

print("Welcome")

user_input = ""

while user_input != "exit":
    user_input = input("Enter something (type 'exit' to quit)")
    print("your entered: " + user_input)

print("Okay")