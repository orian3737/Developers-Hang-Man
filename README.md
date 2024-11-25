# Developer's Hangman Game

Welcome to **Developer's Hangman**, a command-line game tailored specifically for developers! This game is designed to challenge your programming knowledge with words drawn exclusively from the world of coding, software development, and computer science.

## Features

- **Developer-Themed Word List**: Guess words related to programming, such as `function`, `variable`, `syntax`, and more.
- **Random Word Selection**: Each game selects a random programming-related term from a curated list of 45 words.
- **Interactive Gameplay**:
  - Tracks guessed letters and prevents duplicate guesses.
  - Displays partially revealed words after every guess.
  - Provides feedback on remaining attempts.
- **Replay Option**: Decide whether to play another round or exit after each game.
- **Simple and Clean Interface**: Easy-to-follow prompts and clear instructions.

## How to Play

1. **Start the Game**:
   Run the program in your terminal:

   ```bash
   python hangman.py
   ```

## Game Flow:

Enter your name when prompted.
A random programming-related word will be selected for you to guess.
Guess the word by entering one letter at a time.
You have 6 attempts to guess the word correctly before the game ends.
If you guess all the letters correctly, you win!
After the Game:

If you win or lose, you’ll be prompted to play again or exit.
Example Gameplay
plaintext
Copy code
What is your name? >> Alice
Welcome to Developer's Hangman, Alice

Word: _ _ _ _ _ _ _ 

Enter a letter: f
Sorry that was wrong... (5 tries remaining)

Word: _ _ _ _ _ _ _ 

Enter a letter: n
Good guess!

Word: _ _ n _ _ _ _ 

Enter a letter: c
Good guess!

Word: _ _ n c _ _ _ 

Enter a letter: t
Good guess!

Word: _ _ n c t _ _ 

Enter a letter: i
Congratulations! You guessed the word!
Do you want to play again?: y/n. y
Requirements
Python 3.6 or higher.
File Structure
plaintext
Copy code
.
├── hangman.py       # Main Python program file
├── README.md        # This documentation file
Code Overview
Main Functions
run_game()

Core logic of the game.
Handles word selection, guessing mechanics, and tracking the player's progress.
play_again()

Prompts the player to decide whether to play another game or exit.
Restarts the game if the player chooses to continue.
Programming-Themed Word List

Uses Python's random.choice() to select a word from a curated list of programming-related terms, including:
python, hangman, debugging, variable, polymorphism, framework, and more.
How to Customize
Add More Programming Words:
Update the words list in hangman.py to include additional developer-related terms.

Adjust Difficulty:
Modify the tries variable in run_game() to increase or decrease the number of attempts available.

Why This Game?
Developer's Hangman isn’t just a game—it’s a fun way to test and expand your programming vocabulary. Whether you’re a beginner or a seasoned developer, this game is sure to entertain while keeping you sharp.

Future Enhancements
Include hints for tougher words, such as "This is a type of loop" or "This is used to handle errors."
Add a leaderboard to track scores across games.
Expand the word list to include terms from more specialized fields like DevOps, AI, or cybersecurity.
License
This project is licensed under the MIT License. Feel free to use, modify, and share it with others.

Enjoy playing Developer's Hangman, and may your programming vocabulary lead you to victory!