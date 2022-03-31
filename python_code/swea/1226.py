T = 10

for _ in range(T):
    N = 16
    tc = int(input())
    map_input = []
    guide_i = [0, 1, 0, -1]
    guide_j = [1, 0, -1, 0]

    for i in range(N):
        map_input.append(list(map(int, list(input()))))
        for j in range(len(map_input[i])):
            if map_input[i][j] == 2:
                start_idx = [i, j]
            elif map_input[i][j] == 3:
                end_idx = [i, j]

    stack = [start_idx]

    while True:
        if not stack:
            print(f'#{tc} {0}')
            break

        if stack[-1] == end_idx:
            print(f'#{tc} {1}')
            break

        for i in range(4):
            i_now = stack[-1][0] + guide_i[i]
            j_now = stack[-1][1] + guide_j[i]

            if 0 <= i_now < N and 0 <= j_now < N and map_input[i_now][j_now] in [0, 3]:
                stack.append([i_now, j_now])
                map_input[i_now][j_now] = 1
                break

            elif i == 3:
                stack.pop()