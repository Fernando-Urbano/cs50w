people = [
    {"name": "Monica", "t_shirt": "red"},
    {"name": "Cebolinha", "t_shirt": "green"},
    {"name": "Magali", "t_shirt": "yellow"},
]


# How to sort?
def f(person):
    return person["name"]


people.sort(key=f)
print(people)


# How to sort with lambda?
people.sort(key=lambda person: person["name"])
print(people)


