users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234"),
]


username_mapping = {user[1]: user for user in users}

print(username_mapping)
print(type(username_mapping))
print(username_mapping["Rolf"])

# Check the user and password pair using dictionary comprehension

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct!")
else:
    print("Your detail are incorrect!")
