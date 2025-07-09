# Your task today is to build a beginner-friendly Python program that finds the largest number in a list
# by writing your own logic instead of using Python’s built-in max() function.
# But there’s a twist: instead of using a hardcoded list, your program should ask the user to input a list
# of numbers separated by commas.
# Example Output:
# Enter numbers separated by commas: 3, 45, 7, 89, 21
# The largest number is: 89

numbers = input("Enter a list of numbers separated by commas:")

numbers = map(int,numbers.split(','))

print(max(numbers))
    