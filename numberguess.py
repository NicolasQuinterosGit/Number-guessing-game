import random

print("Welcome to the Number Guessing Game!")
print("Select in between which numbers you want to guess.")

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