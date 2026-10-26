import random

from data import EventType


class AdventrueManager:
    Turn = 0
    MaxTurn = random.randrange(9, 12)

    def __init__(self, Selectiondata):
        self.SelectionData = Selectiondata
        self.ExitEvent = None
        for i in self.SelectionData:
            if i.type == EventType.Exit:
                self.ExitEvent = i
                self.SelectionData.remove(i)

    def SelectionSelect(self):
        if AdventrueManager.Turn == AdventrueManager.MaxTurn:
            return self.ExitEvent
        Eventnum = random.randrange(0, len(self.SelectionData))
        Event = self.SelectionData[Eventnum]
        return Event
