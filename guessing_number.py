import random

EASY_LIVES = 10
HARD_LIVES = 5

def get_lives() -> int:
    """Returns the number of lives based on the chosen difficulty level."""
    while True:
        mode = input("Enter 'easy' or 'hard' for easy or hard mode: ").lower()
        if mode == "easy":
            return EASY_LIVES
        if mode == "hard":
            return HARD_LIVES
        print("Enter 'easy' or 'hard', not something else.")

def guess_number() -> int:
    """Prompts the user to enter a number between 1 and 100 and returns it."""
    while True:
        try:
            number = int(input("Enter a number between 1 and 100: "))
            if 1 <= number <= 100:
                return number
            print("Enter a number between 1 and 100")
        except ValueError:
            print("Enter a valid number")

def has_guessed_the_number(number: int, randomized_number: int) -> bool:
    """Checks if the user's guess is correct, too high, or too low."""
    if number == randomized_number:
        return True
    elif number > randomized_number:
        print("Too big, KYAH!!!")
    else:
        print("Ewww... Too small!")
    return False

def is_alive(lives: int) -> bool:
    """Checks if the player still has lives left."""
    return lives > 0

def play() -> None:
    """Main function to run the guessing number game."""
    number_to_guess = random.randint(1, 100)
    lives = get_lives()

    while is_alive(lives):
        print(f"Remaining lives {lives}")
        user_input = guess_number()
        if has_guessed_the_number(user_input, number_to_guess):
            print("*" * 60)
            print("You had won!")
            break
        lives -= 1
    else:
        print("*" * 60)
        print("You had lost!")
    print(f"The number was: {number_to_guess}")

def main():
    play()

if __name__ == "__main__":
    main()