from enum import StrEnum

from Item import Item, ItemType
from Selection import Event, Selection


class EventType(StrEnum):
    Item = "Item"
    Weapon = "Weapon"
    Hungry = "Hungry"
    Water = "Water"
    HP = "HP"
    Battle = "Battle"
    Exit = "Exit"


meat = Item({"name": "생고기", "type": ItemType.Food, "hpChange": 10})

Pigdata = {"name": "멧돼지", "hp": 10, "atk": 3, "dropItem": [meat]}
Beardata = {"name": "곰"}

HungryE = Event(
    {
        "event": {
            "type": EventType.Hungry,
            "Success": {"reward": 10, "Message": "열매를 찾았다\n포만도 10 상승 "},
            "Fail": {"reward": 0, "Message": "먹을 것을 찾지못해 굶었다"},
        },
        "info": "숲에서 과일이라도 찾아보자",
        "Chance": 0.5,
    }
)
BattleE = Event(
    {
        "event": {
            "type": EventType.Battle,
            "Success": {"reward": Pigdata, "Message": "멧돼지와의 전투 시작"},
            "Fail": {"reward": 0, "Message": "먹을 것을 찾지못해 굶었다"},
        },
        "info": "동물을 찾아서 잡는다",
        "Chance": 1,
    }
)
WaterE1 = Event(
    {
        "event": {
            "type": EventType.Water,
            "Success": {
                "reward": 50,
                "Message": "강물을 찾아 마셨다\n수분이 50 증가했다",
            },
            "Fail": {"reward": 0, "Message": "물을 찾지 못했다"},
        },
        "info": "숲 속으로 물을 찾으러 간다",
        "Chance": 0.7,
    }
)
WaterE2 = Event(
    {
        "event": {
            "type": EventType.Water,
            "Success": {"reward": -20, "Message": "바닷물을 마셔 갈증이 심해졌다"},
            "Fail": {"reward": 0, "Message": ""},
        },
        "info": "바닷물을 마신다",
        "Chance": 1,
    }
)

ItemE = Event(
    {
        "event": {
            "type": EventType.Item,
            "Success": {"reward": [], "Message": "먹을 수 있어보이는 식물을 찾았다"},
            "Fail": {"reward": 0, "Message": ""},
        },
        "info": "쓸만한 물건을 찾아보자",
        "Chance": 0.7,
    }
)
ExitE = Event(
    {
        "event": {
            "type": EventType.Exit,
            "Success": {"reward": 0, "Message": "탈출 성공하였습니다"},
        },
        "info": "드디어 무인도 탈출이다",
        "Chance": 1,
    }
)
selections = [
    Selection(
        {
            "type": EventType.Hungry,
            "name": "배고픔 해결하기",
            "info": "먹을 것을 찾아보자",
            "Event1": HungryE,
            "Event2": BattleE,
        }
    ),
    Selection(
        {
            "type": EventType.Water,
            "name": "마실 것을 찾기",
            "info": "목이 마르다 마실 것을 찾아보자",
            "Event1": WaterE1,
            "Event2": WaterE2,
        }
    ),
    Selection(
        {
            "type": EventType.Exit,
            "name": "탈출",
            "info": "구조선이 도착했다",
            "Event1": ExitE,
            "Event2": ExitE,
        }
    ),
]
