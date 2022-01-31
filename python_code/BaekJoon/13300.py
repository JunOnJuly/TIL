N, K = map(int, input().split())

dict_stud = {}

for _ in range(N):
    stud_info = input()

    if stud_info not in dict_stud.keys():
        dict_stud[stud_info] = 1
    else:
        dict_stud[stud_info] += 1

num_room = 0

for value in dict_stud.values():
    if value % K == 0:
        num_room += value // K
    else:
        num_room += value//K + 1

print(num_room)