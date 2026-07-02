# Copilot Course

Welcome to the `copilot_course` repository — a small, friendly Python learning project focused on building interactive console games while exploring object-oriented design, randomness, and user interaction.

## What this course covers

This course is designed for beginners and intermediate learners who want to:
- Learn how Python modules and packages are organized.
- Build small games with clear logic and reusable components.
- Practice working with classes, enums, abstraction, and simple game rules.
- Explore text-based interaction using the terminal.

## Project structure

```
README.md
adventure/
  adv_game.py
  random_item_selector.py
rpsls/
  rpsls.py
```

## File descriptions

### `adventure/adv_game.py`
This file contains a mini adventure game engine built with an encounter system.
It defines:
- `EncounterOutcome`: an enum representing whether the game should continue or end.
- `Encounter`: an abstract base class for all adventure encounters.
- `DefaultEncounter`: prints atmospheric clues and sensory descriptions.
- `TreasureEncounter`: ends the game with a winning message.
- `RedWizard` and `BlueWizard`: interactive spell battle encounters where the player selects a spell and attempts to defeat the wizard.

The game uses a combination of randomness, repeated encounters, and user input to create a simple narrative experience.

### `adventure/random_item_selector.py`
This module contains a reusable helper class:
- `RandomItemSelector`

The selector stores a list of items, returns a random unused item each time, and resets when all items have been used. It is used in the adventure game to rotate clues and sensory descriptions without immediate repetition.

### `rpsls/rpsls.py`
This file is a complete implementation of the classic `Rock Paper Scissors Lizard Spock` game.
It includes:
- Choice validation and user input handling.
- Random computer moves.
- A rule set mapping winning relationships and action verbs.
- Round-by-round play with win/tie detection.
- A replay loop so players can keep playing until they choose to stop.

## How to play

Open a terminal in the repository root and run one of the games:

- Adventure game module:
  - `python adventure/adv_game.py`
- Rock Paper Scissors Lizard Spock:
  - `python rpsls/rpsls.py`

> Note: Depending on your Python setup, you may need to use `python3` instead of `python`.

## Learning opportunities

This repository is ideal for practicing:
- Python package imports and module organization.
- Random selection and stateful item tracking.
- Command-line input validation.
- Object-oriented programming with abstract classes and inheritance.
- Simple game loop design.

## Extend the course

You can make the course more engaging by adding:
- More encounter types in `adventure/adv_game.py`.
- Health, inventory, or story progression mechanics.
- Better input prompts and user-friendly menus.
- A scoreboard or best-of series for `rpsls/rpsls.py`.

Enjoy learning and building with Python!