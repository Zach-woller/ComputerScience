def tally_score():
    score = 0
    if question_1 == 5:
        score = score +1
    if question_2 == 17:
        score = score +1
    if question_3 == 6:
        score = score +1
    if question_4 == 8:
        score = score +1
    if question_5 < 9:
        score = score +1
    print(score)
score = 0
question_1 = int(input("What is 7 - 2\n>"))
question_2 = int(input("What is 10 + 7\n>"))
question_3 = int(input("What is 3 * 2\n>"))
question_4 = int(input("What is 4 * 2\n>"))
question_5 = int(input("Name a number less then 9\n>"))
tally_score()
