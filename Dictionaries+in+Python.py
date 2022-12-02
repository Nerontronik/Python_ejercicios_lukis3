# Python 101 by Anton Ryzhenkov

# Dictionaries - {}, each element represent pair key.value

people_ages = {"Andrew":25, "Lisa":18,"Bob":60}
print(people_ages["Andrew"])
print(people_ages["Lisa"])

colors = {
    "red":[255,0,0],
    "green":[0,255,0],
    "blue":[0,0,255]}

print(colors["red"])
# print(colors["purple"])

# Only immutable objects can be used as keys to dictionaries
''' bad_dictionary = {
    [5,6,7]:"five, six, seven",
    }'''
