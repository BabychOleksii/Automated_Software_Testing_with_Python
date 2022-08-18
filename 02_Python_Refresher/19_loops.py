number = 7

while True:
    user_input = input("Would you like to play? (y/n) :")

    if user_input == "n":
        break

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif (number - user_number) in (1, -1):
        print("You were off by one")
    else:
        print("Sorry, it's wrong!")

# ===================================

grades = [35, 67, 98, 100, 105]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print (total / amount)