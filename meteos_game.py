from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, Choice

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


# Option Dataclass
@dataclass
class MeteosArchipelagoOptions:
    meteos_include_hard_mode: MeteosIncludeHardMode
    meteos_planet_names: MeteosNames

# Main Class
class MeteosGame(Game):
    name = "Meteos"
    platform = KeymastersKeepGamePlatforms.NDS

    is_adult_only_or_unrated = False

    options_cls = MeteosArchipelagoOptions

    # Optional Game Constraints
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Use at least STARS stars in difficulty and CPU level instead",
                data={
                    "STARS": (self.hard_stars, 1),
                },
            ),
            GameObjectiveTemplate(
                label="In Star Trip mode, do not continue when facing annihilation",
                data= dict(),
            ),
        ]

    # Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="As PLANET, beat OPPONENT with at least DIFF stars of difficulty and CPUSTA stars of CPU level",
                data={
                    "PLANET": (self.planets, 1),
                    "OPPONENT": (self.planets, 1),
                    "DIFF": (self.stars, 1),
                    "CPUSTA": (self.stars, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="As PLANET, beat OPPONENT with at least DIFF stars of difficulty and CPUSTA stars of CPU level",
                data={
                    "PLANET": (self.planets, 1),
                    "OPPONENT": (self.planets, 2),
                    "DIFF": (self.stars, 1),
                    "CPUSTA": (self.stars, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="As PLANET, beat OPPONENT with at least DIFF stars of difficulty and CPUSTA stars of CPU level",
                data={
                    "PLANET": (self.planets, 1),
                    "OPPONENT": (self.planets, 3),
                    "DIFF": (self.stars, 1),
                    "CPUSTA": (self.stars, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="In Star Trip mode, win as PLANET in straight mode with at least STARS stars of difficulty",
                data={
                    "PLANET": (self.planets, 1),
                    "STARS": (self.stars, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="In Star Trip mode, win as PLANET in branch mode with at least STARS stars of difficulty and get ending ENDING",
                data={
                    "PLANET": (self.planets, 1),
                    "STARS": (self.stars, 1),
                    "ENDING": (self.endings, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="In Star Trip mode, win as PLANET in multi mode with at least STARS stars of difficulty",
                data={
                    "PLANET": (self.planets, 1),
                    "STARS": (self.stars, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="In Star Trip mode, win as PLANET in multi mode with at least STARS stars of difficulty and defeat True Meteo",
                data={
                    "PLANET": (self.planets, 1),
                    "STARS": (self.stars, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="In Deluge mode, get as least SCORE points with PLANET",
                data={
                    "SCORE": (self.score, 1),
                    "PLANET": (self.planets, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=9,
            )
        ]
    
    def stars(self) -> range:
        if self.include_hard_mode:
            return range(1, 6)
        else:
            return range(1, 4)

    @staticmethod
    def hard_stars() -> range:
        return range(4, 6)
    
    def score(self) -> range:
        return range(50000, 160000 if self.include_hard_mode else 110000, 10000)

    @functools.cached_property
    def planets_normal(self) -> List[str]:
        return  [
            "Anasaze",
            "Oleana",
            "Hevendor",
            "Megadom",
            "Mekks",
            "Bavoom",
            "Forte",
            "Gravitas",
            "Luna=Luna",
            "Globin",
            "Florias",
            "Suburbion",
            "Meteo"
        ]
    
    @functools.cached_property
    def planets_ntsc(self) -> List[str]:
        return [
            "Geolyte",
            "Firim",
            "Freaze",
            "Boggob",
            "Grannest",
            "Dawndus",
            "Gigagush",
            "Layazero",
            "Jeljel",
            "Brabbit",
            "Wiral",
            "Yooj",
            "Hotted",
            "Vubble",
            "Lastar",
            "Thirnova",
            "Cavious",
            "Wuud",
            "Starrii",
        ]
    
    @functools.cached_property
    def planets_pal(self) -> List[str]:
        return [
            "Geolitia",
            "Ignius",
            "Polaria",
            "Perilia",
            "Smogor",
            "Isomnis",
            "Vortinia",
            "Holozero",
            "Magmor",
            "Aetheria",
            "Neuralis",
            "Gigantis",
            "Pyros",
            "Sferia",
            "Candelor",
            "Trinova",
            "Cavernis",
            "Arborea",
            "Stellis",
        ]

    def planets(self) -> List[str]:
        planets: List[str] = self.planets_normal[:]

        if self.use_pal_names:
            planets.extend(self.planets_pal[:])
        else:
            planets.extend(self.planets_ntsc[:])

        return sorted(planets)

    @staticmethod
    def endings() -> List[str]:
        return [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G"
        ]

    @property
    def use_pal_names(self) -> bool:
        return bool(self.archipelago_options.meteos_planet_names.value == MeteosNames.option_pal)
    
    @property
    def include_hard_mode(self) -> bool:
        return bool(self.archipelago_options.meteos_include_hard_mode.value)


# Archipelago Options
class MeteosIncludeHardMode(Toggle):
    """
    Indicates whether to include the possibility of getting 4 or 5 star difficulty requirements, as well as harder Deluge goals when generating Meteos objectives.
    """

    display_name = "Meteos Include Hard Mode"

class MeteosNames(Choice):
    """
    Indicates whether to use NTSC or PAL names for Meteos planets with different names.
    """
    display_name = "Meteos Use PAL Names"
    option_ntsc = 0
    option_pal = 1
    default = 0