from enum import Enum


# This Enum class represents the various positions a player can occupy in a football match.
# Each position is represented by a unique integer.
class FieldPosition(Enum):
    Goalkeeper = 1  # Represents the Goalkeeper position
    LeftWingBack = 2  # Represents the Left Wing Back position
    RightWingBack = 3  # Represents the Right Wing Back position
    LeftCentralDefender = 4  # Represents the Left Central Defender position
    RightCentralDefender = 5  # Represents the Right Central Defender position
    CentralDefender = 6  # Represents the Central Defender position
    LeftWinger = 7  # Represents the Left Winger position
    RightWinger = 8  # Represents the Right Winger position
    LeftInnerMidfield = 9  # Represents the Left Inner Midfield position
    RightInnerMidfield = 10  # Represents the Right Inner Midfield position
    CentralMidfield = 11  # Represents the Central Midfield position
    LeftForward = 12  # Represents the Left Forward position
    RightForward = 13  # Represents the Right Forward position
    CentralForward = 14  # Represents the Central Forward position
    SubstituteGoalkeeper = 15  # Represents the Substitute Goalkeeper position
    SubstituteDefender = 16  # Represents the Substitute Defender position
    SubstituteWinBack = 17  # Represents the Substitute Wing Back position
    SubstituteMidfield = 18  # Represents the Substitute Midfield position
    SubstituteForward = 19  # Represents the Substitute Forward position
    SubstituteWinger = 20  # Represents the Substitute Winger position
    SubstituteExtra = 21  # Represents the Extra Substitute position
