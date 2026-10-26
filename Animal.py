class Animal:
    def __init__(self, data):
        self.name = data["name"]
        self.hp = data["hp"]
        self.atk = data["atk"]
        self.dropItem = data["dropItem"]

        self.live = True

    def attack(self):
        return self.atk

    def hit(self, damage):
        self.hp -= damage

        return self.die()

    def die(self):

        if self.hp <= 0:
            self.live = False
        return self.dropItem
