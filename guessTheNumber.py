import random
secretNum = random.randint(1,20)
print('I am thinking of a number between 1 and 20')

for guessTaken in range(1,7):
    guess = int(input('Take a guess : '))
    if guess < secretNum:
        print('Your guess is too low.')
    elif guess > secretNum:
        print('Your guess is too high.')
    else:
        break
if guess == secretNum:
    print('Good Job! You guessed my number in '+str(guessTaken)+' guesses!')
else:
    print('Nope. The number i was thinking was '+str(secretNum))