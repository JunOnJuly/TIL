T = int(input())

for tc in range(T):

    N = int(input())

    list_map = []
    for i in range(N):
        list_map.append([0] * N)

    idx_point = [0, 0]

    cnt = 1
    while True:
        for i in range(2)[::-1]:
            if cnt > N ** 2:
                break
            while True:
                list_map[idx_point[0]][idx_point[1]] = cnt
                cnt += 1
                if cnt > N**2:
                    break
                idx_point[i] += 1
                if idx_point[i] >= len(list_map) or list_map[idx_point[0]][idx_point[1]] != 0:
                    idx_point[i] -= 1
                    if i == 1:
                        idx_point[1 - i] += 1
                    else:
                        idx_point[1 - i] -= 1
                    break

        if cnt > N ** 2:
            break

        for i in range(2)[::-1]:
            if cnt > N ** 2:
                break
            while True:
                list_map[idx_point[0]][idx_point[1]] = cnt
                cnt += 1
                if cnt > N**2:
                    break
                idx_point[i] -= 1
                if idx_point[i] < 0 or list_map[idx_point[0]][idx_point[1]] != 0:
                    idx_point[i] += 1
                    if i == 1:
                        idx_point[1 - i] -= 1
                    else:
                        idx_point[1 - i] += 1
                    break

        if cnt > N ** 2:
            break

    print(f'#{tc + 1}')
    for i in range(len(list_map)):
        print(*list_map[i])