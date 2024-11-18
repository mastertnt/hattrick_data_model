from enum import StrEnum, auto


class SpecialSkill(StrEnum):
    Head = "Head"
    Unpredictable = "Unpredictable"
    Quick = "Quick"
    Powerful = "Powerful"
    Technical = "Technical"
    Resistant = "Resistant"
    NoSpeciality = "NoSpeciality"

    def from_text(self, text: str):
        if text == "Joueur":
            return SpecialSkill.Head
        elif text == "Imprévisible":
            return SpecialSkill.Unpredictable
        elif text == "Rapide":
            return SpecialSkill.Quick
        elif text == "Costaud":
            return SpecialSkill.Powerful
        elif text == "Technique":
            return SpecialSkill.Technical
        elif text == "Resistant":
            return SpecialSkill.Resistant
        return SpecialSkill.NoSpeciality
