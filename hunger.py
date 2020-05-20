#версия 0.8 (8-й этап)
import random

print("H A N G M A N")
word_list = ['python', 'java', 'kotlin', 'javascript']
guess_word = random.choice(word_list)
N = len(guess_word)
symb_word = N * '-'
symb_list = list(symb_word)
attempts = 8
used_letters = set()

def symb_print(list):
    '''
    The fuction return the list at a string look
    for more accurate printing
    '''
    symb_str = ''
    for i in range(len(list)):
        symb_str += list[i]
    return symb_str


while True:
    choose = input('Type "play" to play the game, "exit" to quit:')
    if choose == "play":
        while attempts > 0:
            print()
            print(symb_print(symb_list))
            letter = input('Input a letter:')
            if len(letter) != 1:
                print("You should print a single letter")
            elif letter == letter.upper():
                print("It is not an ASCII lowercase letter")
            else:
                if letter in guess_word and letter not in used_letters:
                    for i in range(N):
                        if letter == guess_word[i]:
                            symb_list[i] = letter
            # attempts -= 1
                    used_letters.add(letter)
                elif letter in used_letters:
                    print("You already typed this letter")
        # attempts -= 1
                else:
                    print("No such letter in the word")
                    attempts -= 1
                    used_letters.add(letter)
                    if letter not in used_letters:
                        used_letters.add(letter)
                        attempts += 1

                if "-" not in symb_list:
                    print("You survived!")
                    break
        else:
           print("You are hanged!")
    else:
        break
