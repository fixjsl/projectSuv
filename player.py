from inventory import Inventory
from Item import Item
from weapon import Weapon


class Player:
    def __init__(self):
        self.Maxhp = 100  # 최대체력
        self.hp = self.Maxhp  # 현재 체력
        self.atk = 5  # 공격력

        self.agi = 2  # 회피 확률 판정용
        self.luk = 1  # 랜덤 성공 확률 증가
        self.inventory = Inventory()  # 아이템 인벤토리
        self.defaultWeapon = Weapon({"name": "맨손", "atk": 1})
        self.weapon = self.defaultWeapon  # 장착된 무기
        self.finAtk = self.atk + self.weapon.atk  # 무기 합친 공격력

        self.Maxhungry = 100
        self.Maxwater = 100
        self.hungry = self.Maxhungry
        self.water = self.Maxwater

        self.live = True

    def attack(self):
        return self.finAtk

    def playerPeanltyCheck(self):
        if self.hungry <= 0:
            self.hungry = 0
            self.hit(20)
        if self.water <= 0:
            self.water = 0
            self.hit(40)

    def hit(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.die()

    def die(self):
        print("플레이어 사망")
        self.live = False

    def InputInventory(self, item: Item):
        self.inventory.Input(item)

    def UseItem(self, item: Item):
        self.inventory.Use(item)

    def recal(self):
        self.finAtk = self.atk + self.weapon.atk
