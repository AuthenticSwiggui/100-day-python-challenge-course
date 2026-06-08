import random

def grab_card() -> int:
    """Returns a random card """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def initialize_game() -> dict:
    players = {
        "cpu": {
            "hand": [],
            "score": 0,
            "still_playing": True,
            "status": "Playing"
            },
        "human": {
            "hand": [],
            "score": 0,
            "still_playing": True,
            "status" : "Playing" 
        }
    }
        
    return players
    

def play(players: dict):
    while (players["human"]["still_playing"] or players["cpu"]["still_playing"]):
        for player_name, player in players.items():
            if not player["still_playing"]:
                continue
            current_card = grab_card()

            player["hand"].append(current_card)
            player["score"] += current_card

            check_scores(player)

            if player["still_playing"]:
                print(f"Computer first card: {players['cpu']["hand"][0]}")
                player["still_playing"] = continue_playing(player_name, player)
    winner = defining_winners(players)
    print_winner(winner)
    print_results(players)
    
def print_winner(winner: dict[str, int]) -> None:
    """Prints the game result."""
    print("\n" + "=" * 60)
    if winner["winner_name"]:
        print(f"The winner is {winner['winner_name']} with a score of {winner['score']}!")
    else:
        print(f"It's a tie! Both players scored {winner['score']}.")


def defining_winners(players: dict[str, dict]) -> dict[str, int]:
    human = players["human"]
    cpu = players["cpu"]
    human_score = human["score"]
    cpu_score = cpu["score"]



    winner_data = {
        "winner_name": "",
        "score": 0
    }

    if human_score == 21:
        winner_name, winning_score = "Human", 21
    elif cpu_score == 21:
        winner_name, winning_score = "CPU", 21
    elif human_score > 21 and cpu_score > 21:
        winner_name, winning_score = None, human_score  # Both busted — tie
    elif human_score > 21:
        winner_name, winning_score = "CPU", cpu_score
    elif cpu_score > 21:
        winner_name, winning_score = "Human", human_score
    elif human_score > cpu_score:
        winner_name, winning_score = "Human", human_score
    elif cpu_score > human_score:
        winner_name, winning_score = "CPU", cpu_score
    else:
        winner_name, winning_score = None, human_score  # Tie

    # Update statuses
    if winner_name == "Human":
        human["status"], cpu["status"] = "Winner", "Loser"
    elif winner_name == "CPU":
        cpu["status"], human["status"] = "Winner", "Loser"
    else:
        human["status"] = cpu["status"] = "Tie"
 
    return {"winner_name": winner_name, "score": winning_score}


    return winner_data
            
def print_results(players: dict[str, dict]) -> None:
    for player_name, player in players.items():
        print("*" * 60)
        print(f"Player: {player_name}")
        for attrib, value in player.items():
            print(f"{attrib} : {value}")

def check_scores(player: dict) -> None:
    while player["score"] > 21 and 11 in player["hand"]:
            ace_index = player["hand"].index(11)
            player["hand"][ace_index] = 1
            player ["score"] = sum(player["hand"])

    if player["score"] > 21:
        player["still_playing"] = False

    if player["score"] == 21:
        player["still_playing"] = False


def continue_playing(player_name: str, player:dict) -> bool:
    print(player_name)
    print("=" * 60)
    if player_name == "human":
        print(f"This is your hand: {player['hand']}")
        print(f"Your current score is:  {player['score']}")
        choice = input("Do you want to still playing?: Y/N\n").lower()
        return choice not in ["n", "no"]
    if player_name == "cpu":
        return player["score"] < 16

def main() -> None:
    while input("Do you wanna to play a new game? y/n \n") in ["y", "yes"]:
        players = initialize_game()
        play(players)

if __name__ == "__main__":
    main()