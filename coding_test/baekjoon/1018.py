N, M = list(map(int, input().split()))
board = [list(input()) for _ in range(N)]

min_cnt = 64

idx_i = 0
idx_j = 0
while True:
    cnt = 0
    for i in range(idx_i, idx_i+8):
        for j in range(idx_j, idx_j+8):
            if ((i+j) % 2) and (board[i][j] == 'W'):
                cnt += 1
            elif (not ((i+j) % 2)) and (board[i][j] == 'B'):
                cnt += 1

    if cnt < min_cnt:
        min_cnt = cnt

    if 64-cnt < min_cnt:
        min_cnt = 64-cnt

    if min_cnt == 0:
        break

    if idx_i + 8 >= N:
        if idx_j + 8 >= M:
            break
        else:
            idx_i = 0
            idx_j += 1
    else:
        idx_i += 1

print(min_cnt)