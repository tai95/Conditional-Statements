
#!/bin/python3 

#conditional statements 


def drink(money):
    if money >= 2:
        return "You've got yourself a drink"
    else:
        return "No drink for you"

print(drink(5))
print(drink(1))


def alcohol(age, money):
    if (age >= 21) and (money >= 5):
        return "we're getting a drink"
    elif (age >= 21) and (money < 5):
        return "Come back with more money"
    elif (age < 21) and (money >= 5):
        return "Nice try, kid"

    else:
        return "You're too young and too broke "

print(alcohol(25,7))
print(alcohol(26,2))
print(alcohol(20,5))
print(alcohol(20,2))

