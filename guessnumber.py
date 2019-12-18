import random 

hidden = random.randint(1,2000)
print(hidden)

guess = int(input("Please guess a number: "))

def guess(number):
    if number == hidden:
        print('YOU GOT IT!')
    elif number > hidden:
        print('Oh no! You guessed too high')
    elif number < hidden:
        print('Oh no you guessed too low!')
    else:
        print('Error. Please enter valid number')

guess(20)