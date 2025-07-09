# Your project today is to write a Python program that counts how many numbers from 1 to 100 are divisible 
# by both 3 and 5, and also prints out exactly which numbers these are.
# This is a classic small program that teaches you how to use:
# Loops (to go through each number in a range)
# The modulus operator % (to check for divisibility)
# Lists (to store matching numbers)
# And len() (to count the total)
# In the real world, similar logic is used all the time to filter datasets 
# like finding every product with a price that meets multiple discount rules 
# or filtering out transactions that match multiple conditions.

numbers = list(range(1,101))
divisibleNumbers = []

for i in numbers:
    if i % 3 == 0 and i % 5 == 0:
        divisibleNumbers.append(i)

print(divisibleNumbers)
print('total count:',len(divisibleNumbers))