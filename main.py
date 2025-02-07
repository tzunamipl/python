#user_name = input("What is your name? ")
#ser_age = input("How old are you? ")

#print("Hello " + user_name + ", you are " + user_age)

from classes.module import say_hello
from classes.module import double_number

def print_double(number):
    print("Double of " + str(number) + " is " + str(double_number(number)))

say_hello("Dupa", 34)
say_hello("Dddduupaaa", 56)
say_hello("Dudu", 3)

print_double(5)
