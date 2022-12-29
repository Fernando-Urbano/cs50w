def announce(func):
    def wrapper():
        print("About to run the function...")
        func()
        print()
    return wrapper


@announce
def hello():
    print("Hello, world!")


hello()