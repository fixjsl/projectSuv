from Item import Item


class Inventory:
    def __init__(self):
        self.hasItem = {}
        pass


    def Input(self, item : Item):
        self.hasItem[item.name] = self.hasItem.get(item.name, 0) + 1

    def Use(self,item : Item):
        if not self.remove(item): return False
        return item.Use()
        

    def remove(self,item : Item):
        
        
        if self.hasItem[item.name] -1 == 0 :
            self.hasItem.pop(item.name,None)
            return True
        else:
            self.hasItem[item.name] -=1
            return True

        return False
        
    