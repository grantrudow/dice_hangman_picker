import random
repeat = True 
while repeat:
    print('You rolled a', random.randint(1,6))
    print('Roll Again?')
    repeat = ('y' or 'yes') in input().lower()

