#This code is about a hangman game. Previously developed to work in portuguese but then transcribed to english. Updates soon.

import random, os, time, requests

def clear_screen(seconds):
    time.sleep(seconds)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def words_list():
    url = 'https://raw.githubusercontent.com/gustavobalbi/practicing/refs/heads/main/personal-projects/hangman-game/hangman-words.txt'
    response = requests.get(url)
    if response.status_code == 200:
        words = [line.strip() for line in response.text.splitlines()]
        return words
    else:
        print("Failed to acess the file.")

def game_info(words):
    chosen_word = words[random.randint(0, len(words) - 1)]
    blank = ['_' for letter in chosen_word]
    letters = len(chosen_word)
    return chosen_word, blank, letters

def game_screen(chosen_word, blank, letters):
    lives = 5
    errors = []
    while lives > 0 and '_' in blank:
        if lives > 1:
            print(f"Guess the secret word! You have {lives} lives.")
        else:
            print("This you last chance!")
            
        if errors:
            print(f"Misses:", errors)

        for underscore in blank:
            print(underscore, end=' ')
        print(' ', letters, "letters")
    
        lives, blank = input_check(chosen_word, blank, errors, lives)

    if lives == 0:
        print(f"Game over!\nThe word is '{chosen_word}'.")
    else:
        print(f"You win! The word is '{chosen_word}'.")    

def input_check(chosen_word, blank, errors, lives):
        guess = input("-> ").lower()
        clear_screen(0)
        if guess == chosen_word:
            blank = []
            return lives, blank
        if not guess.isalpha() or len(guess) != 1:
            print('Input a letter or a word.')
            clear_screen(1.5)
        else:
            if guess not in chosen_word:
                if guess not in errors:
                    lives -= 1
                    errors.append(guess)
                else:
                    print('Already tried this one!')
                    clear_screen(1.5)
            elif guess in blank:
                print("You already guessed this letter!")
                clear_screen(1.5)
            else:
                for i in range(len(chosen_word)):
                    if chosen_word[i] == guess:
                        blank[i] = chosen_word [i]
        return lives, blank


words = words_list()
word, blank, letters = game_info(words)
game_screen(word, blank, letters)
