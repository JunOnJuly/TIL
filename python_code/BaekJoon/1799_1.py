def bishop(copy_can_bishop, start_num):
    if (copy_can_bishop[start_num] == ['bishop']) or (copy_can_bishop[start_num] == [None]):
        return False
    std_1 = copy_can_bishop[start_num][0] + copy_can_bishop[start_num][1]
    std_2 = copy_can_bishop[start_num][0] - copy_can_bishop[start_num][1]

    copy_can_bishop[start_num] = ['bishop']

    for j in range(len(copy_can_bishop)):
        if j == i:
            continue
        else:
            if (copy_can_bishop[j] == ['bishop']) or (copy_can_bishop[j] == [None]):
                continue
            if (copy_can_bishop[j][0] + copy_can_bishop[j][1] == std_1) or \
                    (copy_can_bishop[j][0] - copy_can_bishop[j][1] == std_2):
                copy_can_bishop[j] = [None]
            else:
                continue
    return copy_can_bishop


def bishop_recur(copy_can_bishop, start_num):
    for i in range(len(copy_can_bishop)):
        if copy_can_bishop[i] == [None] or ['bishop']:
            if i == len(copy_can_bishop) - 1:
                return copy_can_bishop.count(['bishop'])
        else:
            break
    copy_can_bishop = bishop(copy_can_bishop, start_num)

    can_bishop_num = 0
    for i in range(len(copy_can_bishop)):
        if copy_can_bishop[i] not in [['bishop'], [None]]:
            can_bishop_num += 1
    return_list = []
    for i in range(can_bishop_num):

    return



len_chess = int(input().strip())

max_bishop = 0

can_bishop = []

for i in range(len_chess):
    temp_list = list(map(int, input().split()))
    for j in range(len_chess):
        if temp_list[j] == 1:
            can_bishop.append([i, j])

    can_bishop_copy = []
    for idx in can_bishop:
        can_bishop_copy.append(idx.copy())
