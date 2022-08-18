friends = ["Rolf", "Bob", "Jen"]
print("Jen" in friends)

cities = {"Edmonton", "Calgary", "Winnipeg"}
user_city = input("Enter your city: ")
print(user_city in cities)


number = 7
user_number = input("Enter your number")

if user_number == number:
    print("You guessed correctly!")
elif (number - user_number) in (1, -1):
    print("You were off by one")
else:
    print("Sorry, it's wrong!")