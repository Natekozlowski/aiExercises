# Your project for today is to build a basic version of the classic Hangman game in Python.
# The program will choose a single secret word (hardcoded for now), and let the user guess one 
# letter at a time. After each guess, it will show the user their progress by revealing correctly 
# guessed letters and keeping underscores (_) for letters they haven’t guessed yet.


# Hangman Game

# Step 1: Set up the secret word and initialize variables
secret_word = "racecar"
guessed_letters = []
tries = 6

print("Welcome to Hangman!")
print("You have", tries, "tries to guess the word.")

# Step 2: Main game loop
while True:
    # Build the display word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    # Show progress
    print("Word:", display_word)
    
    # Check if player has guessed the word
    if display_word == secret_word:
        print("Congratulations! You guessed the word:", secret_word)
        break

    # Check if no tries left
    if tries == 0:
        print("Sorry, you ran out of tries. The word was:", secret_word)
        break

    # Ask for user input
    guess = input("Guess a letter: ").lower()

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add guess to guessed letters
    guessed_letters.append(guess)

    # Check if guess is in secret word
    if guess in secret_word:
        print("Good guess!")
    else:
        print("Wrong guess!")
        tries -= 1
        print("Tries left:", tries)
       


