from enum import Enum


# This Enum class represents the different types of players in a football match.
# Each player type is represented by a unique integer.
class PlayerType(Enum):
    Goalkeeper = 0  # Represents a potential Goalkeeper
    FieldPlayer = 1  # Represents a potential Field Player
    Unknown = 2  # Represents an Unknown player type
