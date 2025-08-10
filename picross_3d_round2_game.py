from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, DefaultOnToggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


# Option Dataclass
@dataclass
class Picross3dRound2ArchipelagoOptions:
    picross_3d_round2_include_tutorial_levels: Picross3dRound2IncludeTutorialLevels
    picross_3d_round2_include_time_challenges: Picross3dRound2IncludeTimeChallenges
    picross_3d_round2_include_one_chance_challenges: Picross3dRound2IncludeOneChanceChallenges
    picross_3d_round2_include_construction_challenges: Picross3dRound2IncludeConstructionChallenges

# Main Class
class Picross3dRound2Game(Game):
    name = "Picross 3D Round 2"
    platform = KeymastersKeepGamePlatforms._3DS

    is_adult_only_or_unrated = False

    options_cls = Picross3dRound2ArchipelagoOptions

    # Optional Game Constraints
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Play in hard mode",
                data= dict(),
            ),
            GameObjectiveTemplate(
                label="Get only rainbow medals",
                data= dict(),
            ),
            GameObjectiveTemplate(
                label="Do not make any mistakes",
                data= dict(),
            ),
            GameObjectiveTemplate(
                label="Finish in less than 20 minutes",
                data= dict(),
            ),
        ]

    # Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Beat LEVEL and get at least the MEDAL medal",
                data={
                    "LEVEL": (self.levels, 1),
                    "MEDAL": (self.medals, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Beat all levels of book BOOK",
                data={
                    "BOOK": (self.books, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
        ]
    
    @staticmethod
    def medals() -> List[str]:
        return [
            "Ruby",
            "Emerald",
            "Diamond",
            "Rainbow"
        ]

    @functools.cached_property
    def normal_levels(self) -> List[str]:
        return [
            "Book 4 - Puzzle 1",
            "Book 4 - Puzzle 2",
            "Book 4 - Puzzle 3",
            "Book 4 - Puzzle 4",
            "Book 4 - Puzzle 5",
            "Book 4 - Puzzle 6",
            "Book 5 - Puzzle 1",
            "Book 5 - Puzzle 2",
            "Book 5 - Puzzle 3",
            "Book 5 - Puzzle 4",
            "Book 5 - Puzzle 5",
            "Book 6 - Puzzle 1",
            "Book 6 - Puzzle 2",
            "Book 6 - Puzzle 3",
            "Book 6 - Puzzle 4",
            "Book 6 - Puzzle 5",
            "Book 7 - Puzzle 1",
            "Book 7 - Puzzle 2",
            "Book 7 - Puzzle 3",
            "Book 7 - Puzzle 4",
            "Book 9 - Puzzle 1",
            "Book 9 - Puzzle 2",
            "Book 9 - Puzzle 3",
            "Book 9 - Puzzle 4",
            "Book 9 - Puzzle 5",
            "Book 10 - Puzzle 1",
            "Book 10 - Puzzle 2",
            "Book 10 - Puzzle 3",
            "Book 10 - Puzzle 4",
            "Book 10 - Puzzle 5",
            "Book 10 - Puzzle 6",
            "Book 10 - Puzzle 7",
            "Book 11 - Puzzle 1",
            "Book 11 - Puzzle 2",
            "Book 11 - Puzzle 3",
            "Book 11 - Puzzle 4",
            "Book 11 - Puzzle 5",
            "Book 14 - Puzzle 1",
            "Book 14 - Puzzle 2",
            "Book 14 - Puzzle 3",
            "Book 14 - Puzzle 4",
            "Book 14 - Puzzle 5",
            "Book 14 - Puzzle 6",
            "Book 14 - Puzzle 7",
            "Book 15 - Puzzle 1",
            "Book 15 - Puzzle 2",
            "Book 15 - Puzzle 3",
            "Book 15 - Puzzle 4",
            "Book 15 - Puzzle 5",
            "Book 15 - Puzzle 6",
            "Book 15 - Puzzle 7",
            "Book 15 - Puzzle 8",
            "Book 17 - Puzzle 1",
            "Book 17 - Puzzle 2",
            "Book 17 - Puzzle 3",
            "Book 17 - Puzzle 4",
            "Book 17 - Puzzle 5",
            "Book 17 - Puzzle 6",
            "Book 17 - Puzzle 7",
            "Book 18 - Puzzle 1",
            "Book 18 - Puzzle 2",
            "Book 18 - Puzzle 3",
            "Book 18 - Puzzle 4",
            "Book 18 - Puzzle 5",
            "Book 18 - Puzzle 6",
            "Book 18 - Puzzle 7",
            "Book 18 - Puzzle 8",
            "Book 19 - Puzzle 1",
            "Book 19 - Puzzle 2",
            "Book 19 - Puzzle 3",
            "Book 19 - Puzzle 4",
            "Book 19 - Puzzle 5",
            "Book 19 - Puzzle 6",
            "Book 19 - Puzzle 7",
            "Book 21 - Puzzle 1",
            "Book 21 - Puzzle 2",
            "Book 21 - Puzzle 3",
            "Book 21 - Puzzle 4",
            "Book 21 - Puzzle 5",
            "Book 21 - Puzzle 6",
            "Book 21 - Puzzle 7",
            "Book 21 - Puzzle 8",
            "Book 21 - Puzzle 9",
            "Book 21 - Puzzle 10",
            "Book 22 - Puzzle 1",
            "Book 22 - Puzzle 2",
            "Book 22 - Puzzle 3",
            "Book 22 - Puzzle 4",
            "Book 22 - Puzzle 5",
            "Book 22 - Puzzle 6",
            "Book 23 - Puzzle 1",
            "Book 23 - Puzzle 2",
            "Book 23 - Puzzle 3",
            "Book 23 - Puzzle 4",
            "Book 23 - Puzzle 5",
            "Book 23 - Puzzle 6",
            "Book 25 - Puzzle 1",
            "Book 25 - Puzzle 2",
            "Book 25 - Puzzle 3",
            "Book 25 - Puzzle 4",
            "Book 25 - Puzzle 5",
            "Book 26 - Puzzle 1",
            "Book 26 - Puzzle 2",
            "Book 26 - Puzzle 3",
            "Book 26 - Puzzle 4",
            "Book 26 - Puzzle 5",
            "Book 27 - Puzzle 1",
            "Book 27 - Puzzle 2",
            "Book 27 - Puzzle 3",
            "Book 27 - Puzzle 4",
            "Book 27 - Puzzle 5",
            "Book 27 - Puzzle 6",
            "Book 28 - Puzzle 1",
            "Book 28 - Puzzle 2",
            "Book 28 - Puzzle 3",
            "Book 28 - Puzzle 4",
            "Book 28 - Puzzle 5",
            "Book 28 - Puzzle 6",
            "Book 28 - Puzzle 7",
            "Book 28 - Puzzle 8",
            "Book 29 - Puzzle 1",
            "Book 29 - Puzzle 2",
            "Book 29 - Puzzle 3",
            "Book 29 - Puzzle 4",
            "Book 29 - Puzzle 5",
            "Book 30 - Puzzle 1",
            "Book 30 - Puzzle 2",
            "Book 30 - Puzzle 3",
            "Book 30 - Puzzle 4",
            "Book 30 - Puzzle 5",
            "Book 30 - Puzzle 6",
            "Book 30 - Puzzle 7",
            "Book 30 - Puzzle 8",
            "Book 31 - Puzzle 1",
            "Book 31 - Puzzle 2",
            "Book 31 - Puzzle 3",
            "Book 31 - Puzzle 4",
            "Book 31 - Puzzle 5",
            "Book 33 - Puzzle 1",
            "Book 33 - Puzzle 2",
            "Book 33 - Puzzle 3",
            "Book 33 - Puzzle 4",
            "Book 33 - Puzzle 5",
            "Book 33 - Puzzle 6",
            "Book 34 - Puzzle 1",
            "Book 34 - Puzzle 2",
            "Book 34 - Puzzle 3",
            "Book 34 - Puzzle 4",
            "Book 34 - Puzzle 5",
            "Book 34 - Puzzle 6",
            "Book 35 - Puzzle 1",
            "Book 35 - Puzzle 2",
            "Book 35 - Puzzle 3",
            "Book 35 - Puzzle 4",
            "Book 35 - Puzzle 5",
            "Book 35 - Puzzle 6",
            "Book 37 - Puzzle 1",
            "Book 37 - Puzzle 2",
            "Book 37 - Puzzle 3",
            "Book 37 - Puzzle 4",
            "Book 37 - Puzzle 5",
            "Book 37 - Puzzle 6",
            "Book 37 - Puzzle 7",
            "Book 37 - Puzzle 8",
            "Book 38 - Puzzle 1",
            "Book 38 - Puzzle 2",
            "Book 38 - Puzzle 3",
            "Book 38 - Puzzle 4",
            "Book 38 - Puzzle 5",
            "Book 39 - Puzzle 1",
            "Book 39 - Puzzle 2",
            "Book 39 - Puzzle 3",
            "Book 39 - Puzzle 4",
            "Book 39 - Puzzle 5",
            "Book 39 - Puzzle 6",
            "Book 39 - Puzzle 7",
            "Book 41 - Puzzle 1",
            "Book 41 - Puzzle 2",
            "Book 41 - Puzzle 3",
            "Book 41 - Puzzle 4",
            "Book 41 - Puzzle 5",
            "Book 41 - Puzzle 6",
            "Book 41 - Puzzle 7",
            "Book 41 - Puzzle 8",
            "Book 42 - Puzzle 1",
            "Book 42 - Puzzle 2",
            "Book 42 - Puzzle 3",
            "Book 42 - Puzzle 4",
            "Book 42 - Puzzle 5",
            "Book 42 - Puzzle 6",
            "Book 42 - Puzzle 7",
            "Book 43 - Puzzle 1",
            "Book 43 - Puzzle 2",
            "Book 43 - Puzzle 3",
            "Book 43 - Puzzle 4",
            "Book 43 - Puzzle 5",
            "Book 43 - Puzzle 6",
            "Book 44 - Puzzle 1",
            "Book 44 - Puzzle 2",
            "Book 44 - Puzzle 3",
            "Book 44 - Puzzle 4",
            "Book 44 - Puzzle 5",
            "Book 44 - Puzzle 6",
            "Book 44 - Puzzle 7",
            "Book 45 - Puzzle 1",
            "Book 45 - Puzzle 2",
            "Book 45 - Puzzle 3",
            "Book 45 - Puzzle 4",
            "Book 45 - Puzzle 5",
            "Book 46 - Puzzle 1",
            "Book 46 - Puzzle 2",
            "Book 46 - Puzzle 3",
            "Book 46 - Puzzle 4",
            "Book 46 - Puzzle 5",
            "Book 46 - Puzzle 6",
            "Book 47 - Puzzle 1",
            "Book 47 - Puzzle 2",
            "Book 47 - Puzzle 3",
            "Book 47 - Puzzle 4",
            "Book 47 - Puzzle 5",
            "Book 47 - Puzzle 6",
            "Book 49 - Puzzle 1",
            "Book 49 - Puzzle 2",
            "Book 49 - Puzzle 3",
            "Book 49 - Puzzle 4",
            "Book 49 - Puzzle 5",
            "Book 49 - Puzzle 6",
            "Book 49 - Puzzle 7",
            "Book 50 - Puzzle 1",
            "Book 50 - Puzzle 2",
            "Book 50 - Puzzle 3",
            "Book 50 - Puzzle 4",
            "Book 50 - Puzzle 5",
            "Book 50 - Puzzle 6",
            "Book 50 - Puzzle 7",
            "Book 50 - Puzzle 8",
            "Book 51 - Puzzle 1",
            "Book 51 - Puzzle 2",
            "Book 51 - Puzzle 3",
            "Book 51 - Puzzle 4",
            "Book 51 - Puzzle 5",
            "Book 51 - Puzzle 6",
            "Book 51 - Puzzle 7",
            "Book 53 - Puzzle 1",
            "Book 53 - Puzzle 2",
            "Book 53 - Puzzle 3",
            "Book 53 - Puzzle 4",
            "Book 53 - Puzzle 5",
            "Book 54 - Puzzle 1",
            "Book 54 - Puzzle 2",
            "Book 54 - Puzzle 3",
            "Book 54 - Puzzle 4",
            "Book 54 - Puzzle 5",
            "Book 54 - Puzzle 6",
            "Book 55 - Puzzle 1",
            "Book 55 - Puzzle 2",
            "Book 55 - Puzzle 3",
            "Book 55 - Puzzle 4",
            "Book 55 - Puzzle 5",
            "Book 56 - Puzzle 1",
            "Book 56 - Puzzle 2",
            "Book 56 - Puzzle 3",
            "Book 56 - Puzzle 4",
            "Book 56 - Puzzle 5",
            "Book 56 - Puzzle 6",
        ]

    @functools.cached_property
    def normal_books(self) -> List[str]:
        return [
            "Book 4",
            "Book 5",
            "Book 6",
            "Book 7",
            "Book 9",
            "Book 10",
            "Book 11",
            "Book 14",
            "Book 15",
            "Book 17",
            "Book 18",
            "Book 19",
            "Book 21",
            "Book 22",
            "Book 23",
            "Book 25",
            "Book 26",
            "Book 27",
            "Book 28",
            "Book 29",
            "Book 30",
            "Book 31",
            "Book 33",
            "Book 34",
            "Book 35",
            "Book 37",
            "Book 38",
            "Book 39",
            "Book 41",
            "Book 42",
            "Book 43",
            "Book 44",
            "Book 45",
            "Book 46",
            "Book 47",
            "Book 49",
            "Book 50",
            "Book 51",
            "Book 53",
            "Book 54",
            "Book 55",
            "Book 56",
        ]

    @functools.cached_property
    def tutorial_levels(self) -> List[str]:
        return [
            "Book 1 - Puzzle 1",
            "Book 1 - Puzzle 2",
            "Book 1 - Puzzle 3",
            "Book 2 - Puzzle 1",
            "Book 2 - Puzzle 2",
            "Book 2 - Puzzle 3",
            "Book 3 - Puzzle 1",
            "Book 3 - Puzzle 2",
            "Book 3 - Puzzle 3",
            "Book 3 - Puzzle 4"
        ]
    
    @functools.cached_property
    def tutorial_books(self) -> List[str]:
        return [
            "Book 1",
            "Book 2",
            "Book 3"
        ]

    @functools.cached_property
    def time_levels(self) -> List[str]:
        return [
            "Book 12 - Puzzle 1",
            "Book 12 - Puzzle 2",
            "Book 12 - Puzzle 3",
            "Book 12 - Puzzle 4",
            "Book 12 - Puzzle 5",
            "Book 36 - Puzzle 1",
            "Book 36 - Puzzle 2",
            "Book 36 - Puzzle 3",
            "Book 36 - Puzzle 4",
            "Book 36 - Puzzle 5"
        ]
    
    @functools.cached_property
    def time_books(self) -> List[str]:
        return [
            "Book 12",
            "Book 36"
        ]

    @functools.cached_property
    def chance_levels(self) -> List[str]:
        return [
            "Book 20 - Puzzle 1",
            "Book 20 - Puzzle 2",
            "Book 20 - Puzzle 3",
            "Book 20 - Puzzle 4",
            "Book 20 - Puzzle 5",
            "Book 48 - Puzzle 1",
            "Book 48 - Puzzle 2",
            "Book 48 - Puzzle 3",
            "Book 48 - Puzzle 4",
            "Book 48 - Puzzle 5"
        ]

    @functools.cached_property
    def chance_books(self) -> List[str]:
        return [
            "Book 20",
            "Book 48"
        ]
    
    @functools.cached_property
    def construct_levels(self) -> List[str]:
        return [
            "Book 16 - Puzzle 1",
            "Book 16 - Puzzle 2",
            "Book 16 - Puzzle 3",
            "Book 16 - Puzzle 4",
            "Book 16 - Puzzle 5",
            "Book 16 - Puzzle 6",
            "Book 16 - Puzzle 7",
            "Book 16 - Puzzle 8",
            "Book 16 - Puzzle 9",
            "Book 24 - Puzzle 1",
            "Book 24 - Puzzle 2",
            "Book 24 - Puzzle 3",
            "Book 24 - Puzzle 4",
            "Book 24 - Puzzle 5",
            "Book 24 - Puzzle 6",
            "Book 24 - Puzzle 7",
            "Book 24 - Puzzle 8",
            "Book 24 - Puzzle 9",
            "Book 24 - Puzzle 10",
            "Book 24 - Puzzle 11",
            "Book 24 - Puzzle 12",
            "Book 32 - Puzzle 1",
            "Book 32 - Puzzle 2",
            "Book 32 - Puzzle 3",
            "Book 32 - Puzzle 4",
            "Book 32 - Puzzle 5",
            "Book 32 - Puzzle 6",
            "Book 32 - Puzzle 7",
            "Book 32 - Puzzle 8",
            "Book 32 - Puzzle 9",
            "Book 32 - Puzzle 10",
            "Book 32 - Puzzle 11",
            "Book 32 - Puzzle 12",
            "Book 32 - Puzzle 13",
            "Book 40 - Puzzle 1",
            "Book 40 - Puzzle 2",
            "Book 40 - Puzzle 3",
            "Book 40 - Puzzle 4",
            "Book 40 - Puzzle 5",
            "Book 40 - Puzzle 6",
            "Book 40 - Puzzle 7",
            "Book 40 - Puzzle 8",
            "Book 40 - Puzzle 9",
            "Book 40 - Puzzle 10",
            "Book 40 - Puzzle 11",
            "Book 40 - Puzzle 12",
            "Book 40 - Puzzle 13",
            "Book 40 - Puzzle 14",
            "Book 40 - Puzzle 15",
            "Book 52 - Puzzle 1",
            "Book 52 - Puzzle 2",
            "Book 52 - Puzzle 3",
            "Book 52 - Puzzle 4",
            "Book 52 - Puzzle 5",
            "Book 52 - Puzzle 6",
            "Book 52 - Puzzle 7",
            "Book 52 - Puzzle 8",
            "Book 52 - Puzzle 9",
            "Book 52 - Puzzle 10",
            "Book 52 - Puzzle 11",
            "Book 52 - Puzzle 12",
            "Book 52 - Puzzle 13",
            "Book 52 - Puzzle 14"
        ]

    @functools.cached_property
    def construct_books(self) -> List[str]:
        return [
            "Book 16",
            "Book 24",
            "Book 32",
            "Book 40",
            "Book 52"
        ]

    def levels(self) -> List[str]:
        levellist: List[str] = self.normal_levels[:]
        if self.include_tutorial_levels:
            levellist.extend(self.tutorial_levels[:])
        if self.include_time_challenges:
            levellist.extend(self.time_levels[:])
        if self.include_one_chance_challenges:
            levellist.extend(self.chance_levels[:])
        if self.include_construction_challenges:
            levellist.extend(self.construct_levels[:])
        return levellist

    def books(self) -> List[str]:
        booklist: List[str] = self.normal_books[:]
        if self.include_tutorial_levels:
            booklist.extend(self.tutorial_books[:])
        if self.include_time_challenges:
            booklist.extend(self.time_books[:])
        if self.include_one_chance_challenges:
            booklist.extend(self.chance_books[:])
        if self.include_construction_challenges:
            booklist.extend(self.construct_books[:])
        return booklist

    @property
    def include_tutorial_levels(self) -> bool:
        return bool(self.archipelago_options.picross_3d_round2_include_tutorial_levels.value)

    @property
    def include_time_challenges(self) -> bool:
        return bool(self.archipelago_options.picross_3d_round2_include_time_challenges.value)

    @property
    def include_one_chance_challenges(self) -> bool:
        return bool(self.archipelago_options.picross_3d_round2_include_one_chance_challenges.value)

    @property
    def include_construction_challenges(self) -> bool:
        return bool(self.archipelago_options.picross_3d_round2_include_construction_challenges.value)

# Archipelago Options
class Picross3dRound2IncludeTutorialLevels(Toggle):
    """
    Indicates whether to include Tutorial levels (Books 1 through 3)
    """

    display_name = "Picross 3D Round 2 Include Tutorial Levels"

class Picross3dRound2IncludeTimeChallenges(DefaultOnToggle):
    """
    Indicates whether to include Time challenges (Books 12 and 36).
    """

    display_name = "Picross 3D Round 2 Include Time Challenges"

class Picross3dRound2IncludeOneChanceChallenges(DefaultOnToggle):
    """
    Indicates whether to include One Chance challenges (Books 20 and 48).
    """

    display_name = "Picross 3D Round 2 Include One Chance Challenges"

class Picross3dRound2IncludeConstructionChallenges(DefaultOnToggle):
    """
    Indicates whether to include Construction challenges (Books 16, 24, 32, 40, and 52).
    """

    display_name = "Picross 3D Round 2 Include Construction Challenges"
