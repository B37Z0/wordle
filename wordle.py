import random

'''
Wordle but slightly lacking. This program does not account for guessing repeated letters in the correct word.
'''

def get_word(valid_words):
    '''
    Pick the word to guess from a list.
    '''
    i = random.randint(0, len(valid_words)-1)
    return valid_words[i]

def get_guess(valid_words):
    '''
    Get a valid guess.
    '''
    guess = input("Input a guess: ")
    guess = guess.lower()

    while not guess in valid_words:
        print('That is not a valid word.')
        guess = input("Input a guess: ")
        guess = guess.lower()

    return guess

def check_letter(guess, word, index):
    '''
    Checks correctness of a single letter.
    - returns 1 if correct, 0 otherwise
    - also returns True if the letter is inside the word, False otherwise  
    '''
    if guess[index] == word[index]:
        return 1, True
    elif guess[index] in word:
        return 0, True
    else:
        return 0, False
    
def evaluate_guess(guess, word):
    '''
    Returns # correct letters, incorrect letters, and list for the background.
    '''
    green_bg = "\x1b[42m"
    yellow_bg = "\x1b[43m"
    grey_bg = "\x1b[47m"

    score = 0
    incorrect_letters = ""
    bg = []

    for i in range(len(guess)):
        correct, in_word = check_letter(guess, word, i)
        if correct == 1:
            bg.append(green_bg)
        elif in_word:
            bg.append(yellow_bg)
        else:
            bg.append(grey_bg)

            if guess[i] not in incorrect_letters:
                incorrect_letters += guess[i]
        
        score += correct
    
    return score, incorrect_letters, bg

def print_guess(guess, incorrect_letters, bg):
    '''
    Display guess in Wordle style.
    '''
    white = "\x1b[0m"
    grey = "\x1b[47m"

    for i in range(len(guess)):
        print(bg[i] + guess[i], end=' ')

    print(white, end='\t')

    print("Incorrect: ", end=' ')
    for letter in sorted(incorrect_letters):
        print(grey+letter, end=' ')

    print(white)


valid_words = []
with open("C:\\Users\\benjz\\Downloads\\wordle\\valid-wordle-words.txt", 'r') as word_list:
    for line in word_list:
        valid_words.append(line.strip())

word = get_word(valid_words)
chances = 6
incorrect_letters = ""
score = 0

game = True
while game:
    guess = get_guess(valid_words)
    score, guess_incorrect_letters, bg = evaluate_guess(guess, word)

    for letter in guess_incorrect_letters:
        if letter not in incorrect_letters:
            incorrect_letters += letter

    chances -= 1

    print_guess(guess, incorrect_letters, bg)

    if score == 5:
        print("Well done. The word was " + word)
        game = False
    elif chances == 0:
        print("Better luck next time. The word was " + word)
        game = False