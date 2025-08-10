from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import OptionSet, DefaultOnToggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


# Option Dataclass
@dataclass
class Picross3dArchipelagoOptions:
    picross_3d_difficulties: Picross3dDifficulties
    picross_3d_include_time_challenges: Picross3dIncludeTimeChallenges
    picross_3d_include_one_chance_challenges: Picross3dIncludeOneChanceChallenges
    picross_3d_include_construction_challenges: Picross3dIncludeConstructionChallenges

# Main Class
class Picross3dGame(Game):
    name = "Picross 3D"
    platform = KeymastersKeepGamePlatforms.NDS

    is_adult_only_or_unrated = False

    options_cls = Picross3dArchipelagoOptions

    # Optional Game Constraints
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Get 3 stars",
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
                label="Beat LEVEL and get at least MEDAL star(s)",
                data={
                    "LEVEL": (self.puzzles, 1),
                    "MEDAL": (self.stars, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Beat all puzzles of LEVEL",
                data={
                    "LEVEL": (self.levels, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
        ]
    
    @staticmethod
    def stars() -> range:
        return range(1, 4)

    @functools.cached_property
    def normal_levels(self) -> List[str]:
        return [
            "Tutorial - How to play-A",
            "Tutorial - How to play-B",
            "Tutorial - How to play-C",
            "Tutorial - Circles-A",
            "Tutorial - Circles-B",
            "Tutorial - Circles-C",
            "Tutorial - Level 1-A",
            "Tutorial - Level 1-B",
            "Tutorial - Level 1-C",
            "Tutorial - Level 1-D",
            "Tutorial - Level 1-E",
            "Tutorial - Techniques-A",
            "Tutorial - Techniques-B",
            "Tutorial - Techniques-C",
            "Tutorial - Level 2-A",
            "Tutorial - Level 2-B",
            "Tutorial - Level 2-C",
            "Tutorial - Level 2-D",
            "Tutorial - Level 2-E",
            "Tutorial - Level 3-A",
            "Tutorial - Level 3-B",
            "Tutorial - Level 3-C",
            "Tutorial - Level 3-D",
            "Tutorial - Level 3-Silver",
            "Tutorial - Large Puzzles-A",
            "Tutorial - Large Puzzles-B",
            "Tutorial - Level 4-A",
            "Tutorial - Level 4-B",
            "Tutorial - Level 4-C",
            "Tutorial - Level 4-D",
            "Tutorial - Level 4-Silver",
            "Tutorial - Squares-A",
            "Tutorial - Squares-B",
            "Tutorial - Level 5-A",
            "Tutorial - Level 5-B",
            "Tutorial - Level 5-C",
            "Tutorial - Level 5-D",
            "Tutorial - Level 5-Silver",
            "Easy - Level 1-A",
            "Easy - Level 1-B",
            "Easy - Level 1-C",
            "Easy - Level 1-D",
            "Easy - Level 1-E",
            "Easy - Level 1-F",
            "Easy - Level 1-G",
            "Easy - Level 1-H",
            "Easy - Level 1-Silver",
            "Easy - Level 1-Gold",
            "Easy - Level 2-A",
            "Easy - Level 2-B",
            "Easy - Level 2-C",
            "Easy - Level 2-D",
            "Easy - Level 2-E",
            "Easy - Level 2-F",
            "Easy - Level 2-G",
            "Easy - Level 2-H",
            "Easy - Level 2-Silver",
            "Easy - Level 2-Gold",
            "Easy - Level 3-A",
            "Easy - Level 3-B",
            "Easy - Level 3-C",
            "Easy - Level 3-D",
            "Easy - Level 3-E",
            "Easy - Level 3-F",
            "Easy - Level 3-G",
            "Easy - Level 3-H",
            "Easy - Level 3-Silver",
            "Easy - Level 3-Gold",
            "Easy - Level 4-A",
            "Easy - Level 4-B",
            "Easy - Level 4-C",
            "Easy - Level 4-D",
            "Easy - Level 4-E",
            "Easy - Level 4-F",
            "Easy - Level 4-G",
            "Easy - Level 4-H",
            "Easy - Level 4-Silver",
            "Easy - Level 4-Gold",
            "Easy - Level 5-A",
            "Easy - Level 5-B",
            "Easy - Level 5-C",
            "Easy - Level 5-D",
            "Easy - Level 5-E",
            "Easy - Level 5-F",
            "Easy - Level 5-G",
            "Easy - Level 5-H",
            "Easy - Level 5-Silver",
            "Easy - Level 5-Gold",
            "Easy - Level 6-A",
            "Easy - Level 6-B",
            "Easy - Level 6-C",
            "Easy - Level 6-D",
            "Easy - Level 6-E",
            "Easy - Level 6-F",
            "Easy - Level 6-G",
            "Easy - Level 6-H",
            "Easy - Level 6-Silver",
            "Easy - Level 6-Gold",
            "Easy - Level 7-A",
            "Easy - Level 7-B",
            "Easy - Level 7-C",
            "Easy - Level 7-D",
            "Easy - Level 7-E",
            "Easy - Level 7-F",
            "Easy - Level 7-G",
            "Easy - Level 7-H",
            "Easy - Level 7-Silver",
            "Easy - Level 7-Gold",
            "Easy - Level 8-A",
            "Easy - Level 8-B",
            "Easy - Level 8-C",
            "Easy - Level 8-D",
            "Easy - Level 8-E",
            "Easy - Level 8-F",
            "Easy - Level 8-G",
            "Easy - Level 8-H",
            "Easy - Level 8-Silver",
            "Easy - Level 8-Gold",
            "Easy - Level 9-A",
            "Easy - Level 9-B",
            "Easy - Level 9-C",
            "Easy - Level 9-D",
            "Easy - Level 9-E",
            "Easy - Level 9-F",
            "Easy - Level 9-G",
            "Easy - Level 9-H",
            "Easy - Level 9-Silver",
            "Easy - Level 9-Gold",
            "Easy - Level 10-A",
            "Easy - Level 10-B",
            "Easy - Level 10-C",
            "Easy - Level 10-D",
            "Easy - Level 10-E",
            "Easy - Level 10-F",
            "Easy - Level 10-G",
            "Easy - Level 10-H",
            "Easy - Level 10-Silver",
            "Easy - Level 10-Gold",
            "Normal - Level 1-A",
            "Normal - Level 1-B",
            "Normal - Level 1-C",
            "Normal - Level 1-D",
            "Normal - Level 1-E",
            "Normal - Level 1-F",
            "Normal - Level 1-G",
            "Normal - Level 1-H",
            "Normal - Level 1-Silver",
            "Normal - Level 1-Gold",
            "Normal - Level 2-A",
            "Normal - Level 2-B",
            "Normal - Level 2-C",
            "Normal - Level 2-D",
            "Normal - Level 2-E",
            "Normal - Level 2-F",
            "Normal - Level 2-G",
            "Normal - Level 2-H",
            "Normal - Level 2-Silver",
            "Normal - Level 2-Gold",
            "Normal - Level 3-A",
            "Normal - Level 3-B",
            "Normal - Level 3-C",
            "Normal - Level 3-D",
            "Normal - Level 3-E",
            "Normal - Level 3-F",
            "Normal - Level 3-G",
            "Normal - Level 3-H",
            "Normal - Level 3-Silver",
            "Normal - Level 3-Gold",
            "Normal - Level 4-A",
            "Normal - Level 4-B",
            "Normal - Level 4-C",
            "Normal - Level 4-D",
            "Normal - Level 4-E",
            "Normal - Level 4-F",
            "Normal - Level 4-G",
            "Normal - Level 4-H",
            "Normal - Level 4-Silver",
            "Normal - Level 4-Gold",
            "Normal - Level 5-A",
            "Normal - Level 5-B",
            "Normal - Level 5-C",
            "Normal - Level 5-D",
            "Normal - Level 5-E",
            "Normal - Level 5-F",
            "Normal - Level 5-G",
            "Normal - Level 5-H",
            "Normal - Level 5-Silver",
            "Normal - Level 5-Gold",
            "Normal - Level 6-A",
            "Normal - Level 6-B",
            "Normal - Level 6-C",
            "Normal - Level 6-D",
            "Normal - Level 6-E",
            "Normal - Level 6-F",
            "Normal - Level 6-G",
            "Normal - Level 6-H",
            "Normal - Level 6-Silver",
            "Normal - Level 6-Gold",
            "Normal - Level 7-A",
            "Normal - Level 7-B",
            "Normal - Level 7-C",
            "Normal - Level 7-D",
            "Normal - Level 7-E",
            "Normal - Level 7-F",
            "Normal - Level 7-G",
            "Normal - Level 7-H",
            "Normal - Level 7-Silver",
            "Normal - Level 7-Gold",
            "Normal - Level 8-A",
            "Normal - Level 8-B",
            "Normal - Level 8-C",
            "Normal - Level 8-D",
            "Normal - Level 8-E",
            "Normal - Level 8-F",
            "Normal - Level 8-G",
            "Normal - Level 8-H",
            "Normal - Level 8-Silver",
            "Normal - Level 8-Gold",
            "Normal - Level 9-A",
            "Normal - Level 9-B",
            "Normal - Level 9-C",
            "Normal - Level 9-D",
            "Normal - Level 9-E",
            "Normal - Level 9-F",
            "Normal - Level 9-G",
            "Normal - Level 9-H",
            "Normal - Level 9-Silver",
            "Normal - Level 9-Gold",
            "Normal - Level 10-A",
            "Normal - Level 10-B",
            "Normal - Level 10-C",
            "Normal - Level 10-D",
            "Normal - Level 10-E",
            "Normal - Level 10-F",
            "Normal - Level 10-G",
            "Normal - Level 10-H",
            "Normal - Level 10-Silver",
            "Normal - Level 10-Gold",
            "Hard - Level 1-A",
            "Hard - Level 1-B",
            "Hard - Level 1-C",
            "Hard - Level 1-D",
            "Hard - Level 1-E",
            "Hard - Level 1-F",
            "Hard - Level 1-G",
            "Hard - Level 1-H",
            "Hard - Level 1-Silver",
            "Hard - Level 1-Gold",
            "Hard - Level 2-A",
            "Hard - Level 2-B",
            "Hard - Level 2-C",
            "Hard - Level 2-D",
            "Hard - Level 2-E",
            "Hard - Level 2-F",
            "Hard - Level 2-G",
            "Hard - Level 2-H",
            "Hard - Level 2-Silver",
            "Hard - Level 2-Gold",
            "Hard - Level 3-A",
            "Hard - Level 3-B",
            "Hard - Level 3-C",
            "Hard - Level 3-D",
            "Hard - Level 3-E",
            "Hard - Level 3-F",
            "Hard - Level 3-G",
            "Hard - Level 3-H",
            "Hard - Level 3-Silver",
            "Hard - Level 3-Gold",
            "Hard - Level 4-A",
            "Hard - Level 4-B",
            "Hard - Level 4-C",
            "Hard - Level 4-D",
            "Hard - Level 4-E",
            "Hard - Level 4-F",
            "Hard - Level 4-G",
            "Hard - Level 4-H",
            "Hard - Level 4-Silver",
            "Hard - Level 4-Gold",
            "Hard - Level 5-A",
            "Hard - Level 5-B",
            "Hard - Level 5-C",
            "Hard - Level 5-D",
            "Hard - Level 5-E",
            "Hard - Level 5-F",
            "Hard - Level 5-G",
            "Hard - Level 5-H",
            "Hard - Level 5-Silver",
            "Hard - Level 5-Gold",
            "Hard - Level 6-A",
            "Hard - Level 6-B",
            "Hard - Level 6-C",
            "Hard - Level 6-D",
            "Hard - Level 6-E",
            "Hard - Level 6-F",
            "Hard - Level 6-G",
            "Hard - Level 6-H",
            "Hard - Level 6-Silver",
            "Hard - Level 6-Gold",
            "Hard - Level 7-A",
            "Hard - Level 7-B",
            "Hard - Level 7-C",
            "Hard - Level 7-D",
            "Hard - Level 7-E",
            "Hard - Level 7-F",
            "Hard - Level 7-G",
            "Hard - Level 7-H",
            "Hard - Level 7-Silver",
            "Hard - Level 7-Gold",
            "Hard - Level 8-A",
            "Hard - Level 8-B",
            "Hard - Level 8-C",
            "Hard - Level 8-D",
            "Hard - Level 8-E",
            "Hard - Level 8-F",
            "Hard - Level 8-G",
            "Hard - Level 8-H",
            "Hard - Level 8-Silver",
            "Hard - Level 8-Gold",
            "Hard - Level 9-A",
            "Hard - Level 9-B",
            "Hard - Level 9-C",
            "Hard - Level 9-D",
            "Hard - Level 9-E",
            "Hard - Level 9-F",
            "Hard - Level 9-G",
            "Hard - Level 9-H",
            "Hard - Level 9-Silver",
            "Hard - Level 9-Gold",
            "Hard - Level 10-A",
            "Hard - Level 10-B",
            "Hard - Level 10-C",
            "Hard - Level 10-D",
            "Hard - Level 10-E",
            "Hard - Level 10-F",
            "Hard - Level 10-G",
            "Hard - Level 10-H",
            "Hard - Level 10-Silver",
            "Hard - Level 10-Gold"
        ]

    @functools.cached_property
    def normal_books(self) -> List[str]:
        return [
            "Tutorial - How to play",
            "Tutorial - Circles",
            "Tutorial - Level 1",
            "Tutorial - Techniques",
            "Tutorial - Level 2",
            "Tutorial - Level 3",
            "Tutorial - Large Puzzles",
            "Tutorial - Level 4",
            "Tutorial - Squares",
            "Tutorial - Level 5",
            "Easy - Level 1",
            "Easy - Level 2",
            "Easy - Level 3",
            "Easy - Level 4",
            "Easy - Level 5",
            "Easy - Level 6",
            "Easy - Level 7",
            "Easy - Level 8",
            "Easy - Level 9",
            "Easy - Level 10",
            "Normal - Level 1",
            "Normal - Level 2",
            "Normal - Level 3",
            "Normal - Level 4",
            "Normal - Level 5",
            "Normal - Level 6",
            "Normal - Level 7",
            "Normal - Level 8",
            "Normal - Level 9",
            "Normal - Level 10",
            "Hard - Level 1",
            "Hard - Level 2",
            "Hard - Level 3",
            "Hard - Level 4",
            "Hard - Level 5",
            "Hard - Level 6",
            "Hard - Level 7",
            "Hard - Level 8",
            "Hard - Level 9",
            "Hard - Level 10"
        ]

    @functools.cached_property
    def time_levels(self) -> List[str]:
        return [
            "Easy - Time Challenge 1-A",
            "Easy - Time Challenge 2-A",
            "Normal - Time Challenge 1-A",
            "Normal - Time Challenge 1-B",
            "Normal - Time Challenge 2-A",
            "Normal - Time Challenge 2-B",
            "Hard - Time Challenge 1-A",
            "Hard - Time Challenge 1-B",
            "Hard - Time Challenge 1-C",
            "Hard - Time Challenge 2-A",
            "Hard - Time Challenge 2-B",
            "Hard - Time Challenge 2-C"
        ]
    
    @functools.cached_property
    def time_books(self) -> List[str]:
        return [
            "Easy - Time Challenge 1",
            "Easy - Time Challenge 2",
            "Normal - Time Challenge 1",
            "Normal - Time Challenge 2",
            "Hard - Time Challenge 1",
            "Hard - Time Challenge 2"
        ]

    @functools.cached_property
    def chance_levels(self) -> List[str]:
        return [
            "Tutorial - One Chance Challenge-A",
            "Easy - One Chance Challenge 1-A",
            "Easy - One Chance Challenge 2-A",
            "Normal - One Chance Challenge 1-A",
            "Normal - One Chance Challenge 1-B",
            "Normal - One Chance Challenge 2-A",
            "Normal - One Chance Challenge 2-B",
            "Hard - One Chance Challenge 1-A",
            "Hard - One Chance Challenge 1-B",
            "Hard - One Chance Challenge 1-C",
            "Hard - One Chance Challenge 2-A",
            "Hard - One Chance Challenge 2-B",
            "Hard - One Chance Challenge 2-C"
        ]

    @functools.cached_property
    def chance_books(self) -> List[str]:
        return [
            "Tutorial - One Chance Challenge",
            "Easy - One Chance Challenge 1",
            "Easy - One Chance Challenge 2",
            "Normal - One Chance Challenge 1",
            "Normal - One Chance Challenge 2",
            "Hard - One Chance Challenge 1",
            "Hard - One Chance Challenge 2"
        ]
    
    @functools.cached_property
    def construct_levels(self) -> List[str]:
        return [
            "Easy - Construction Challenge A-A",
            "Easy - Construction Challenge A-B",
            "Easy - Construction Challenge A-C",
            "Easy - Construction Challenge A-D",
            "Easy - Construction Challenge A-E",
            "Normal - Construction Challenge A-A",
            "Normal - Construction Challenge A-B",
            "Normal - Construction Challenge A-C",
            "Normal - Construction Challenge A-D",
            "Normal - Construction Challenge A-E",
            "Normal - Construction Challenge A-F",
            "Normal - Construction Challenge A-G",
            "Normal - Construction Challenge B-A",
            "Normal - Construction Challenge B-B",
            "Normal - Construction Challenge B-C",
            "Normal - Construction Challenge B-D",
            "Normal - Construction Challenge B-E",
            "Normal - Construction Challenge B-F",
            "Normal - Construction Challenge B-G",
            "Hard - Construction Challenge A-A",
            "Hard - Construction Challenge A-B",
            "Hard - Construction Challenge A-C",
            "Hard - Construction Challenge A-D",
            "Hard - Construction Challenge A-E",
            "Hard - Construction Challenge A-F",
            "Hard - Construction Challenge A-G",
            "Hard - Construction Challenge A-H",
            "Hard - Construction Challenge A-I",
            "Hard - Construction Challenge A-J",
            "Hard - Construction Challenge A-K",
            "Hard - Construction Challenge A-L",
            "Hard - Construction Challenge B-A",
            "Hard - Construction Challenge B-B",
            "Hard - Construction Challenge B-C",
            "Hard - Construction Challenge B-D",
            "Hard - Construction Challenge C-A",
            "Hard - Construction Challenge C-B",
            "Hard - Construction Challenge C-C",
            "Hard - Construction Challenge C-D",
            "Hard - Construction Challenge C-E",
            "Hard - Construction Challenge C-F",
            "Hard - Construction Challenge C-G",
            "Hard - Construction Challenge C-H",
            "Hard - Construction Challenge C-I",
            "Hard - Construction Challenge C-J",
            "Hard - Construction Challenge C-K"
        ]

    @functools.cached_property
    def construct_books(self) -> List[str]:
        return [
            "Easy - Construction Challenge A",
            "Normal - Construction Challenge A",
            "Normal - Construction Challenge B",
            "Hard - Construction Challenge A",
            "Hard - Construction Challenge B",
            "Hard - Construction Challenge C"
        ]

    def puzzles(self) -> List[str]:
        levellist: List[str] = self.normal_levels[:]
        if self.include_time_challenges:
            levellist.extend(self.time_levels[:])
        if self.include_one_chance_challenges:
            levellist.extend(self.chance_levels[:])
        if self.include_construction_challenges:
            levellist.extend(self.construct_levels[:])

        levellist = [level for level in levellist if any(level.startswith(difficulty) for difficulty in self.difficulties)]
        return levellist

    def levels(self) -> List[str]:
        booklist: List[str] = self.normal_books[:]
        if self.include_time_challenges:
            booklist.extend(self.time_books[:])
        if self.include_one_chance_challenges:
            booklist.extend(self.chance_books[:])
        if self.include_construction_challenges:
            booklist.extend(self.construct_books[:])

        booklist = [book for book in booklist if any(book.startswith(difficulty) for difficulty in self.difficulties)]
        return booklist

    @property
    def difficulties(self) -> List[str]:
        return sorted(self.archipelago_options.picross_3d_difficulties.value)

    @property
    def include_time_challenges(self) -> bool:
        return bool(self.archipelago_options.picross_3d_include_time_challenges.value)

    @property
    def include_one_chance_challenges(self) -> bool:
        return bool(self.archipelago_options.picross_3d_include_one_chance_challenges.value)

    @property
    def include_construction_challenges(self) -> bool:
        return bool(self.archipelago_options.picross_3d_include_construction_challenges.value)

# Archipelago Options
class Picross3dDifficulties(OptionSet):
    """
    Indicates which Picross 3D difficulty levels are available.
    """

    display_name = "Picross 3D Difficulty Levels"
    valid_keys = [
        "Tutorial",
        "Easy",
        "Normal",
        "Hard"
    ]

    default = valid_keys

class Picross3dIncludeTimeChallenges(DefaultOnToggle):
    """
    Indicates whether to include Time challenges (Books 12 and 36).
    """

    display_name = "Picross 3D Include Time Challenges"

class Picross3dIncludeOneChanceChallenges(DefaultOnToggle):
    """
    Indicates whether to include One Chance challenges (Books 20 and 48).
    """

    display_name = "Picross 3D Include One Chance Challenges"

class Picross3dIncludeConstructionChallenges(DefaultOnToggle):
    """
    Indicates whether to include Construction challenges (Books 16, 24, 32, 40, and 52).
    """

    display_name = "Picross 3D Include Construction Challenges"
