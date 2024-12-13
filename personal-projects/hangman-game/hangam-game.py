#This code is about a hangman game. Previously developed to work in portuguese but then transcribed to english.

import random, os, time, requests 

def clear(tempo):
    time.sleep(tempo)
    if os.name == 'nt': 
        os.system('cls')
    else: 
        os.system('clear')


url = 'https://raw.githubusercontent.com/gustavobalbi/practicing/refs/heads/main/personal-projects/hangman-game/hangman-words.txt'
response = requests.get(url)
if response.status_code == 200:
    words = [line.strip() for line in response.text.splitlines()]
else:
    print("Failed to acess the file.")

hang = words[random.randint(0, len(words) - 1)]
blank = ["_" for i in hang]
errors = []
letters = len(hang)
lives = 10
stts = True

while stts:
    print(f"Guess the word! You have {lives} live(s).")
    if errors:
        print("Misses: ", errors)

    for i in range(len(hang)):
        print(blank[i], end=" ")
    print(f"{letters} letters")

    guess = input("-> ").lower()
    if guess.isalpha():    
        clear(0) 
        
        if guess not in hang:
            if guess not in errors:
                lives = lives - 1
                errors.append(guess)
            else: 
                print("Already tried this one!")
                clear(1.5)
        else:
            if guess in blank:
                print(f"Already tried this one! '{guess.upper()}'")
                clear(1.5)
            else:
                for i in range(len(hang)):
                    if hang[i] == guess:
                        blank[i] = hang[i]

        if lives == 0:
            print(f"Game over!\nThe word is '{hang}'")
            stts = False

        if "_" not in blank or guess == hang:
            print(f"You win!\nThe word is '{hang}'")
            stts = False
    else:
        clear(0)
        print("Input a letter or a word.")
        clear(1.5)