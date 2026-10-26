from enum import StrEnum


class ItemType(StrEnum):
    HealItem = "Heal"
    Food = "Food"
    Water = "Water"


class Item:
    def __init__(self, data):
        self.name = data["name"]
        self.type = data["type"]
        self.hpChange = data.get("hpChange", 0)
        self.hungryChange = data.get("hungryChange", 0)
        self.waterChange = data.get("waterChange", 0)

    def Use(self):
        match self.type:
            case ItemType.HealItem:
                return self.hpChange
            case ItemType.Food:
                return self.hungryChange
            case ItemType.Water:
                return self.waterChange
