# Today’s project is all about cleaning up data — a crucial step in
# any real-world application. Your task is to build a Python program
# that removes duplicate values from a list provided by the user.
# But here's the twist: instead of using a hardcoded list, your program 
# should prompt the user to input a list of values separated by commas 
# (for example: apple, banana, apple, orange).
# The program should then:
# Convert the input into a list
# Remove any duplicate entries
# Print the cleaned list
# And show how many duplicates were removed

words = input("Enter a list of words separated by commas:")

words = words.split(', ')

# create an empty list to hold items that are not a duplicate
# the naming scheme here might be confusing as it will be called duplicates
# however we will check for duplicates using the numbers that are not duplicates
duplicates = []
# pop() would work here if duplicate is found and we were restricted to the original list
# however we can append the word to our empty list if it is not found
for item in words:
    if item not in duplicates:
        duplicates.append(item)

print(duplicates)
print("Duplicates removed:", len(words)-len(duplicates))