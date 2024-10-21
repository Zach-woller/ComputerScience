prime = True
cost = 20
age = 17
consent = False

if prime:
    if age >=18:
        print ("You are eligible for free shipping!")
    else:
        if consent:
            print ("You are eligible for free shipping!")
        else:
            print ("You are NOT eligible for free shipping.")

raining = True
outside = True

if raining == True:
    if outside == True:
        print ("Bring an umbrella")
else:
    print("Don't bring an umbrella")