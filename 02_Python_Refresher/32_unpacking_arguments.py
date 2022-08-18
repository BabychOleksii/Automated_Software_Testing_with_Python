def add_list(x, y):
    return x + y


list_nums = [3, 5]
print(add_list(*list_nums))


# ===========================

def add_dict(x, y):
    return x + y


dict_nums = {"x": 15, "y": 23}
print(add_dict(**dict_nums))

# ===========================


def multiply(*args):
    print(args)

    total = 1
    for arg in args:
        total = total * arg

    return total


print(multiply(1, 4, 3))


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 3, 6, 7, operator="*"))

