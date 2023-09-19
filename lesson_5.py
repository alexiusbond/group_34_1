from random import randint as generate_number, choice
import calculator
from person import Person
from termcolor import cprint
import emoji
from decouple import config

print(generate_number(2, 10))
print(calculator.addition(2, 10))

friend = Person('Jim', 25)
print(friend)
cprint("Hello, World!", "green", "on_red", attrs=["bold", "underline"])
print(emoji.emojize('Python is :thumbs_up:'))

print(config('DATABASE_URL'))
commented = config('COMMENTED', default=0, cast=int)
print(commented * 2)