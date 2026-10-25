from enum import StrEnum


class ItemType(StrEnum):
    HealItem = "Heal"
    Food = "Food"
    Water = "Water"

class Item:
    def __init__(self,data):
        self.name = data["name"]
        self.type = data["type"]
        self.hpChange = data.get("hpChange",0)
        self.hungryChange = data.get("hungryChange",0)
        self.waterChange = data.get("waterChanger",0)
        pass


    def Use(self):
        match type:
            case ItemType.HealItem: return self.hpChange
            case ItemType.Food : return self.hpChange
            case ItemType.Water: return self.waterChange
                