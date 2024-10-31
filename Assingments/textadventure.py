import random

def random_end():
    print

weird_end = random.randint(0, 1000001)

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



    print


def path_1():
    print("As you in the back seat your dad says:")
    print("Good thinking")
    print("As the car drives down the road you see a traffic traffic jam")


def start_jonas():     
    print("You wake up to the sound of sirens stating:")
    print("infection has breached contament!")
    print("As this happens your mom yells:")
    print("Grab what ever you can and get in the car")
    print("1. Grab your dads hunting shotgun")
    print("2. Grab some medicine")
    print("3. Grab  cds and magazines")
    print("4. Exit game")

    start_jonas_choice = input("> ")

    if start_jonas_choice == "1":
        print
    elif start_jonas_choice == "2":
        print
    elif start_jonas_choice == "3":
        print
    elif start_jonas_choice == "4":
        print("ending program")
    else:
        print("ERROR Unexpected input")
        start_jonas()

def character_menu():   
    print("The year is 1998. A zombie virus has taken the world by storm. it is unknown how it came to but its here now. You are living in New York.  You need to leave")
    print("You are jonas a 19 year old college student. he lives with with his mom and dad in a quaint little neighborhood in Queens. He owns a taser for self defence. his family has a weeks worth of food and water.")
    print ("1. start")
    print ("2. Back")

    start = input("> ")

    if start == "1":
        start_jonas()
    elif start == "2":
        start_menu()
    else:
        print("ERROR Unexpected input")
        character_menu()

def start_menu():       #menu
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