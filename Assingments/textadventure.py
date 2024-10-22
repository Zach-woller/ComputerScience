def character_menu():
    print("choose your character")
    print("1. Nate") 
    print("2. Rose")
    print("3.")
    print("4. Jonas")


def start_game():
    print("The year is 1997. A zombie virus has taken the world by storm. it is unknown how it came to but its here now. You are living in new york.  You need to leave")
    character_menu()
def start_menu():
    print("ROAD TO DULUTH")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print ("1. Start")
    print ("2. Close")

    start = input("> ")

    if start == "2":
        print("ending program")
    elif start == "1":
          start_game()
    else:
        print("ERROR Unexpected input")
        start_menu()
start_menu()