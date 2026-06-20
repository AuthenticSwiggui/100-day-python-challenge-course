from final_beginner_projects.game_data import game_data
import random

#TODO 1: Initialize the game: load 2 random terms -> accepts input choice -> compare both terms -> calcu
def play() -> None:
    score = 0
    last_term = {}
    comparison_results = ""
    user_input = ""
    game_over = False
    higher_result = {}
    while not game_over:
        term_a, term_b = load_terms(a = last_term)
        comparison_results, higher_result = compare_terms(option_a= term_a, option_b=term_b)
        user_input = check_user_input(choice_a=term_a['term'], choice_b=term_b['term'])
        game_over = did_player_lose(user_choice = user_input, results=comparison_results)
        print("*" * 60)
        print(f"A. {term_a['term']} has {term_a['searches']:,}")
        print(f"B. {term_b['term']} has {term_b['searches']:,}")
        if game_over:
            print("GOOONG!!! Game Over!!! :'(")
            print(f"{higher_result['term']} has more results with {higher_result['searches']:,} Average searches on Google!")
            break
        print(f"Well Done! {higher_result['term']} had more searchs on Google with {higher_result['searches']:,}!")
        last_term = term_b
        score += 1
        print(f"Your current score is: {score}")
    print_results(score)


#TODO 2: Load terms
def load_terms(a: dict) -> tuple[dict, dict]:
    if not a:
        a = random.choice(game_data)
    while True:
        b = random.choice(game_data)
        if not b == a:
            break
    return a, b

#TODO 3: Accept and check player's choice
def check_user_input(choice_a: str, choice_b: str) -> str:
    print("Guess which term has more searches on Google!")
    print("Choose between:")
    print(f"A. {choice_a}")
    print("Ooooorrr")
    print(f"B. {choice_b}")
    while True:
        choice = input("So tell me!!! What is the most searched on GOOGLE!!!\n").lower()
        if choice in ["a", "b", "none"]:
            return choice
        print("GOOONG! \nThere are no more choices! \nJust A, B or none!")

#TODO 4: Compare two terms to define which term is the most searched
def did_player_lose(user_choice: str, results: str) -> bool:
    if user_choice == results:
        return False
    return True

#TODO 5: Compare which is higher and returns the higher result
def compare_terms(option_a: dict[str, int], option_b: dict[str, int]) -> tuple[str, dict[str, int]]:
    if option_b["searches"] == option_a["searches"]:
        return "none", option_a
    if option_b["searches"] > option_a["searches"]:
        return "b", option_b
    return "a", option_a

#TODO 6: Print game results
def print_results(score: int) -> None:
    print(f"That was a tough one!")
    print(f"The final score was {score} points!")

def main():
    continue_playing = True
    retry = ""
    while continue_playing:
        play()
        retry = input("Continue?\n").lower()
        if retry not in ["y", "yes"]:
            break



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()