import random

from Selection import EventType


class AdventrueManager():
    Turn = 0
    MaxTurn = random.randrange(9,12)

    def __init__(self,Selectiondata):
        self.SelectionData = self.SelectionData
        self.ExitEvent
        for i in self.SelectionData:
            if i["type"] == EventType.Exit:
                self.Exitevent = i
                self.SelectionData.remove(i)

    def SelectionSelect(self):
        if AdventrueManager.turn == AdventrueManager.MaxTurn: 
            return self.Exitevent
        Eventnum = random.randrange(0,len(self.SelectionData))
        Event = self.SelectionData[Eventnum]
        return Event
