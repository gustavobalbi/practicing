import random, os, time, requests, winsound, keyboard

messages = {
    'ptbr': {
        'letters': 'letras',
        'thanks': 'Obrigado por jogar!',
        'again': 'Jogar de novo?\n0 - SIM\n1 - NÃO',
        'esc': 50*'-' + '\nPressione ESC para retornar',
        'info': 'Me chamo Gustavo Balbi e sou estudante de Sistemas de Informação pela Universade Federal do Pará.\n' + 50*'-' + '\n>Descubra a palavra secreta inserindo letras ou a palavra exata.\n>Você perde uma vida por palpites errados ou perde o jogo por tentar uma palavra errada.\n>As palavras estão relacionadas ao tema TECNOLOGIA.',
        'home_screen': '0 - JOGAR\n1 - INFO',
        'welcome': 'Adivinhe a palavra secreta! Você tem {lives} vidas.',
        'last_chance': 'Esta é sua última chance!',
        'misses': 'Erros:',
        'game_over': 'Fim de jogo! A palavra era "{word}".',
        'you_win': 'Você venceu! A palavra é "{word}".',
        'input_error': 'Digite uma letra ou uma palavra.',
        'already_tried': 'Você já tentou essa letra!',
        'already_guessed': 'Você já adivinhou esta letra!'
    },
    'en': {
        'letters': 'letters',
        'thanks': 'Thanks for playing!',
        'again': 'Play again?\n0 - YES\n1 - NO',
        'esc': 50*'-' + '\nPress ESC to return',
        'info': "My name is Gustavo Balbi, and I am a student of Information Systems at the Federal University of Pará.\n" + 50*'-' + "\n>Discover the secret word by entering letters or guessing the exact word.\n>You lose a life for incorrect guesses or lose the game by guessing the wrong word.\n>The words are related to the theme of TECHNOLOGY.",
        'home_screen': '0 - PLAY\n1 - INFO',
        'welcome': 'Guess the secret word! You have {lives} lives.',
        'last_chance': 'This is your last chance!',
        'misses': 'Misses:',
        'game_over': 'Game over! The word was "{word}".',
        'you_win': 'You win! The word is "{word}".',
        'input_error': 'Input a letter or a word.',
        'already_tried': 'Already tried this one!',
        'already_guessed': 'You already guessed this letter!'
    }
}

def press():
    event = keyboard.read_event(suppress=True)
    if event.event_type == keyboard.KEY_DOWN:
        select = int(event.name)
    return select

def clear_screen(seconds):
    time.sleep(seconds)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def words_list(language):
    if language == 'en':
        url = 'https://raw.githubusercontent.com/gustavobalbi/practicing/refs/heads/main/personal-projects/hangman-game/hangman-wordsEN.txt'
    else:
        url = 'https://raw.githubusercontent.com/gustavobalbi/practicing/refs/heads/main/personal-projects/hangman-game/hangman-wordsPTBR.txt'
    response = requests.get(url)
    if response.status_code == 200:
        words = [line.strip() for line in response.text.splitlines()]
        return words
    else:
        print("Failed to access the file.")

def game_info(words):
    chosen_word = words[random.randint(0, len(words) - 1)]
    blank = ['_' if letter.isalpha() else ' ' for letter in chosen_word]
    letters = len(chosen_word.replace(' ',''))
    return chosen_word, blank, letters

def language_select():
    stts = True
    print('ENGLISH - 0')
    print('PORTUGUÊS - 1')
    while stts:
        event = keyboard.read_event(suppress=True)
        button_sound()
        clear_screen(0)
        if event.event_type == keyboard.KEY_DOWN:
            select = event.name
            if select == '0':
                return 'en'
            if select == '1':
                return 'ptbr'

def info(language):
    stts = True
    print(messages[language]['info'])
    print(messages[language]['esc'])
    while stts:
        event = keyboard.read_event(suppress=True)
        button_sound()
        if event.event_type == keyboard.KEY_DOWN:
            select = event.name
            if select == 'esc':
                stts = False

def home_screen(language):
    stts = True
    launch_sound()

    while stts:
        print(messages[language]['home_screen'])
        event = keyboard.read_event(suppress=True)
        button_sound()
        if event.event_type == keyboard.KEY_DOWN:
            select = event.name
            clear_screen(0)
            if select == '0':
                stts = False
            if select == '1':
                info(language)
        clear_screen(0)
                
                    
def game_screen(chosen_word, blank, letters, language, words):
    lives = 5
    errors = []
    while lives > 0 and '_' in blank:
        if lives > 1:
            print(messages[language]['welcome'].format(lives=lives))
        else:
            print(messages[language]['last_chance'])
            
        if errors:
            print(f"{messages[language]['misses']}", errors)

        for underscore in blank:
            print(underscore, end=' ')
        print(' ', letters, messages[language]['letters'])
    
        lives, blank = input_check(chosen_word, blank, errors, lives, language, words)

    if lives == 0:
        gameover_sound()
        print(messages[language]['game_over'].format(word=chosen_word))
    else:
        print(messages[language]['you_win'].format(word=chosen_word)) 
        youwin_sound()
    
    clear_screen(2)

def input_check(chosen_word, blank, errors, lives, language, words):
        guess = input("-> ").lower()
        clear_screen(0)
        if guess == chosen_word:
            blank = []
            return lives, blank
        if guess in words and guess != chosen_word:
                lives = 0
                return lives, blank
        if not guess.isalpha() or len(guess) != 1 or guess == '':
            print(messages[language]['input_error'])
            clear_screen(1.5)
        else:
            if guess not in chosen_word:
                if guess not in errors:
                    miss_sound()
                    lives -= 1
                    errors.append(guess)
                else:
                    print(messages[language]['already_tried'])
                    clear_screen(1.5)
            elif guess in blank:
                print(messages[language]['already_guessed'])
                clear_screen(1.5)
            else:
                for i in range(len(chosen_word)):
                    if chosen_word[i] == guess:   
                        success_sound()
                        blank[i] = chosen_word[i]
        return lives, blank

def play_again(language):
    stts = True
    while stts:
        print(messages[language]['again'])
        event = keyboard.read_event(suppress=True)
        button_sound()
        if event.event_type == keyboard.KEY_DOWN:
            select = event.name
            clear_screen(0)
            if select == '0':
                return '0'
            if select == '1':
                return '1'
        clear_screen(0)

###############################################
def launch_sound():
    winsound.Beep(800, 100)
    winsound.Beep(1000, 100)
    winsound.Beep(1200, 100)
    winsound.Beep(600, 100)
    winsound.Beep(800, 100)
    winsound.Beep(1500, 50)
    winsound.Beep(1200, 50)

def gameover_sound():
    winsound.Beep(600, 300)
    winsound.Beep(400, 300)
    winsound.Beep(200, 500)  

def youwin_sound():
    winsound.Beep(660, 100)
    winsound.Beep(660, 100)
    winsound.Beep(660, 100)
    winsound.Beep(510, 100)
    winsound.Beep(660, 100)
    winsound.Beep(770, 100)
    winsound.Beep(380, 100)

def miss_sound():
    winsound.Beep(400, 300)
    winsound.Beep(300, 200)

def success_sound():
    winsound.Beep(800, 100)
    winsound.Beep(1000, 100)
    winsound.Beep(1200, 150)

def button_sound():
    winsound.Beep(500, 75)

##############################################
def main_code():
    stts = True
    language = language_select()
    home_screen(language)
    while stts:
        words = words_list(language)
        word, blank, letters = game_info(words)
        game_screen(word, blank, letters, language, words)
        condition = play_again(language)
        if condition == '1':
            stts = False
    print(messages[language]['thanks'])

main_code()
