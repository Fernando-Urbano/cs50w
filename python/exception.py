import sys

x = int(input("X: "))
y = int(input("Y: "))

try:
    result = x / y
    print(result)
except Exception as e:
    print(f"Problem in division: {e}")
    sys.exit(1) # Exit the program saying that there was a problem