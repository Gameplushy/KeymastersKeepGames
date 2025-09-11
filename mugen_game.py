from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import OptionSet, OptionList, OptionError

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


# Option Dataclass
@dataclass
class MugenArchipelagoOptions:
    mugen_characters: MugenCharacters
    mugen_player_only_characters: MugenPlayerOnlyCharacters
    mugen_ai_only_characters: MugenAiOnlyCharacters
    mugen_stages: MugenStages

# Main Class
class MugenGame(Game):
    name = "M.U.G.E.N."
    platform = KeymastersKeepGamePlatforms.PC

    is_adult_only_or_unrated = False

    options_cls = MugenArchipelagoOptions

    # Optional Game Constraints
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Set HP to HEALTH%",
                data={
                    "HEALTH": (self.health, 1),
                },
            ),
            GameObjectiveTemplate(
                label="Set timer to TIMER",
                data={
                    "TIMER": (self.timer, 1),
                },
            ),
            GameObjectiveTemplate(
                label="Set timer to TIMER and HP to HEALTH%",
                data={
                    "TIMER": (self.timer, 1),
                    "HEALTH": (self.health, 1),
                },
            ),
        ]

    # Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives: List[GameObjectiveTemplate] = [            
            GameObjectiveTemplate(
                label="Win as PLAYER against OPPONENT in STAGE",
                data={
                    "PLAYER": (self.player_characters, 1),
                    "OPPONENT": (self.ai_characters, 1),
                    "STAGE": (self.stages, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=11,
            ),
            GameObjectiveTemplate(
                label="Win 5 rounds of survival mode with CHARACTER",
                data={
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win 5 rounds of survival mode with CHARACTER teaming with ALLY",
                data={
                    "CHARACTER": (self.player_characters, 1),
                    "ALLY": (self.all_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Finish Arcade mode with CHARACTER",
                data={
                    "CHARACTER": (self.player_characters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
        ]
        if(len(self.ai_characters())>=2):
            objectives.append(            
                GameObjectiveTemplate(
                    label="Win in a 2v2 simul battle as PLAYER with ALLY against OPPONENT in STAGE",
                    data={
                        "PLAYER": (self.player_characters, 1),
                        "ALLY": (self.all_characters, 1),
                        "OPPONENT": (self.ai_characters, 2),
                        "STAGE": (self.stages, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3,
                )
            )
            if(len(self.player_characters())>=2):
                objectives.append(
                    GameObjectiveTemplate(
                        label="Win in a 2v2 turns battle as PLAYERS against OPPONENT in STAGE",
                        data={
                            "PLAYERS": (self.player_characters, 2),
                            "OPPONENT": (self.ai_characters, 2),
                            "STAGE": (self.stages, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    )
                )
        if(len(self.player_characters())>=3):
            objectives.append(
                GameObjectiveTemplate(
                    label="Win 5 rounds of survival mode with a team of CHARACTER",
                    data={
                        "CHARACTER": (self.player_characters, 3),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                )
            )
            if(len(self.ai_characters())>=3):
                objectives.append(
                    GameObjectiveTemplate(
                        label="Win in a 3v3 turns battle as PLAYERS against OPPONENT in STAGE",
                        data={
                            "PLAYERS": (self.player_characters, 3),
                            "OPPONENT": (self.ai_characters, 3),
                            "STAGE": (self.stages, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    )
                )
        if(len(self.player_characters())>=4):
            objectives.append(
                GameObjectiveTemplate(
                    label="Win 5 rounds of survival mode with a team of CHARACTER",
                    data={
                        "CHARACTER": (self.player_characters, 4),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                )
            )
            if(len(self.ai_characters)>=4):
                objectives.append(
                    GameObjectiveTemplate(
                        label="Win in a 4v4 turns battle as PLAYERS against OPPONENT in STAGE",
                        data={
                            "PLAYERS": (self.player_characters, 4),
                            "OPPONENT": (self.ai_characters, 4),
                            "STAGE": (self.stages, 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=2,
                    )
                )
        return objectives
    
    def all_characters(self) -> List[str]:
        return self.mugen_characters[:]
    
    def player_characters(self) -> List[str]:
        characters: List[str] = self.mugen_characters[:]
        characters = [c for c in characters if c not in self.mugen_ai_only_characters]
        if(len(characters)==0):
            raise OptionError("No player characters available for M.U.G.E.N.")
        return characters

    def ai_characters(self) -> List[str]:
        characters: List[str] = self.mugen_characters[:]
        characters = [c for c in characters if c not in self.mugen_player_only_characters]
        if(len(characters)==0):
            raise OptionError("No AI characters available for M.U.G.E.N.")
        return characters


    def stages(self) -> List[str]:
        return self.mugen_stages[:]

    @staticmethod
    def health() -> range:
        return range(30, 310, 10)
    
    @staticmethod
    def timer() -> List[str]:
        return ["20s", "40s", "60s", "80s", "99s", "None"]
    
    @property
    def mugen_characters(self) -> List[str]:
        if(len(self.archipelago_options.mugen_characters.value)==0):
            raise OptionError("No characters selected for M.U.G.E.N.")
        return sorted(self.archipelago_options.mugen_characters.value)
    
    @property
    def mugen_player_only_characters(self) -> List[str]:
        return sorted(self.archipelago_options.mugen_player_only_characters.value)

    @property
    def mugen_ai_only_characters(self) -> List[str]:
        return sorted(self.archipelago_options.mugen_ai_only_characters.value)

    @property
    def mugen_stages(self) -> List[str]:
        if(len(self.archipelago_options.mugen_stages.value)==0):
            raise OptionError("No stages selected for M.U.G.E.N.")
        return sorted(self.archipelago_options.mugen_stages.value)


# Archipelago Options
class MugenCharacters(OptionList):
    """
    Indicates which characters can be used for M.U.G.E.N.
    This list is fully customizable. Duplicates can be used to skew weights. (Can cause duplicates in team fights)
    """

    display_name = "M.U.G.E.N. Characters"
    default = ["Kung-Fu Man", "Mario", "Wario"]

class MugenPlayerOnlyCharacters(OptionSet):
    """
    Indicates which characters can only be used by the player, not the AI, for M.U.G.E.N.
    This list is fully customizable, and must be a subset of the full list of characters (Extra characters will be ignored). Make sure at least have one character available.
    For the best experience, make sure at least 4 characters are accessible.
    """

    display_name = "M.U.G.E.N. Player Only Characters"
    default = ["Mario"]

class MugenAiOnlyCharacters(OptionSet):
    """
    Indicates which characters can only be used by the AI, not the player, for M.U.G.E.N.
    This list is fully customizable, and must be a subset of the full list of characters (Extra characters will be ignored). Make sure at least have one character available.
    For the best experience, make sure at least 4 characters are accessible.
    """

    display_name = "M.U.G.E.N. AI Only Characters"
    default = ["Wario"]

class MugenStages(OptionSet):
    """
    Indicates which stages can be used for M.U.G.E.N.
    This list is fully customizable.
    This cannot be empty.
    """

    display_name = "M.U.G.E.N. Stages"
    default = ["Training Room", "Mountainside Temple"]