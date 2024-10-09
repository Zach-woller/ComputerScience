hurricane_speed = input("How fast is the storm?\n>").upper()
hurricane_speed = int(hurricane_speed)

if hurricane_speed < 74:
    print("Tropical storm")

elif hurricane_speed < 96:
    print("Category 1")

elif hurricane_speed < 111:
    print("category 2")

elif hurricane_speed < 130:
    print("catergory 3")

elif hurricane_speed < 157:
    print("category 4")

elif hurricane_speed >= 157:
    print("category 5")