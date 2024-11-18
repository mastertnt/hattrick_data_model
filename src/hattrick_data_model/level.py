from hattrick.datamodel.skill_type import SkillType

class Level:
    """
    This class represents a level in the game Hattrick.

    Attributes:
        current_level (int): The current level of the skill. Initialized as -1.
        max_level (int): The maximum level of the skill. Initialized as -1.
        type (SkillType): The type of the skill. Initialized as SkillType.Keeper.
    """
    def __init__(self, current_level=-1, max_level=-1, type=SkillType.Keeper):
        """
         Initializes the Level class with default values.
        """
        self.current_level = current_level
        self.max_level = max_level
        self.type = type

    def is_maxed(self):
        """
        Returns True if the current level is equal to the maximum level, False otherwise.
        """
        if self.max_level == -1:
            return False
        return self.current_level >= self.max_level

    def __str__(self):
        return f"{self.type}: {self.current_level}/{self.max_level}"
