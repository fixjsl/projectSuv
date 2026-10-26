import random


class Selection:
    def __init__(self, data):
        self.type = data.get("type")
        self.name = data.get("name")  # 이벤트 이름
        self.info = data.get("info")  # 이벤트 설명
        self.Event1: Event = data.get("Event1")  # 1번 선택지 이벤트
        self.Event2: Event = data.get("Event2")  # 2번 선택지 이벤트

    def EventInvoke(self, eventNumber):  # 이벤트 발생 시
        match eventNumber:
            case 1:
                return self.Event1.Invoke()
            case 2:
                return self.Event2.Invoke()

    def Eventinfo(self):
        return f"1. {self.Event1.eventInfo}\n\n2. {self.Event2.eventInfo}\n"


class Event:
    def __init__(self, data):
        self.event = data[
            "event"
        ]  # 선택지 타입과 지급하는 양 구조 { event: { type : type, 성공 : {보상 : x, 메세지 :  x},실패 :  [실패시]]}
        self.eventInfo = data["info"]  # 이벤트 설명
        self.eventChance = data.get("Chance")  # 이벤트 성공 실패 확률

    def Invoke(self):
        result = [self.event["type"]]
        if random.random() < self.eventChance:
            result.append(self.event["Success"]["reward"])
            return result, self.event["Success"]["Message"]
        else:
            result.append(self.event["Fail"]["reward"])
            return result, self.event["Fail"]["Message"]
