add = lambda x, y: x + y

print(add(5, 7))

# =============================

(lambda x, y: x + y)(5, 7)


# =============================

def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]
doubled2 = [(lambda x: x * 2)(x) for x in sequence]
doubled3 = list(map(double, sequence))
doubled4 = list(map(lambda x: x * 2, sequence))
