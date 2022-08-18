name = "Bob"

print("Hello, {}".format(name))

print("{} {}".format("Hello,", name))

print(f"Hello, {name}")

greeting = "Hello, {}"
with_name = greeting.format(name)
print(with_name)

square_feet = 2000
square_meters = square_feet / 10.8
print(f"{square_feet} square feet is equal to {square_meters:.2f} square meters.")