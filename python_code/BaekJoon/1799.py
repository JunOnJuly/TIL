# 재귀로 다시 해보자
# 리스트 안에 있는거 다 리턴

len_chess = int(input().strip())

max_bishop = 0

can_bishop = []

for i in range(len_chess):
    temp_list = list(map(int, input().split()))
    for j in range(len_chess):
        if temp_list[j] == 1:
            can_bishop.append([i, j])

tik = 0

while True:
    if tik == len(can_bishop):
        break

    can_bishop_copy = []
    for idx in can_bishop:
        can_bishop_copy.append(idx.copy())

    can_bishop_copy = can_bishop_copy[tik:] + can_bishop_copy[:tik]

    for i in range(len(can_bishop)):
        if (can_bishop_copy[i] == ['bishop']) or (can_bishop_copy[i] == [None]):
            continue
        std_1 = can_bishop_copy[i][0] + can_bishop_copy[i][1]
        std_2 = can_bishop_copy[i][0] - can_bishop_copy[i][1]

        can_bishop_copy[i] = ['bishop']

        for j in range(len(can_bishop)):
            if j == i:
                continue
            else:
                if (can_bishop_copy[j] == ['bishop']) or (can_bishop_copy[j] == [None]):
                    continue
                if (can_bishop_copy[j][0] + can_bishop_copy[j][1] == std_1) or \
                        (can_bishop_copy[j][0] - can_bishop_copy[j][1] == std_2):
                    can_bishop_copy[j] = [None]
                else:
                    continue

    if can_bishop_copy.count(['bishop']) > max_bishop:
        max_bishop = can_bishop_copy.count(['bishop'])
    tik += 1

print(max_bishop)