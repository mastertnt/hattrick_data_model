from enum import Enum

from field_position import FieldPosition


class FormationType(Enum):
    Formation_550 = 0
    Formation_541 = 1
    Formation_532 = 2
    Formation_523 = 3
    Formation_451 = 4
    Formation_442 = 5
    Formation_433 = 6
    Formation_352 = 7
    Formation_343 = 8
    Formation_253 = 9


class PlayerPosition:
    def __init__(self, position):
        self.position = position
        self.player = None


class Formation:
    def __init__(self, type: FormationType):
        self.type = type

        match self.type:
            case FormationType.Formation_550:
                self.positions = [PlayerPosition(FieldPosition.LeftWingBack),
                                  PlayerPosition(FieldPosition.LeftCentralDefender),
                                  PlayerPosition(FieldPosition.CentralDefender),
                                  PlayerPosition(FieldPosition.RightCentralDefender),
                                  PlayerPosition(FieldPosition.RightWinback),
                                  PlayerPosition(FieldPosition.LeftWinger),
                                  PlayerPosition(FieldPosition.LeftInnerMidfield),
                                  PlayerPosition(FieldPosition.CentralMidfield),
                                  PlayerPosition(FieldPosition.RightInnerMidfield),
                                  PlayerPosition(FieldPosition.RightWinger)
                                  ]
            case FormationType.Formation_541:
                self.positions = [PlayerPosition(FieldPosition.LeftWingBack),
                                  PlayerPosition(FieldPosition.LeftCentralDefender),
                                  PlayerPosition(FieldPosition.CentralDefender),
                                  PlayerPosition(FieldPosition.RightCentralDefender),
                                  PlayerPosition(FieldPosition.RightWinback),
                                  PlayerPosition(FieldPosition.LeftWinger),
                                  PlayerPosition(FieldPosition.LeftInnerMidfield),
                                  PlayerPosition(FieldPosition.CentralMidfield),
                                  PlayerPosition(FieldPosition.RightInnerMidfield),
                                  PlayerPosition(FieldPosition.CentralForward)
                                  ]
            case FormationType.Formation_532:
                self.positions = [PlayerPosition(FieldPosition.LeftWingBack),
                                  PlayerPosition(FieldPosition.LeftCentralDefender),
                                  PlayerPosition(FieldPosition.CentralDefender),
                                  PlayerPosition(FieldPosition.RightCentralDefender),
                                  PlayerPosition(FieldPosition.LeftInnerMidfield),
                                  PlayerPosition(FieldPosition.CentralMidfield),
                                  PlayerPosition(FieldPosition.RightInnerMidfield),
                                  PlayerPosition(FieldPosition.LeftForward),
                                  PlayerPosition(FieldPosition.RightForward),
                                  ]
            case FormationType.Formation_523:
                self.positions = [PlayerPosition(FieldPosition.LeftWingBack),
                                  PlayerPosition(FieldPosition.LeftCentralDefender),
                                  PlayerPosition(FieldPosition.CentralDefender),
                                  PlayerPosition(FieldPosition.RightCentralDefender),
                                  PlayerPosition(FieldPosition.RightWinback),
                                  PlayerPosition(FieldPosition.LeftInnerMidfield),
                                  PlayerPosition(FieldPosition.CentralMidfield),
                                  PlayerPosition(FieldPosition.CentralForward),
                                  PlayerPosition(FieldPosition.LeftForward),
                                  PlayerPosition(FieldPosition.RightForward),
                                  ]
            case FormationType.Formation_523:
                self.positions = [PlayerPosition(FieldPosition.LeftWingBack),
                                  PlayerPosition(FieldPosition.LeftCentralDefender),
                                  PlayerPosition(FieldPosition.CentralDefender),
                                  PlayerPosition(FieldPosition.RightCentralDefender),
                                  PlayerPosition(FieldPosition.RightWinback),
                                  PlayerPosition(FieldPosition.LeftInnerMidfield),
                                  PlayerPosition(FieldPosition.CentralMidfield),
                                  PlayerPosition(FieldPosition.CentralForward),
                                  PlayerPosition(FieldPosition.LeftForward),
                                  PlayerPosition(FieldPosition.RightForward),
                                  ]
            case FormationType.Formation_451:
                self.positions = [PlayerPosition(FieldPosition.LeftWingBack),
                                  PlayerPosition(FieldPosition.LeftCentralDefender),
                                  PlayerPosition(FieldPosition.RightCentralDefender),
                                  PlayerPosition(FieldPosition.RightWinback),
                                  PlayerPosition(FieldPosition.LeftWinger),
                                  PlayerPosition(FieldPosition.LeftInnerMidfield),
                                  PlayerPosition(FieldPosition.CentralMidfield),
                                  PlayerPosition(FieldPosition.RightInnerMidfield),
                                  PlayerPosition(FieldPosition.RightWinger),
                                  PlayerPosition(FieldPosition.CentralForward),
                                  ]
            case FormationType.Formation_442:
                self.positions = [PlayerPosition(FieldPosition.LeftWingBack),
                                  PlayerPosition(FieldPosition.LeftCentralDefender),
                                  PlayerPosition(FieldPosition.RightCentralDefender),
                                  PlayerPosition(FieldPosition.RightWinback),
                                  PlayerPosition(FieldPosition.LeftWinger),
                                  PlayerPosition(FieldPosition.LeftInnerMidfield),
                                  PlayerPosition(FieldPosition.RightInnerMidfield),
                                  PlayerPosition(FieldPosition.RightWinger),
                                  PlayerPosition(FieldPosition.LeftForward),
                                  PlayerPosition(FieldPosition.RightForward),
                                  ]
            case FormationType.Formation_433:
                self.positions = [PlayerPosition(FieldPosition.LeftWingBack),
                                  PlayerPosition(FieldPosition.LeftCentralDefender),
                                  PlayerPosition(FieldPosition.RightCentralDefender),
                                  PlayerPosition(FieldPosition.RightWinback),
                                  PlayerPosition(FieldPosition.LeftWinger),
                                  PlayerPosition(FieldPosition.CentralMidfield),
                                  PlayerPosition(FieldPosition.RightWinger),
                                  PlayerPosition(FieldPosition.LeftForward),
                                  PlayerPosition(FieldPosition.CentralForward),
                                  PlayerPosition(FieldPosition.RightForward),
                                  ]
            case FormationType.Formation_352:
                self.positions = [PlayerPosition(FieldPosition.LeftWingBack),
                                  PlayerPosition(FieldPosition.CentralDefender),
                                  PlayerPosition(FieldPosition.RightWinback),
                                  PlayerPosition(FieldPosition.LeftWinger),
                                  PlayerPosition(FieldPosition.RightWinger),
                                  PlayerPosition(FieldPosition.LeftInnerMidfield),
                                  PlayerPosition(FieldPosition.CentralMidfield),
                                  PlayerPosition(FieldPosition.RightInnerMidfield),
                                  PlayerPosition(FieldPosition.LeftWinger),
                                  PlayerPosition(FieldPosition.CentralForward),
                                  PlayerPosition(FieldPosition.RightForward),
                                  ]
            case FormationType.Formation_343:
                self.positions = [PlayerPosition(FieldPosition.LeftWingBack),
                                  PlayerPosition(FieldPosition.CentralDefender),
                                  PlayerPosition(FieldPosition.RightWinback),
                                  PlayerPosition(FieldPosition.LeftWinger),
                                  PlayerPosition(FieldPosition.LeftInnerMidfield),
                                  PlayerPosition(FieldPosition.RightInnerMidfield),
                                  PlayerPosition(FieldPosition.RightWinger),
                                  PlayerPosition(FieldPosition.LeftForward),
                                  PlayerPosition(FieldPosition.CentralForward),
                                  PlayerPosition(FieldPosition.RightForward),
                                  ]
            case FormationType.Formation_253:
                self.positions = [PlayerPosition(FieldPosition.LeftWingBack),
                                  PlayerPosition(FieldPosition.RightWinback),
                                  PlayerPosition(FieldPosition.LeftWinger),
                                  PlayerPosition(FieldPosition.RightWinger),
                                  PlayerPosition(FieldPosition.LeftInnerMidfield),
                                  PlayerPosition(FieldPosition.CentralMidfield),
                                  PlayerPosition(FieldPosition.RightInnerMidfield),
                                  PlayerPosition(FieldPosition.LeftWinger),
                                  PlayerPosition(FieldPosition.LeftForward),
                                  PlayerPosition(FieldPosition.CentralForward),
                                  PlayerPosition(FieldPosition.RightForward),
                                  ]
