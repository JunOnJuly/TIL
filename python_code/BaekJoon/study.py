T = int(input())

for i in range(T):
    N = int(input())

    list_block = list(map(int, input().split()))

    list_fall_len = []

    for j in range(len(list_block)):
        num_over = 0
        for k in range(j + 1, len(list_block)):
            if list_block[j] <= list_block[k]:
                num_over += 1
        list_fall_len.append(N - j - 1 - num_over)

    print(f'#{i+1} {max(list_fall_len)}')