from enum import StrEnum, auto


class SkillType(StrEnum):
    """
     This class represents the different types of skills in the game Hattrick.

     It is a subclass of StrEnum, which is a variant of Enum where the members are also (and must be) strings.

     Attributes:
         Keeper (str): Represents the Keeper skill type.
         Defender (str): Represents the Defender skill type.
         Playmaking (str): Represents the Playmaking skill type.
         Winger (str): Represents the Winger skill type.
         Passer (str): Represents the Passer skill type.
         Scoring (str): Represents the Scorer skill type.
         Kicker (str): Represents the Kicker skill type.
     """
    Keeper = "Keeper"
    Defender = "Defender"
    Playmaking = "Playmaking"
    Winger = "Winger"
    Passer = "Passer"
    Scoring = "Scoring"
    Kicker = "Kicker"
    Overall = "Overall"
