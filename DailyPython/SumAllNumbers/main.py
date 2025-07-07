### Your task for today is to build a Python program that calculates the sum of all numbers in a user-defined range. 
# Instead of hardcoding the start and end values, your program will prompt the user to enter them.
# You’ll then write a function that loops through each number from the start to the end (inclusive) and calculates the total sum. 
# This is a super practical beginner project — you’ll see similar logic in billing systems(summing prices from one invoice to another)
# Generating statistics over days or months, or even calculating cumulative points in a game

def rangeSum(start, end):
    numbers = []
    x = range(start,end+1)
    for n in x:
        numbers.append(n)
    print(sum(numbers))

rangeSum(int(input('Enter the start of the range: ')), int(input('Enter the end of the range: ')))
