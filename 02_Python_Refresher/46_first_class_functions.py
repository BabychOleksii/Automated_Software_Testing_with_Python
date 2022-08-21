def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 3, operator=divide)
print(result)

# result2 = calculate(20, 4, 3, operator=divide)
# print(result2)

# ========================================================


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "Rolf Smith", "age": 34},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Adam Wool", lambda friend: friend["name"]))
print(search(friends, "Rolf Smith", get_friend_name))
print(search(friends, "Rolf Wool", get_friend_name))
