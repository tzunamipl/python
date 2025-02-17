# Required arguments

def print_hello(name):
    print("Hello", name)

print_hello("Name")

# Positional arguments

def user_info(name, age):
    print("Hello ", name, age)

user_info("Tom", 33)

# Keyword arguments

user_info(age=33, name="Dupa")

# Default arguments

def user_data(name, ID, age=20):
    print("Hello", name, ID, "your age is", age)

user_data("Michael", "DF3623")

# Varable=length arguments

def greet(*name, age):
    for s in name:
        print("Hello", s, age, end="! ")

greet("Tom", "Michael", "Gloin", "Bofur", "Bombur", age=40)