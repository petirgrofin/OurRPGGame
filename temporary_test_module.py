from random import randint

fruits = ["apples", "cherries", "strawberries", "bananas", "watermelons", "melons"]

available_fruits = {keys: "In stock" for keys in fruits}

for fruit in list(available_fruits.keys()):
    probability = randint(0, 100)
    if probability > 50:
        unavailable_fruits = {fruit: "Not in stock"}
        available_fruits.update(unavailable_fruits)

print(available_fruits)

# -----------------------------------

new_dictionary = {}

for item in fruits:

    items = {item: item}

    new_dictionary.update(items)

print(new_dictionary)