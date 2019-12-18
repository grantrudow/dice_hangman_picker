import random

restaurant = {1:"Chilis", 2:"Rice & Spice", 3:"Applebees", 4:"Volta", 5:"Bravo"}

number = int(input('Pick a number 1-5: '))

def picker(number):
        value = number
        return restaurant.get(value)

print('You should go to: ' + picker(number))