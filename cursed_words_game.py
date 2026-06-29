from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet, OptionError

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


# Option Dataclass
@dataclass
class CursedWordsArchipelagoOptions:
    cursed_words_characters: CursedWordsCharacters
    cursed_words_crowns: CursedWordsCrowns
    cursed_words_cursed_bosses: CursedWordsCursedBosses
    cursed_words_secret_final_boss: CursedWordsMichael

# Main Class
class CursedWordsGame(Game):
    name = "Cursed Words"
    platform = KeymastersKeepGamePlatforms.PC

    is_adult_only_or_unrated = False

    options_cls = CursedWordsArchipelagoOptions

    # Optional Game Constraints
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Only upgrade the SIDE side of your pin",
                data={
                    "SIDE": (self.sides, 1),
                },
            ),
            GameObjectiveTemplate(
                label="Only use 4 grids max",
                data=dict()
            )
        ]

    # Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        obj: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Win as CHAR",
                data={
                    "CHAR": (self.characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a CROWN (or harder) run as CHAR",
                data={
                    "CROWN": (self.crowns, 1),
                    "CHAR": (self.characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Defeat BOSS",
                data={
                    "BOSS": (self.bosses, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
        ]
        if self.include_cursed_bosses:
            obj.append(            
                GameObjectiveTemplate(
                    label="Defeat a cursed BOSS",
                    data={
                        "BOSS": (self.bosses, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=5,
                )
            )
        if self.include_michael:
            obj.extend([         
                GameObjectiveTemplate(
                    label="Defeat Michael as CHAR",
                    data={
                        "CHAR": (self.characters, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Defeat Michael in a CROWN run as CHAR",
                    data={
                        "CHAR": (self.characters, 1),
                        "CROWN": (self.crowns, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                )
            ]
            )
        return obj

    @property
    def include_cursed_bosses(self) -> bool:
        return bool(self.archipelago_options.cursed_words_cursed_bosses.value)

    @property
    def include_michael(self) -> bool:
        return bool(self.archipelago_options.cursed_words_secret_final_boss.value)

    @property
    def characters(self) -> Set[str]:
        if(len(self.archipelago_options.cursed_words_characters.value)==0):
            raise OptionError("No characters selected for Cursed Words.")
        return sorted(self.archipelago_options.cursed_words_characters.value)
    
    @property
    def crowns(self) -> Set[str]:
        if(len(self.archipelago_options.cursed_words_crowns.value)==0):
            raise OptionError("No crowns selected for Cursed Words.")
        return sorted(self.archipelago_options.cursed_words_crowns.value)
    
    @staticmethod
    def bosses() -> List[str]:
        return [
            "Axolotl",
            "Axolotl",
            "Badger",
            "Bat",
            "Bison",
            "Capybara",
            "Cobra",
            "Robo-Eel",
            "Fox",
            "Hyena",
            "Mole",
            "Robo-Monkey",
            "Salamander",
            "Toothed Whale",
            "Wolf",
            "Yeti Crab",
        ]
    
    @staticmethod
    def sides() -> List[str]:
        return ["Left", "Right"]

# Archipelago Options
class CursedWordsCursedBosses(Toggle):
    """
    Indicates whether to include Cursed Bosses in Cursed Words.
    """

    display_name = "Cursed Words Cursed Bosses"

class CursedWordsMichael(Toggle):
    """
    Indicates whether to include the secret final boss in Cursed Words.
    """

    display_name = "Cursed Words Secret Final Boss"

class CursedWordsCharacters(OptionSet):
    """
    Indicates which characters you want to play as in Cursed Words.
    """

    display_name = "Cursed Words Characters"
    valid_keys = [
        "Rodman",
        "Nina Nix",
        "Hayley Bayles",
        "Sam Gambit",
        "Bones The Dog",
        "Octacles",
        "Nat-H4",
        "Sandy Saguaro",
        "Cretaceous Meg",
        "Human Boy",
        "Beans"
    ]
    
    default = valid_keys

class CursedWordsCrowns(OptionSet):
    """
    Indicates which crowns you want to play with in Cursed Words.
    """

    display_name = "Cursed Words Crowns"
    valid_keys = [
        "Crownless",
        "Purple Crown",
        "Yellow Crown",
        "Orange Crown",
        "Pink Crown",
        "Green Crown",
        "Blue Crown",
        "Red Crown"
    ]
    
    default = valid_keys