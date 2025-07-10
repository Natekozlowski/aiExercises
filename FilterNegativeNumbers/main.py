# Your task for today is to write a Python program that takes a list of numbers and removes all the negative ones.
# The goal is to keep only numbers that are greater than or equal to zero.
# useful in real world situations:
# Cleaning data for analysis
# Preparing inputs for machine learning
# Validating form entries or user input
###
# You’ll start with a predefined list of integers — some positive, some negative, and maybe even zero. 
# Store that list in a variable like so:

numbers = [3, -1, 7, -5, 0, 8, -2]

# Your program should create a new list that includes only the non-negative numbers and then print it.

notnegativelist = [number for number in numbers if number >= 0]

print(notnegativelist)