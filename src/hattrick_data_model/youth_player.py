from src.hattrick_data_model.age import Age
from level import Level
from player_type import PlayerType
from skill_type import SkillType
from special_skill import SpecialSkill


class YouthPlayer:
    """
    This class represents a youth player in the game Hattrick.

    Attributes:
        id (int): The unique identifier of the player. Initialized as None.
        age (Age): The age of the player. Initialized as None.
        keeper (LevelType): The Keeper skill level of the player. Initialized as None.
        defender (LevelType): The Defender skill level of the player. Initialized as None.
        playmaking (LevelType): The Playmaking skill level of the player. Initialized as None.
        winger (LevelType): The Winger skill level of the player. Initialized as None.
        passer (LevelType): The Passer skill level of the player. Initialized as None.
        scorer (LevelType): The Scorer skill level of the player. Initialized as None.
    """

    rma_training_speeds = {SkillType.Keeper: (0, 130), SkillType.Defender: (2, 230), SkillType.Playmaking: (1, 200), SkillType.Winger: (1, 140), SkillType.Passer: (1, 180), SkillType.Scoring: (1, 210), SkillType.Kicker: (2, 40)}

    def __init__(self):
        """
        Initializes the YouthPlayer class with default values.
        """
        self.id = -1
        self.first_name = None
        self.last_name = None
        self.age = Age(0, 0)
        self.promoted_in_days = -1
        self.special_skill = SpecialSkill.NoSpeciality
        self.keeper = Level(-1, -1, SkillType.Keeper)
        self.defender = Level(-1, -1, SkillType.Defender)
        self.playmaking = Level(-1, -1, SkillType.Playmaking)
        self.winger = Level(-1, -1, SkillType.Winger)
        self.passer = Level(-1, -1, SkillType.Passer)
        self.scorer = Level(-1, -1, SkillType.Scoring)
        self.kicker = Level(-1, -1, SkillType.Kicker)
        self.overall = Level(-1, -1, SkillType.Overall)
        self.player_type = PlayerType.Unknown
        self.__rma = -1
        self.htms = -1
        self.initial_comment = None

    def set_level(self, level):
        """
        Sets the level of a specific skill for the player.

        Args:
            level (LevelType): The type of the level to be set.

        The method uses pattern matching to determine which skill level to set.
        """
        match level.type:
            case SkillType.Keeper:
                self.keeper = level
            case SkillType.Defender:
                self.defender = level
            case SkillType.Playmaking:
                self.playmaking = level
            case SkillType.Winger:
                self.winger = level
            case SkillType.Passer:
                self.passer = level
            case SkillType.Scoring:
                self.scorer = level
            case SkillType.Kicker:
                self.kicker = level
            case SkillType.Overall:
                self.overall = level

    def get_level(self, skill_type: SkillType) -> Level:
        """
        Gets the level of a specific skill for the player.

        Args:
            skill_type (SkillType): The type of the skill to get.

        Returns:
            LevelType: The level of the skill.
        """
        match skill_type:
            case SkillType.Keeper:
                return self.keeper
            case SkillType.Defender:
                return self.defender
            case SkillType.Playmaking:
                return self.playmaking
            case SkillType.Winger:
                return self.winger
            case SkillType.Passer:
                return self.passer
            case SkillType.Scoring:
                return self.scorer
            case SkillType.Kicker:
                return self.kicker
            case SkillType.Overall:
                return self.overall

    def get_rma(self):
        self.update_scores();
        return self.__rma

    def get_skill_to_train(self):
        skill_to_train = []

        for skill_type in SkillType:
            if skill_type != SkillType.Overall:
                if self.player_type == PlayerType.FieldPlayer:
                    if YouthPlayer.rma_training_speeds[skill_type][0] != 0:
                        skill_level = self.get_level(skill_type)
                        if skill_level.max_level != -1:
                            if skill_level.current_level < skill_level.max_level:
                                skill_to_train.append((skill_type, self.get_skill_rma(skill_type)))
                        else:
                            skill_to_train.append((skill_type, self.get_skill_rma(skill_type)))

                elif self.player_type == PlayerType.Goalkeeper:
                    if YouthPlayer.rma_training_speeds[skill_type][0] != 1:
                        skill_level = self.get_level(skill_type)
                        if skill_level.max_level != -1:
                            if skill_level.current_level < skill_level.max_level:
                                skill_to_train.append((skill_type, self.get_skill_rma(skill_type)))
                        else:
                            skill_to_train.append((skill_type, self.get_skill_rma(skill_type)))
                else:
                    skill_level = self.get_level(skill_type)
                    if skill_level.max_level != -1:
                        if skill_level.current_level < skill_level.max_level:
                            skill_to_train.append((skill_type, self.get_skill_rma(skill_type)))
                    else:
                        skill_to_train.append((skill_type, self.get_skill_rma(skill_type)))
        return skill_to_train

    def get_skill_to_discover(self):
        skill_to_discover = []
        for skill_type in SkillType:
            if skill_type != SkillType.Overall:
                if self.player_type == PlayerType.FieldPlayer:
                    if YouthPlayer.rma_training_speeds[skill_type][0] != 0:
                        skill_level = self.get_level(skill_type)
                        if skill_level.max_level == -1:
                            skill_to_discover.append((skill_type, self.get_skill_rma(skill_type)))
                elif self.player_type == PlayerType.Goalkeeper:
                    if YouthPlayer.rma_training_speeds[skill_type][0] != 1:
                        skill_level = self.get_level(skill_type)
                        if skill_level.max_level == -1:
                            skill_to_discover.append((skill_type, self.get_skill_rma(skill_type)))
                else:
                    skill_level = self.get_level(skill_type)
                    if skill_level.max_level == -1:
                        skill_to_discover.append((skill_type, self.get_skill_rma(skill_type)))
        return skill_to_discover

    def get_skill_rma(self, skill_type):
        skill_value_to_consider = 3
        skill_level = self.get_level(skill_type)
        if skill_level is not None:
            if skill_level.max_level != -1:
                skill_value_to_consider = skill_level.max_level
            elif skill_level.current_level != -1:
                skill_value_to_consider = skill_level.current_level + 1
            elif self.overall.max_level != -1:
                if skill_type == SkillType.Keeper:
                    skill_value_to_consider = 1
                elif skill_type == SkillType.Kicker:
                    skill_value_to_consider = 3
                else:
                    skill_value_to_consider = self.overall.max_level - 1
            else:
                if skill_type == SkillType.Keeper:
                    skill_value_to_consider = 1
                elif skill_type == SkillType.Kicker:
                    skill_value_to_consider = 3
                else:
                    skill_value_to_consider = 3

        skill_value_to_consider = int(skill_value_to_consider) + 1

        skill_rma = 0
        for y in range(1, skill_value_to_consider):
            skill_rma += YouthPlayer.rma_training_speeds[skill_type][1] * pow(0.87, (8 - y))

        return skill_rma

    def update_scores(self):
        rma_goalkeeper = 0
        rma_field_player = 0
        for skill in YouthPlayer.rma_training_speeds:
            skill_rma = self.get_skill_rma(skill)

            if YouthPlayer.rma_training_speeds[skill][0] == 0:
                rma_goalkeeper += skill_rma
            elif YouthPlayer.rma_training_speeds[skill][0] == 1:
                rma_field_player += skill_rma
            else:
                rma_goalkeeper += skill_rma
                rma_field_player += skill_rma
        rma_goalkeeper *= 2.2

        overload = self.promotion_age().difference_in_days(17, 0)
        if overload > 0:
            rma_field_player -= 10 * overload
            rma_goalkeeper -= 10 * overload

        if self.special_skill != SpecialSkill.NoSpeciality:
            rma_field_player += 100
            rma_goalkeeper += 100
            if self.special_skill != SpecialSkill.Resistant:
                rma_field_player += 100

        self.__rma = round(max(rma_goalkeeper, rma_field_player))
        if rma_goalkeeper > rma_field_player:
            self.player_type = PlayerType.Goalkeeper
        else:
            self.player_type = PlayerType.FieldPlayer
        if self.__rma < 1800:
            self.player_type = PlayerType.Unknown

    def promotion_age(self):
        return self.age.add_days(self.promoted_in_days)

    def __str__(self):
        return f"ID: {self.id}, [{self.player_type}] {self.first_name}, {self.last_name}, {self.age}, promoted in {self.promoted_in_days} days ({self.promotion_age()}), {self.special_skill}, {self.keeper}, {self.defender}, {self.playmaking}, {self.winger}, {self.passer}, {self.scorer}, {self.kicker}, {self.overall}, RMA = {self.get_rma()}, HTMS = {self.htms}"
