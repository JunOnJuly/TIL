T = int(input())

for i in range (T):
    K, N, M = map(int, input().split())

    stop_list = list(map(int, input().split()))

    idx_bus = 0

    cnt_stop = 0

    while True:
        switch = 0
        for j in range(len(stop_list))[::-1]:
            if idx_bus + K >= stop_list[j]:
                if idx_bus >= stop_list[j]:
                    print(f'#{i+1} {0}')
                    switch = 1
                    break
                idx_bus = stop_list[j]
                cnt_stop += 1
                break
            else:
                if j == 0:
                    print(f'#{i+1} {0}')
                    switch = 1
                    break
        if switch == 1:
            break

        if idx_bus + K >= N:
            print(f'#{i+1} {cnt_stop}')
            break