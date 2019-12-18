import random
import time

print('Welcome to rock, paper, scissors...lets see what you can do!')
time.sleep(0.5)

rock = "rock"
paper = "paper"
scissors = "scissors"


choice = input('Pick your fighter: rock, paper, or scissors? ')

print('Get Ready...')
time.sleep(1)
print('..3')
time.sleep(1)
print('..2')
time.sleep(1)
print('..1')
time.sleep(1)
print('..shoot!')
time.sleep(0.5)

computer_choices = {1: 'rock', 2: 'paper', 3: 'scissors'}
computer_choice = random.choice(list(computer_choices.values()))

def user_choice(choice):
    if choice == computer_choice:
        time.sleep(1)
        print('The computer chose ' + computer_choice)
        print('It looks to be a tie')
    elif choice == rock and computer_choice == scissors:
        time.sleep(1)
        print('The computer chose ' + computer_choice)
        print('Congratulations! You won!')
    elif choice == paper and computer_choice == scissors:
        time.sleep(1)
        print('The computer chose ' + computer_choice)
        print('It looks like you lost :(')
    elif choice == rock and computer_choice == paper:
        time.sleep(1)
        print('The computer chose ' + computer_choice)
        print('It looks like you lost :(')
    elif choice == paper and computer_choice == rock:
        time.sleep(1)
        print('The computer chose ' + computer_choice)
        print('Congratulations! You won!')
    else:
        time.sleep(1)
        print('Error')




user_choice(choice)
