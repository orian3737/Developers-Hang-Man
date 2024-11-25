from random import choice
import sys
words = [
    "python", "hangman", "programming", "developer", "variable", 
    "function", "loop", "iteration", "debugging", "syntax", 
    "exception", "keyword", "compile", "execute", "terminal", 
    "console", "algorithm", "data", "binary", "decimal", 
    "integer", "boolean", "string", "dictionary", "list", 
    "tuple", "class", "object", "inheritance", "polymorphism", 
    "encapsulation", "abstraction", "framework", "library", "package", 
    "virtual", "server", "client", "database", "frontend", 
    "backend", "fullstack", "api", "request", "response"
]


def run_game():
   word: str = choice(words)
   
   username: str = input('What is your name? >> ')
   print(f'Welcome to HangMan, {username}')
   
   #setup
   guessed: str = ''
   tries: int = 6
   
   
   while tries > 0:
        blanks: int = 0

        print('\nWord: ', end='')
        for char in word:
            if char in guessed:
                print(char, end=' ')
            else:
                print('_', end=' ')
                blanks += 1

        print("")  # Adds a blank line for readability

        
        if blanks == 0:
            print('Congratulations! You guessed the word!')
            play_again()
            break
        
        guess: str = input('Enter a letter: ')
        
        if guess in guessed:
            print(f'You already used: "{guess}". Please try another letter!')
            continue
        guessed += guess
        
        if guess not in word:
            tries -= 1
            print(f'Sorry that was wrong... ({tries} tries remaining)')
            
            if tries == 0:
                print('No more tries remaining... You lose.')
                play_again()       
        
def play_again() -> bool:
    play_through: bool = input('Do you want to play again?: y/n. ')
    if play_through == "y":
        run_game()
    else:
        print('Goodbye!')
        sys.exit()

if __name__ == "__main__":
    run_game()