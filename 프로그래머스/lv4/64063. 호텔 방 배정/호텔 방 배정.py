import sys
sys.setrecursionlimit(10**5)

def NextRoom(info, room):
    if not info.get(room):
        info[room] = room + 1
        return room
    else:
        info[room] = NextRoom(info, info[room])
        return info[room]

def solution(k, room_number):
    info = {}
    return [NextRoom(info, room) for room in room_number]