import random
from word_list import WORD_LIST
from waifu_ascii_art import WAIFU

print(WAIFU)

def cargar_palabra():
    #TODO 1: load list
    current_word = random.choice(WORD_LIST)
    print(f"This word has {len(current_word)} words.")
    return current_word

def adivinar_palabra():
    current_word = cargar_palabra()
    lives = 3
    placeholder = ["_" for _ in current_word]
    print("".join(placeholder))

    while is_alive(lives):
        guess = input("Inserte letra: ").lower()
        if len(guess) != 1:
            print("Insert ONLY a character cyka!")
            continue
        if guess in placeholder:
            print(f"The character {guess} was already placed CYKA!")
            continue
        if guess in current_word:
            print("Oka")
            update_placeholder(placeholder, current_word, guess)
        else:
            print("Non, wrong char!")
            lives -= 1
            print(f"The character {guess} is not in the word, CYKA!")
        print("".join(placeholder))

        if not "_" in placeholder:
            print("You won!")
            return
    print(f"You lost cyka!")
    print(f"The word was: {current_word.capitalize()}")
        
def update_placeholder(placeholder, current_word, guess):
    for index, char in enumerate(current_word):
            if char == guess:
                placeholder[index] = guess

def is_alive(lives: int) -> bool:
    if lives > 0:
        print(f"Remaining lives: {lives}")
        return True
    return False
    

adivinar_palabra()