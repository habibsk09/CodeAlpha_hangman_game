import random

# List of words for the game
words = ["python", "computer", "game", "code", "program", "simple", "easy", "fun"]

# Select a random word
word = random.choice(words).upper()
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman!")
print("Try to guess the word one letter at a time.")
print(f"You have {max_wrong_guesses} wrong guesses allowed.\n")

# Main game loop
while wrong_guesses < max_wrong_guesses:
    # Display current state of the word
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print(f"Word: {display_word}")
    print(f"Wrong guesses: {wrong_guesses}/{max_wrong_guesses}")
    
    if guessed_letters:
        print(f"Guessed letters: {', '.join(guessed_letters)}")
    
    # Check if word is complete
    if all(letter in guessed_letters for letter in word):
        print(f"\nCongratulations! You won! The word was: {word}")
        break
    
    # Get player's guess
    guess = input("\nEnter a letter: ").upper().strip()
    
    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    
    # Add guess to list
    guessed_letters.append(guess)
    
    # Check if guess is correct
    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        wrong_guesses += 1
        print(f"Sorry, '{guess}' is not in the word.")

# Check if player lost
if wrong_guesses >= max_wrong_guesses:
    print(f"\nGame Over! The word was: {word}")

print("Thanks for playing!")