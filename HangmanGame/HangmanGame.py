import random # Imports the random module
from hangman_words import word_list # Imports the word_list from hangman_words.py
from hangman_art import logo,stages # Imports the logo and stages from hangman_art.py
print(logo) # Prints the hangman logo

chosen_word = random.choice(word_list) # Chooses a random word from the word_list
word_length = len(chosen_word) # Gets the length of the chosen word

end_of_game = False # Sets the end_of_game variable to False
lives = 6 # Sets the lives variable to 6

display = [] # Creates an empty list called display
for _ in range(word_length): # Loops through the chosen word
    display += "_" # Adds an underscore to the display list

while not end_of_game: # Loops while end_of_game is False
    guess = input("Guess a letter: ").lower() # Gets the user's guess and converts it to lowercase

    if guess in display: # Checks if the guess is already in the display list
        print(f"You've already guessed {guess}") # Prints a message  
      
    for position in range(word_length): # Loops through the chosen word
        letter = chosen_word[position] # Gets the letter at the current position
        if letter == guess: # Checks if the letter is the same as the guess
            display[position] = letter # Replaces the underscore with the letter

    if guess not in chosen_word: # Checks if the guess is not in the chosen word
        print(f"You guessed {guess}, that's not in the word. You lose a life.") # Prints a message

        lives -= 1 # Reduces the lives by 1
        if lives == 0: # Checks if the lives are 0
            end_of_game = True # Sets end_of_game to True
            print("You lose.") # Prints a message
          
    print(f"{' '.join(display)}") # Prints the display list as a string with spaces in between each letter

    if "_" not in display: # Checks if there are no more underscores in the display list
        end_of_game = True # Sets end_of_game to True
        print("You win.") # Prints a message

    print(stages[lives]) # Prints the stages list at the current lives index