N = int(input())

list_num = list(map(int, input().split()))

max_len_up = 1
for i in range(N):
    if max_len_up > N - i:
        break
    index_start = i
    index_end = i
    for j in range(i, N - 1):
        if list_num[j] <= list_num[j + 1]:
            index_end += 1
            if j == N - 2:
                max_len_up = max(index_end - index_start + 1, max_len_up)
                break
        else:
            max_len_up = max(index_end - index_start + 1, max_len_up)
            break

max_len_down = 1
for i in range(N):
    if max_len_up > N - i:
        break
    index_start = i
    index_end = i
    for j in range(i, N - 1):
        if list_num[j] >= list_num[j + 1]:
            index_end += 1
            if j == N - 2:
                max_len_up = max(index_end - index_start + 1, max_len_up)
                break
        else:
            max_len_down = max(index_end - index_start + 1, max_len_down)
            break
print(max(max_len_up, max_len_down))