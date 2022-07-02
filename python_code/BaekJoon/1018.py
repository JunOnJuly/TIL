N, M = map(int, input().split())

map_input = []
for i in range(N):
    map_input.append(list(input()))

min_count = 64

for i in range(N):
    for j in range(M):

        count = 0
        for n in range(8):
            for m in range(8):
                if i+n >= N or j+m >= M:
                    break
                print(count)
                if (i + j + n + m) % 2:
                    if map_input[i + n][j + m] == 'B':
                        count += 1
                else:
                    if map_input[i + n][j + m] == 'W':
                        count += 1
        if count > 32:
            if min_count > 64 - count:
                min_count = 64 - count
        if count <= 32:
            if min_count > count:
                min_count = count

print(min_count)