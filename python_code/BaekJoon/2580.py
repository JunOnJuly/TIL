data_input = [list(map(int, input().split())) for _ in range(9)]
map_data = []
visited = [[1] * 9 for _ in range(9)]

for i in range(9):
    temp_list = []
    for j in range(9):
        if data_input[i][j] == 0:
            temp_list.append(list(range(1, 10)))
        else:
            temp_list.append([])
    map_data.append(temp_list)
while True:
    for i in range(9):
        if 0 in data_input[i]:
            end = 0
            break
        elif i == 8:
            end = 1
            break
    if end == 1:
        break

    for i in range(9):
        for j in range(9):
            num = data_input[i][j]

            if num == 0:
                continue
            else:
                for k in range(9):
                    if visited[i][k] and num in map_data[i][k]:
                        map_data[i][k].remove(num)
                        visited[i][k] = 2
                    if visited[i][k] and num in map_data[k][j]:
                        map_data[k][j].remove(num)
                        visited[i][k] = 2

                i_divide = i // 3
                j_divide = j // 3

                for k in range(i_divide * 3, (i_divide + 1) * 3):
                    for l in range(j_divide * 3, (j_divide + 1) * 3):
                        if visited[i][k] and num in map_data[k][l]:
                            map_data[k][l].remove(num)
    for i in range(9):
        for j in range(9):
            if visited[i][j] == 2:
                visited[i][j] = 0
            if len(map_data[i][j]) == 1:
                data_input[i][j] = map_data[i][j][0]
for i in range(9):
    print(*data_input[i])