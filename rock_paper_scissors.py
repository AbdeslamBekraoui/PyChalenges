# ----------------------------------------
# --------- Rock Paper Scissors ----------
# ----------------------------------------

"""
Welcome to the Classic Rock Paper Scissors.
This code showcases my simple approach for this very famous game that we've all played.
"""
import random
game_choices = ["Rock", "Paper", "Scissors"]
# player input

def game_player(player_input) :
    """
    take the player choice if it is one of the game_choices
    else it asks the player again plus the function picks a random option
    from the variable game choices and add to the variable ai_bot
    """
    while player_input not in game_choices : # makes sure the player chooses one of the options
        print("Please choose one of the options!")
        player_input = input("Your choice is : ").strip().capitalize()
    global ai_bot
    ai_bot = random.choice(game_choices) # random choice
    print(f"AI choice is : {ai_bot} ! ")
# check for win or lose

def check_result(player_input) :
    """
    takes the player choice and compare it to the ai choice 
    and then prints a message depending in the result of the comparisson
    """
    if player_input == ai_bot :
        print ("It's a tie!")
    elif player_input == "Rock" :
        if ai_bot == "Paper" :
            print ("I Won maybe next time!")
        else :
            print ("Congrats! you won")
    elif player_input == "Paper" :
        if ai_bot == "Scissors" :
            print ("I Won maybe next time!")
        else :
            print ("Congrats! you won")
    elif player_input == "Scissors" :
        if ai_bot == "Rock" :
            print ("I Won maybe next time!")
        else :
            print ("Congrats! you won")
# put the whole thing together

while True:
    player_choice = input("Your choice is :").strip().capitalize()
    game_player(player_choice)
    check_result(player_choice)
    repeat = input("Do you want to play again Y/N ?").strip().capitalize()
    while repeat not in ('Y', 'N') :
        repeat = input("Invalid input. Please enter Y or N:").strip().capitalize()
    if repeat == "Y" :
        continue
    if repeat == "N" :
        break
