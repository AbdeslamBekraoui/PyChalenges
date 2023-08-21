# -------------------------------------------------------------------------------------------------------------------
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
# -------------------------------------------------------------------------------------------------------------------

import random
random_number = random.randint(1, 9)
gamerunning = True
def Guess_Result(guess, item) :
    global gamerunning
    if guess == item :
        print(f"Great guess! That's exactly right, it took only {numbers_guessed} trys.")
        gamerunning = False
    elif guess > item :
        print("Close! maybe a little bit lower.")
    elif guess < item :
        print("Close! Try a little higher.")

numbers_guessed = 0

while gamerunning :
    
    user_guess_int = int(input("Guess the number from 1 to 9 :".strip()))
    if user_guess_int not in range(1, 10):
        print("Please choose a number from 1 to 9!")
    else:
        numbers_guessed += 1  # Increment the counter
        Guess_Result(user_guess_int, random_number)