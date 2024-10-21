def bonus_time(salary, bonus):
    salary = int(salary)
    if bonus == True:
        salary = salary * 10
    else:
        salary = salary * 1

bonus_time(10, True)