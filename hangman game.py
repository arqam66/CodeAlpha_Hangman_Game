import random

def get_word():
  """
  Selects a random word from a list of words.
  """
  words = ["python", "programming", "computer", "science", "machine", "learning"]
  
  return random.choice(words)

def display_hangman(wrong_guesses):
  """
  Displays the hangman figure based on the number of incorrect guesses.
  """
  stages = [
      """
          --------
          |      |
          |      O
          |     /|\\
          |     / \\
          -
      """,
      """
          --------
          |      |
          |      O
          |     /|\\
          |      \\
          -
      """,
      """
          --------
          |      |
          |      O
          |     /|
          |      \\
          -
      """,
      """
          --------
          |      |
          |      O
          |      |
          |      \\
          -
      """,
      """
          --------
          |      |
          |      O
          |      |
          |      
          -
      """,
      """
          --------
          |      |
          |      O
          |       
          |      
          -
      """,
      """
          --------
          |      |
          |      
          |       
          |      
          -
      """
  ]
  print(stages[wrong_guesses])

def play_game():
  """
  Main function that runs the Hangman game.
  """
  word = get_word().upper()
  word_letters = set(word) # Letters in the word as a set
  alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  wrong_guesses = 0
  guessed_letters = set() # Letters guessed by the player

  print("Welcome to Hangman!")

  # Define stages within the function
  stages = [
      """
          --------
          |      |
          |      O
          |     /|\\
          |     / \\
          -
      """,
      """
          --------
          |      |
          |      O
          |     /|\\
          |      \\
          -
      """,
      """
          --------
          |      |
          |      O
          |     /|
          |      \\
          -
      """,
      """
          --------
          |      |
          |      O
          |      |
          |      \\
          -
      """,
      """
          --------
          |      |
          |      O
          |      |
          |      
          -
      """,
      """
          --------
          |      |
          |      O
          |       
          |      
          -
      """,
      """
          --------
          |      |
          |      
          |       
          |      
          -
      """
  ]

  while wrong_guesses < len(stages) - 1:
    # Display current state
    print("You have", len(stages) - wrong_guesses, "wrong guesses left.")
    display_hangman(wrong_guesses)
    print("Guessed letters:", ' '.join(guessed_letters))

    # Create the word display with blanks and guessed letters
    word_display = [letter if letter in guessed_letters else "_" for letter in word]
    print("Word: ", ' '.join(word_display))

    # Get player guess
    while True:
      guess = input("Guess a letter: ").upper()
      if len(guess) != 1 or guess not in alphabet - guessed_letters:
        print("Invalid guess. Please enter a single letter you haven't guessed yet.")
      else:
        break

    # Update game state
    if guess in word_letters:
      guessed_letters.add(guess)
    else:
      wrong_guesses += 1

    # Check if game is won or lost
    if all(letter in guessed_letters for letter in word_letters):
      print("You won! The word was", word)
      break
  else:
    display_hangman(wrong_guesses)
    print("You lost! The word was", word)

  # Ask to play again
  while True:
    play_again = input("Play again? (y/n): ").lower()
    if play_again in ('y', 'n'):
      break
    else:
      print("Invalid input. Please enter 'y' or 'n'.")
  if play_again == 'y':
    play_game()

# Start the game
play_game()
