import pytest
from rpsls.rpsls import determine_winner, describe_result


def test_determine_winner_tie_returns_none():
    assert determine_winner("rock", "rock") is None


def test_determine_winner_player_wins():
    assert determine_winner("rock", "scissors") == "player"
    assert determine_winner("spock", "rock") == "player"


def test_determine_winner_computer_wins():
    assert determine_winner("scissors", "rock") == "computer"
    assert determine_winner("lizard", "scissors") == "computer"


def test_describe_result_uses_action_verb():
    assert describe_result("rock", "scissors") == "Rock crushes scissors."
    assert describe_result("spock", "rock") == "Spock vaporizes rock."
