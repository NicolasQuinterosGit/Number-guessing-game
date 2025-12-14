import random

print("Welcome to the Number Guessing Game!")
print("Select in between which numbers you want to guess.")

## Bound settings
lower_bound = 0
print("Define the lower bound:")
try:
    lower_bound = int(input())
except ValueError:
    print("Invalid input. Using default lower bound of 0.")
                  
upper_bound = 100
print("Define the upper bound:")
try:
    upper_bound = int(input())
except ValueError:
    print("Invalid input. Using default upper bound of 100.")

if lower_bound >= upper_bound:
    print("Invalid bounds. The lower bound must be less than the upper bound.")
    exit()

#-----------------------------------------------------------------------------------
# Generate a random number within the specified bounds
random_number = random.randint(lower_bound, upper_bound)

# Initialize variables
attempts = 0
while True:
    print(f"Guess a number between {lower_bound} and {upper_bound}:")
    user_guess = input()
    attempts += 1
    try:
        user_guess = int(user_guess)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    if user_guess == random_number:
        print(f"Congratulations! You've guessed the correct number {random_number} in {attempts} attempts.")
        break
    else:
        if user_guess < lower_bound or user_guess > upper_bound:
            print(f"Your guess is out of bounds. Please guess a number between {lower_bound} and {upper_bound}.")
            continue   
        else:
            if user_guess < random_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
#-----------------------------------------------------------------------------------