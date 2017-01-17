#This is a guess the number game.
import random

def guessing():
    guesses_taken = 0

    player_name = raw_input("Welcome to Guess the Number! What is your name? ")
    number = random.randint(1,100)
    print player_name,", I am thinking of a number between 1 and 100."

    while guesses_taken < 7:
        guess = int(raw_input("Take a guess: "))
        guesses_taken += 1
        if guess < number:
            print "Your guess is too low. "
        elif guess > number:
            print "Your guess is too high. "
        else:
            break

    if guess == number:
        guesses_taken = str(guesses_taken)
        print "Great job %s ! You guessed the number in %s guesses. " % (player_name,guesses_taken)
        start()

    if guess != number:
        number = str(number)
        print "I won! The number I was thinking of was %s. " % (number)
        start()


def start():
    game_state = raw_input("Would you like to play Guess the Number? Y/N ")
    if game_state.lower() == "y":
        guessing()
    else:
        print "There are lots of other games to play. Goodbye. "

start()
