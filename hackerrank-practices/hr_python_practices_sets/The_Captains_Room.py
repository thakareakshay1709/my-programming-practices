k = int(input())
room_list = list(map(int, input().split()))
single_room = set()
multiple_rooms = set()

for room in room_list:
    if room not in single_room:
        single_room.add(room)
    else:
        multiple_rooms.add(room)
print(single_room.difference(multiple_rooms).pop())
# print(multiple_rooms)
