health = 30 
if health == 0:
    death_health()

    def death_health():
        print

def start_nate():
    print

def nate(): 
    print("Nate is a 45 year old retired firefighter who resides in a small apartment in the Bronx. He has a backpack with 3 days of canned food and 5 days of water. He owns a car and survival hatchet.")
    print ("1. start journey")
    print ("2. choose different character")

    character_1 = input("> ")

    if character_1 == "1":
        start_nate()
    elif character_1 == "2":
        character_menu()
    else:
        print("ERROR Unexpected input")
        nate()

def rose():
    print("Rose is a 22 year old barista who works at starbucks. She owns a apartment in Manhattan her purse has 2 days of canned food")

def robbie():
    print

def jonas():
    print

def character_menu():
    print("The year is 1997. A zombie virus has taken the world by storm. it is unknown how it came to but its here now. You are living in new york.  You need to leave")
    print("choose your character")
    print("1. Nate") 
    print("2. Rose")
    print("3. Robbie")
    print("4. Jonas")

    character = input("> ")
    
    if character == "1": 
        nate()
    elif character == "2":
        rose()
    elif character == "3":
        robbie()
    elif character == "4":
        jonas()
    else:
        print("ERROR Unexpected input")
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
          character_menu()
    else:
        print("ERROR Unexpected input")
        start_menu()
start_menu()