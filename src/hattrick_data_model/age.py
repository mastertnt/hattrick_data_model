class Age:
    """
    This class represents the age of a player in the game Hattrick.

    Attributes:
        years (int): The number of years of the player's age.
        days (int): The number of days of the player's age in addition to the years.
    """

    def __init__(self, years, days):
        """
        Initializes the Age class with the given years and days.

        Args:
            years (int): The number of years of the player's age.
            days (int): The number of days of the player's age in addition to the years.
        """
        self.years = years
        self.days = days

    def difference_in_days(self, year, days):
        year_diff = self.years - year
        day_diff = self.days - days
        return year_diff * 112 + day_diff

    def add_days(self, days):
        """
        Adds a specified number of days to the current age.

        Args:
            days (int): The number of days to add.

        Returns:
            Age: A new Age instance with the updated years and days.
        """
        result = Age(self.years, self.days)
        result.days += days
        while result.days >= 112:
            result.years += 1
            result.days -= 112
        while result.days < 0:
            result.years -= 1
            result.days += 112
        return result

    def __str__(self):
        return f"{self.years} years, {self.days} days"