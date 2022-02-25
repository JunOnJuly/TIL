N, M = map(int, input().split())

list_num = sorted(list(map(int, input().split())))

for i in range(len(list_num)):
    if list_num[i] >= M:
        list_num = list_num[: i]
        break

list_num = list_num[::-1]

num_left_min = M + 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        num_left = M - list_num[i]
        if list_num[j] > num_left:
            continue
        num_left = M - list_num[i] - list_num[j]
        for k in range(j + 1, N):
            num_left = M - list_num[i] - list_num[j]
            if list_num[k] > num_left:
                continue
            num_left -= list_num[k]
            if num_left < num_left_min:
                num_left_min = num_left
                break

print(M - num_left_min)