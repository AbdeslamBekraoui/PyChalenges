# -------------------------------------------------------------------
# ----------------------- Cows and Bulls ----------------------------
# -------------------------------------------------------------------

import random

# Generate a 4 digit number 

random_n = str(random.randint(1000, 9999))
random_num = list(random_n)
# User input

print("#" * 70)
print(" Welcome to the Cows and Bulls! ".center(70, "#"))
print(" If your digit is in the correct place it's a 'cow'! ".center(70, "#"))
print(" If your digit is in not in the correct place it's a 'bull'! ".center(70, "#"))
print("#" * 70)

game_running = True

# Result

def cows_and_bulls(user_num) :
    Cows = 0
    index = 0
    cow_list = []
    for num in user_num :

        if user_num[index] == random_num[index] :
            Cows += 1
            cow_list.append(num)
        else :
            pass
        index += 1
    Bulls_ = []
    set_user_num = set(user_num)
    set_random_num = set(random_num)
    set_cow_list = set(cow_list)

    set_user_num.intersection_update(set_random_num)
    set_user_num.difference_update(set_cow_list)
    n = list(set_user_num)
    Bulls_.extend(n)
    Bulls = len(Bulls_)
    if Cows == 4 :
        return ("Congrats you got it!")
    else :

        return (f"{Cows} cows," if Cows > 1 or Cows == 0 else f"{Cows} cow,") + (f" {Bulls} bulls" if Bulls > 1 or Bulls == 0 else f" {Bulls} bull")

# repeat

while game_running :

    User_input = list(input(">>> Enter a four digit number: ").strip())
    result = cows_and_bulls(User_input)
    print(result)
    if result == "Congrats you got it!" :
        game_running = False