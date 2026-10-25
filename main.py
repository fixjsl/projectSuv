from player import Player
from Animal import Animal
from AdventrueManager import AdventrueManager


player = Player()

Pigdata = {"name" : "멧돼지", "hp":10, "atk" : 3, "dropItem" :[] }

pig = Animal(Pigdata)


def Screen(player:Player, message ):

    print("----------------------------------------------------------------")
    print(f"| {player.hp:2}/{player.Maxhp:2} | 배고픔 : {player.hungry:3} | 목마름 : {player.water:2} | 무기 : {player.weapon.name:5}| {AdventrueManager.Turn:2}일차 |")
    print("----------------------------------------------------------------\n")
    print(message)

Screen(player, "ss")

#while True:
 #   pass



    

    


