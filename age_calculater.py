#----------------------------
# age calculater
#----------------------------


# data collection

age = int(input("Please write your age: "))

# note

print("=" * 90)
print(" you can write the time unit or the first letter of the time unit. ".capitalize().center(90,"="))
print("=" * 90)

# Time unit

TimeUnitInput = input("Choose your time unit, Months, Weeks, days:").lower().strip()

months = age*12
weeks = months*4
days = age*365

# Time unit control
if TimeUnitInput == "months" or TimeUnitInput == "m" :

    print("you choosed time unit months.")
    print(f"you lived for {months:,} Months.")

elif TimeUnitInput == "weeks" or TimeUnitInput == "w" :

    print("you choosed time unit weeks.")
    print(f"you lived for {weeks:,} weeks.")

elif TimeUnitInput == "days" or TimeUnitInput == "d":

    print("you choosed time unit days.")
    print(f"you lived for {days:,} Days.")
