import random

print('----------------------------------')
print('      GUESS THE NUMBER APP')
print('----------------------------------')
print()


ran_number = random.randint(0, 100)
guess = -1

name = input('What is your name? ')

while guess != ran_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess == ran_number:
        print('Great job {}, that is Correct!'.format(name))
    elif guess < ran_number:
        print('Sorry {}, your guess of {} is too low.'.format(name, guess))
    else:
        print('Sorry {}, your guess of {} is too high.'.format(name, guess))

print('Done')

