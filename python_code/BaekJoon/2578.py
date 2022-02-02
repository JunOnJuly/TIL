bingo_list = []
for i in range(5):
    bingo_list.append(list(map(int, input().split())))

num_list = []
for i in range(5):
    num_list.extend(list(map(int, input().split())))

bingo_line = 0
i = 0
tik = 0
while True:
    bingo_line = 0

    for j in range(len(bingo_list)):
        if num_list[i] in bingo_list[j]:
            bingo_list[j][bingo_list[j].index(num_list[i])] = 0
            break

    for j in range(len(bingo_list)):
        if sum(bingo_list[j]) == 0:
            bingo_line += 1

    sum_nums = 0
    for j in range(len(bingo_list)):
        sum_nums += bingo_list[j][j]
    if sum_nums == 0:
        bingo_line += 1

    sum_nums = 0
    for j in range(len(bingo_list)):
        sum_nums += bingo_list[4 - j][j]
    if sum_nums == 0:
        bingo_line += 1

    for j in range(len(bingo_list)):
        sum_nums = 0
        for k in range(len(bingo_list)):
            sum_nums += bingo_list[k][j]
        if sum_nums == 0:
            bingo_line += 1

    if bingo_line >= 3:
        break

    i += 1

print(i+1)