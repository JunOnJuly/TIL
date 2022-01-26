N = int(input().strip())

N_list = list(map(int, input().split()))

i = 0
max_len = 0
while True:
    if i == len(N_list) - 1:
        break
    j = i + 0
    while True:
        j += 1
        if sorted(N_list[i: j]) != N_list[i: j]:
            if len(N_list[i: j]) - 1 > max_len:
                max_len = len(N_list[i: j]) - 1
            break
        if j == len(N_list):
            break
    i += 1

i = 0
while True:
    if i == len(N_list) - 1:
        break
    j = i + 0
    while True:
        j += 1
        if sorted(N_list[i: j], reverse=True) != N_list[i: j]:
            if len(N_list[i: j]) - 1 > max_len:
                max_len = len(N_list[i: j]) - 1
            break
        if j == len(N_list):
            break
    i += 1


print(max_len)