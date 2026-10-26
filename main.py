from time import sleep

import data
from AdventrueManager import AdventrueManager
from Animal import Animal
from player import Player
from Selection import Selection

player = Player()
ADM = AdventrueManager(data.selections)
hungryD = 15
waterD = 30


def Screen(player: Player, message, wait=False):
    print("\033[2J\033[H", end="", flush=True)
    print("----------------------------------------------------------------")
    print(
        f"| {player.hp:2}/{player.Maxhp:2} | 포만도 : {player.hungry:3} | 수분 : {player.water:3} | 무기 : {player.weapon.name:5}| {AdventrueManager.Turn:2}일차 |"
    )
    print("----------------------------------------------------------------\n")
    print(message)
    if wait:
        input("엔터 입력...")


def Battle(player: Player, animal: Animal):
    message = ""
    while True:
        drop = animal.hit(player.attack())
        message += f"{animal.name}에게 {player.attack()}만큼의 데미지를 주었습니다\n"
        Screen(player, message)
        sleep(2)
        if not animal.live:
            for item in drop:
                player.InputInventory(item)
                message += f"{item.name}을/을 획득했다"
            Screen(player, message, wait=True)
            return True
        player.hit(animal.attack())
        message += f"{animal.name}에게 {animal.attack()}만큼의 데미지를 받았습니다.\n"
        Screen(player, message)
        sleep(2)
        if not player.live:
            message += "사망하였습니다\n게임오버"
            Screen(player, message, wait=True)
            return False


def MainLoop(player: Player):
    # 이벤트 선택
    event: Selection = ADM.SelectionSelect()
    infoString = event.info
    eventInfoString = event.Eventinfo()
    Screen(player, infoString + "\n\n" + eventInfoString)
    # 메세지 출력
    # 행동 기다리기
    be = int(input("선택지를 번호로 선택해주세요 : "))
    # 행동에 따른 이벤트 계산
    eventresult, eventmessage = event.EventInvoke(be)
    match eventresult[0]:
        case data.EventType.Hungry:
            player.hungry = min(player.hungry + eventresult[1], player.Maxhungry)
        case data.EventType.Water:
            player.water = min(player.water + eventresult[1], player.Maxwater)
        case data.EventType.Battle:
            Screen(player, eventmessage, wait=True)
            animal = Animal(eventresult[1])
            if not Battle(player, animal):
                return False
            eventmessage = f"{animal.name}을 쓰러뜨렸다"
        case data.EventType.Weapon:
            player.weapon = eventresult[1]
        case data.EventType.Item:
            [player.InputInventory(item) for item in eventresult[1]]
        case data.EventType.HP:
            player.hp += eventresult[1]
        case data.EventType.Exit:
            Screen(player, eventmessage, wait=True)
            return False
    Screen(player, eventmessage, wait=True)
    AdventrueManager.Turn += 1
    player.hungry -= hungryD
    player.water -= waterD
    player.playerPeanltyCheck()
    if not player.live:
        return player.live
    Screen(
        player,
        f"하루가 지나 포만감이 {hungryD}만큼, 수분이 {waterD}만큼 감소했다",
        wait=True,
    )
    return True


print("무인도에 조난당했습니다. 구조가 올때까지 살아남으세요")
while True:
    if not MainLoop(player):
        break
