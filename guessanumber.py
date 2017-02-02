#This is a guess the number game.
import random

def guessing():
    """ This function chooses a random number between 1 and 100 and takes in the player's 
        guesses as input. If the player guesses right within 7 tries, the player wins. No
        matter whether the player wins or loses, he/she is asked if they want to play again
    """
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
        print "Great job %s! You guessed the number, %d, in %s guesses. " % (player_name, number, guesses_taken)
        start()

    if guess != number:
        print "I won! The number I was thinking of was  %d. " % (number)
        start()


def start():
    """ This function starts the game by asking the player if they'd like to win or not
    """
    game_state = raw_input("Would you like to play Guess the Number? Y/N ")
    if game_state.lower() == "y":
        guessing()
    else:
        print "There are lots of other games to play. Goodbye. "

if __name__ == "__main__":
    start()
