import random

def random_end():
    print

weird_end = random.randint(1, 1000001)

if weird_end == 1: 
    random_end()

def death():            #death screen
    print ("You  have died!")
    print("continue?")
    print("1. Yes")
    print("2. No")

    death_health_choice = input("> ")

    if death_health_choice == "1":
        start_menu()
    elif death_health_choice == "2":
        print("ending program")
    else:
        print("ERROR Unexpected input")
        death()


health = 30 
if health == 0:         #tracks health and plays a death screen if none is left
    death()



def start_nate():       #start game with choosen character
    print("You awake to the sound of explosion. You get up of the couch and look out the window to see a crashed helicopter in the middle of the street. Luckly since the whole city is under lockdown do to a pandemic no one was hurt apart from the pilot and the other people on the helicopter. as you think you see some people rush out of buildings as they do the crew of the helicopter jump out at them, attacking them as this happens a hoarde of what look like people approach from the right.")
    print("what do you do?")
    print("1. grab your stuff and run to the car")
    print("2. hide in your apartment")
    print("3. run out and help the people near the helicopter")

    nate_choice_1 = input("> ")
    

    if nate_choice_1 == "1":
        print

def start_rose():       #start game with choosen character
    print  

def start_robbie():     #start game with choosen character
    print

def start_jonas():      #start game with choosen character
    print

def nate():             #tells player what the character has and who they are
    print("Nate is a 45 year old retired firefighter who resides in a small apartment in the Bronx. He has a backpack with 3 days of canned food and water. He owns a car and survival hatchet.")
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

def rose():             #tells player what the character has and who they are
    print("Rose is a 22 year old barista who works at starbucks. She owns a apartment in Manhattan. her purse has 2 days of canned food and water.")
    print ("1. start journey")
    print ("2. choose different character")

    character_2 = input("> ")

    if character_2 == "1":
        start_rose()
    elif character_2 == "2":
        character_menu()
    else:
        print("ERROR Unexpected input")
        rose()

def robbie():           #tells player what the character has and who they are
    print("Robbie is a 26 year old artist living Brooklyln. He is living out of his car he has a plasic bag with 5 days of food and water. he owns a  swiss army knife.")
    print ("1. start journey")
    print ("2. choose different character")

    character_2 = input("> ")

    if character_2 == "1":
        start_robbie()
    elif character_2 == "2":
        character_menu()
    else:
        print("ERROR Unexpected input")
        robbie()

def jonas():            #tells player what the character has and who they are
    print("Jonas is a 19 year old college student. he lives with with his mom and dad in a quaint little neighborhood in Queens. He owns a moped and has a tazer for self defence. he has 4 days of food and water.")
    print ("1. start journey")
    print ("2. choose different character")

    character_2 = input("> ")

    if character_2 == "1":
        start_jonas()
    elif character_2 == "2":
        character_menu()
    else:
        print("ERROR Unexpected input")
        jonas()

def character_menu():   #one of two menus
    print("The year is 1998. A zombie virus has taken the world by storm. it is unknown how it came to but its here now. You are living in new york.  You need to leave")
    print("choose your character")
    print("1. Nate") 
    print("2. Rose")
    print("3. Robbie")
    print("4. Jonas")
    print("5. return to menu")

    character = input("> ")
    
    if character == "1": 
        nate()
    elif character == "2":
        rose()
    elif character == "3":
        robbie()
    elif character == "4":
        jonas()
    elif character == "5":
        start_menu()
    else:
        print("ERROR Unexpected input")
        character_menu()

def start_menu():       #one of two menus
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