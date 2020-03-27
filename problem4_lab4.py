import random
guessesTaken = 0
print('Hello! What is your name?')
myName = input()
number = random.randint(1, 100)
print('Well, ' + myName + ', I am thinking of a number between 1 and 100.')
while guessesTaken < 10:
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess > 100:
        print("that is not allowed and don't count this as a try")
        guessesTaken = guessesTaken - 1

    elif guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    elif guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)