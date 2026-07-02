import random

CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]
RULES = {
    ("scissors", "lizard"): "decapitates",
    ("scissors", "paper"): "cuts",
    ("paper", "rock"): "covers",
    ("rock", "lizard"): "crushes",
    ("lizard", "spock"): "poisons",
    ("spock", "scissors"): "smashes",
    ("lizard", "paper"): "eats",
    ("paper", "spock"): "disproves",
    ("spock", "rock"): "vaporizes",
    ("rock", "scissors"): "crushes",
}


def get_player_choice():
    prompt = "Choose one of the following: " + ", ".join(CHOICES) + ": "
    while True:
        choice = input(prompt).strip().lower()
        if choice in CHOICES:
            return choice
        print(f"Invalid choice '{choice}'. Please select from: {', '.join(CHOICES)}.")


def get_computer_choice():
    return random.choice(CHOICES)


def determine_winner(player: str, computer: str) -> str | None:
    if player == computer:
        return None
    if (player, computer) in RULES:
        return "player"
    return "computer"


def describe_result(winner_choice: str, loser_choice: str) -> str:
    action = RULES.get((winner_choice, loser_choice))
    if action:
        return f"{winner_choice.capitalize()} {action} {loser_choice}."
    return "No rule found."


def play_round():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {player_choice}. Computer chose {computer_choice}.")

    winner = determine_winner(player_choice, computer_choice)
    if winner is None:
        print("It's a tie!")
        return

    if winner == "player":
        result_text = describe_result(player_choice, computer_choice)
        print(f"You win! {result_text}")
    else:
        result_text = describe_result(computer_choice, player_choice)
        print(f"Computer wins! {result_text}")


def main():
    print("Welcome to Rock Paper Scissors Lizard Spock!")
    while True:
        play_round()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
