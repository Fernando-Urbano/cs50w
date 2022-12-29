# Python
Python is a interpretable language, meaning we can read and execute it line by line.

`e = None` has NoneType

# Class
Define a class:
```
class Point():
    def __init__(self, x_axis, y_axis):
        self.x_axis = x_axis
        self.y_axis = y_axis
```
`self`: represents the object it self.
`__init__`: server as a magic method to instanciate a class.

# Decorators
Is a function that takes a function as input and gives a modified version of that function.

A function can be viewed as a value.

```
def announce(func):
    def wrapper():
        print("About to run the function...")
        func()
        print()
    return wrapper
```

The announce is a decorator that adds a function to the other function.

Than we add the announce function to the hello function:

```
@announce
def hello():
    print("Hello, world!")
```

For instance, decorator can be really useful to assure that a function can only be run if a user is log-in.

# Lambda Function
Useful to sort dictionary.
```
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
```

# Exceptions
```
import sys

x = int(input("X: "))
y = int(input("Y: "))

try:
    x / y = result
    print(result)
except Exception as e:
    print(f"Problem in division: {e}")
    sys.exit(1) # Exit the program saying that there was a problem
```