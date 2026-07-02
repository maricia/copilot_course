import random

import pytest
from adventure.adv_game import (
    BlueWizard,
    DefaultEncounter,
    EncounterOutcome,
    RedWizard,
    Room,
    TreasureEncounter,
)


def test_default_encounter_returns_continue(capsys):
    encounter = DefaultEncounter()
    result = encounter.run_encounter()

    captured = capsys.readouterr()
    assert result == EncounterOutcome.CONTINUE
    assert "You" in captured.out


def test_treasure_encounter_ends_game(capsys):
    encounter = TreasureEncounter()
    result = encounter.run_encounter()

    captured = capsys.readouterr()
    assert result == EncounterOutcome.END
    assert "found the treasure" in captured.out


def test_room_visit_room_calls_encounter():
    class StubEncounter:
        def run_encounter(self):
            return EncounterOutcome.CONTINUE

    room = Room("Test Room", StubEncounter())
    assert room.visit_room() == EncounterOutcome.CONTINUE


def test_red_wizard_player_wins(monkeypatch, capsys):
    wizard = RedWizard()
    inputs = iter(["Fireball"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr(random, "choice", lambda choices: "Ice Shard")

    result = wizard.run_encounter()

    captured = capsys.readouterr()
    assert result == EncounterOutcome.CONTINUE
    assert "Your spell overpowers the wizard" in captured.out


def test_red_wizard_player_loses(monkeypatch, capsys):
    wizard = RedWizard()
    inputs = iter(["Fireball"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr(random, "choice", lambda choices: "Earthquake")

    result = wizard.run_encounter()

    captured = capsys.readouterr()
    assert result == EncounterOutcome.END
    assert "The wizard's spell overwhelms you" in captured.out


def test_blue_wizard_player_wins(monkeypatch, capsys):
    wizard = BlueWizard()
    inputs = iter(["Fireball"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr(random, "choice", lambda choices: "Frost")

    result = wizard.run_encounter()

    captured = capsys.readouterr()
    assert result == EncounterOutcome.CONTINUE
    assert "Your spell defeats the Blue Wizard" in captured.out


def test_blue_wizard_player_loses(monkeypatch, capsys):
    wizard = BlueWizard()
    inputs = iter(["Fireball"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr(random, "choice", lambda choices: "Lightning")

    result = wizard.run_encounter()

    captured = capsys.readouterr()
    assert result == EncounterOutcome.END
    assert "The Blue Wizard's spell defeats yours" in captured.out
