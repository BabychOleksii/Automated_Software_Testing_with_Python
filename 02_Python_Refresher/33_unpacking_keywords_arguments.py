def named(name, age):
    print(name, age)


details = {"name": "Bob", "age": 25}

named(**details)


# ====================================


def named2(**kwargs):
    print(kwargs)


details2 = {"name": "Bob", "age": 25}

named(**details2)

# ====================================


def both(*args, **kwargs):
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)


both(1, 3, 5, "Canada", name="Alex", age=34)

