#if statements deside what code to run next
#take temp
#print "temp is hot" if temp is > or = 80
temp = input("What is the temp\n>")
temp = int(temp)
if temp >= 80:
    print(str(temp) + " degrees is hot")

if temp < 80:
    print(str(temp) + " degrees is not hot")