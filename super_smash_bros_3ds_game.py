from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import OptionSet, Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class SuperSmashBros3dsArchipelagoOptions:
    super_smash_bros_3ds_dlc_characters: SuperSmashBros3dsDLCOwnedCharacters
    super_smash_bros_3ds_dlc_stages: SuperSmashBros3dsDLCOwnedStages
    super_smash_bros_3ds_hard_mode: SuperSmashBros3dsHardMode


class SuperSmashBros3dsGame(Game):
    name = "Super Smash Bros. 3DS"
    platform = KeymastersKeepGamePlatforms._3DS

    platforms_other = None

    is_adult_only_or_unrated = False

    options_cls = SuperSmashBros3dsArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Select CPU Level LEVEL instead (when applicable)",
                data={
                    "LEVEL": (self.hard_cpu_level_range, 1),
                },
            ),
            GameObjectiveTemplate(
                label="Don't Continue (when applicable)",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label="Play with competitive settings (No Items, 3 Stocks) (when applicable)",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label="Play with assist trophies active (when applicable)",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label="Play with Pokeballs and Master Balls active (when applicable)",
                data=dict(),
            ),
            GameObjectiveTemplate(
                label="Play with all items active (when applicable)",
                data=dict(),
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Win a 1 vs 1 Smash MODE as CHARACTER against a level LEVEL OPPONENT in STAGE",
                data={
                    "MODE": (self.vs_battle_modes, 1),
                    "CHARACTER": (self.characters, 1),
                    "OPPONENT": (self.characters, 1),
                    "STAGE": (self.stages, 1),
                    "LEVEL": (self.cpu_level_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=125,
            ),
            GameObjectiveTemplate(
                label="Win a Free For All MODE as CHARACTER against level LEVEL OPPONENTS in STAGE",
                data={
                    "MODE": (self.vs_battle_modes, 1),
                    "CHARACTER": (self.characters, 1),
                    "OPPONENTS": (self.characters, 3),
                    "STAGE": (self.stages, 1),
                    "LEVEL": (self.cpu_level_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=125,
            ),
            GameObjectiveTemplate(
                label="Win a Team Battle MODE with a team of CHARACTERS against level LEVEL OPPONENTS in STAGE",
                data={
                    "MODE": (self.vs_battle_modes, 1),
                    "CHARACTERS": (self.characters, 2),
                    "OPPONENTS": (self.characters, 2),
                    "STAGE": (self.stages, 1),
                    "LEVEL": (self.cpu_level_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=125,
            ),
            GameObjectiveTemplate(
                label="Win a Team Battle MODE as CHARACTER against level LEVEL OPPONENTS in STAGE",
                data={
                    "MODE": (self.vs_battle_modes, 1),
                    "CHARACTER": (self.characters, 1),
                    "OPPONENTS": (self.characters, 3),
                    "STAGE": (self.stages, 1),
                    "LEVEL": (self.cpu_level_range, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=125,
            ),
            GameObjectiveTemplate(
                label="Complete MODE as CHARACTER",
                data={
                    "MODE": (self.singleplayer_modes, 1),
                    "CHARACTER": (self.characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=167,
            ),
            GameObjectiveTemplate(
                label="Complete Smash Run with CHARACTER against level LEVEL opponents",
                data={
                    "CHARACTER": (self.characters, 1),
                    "LEVEL": (self.cpu_level_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=83,
            ),
            GameObjectiveTemplate(
                label="Get METERS m with CHARACTER in Home-Run Contest",
                data={
                    "CHARACTER": (self.characters, 1),
                    "METERS": (self.home_run, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=60,
            ),
            GameObjectiveTemplate(
                label="Get POINTS points with CHARACTER in Target Blast",
                data={
                    "CHARACTER": (self.characters, 1),
                    "POINTS": (self.target_blast, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=60,
            ),
            GameObjectiveTemplate(
                label ="Win 10-Man Smash with CHARACTER in SECONDS seconds",
                data={
                    "CHARACTER": (self.characters, 1),
                    "SECONDS": (self.ten_man, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            ),
            GameObjectiveTemplate(
                label ="Win 100-Man Smash with CHARACTER in SECONDS",
                data={
                    "CHARACTER": (self.characters, 1),
                    "SECONDS": (self.time_stamps, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            ),
            GameObjectiveTemplate(
                label ="Get POINTS KOs with CHARACTER in 3-Minute Smash",
                data={
                    "CHARACTER": (self.characters, 1),
                    "POINTS": (self.kos, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            ),
            GameObjectiveTemplate(
                label ="Get POINTS points with CHARACTER in Rival Smash",
                data={
                    "CHARACTER": (self.characters, 1),
                    "POINTS": (self.kos, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            ),
            GameObjectiveTemplate(
                label ="Get POINTS KOs with CHARACTER in Infinite Smash",
                data={
                    "CHARACTER": (self.characters, 1),
                    "POINTS": (self.kos, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            ),
            GameObjectiveTemplate(
                label ="Get POINTS KOs with CHARACTER in Cruel Smash",
                data={
                    "CHARACTER": (self.characters, 1),
                    "POINTS": (self.cruel, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=20,
            )
        ]

        return templates

    @functools.cached_property
    def characters_base(self) -> List[str]:
        return [
            "Mario",
            "Luigi",
            "Peach",
            "Bowser",
            "Dr. Mario",
            "Yoshi",
            "Donkey Kong",
            "Diddy Kong",
            "Link",
            "Toon Link",
            "Zelda",
            "Sheik",
            "Ganondorf",
            "Samus",
            "Zero Suit Samus",
            "Kirby",
            "Meta Knight",
            "King Dedede",
            "Fox",
            "Falco",
            "Pikachu",
            "Jigglypuff",
            "Charizard",
            "Lucario",
            "Greninja",
            "Captain Falcon",
            "Little Mac",
            "Wii Fit Trainer",
            "Ness",
            "Marth",
            "Ike",
            "Robin",
            "Mr. Game & Watch",
            "Pit",
            "Wario",
            "Olimar",
            "Palutena",
            "R.O.B.",
            "Sonic",
            "Rosalinea & Luma",
            "Bowser Jr.",
            "Lucina",
            "Dark Pit",
            "Shulk",
            "Villager",
            "Duck Hunt",
            "Mega Man",
            "Pac-Man"
            "Mii Brawler",
            "Mii Swordfighter",
            "Mii Gunner",
        ]

    def characters(self) -> List[str]:
        characters: List[str] = self.characters_base[:]
        characters.extend(self.dlc_characters[:])

        return sorted(characters)

    @functools.cached_property
    def stages_base(self) -> List[str]:
        return [
            "Battlefield",
            "Final Destination",
            "3D Land",
            "Golden Plains",
            "Rainbow Road",
            "Paper Mario",
            "Gerudo Valley",
            "Spirit Train",
            "Dream Land",
            "Unova Pokémon League",
            "Prism Tower",
            "Mute City",
            "Magicant",
            "Arena Ferox",
            "Reset Bomb Forest",
            "Tortimer Island",
            "Boxing Ring",
            "Gaur Plain",
            "Duck Hunt",
            "Wily Castle",
            "Pac-Maze",
            "PictoChat 2",
            "Balloon Fight",
            "Living Room",
            "Find Mii",
            "Tomodachi Life",
            "Mushroomy Kingdom",
            "Yoshi's Island",
            "Jungle Japes",
            "Brinstar",
            "Corneria",
            "Flat Zone 2",
            "WarioWare, Inc.",
            "Distant Planet",
            "Green Hill Zone",
        ]

    def stages(self) -> List[str]:
        stages: List[str] = self.stages_base[:]

        stages.extend(self.dlc_stages[:])

        return sorted(stages)

    def cpu_level_range(self) -> range:
        return range(4 if self.is_hard_mode else 1, 10 if self.is_hard_mode else 7)

    @staticmethod
    def hard_cpu_level_range() -> range:
        return range(7, 10)
    
    @staticmethod
    def home_run() -> range:
        return range(300, 501, 50)
    
    @staticmethod
    def target_blast() -> range:
        return range(120000, 200010, 10)

    @staticmethod
    def ten_man() -> range:
        return range(25, 61)

    @staticmethod
    def kos() -> range:
        return range(60, 91)
    
    @staticmethod
    def rival() -> range:
        return range(14, 31)

    @staticmethod
    def cruel() -> range:
        return range(1, 4)

    @staticmethod
    def singleplayer_modes() -> List[str]:
        return [
            "Classic Mode",
            "All-Star Smash"
        ]

    @staticmethod
    def vs_battle_modes() -> List[str]:
        return [
            "Time Battle",
            "Stock Battle"
        ]

    @staticmethod
    def time_stamps() -> List[str]:
        return [f"{x//60}:{(x%60):02d}" for x in range(180,301)]
    
    @property
    def dlc_characters(self) -> List[str]:
        return sorted(self.archipelago_options.super_smash_bros_3ds_dlc_characters.value)
    
    @property
    def dlc_stages(self) -> List[str]:
        return sorted(self.archipelago_options.super_smash_bros_3ds_dlc_stages.value)

    @property
    def is_hard_mode(self) -> bool:
        return bool(self.archipelago_options.super_smash_bros_3ds_hard_mode.value)


# Archipelago Options
class SuperSmashBros3dsDLCOwnedCharacters(OptionSet):
    """
    Indicates which Super Smash Bros. Ultimate DLC characters the player owns, if any.
    """

    display_name = "Super Smash Bros. 3DS DLC Characters Owned"
    valid_keys = [
        "Lucas",
        "Mewtwo",
        "Roy",
        "Ryu",
        "Cloud",
        "Corrin",
        "Bayonetta",
    ]

    default = valid_keys

class SuperSmashBros3dsDLCOwnedStages(OptionSet):
    """
    Indicates which Super Smash Bros. Ultimate DLC stages the player owns, if any.
    """

    display_name = "Super Smash Bros. 3DS DLC Stages Owned"
    valid_keys = [
        "Super Mario Maker",
        "Suzaku Castle",
        "Midgar",
        "Umbra Clock Tower",
        "Peach's Castle (64)",
        "Hyrule Castle (64)",
        "Dream Land (64)",
    ]

    default = valid_keys

class SuperSmashBros3dsHardMode(Toggle):
    """
    Indicates whether to include harder CPU levels. Normal mode CPU level range is 1-6, while hard mode is 4-9
    """

    display_name = "Super Smash Bros. 3DS Hard Mode"