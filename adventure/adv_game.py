import random
from abc import ABC, abstractmethod
from enum import Enum
from typing import Generic, Iterable, List, Optional, TypeVar

T = TypeVar("T")


class EncounterOutcome(Enum):
    CONTINUE = "CONTINUE"
    END = "END"


class Encounter(ABC):
    @abstractmethod
    def run_encounter(self) -> EncounterOutcome:
        pass

# This is a list of clues that can be used in an adventure game. Each clue provides a hint or piece of information that can help the player solve puzzles or uncover secrets within the game environment.
clues = [
    "There is a strange shadow burned into the corner of the wall.",
    "There is a faint scent of smoke lingering in the air.",
    "There is an old newspaper clipping folded and left behind.",
    "There is a whisper of footsteps that stopped abruptly.",
    "There is a set of muddy prints leading away from the doorway.",
    "There is a silken ribbon tangled around a chair leg.",
    "There is a half-empty cup that seems to have been abandoned in a hurry.",
    "There is a small pile of ashes that does not belong.",
    "There is an impression in the carpet as if someone knelt there.",
    "There is a voice on the edge of memory, hinting at something lost."
]
# This is a list of sensory experiences that can be used to enhance the atmosphere and immersion in the adventure game.
sense_exp = [
    "You see flickering torchlight dancing across the stone walls.",
    "You hear distant footsteps echoing through empty halls.",
    "You smell cold stone mixed with a hint of old incense.",
    "You feel a draft that carries the weight of unanswered questions.",
    "You sense the air trembling with a secret just out of reach.",
    "You hear a soft whisper sliding past the rafters.",
    "You see an ancient tapestry swaying though the room is still.",
    "You smell smoke from a hearth that has long since cooled.",
    "You feel the grain of polished wood beneath your fingertips.",
    "You sense a presence watching from the shadowed corners.",
    "You hear the low drip of water somewhere deeper within the castle.",
    "You see a faint glow where no candle is lit."
]

# This class is designed to manage a collection of items, allowing for random selection without repetition until all items have been used. It can be useful in scenarios where you want to present unique options or clues to the player in an adventure game.
class RandomItemSelector(Generic[T]):
    def __init__(self, items: Optional[Iterable[T]] = None) -> None:
        self.items: List[T] = list(items) if items is not None else []
        self.used_items: List[T] = []

    def add_item(self, item: T) -> None:
        self.items.append(item)

    def pull_random_item(self) -> Optional[T]:
        if not self.items:
            self.reset()
            return None

        available_items = [item for item in self.items if item not in self.used_items]
        if not available_items:
            self.reset()
            available_items = list(self.items)

        selected = random.choice(available_items)
        self.used_items.append(selected)
        return selected

    def reset(self) -> None:
        self.used_items.clear()


class SenseClueGenerator:
    _instance = None
    clue_selector: RandomItemSelector[str]
    sense_selector: RandomItemSelector[str]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.clue_selector = RandomItemSelector(clues)
            cls._instance.sense_selector = RandomItemSelector(sense_exp)
        return cls._instance

    def get_senseclue(self):
        clue = self.clue_selector.pull_random_item()
        sense = self.sense_selector.pull_random_item()
        return f"{clue} {sense}"

    def pull_random_item(self):
        return self.get_senseclue()


class DefaultEncounter(Encounter):
    def __init__(self):
        self.generator = SenseClueGenerator()

    def run_encounter(self) -> EncounterOutcome:
        result = self.generator.pull_random_item()
        print(result)
        return EncounterOutcome.CONTINUE


class TreasureEncounter(Encounter):
        
    def run_encounter(self) -> EncounterOutcome:
        print("You found the treasure! You have won the game!")
        return EncounterOutcome.END


class RedWizard(Encounter):
    def __init__(self):
        self.game_rules = {
            "Fireball": ["Ice Shard", "Lightning Bolt"],
            "Ice Shard": ["Wind Gust", "Earthquake"],
            "Wind Gust": ["Lightning Bolt", "Fireball"],
            "Lightning Bolt": ["Earthquake", "Ice Shard"],
            "Earthquake": ["Fireball", "Wind Gust"]
        }
        self.valid_choices = list(self.game_rules.keys())
    
    def run_encounter(self) -> EncounterOutcome:
        print("\n" + "="*50)
        print("A Red Wizard appears before you!")
        print("You must engage the wizard in a spell battle!")
        print("="*50 + "\n")
        
        while True:
            print(f"Available spells: {', '.join(self.valid_choices)}")
            user_choice = input("Cast a spell: ").strip()
            
            if user_choice not in self.valid_choices:
                print("Invalid spell. Please try again.\n")
                continue
            
            wizard_choice = random.choice(self.valid_choices)
            
            print(f"\nYou cast: {user_choice}")
            print(f"The Red Wizard casts: {wizard_choice}\n")
            
            if user_choice == wizard_choice:
                print("Both spells clash in a brilliant explosion! It's a draw!\n")
                continue
            
            if wizard_choice in self.game_rules[user_choice]:
                print("="*50)
                print("Your spell overpowers the wizard's!")
                print("The Red Wizard has been vanquished from this castle!")
                print("="*50 + "\n")
                return EncounterOutcome.CONTINUE
            else:
                print("="*50)
                print("The wizard's spell overwhelms you!")
                print("You have been vanquished from this castle!")
                print("="*50 + "\n")
                return EncounterOutcome.END


class BlueWizard(Encounter):
    def __init__(self):
        self.game_rules = {
            "Fireball": ["Frost"],
            "Frost": ["Lightning"],
            "Lightning": ["Fireball"]
        }
        self.valid_choices = list(self.game_rules.keys())
    
    def run_encounter(self) -> EncounterOutcome:
        print("\n" + "="*50)
        print("A Blue Wizard appears before you!")
        print("You must challenge the wizard to a spell duel!")
        print("="*50 + "\n")
        
        while True:
            print(f"Available spells: {', '.join(self.valid_choices)}")
            user_choice = input("Cast a spell: ").strip()
            
            if user_choice not in self.valid_choices:
                print("Invalid spell. Please try again.\n")
                continue
            
            wizard_choice = random.choice(self.valid_choices)
            
            print(f"\nYou cast: {user_choice}")
            print(f"The Blue Wizard casts: {wizard_choice}\n")
            
            if user_choice == wizard_choice:
                print("Both spells collide in a spectacular display! It's a draw!\n")
                continue
            
            if wizard_choice in self.game_rules[user_choice]:
                print("="*50)
                print("Your spell defeats the Blue Wizard's!")
                print("The Blue Wizard has been vanquished from this castle!")
                print("="*50 + "\n")
                return EncounterOutcome.CONTINUE
            else:
                print("="*50)
                print("The Blue Wizard's spell defeats yours!")
                print("You have been vanquished from this castle!")
                print("="*50 + "\n")
                return EncounterOutcome.END


class Room:
       
    def __init__(self, name: str, encounter: Encounter) -> None:
        self.name: str = name
        self.encounter: Encounter = encounter

    def visit_room(self) -> EncounterOutcome:
        return self.encounter.run_encounter()

# This is a list of rooms that can be explored in the adventure game. Each room has a name and an associated encounter that defines what happens when the player visits that room. The encounters can provide clues, sensory experiences, or lead to the discovery of treasure.
rooms = [
    Room("Great Hall", DefaultEncounter()),
    Room("Armory", DefaultEncounter()),
    Room("Tower Chamber", DefaultEncounter()),
    Room("Library", DefaultEncounter()),
    Room("Guard Barracks", DefaultEncounter()),
    Room("Castle Courtyard", DefaultEncounter()),
    ]

rooms.append(Room("Treasure Room", TreasureEncounter()))
rooms.append(Room("Wizard's Chamber", RedWizard()))
# create a room called “The Red Wizard’s Lair” with the Red Wizard Encounter and add it to the rooms list
rooms.append(Room("The Red Wizard’s Lair", RedWizard()))
# create a room called “The Blue Wizard’s Lair” with the Blue Wizard Encounter and add it to the rooms list
rooms.append(Room("The Blue Wizard’s Lair", BlueWizard()))

class Castle:
    def __init__(self, rooms: List[Room]) -> None:
        self.room_selector = RandomItemSelector(rooms)

    def select_door(self):
        min_doors = 2
        max_doors = 4
        print("\nA set of doors appears before you.")
        print(f"Choose a door between {min_doors} and {max_doors}.")

        while True:
            user_input = input("Enter door number: ").strip()
            if not user_input.isdigit():
                print("Invalid input. Please enter a number.")
                continue

            door_number = int(user_input)
            if door_number < min_doors or door_number > max_doors:
                print(f"Please choose a door between {min_doors} and {max_doors}.")
                continue

            print(f"You selected door {door_number}.")
            return door_number

    def next_room(self):
        selected_door = self.select_door()
        print(f"\nDoor {selected_door} swings open...\n")

        chosen_room = self.room_selector.pull_random_item()
        if chosen_room is None:
            print("No rooms are available to explore.")
            return None

        print(f"You step into the {chosen_room.name}.")
        result = chosen_room.visit_room()
        return result

    def reset(self):
        self.room_selector.reset()
        print("The castle resets, and all rooms are available again.")


class Game:
    def __init__(self, rooms: List[Room]) -> None:
        self.castle = Castle(rooms)

    def play_game(self):
        print("Welcome to the castle adventure!")
        print("Your objective is to navigate through the castle and find the treasure.")
        print("Choose doors carefully and explore each room.")

        while True:
            result = self.castle.next_room()
            if result == EncounterOutcome.END:
                self.castle.reset()
                print("Game Over")

                answer = input("Would you like to explore a different castle? (yes/no): ").strip().lower()
                if answer in {"yes", "y"}:
                    print("Starting a new adventure in a fresh castle...")
                    continue
                print("Thank you for playing.")
                break
            elif result == EncounterOutcome.CONTINUE:
                continue
            else:
                break




# run the game
if __name__ == "__main__":
    game = Game(rooms)
    game.play_game()