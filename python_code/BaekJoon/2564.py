len_block = list(map(int, input().split()))

num_shop = int(input())
guide_move = [1, 3, 2, 4]
index_list = []
sum_min = 0

for _ in range(num_shop + 1):
    index_list.append(list(map(int, input().split())))

for i in range(len(index_list)):
    if index_list[i][0] in [1, 2]:
        index_list[i] = [index_list[i][0], index_list[i][1], len_block[0] - index_list[i][1]]
    else:
        index_list[i] = [index_list[i][0], index_list[i][1], len_block[1] - index_list[i][1]]

index_list_sorted = []
for i in range(len(index_list)):
    index_list_sorted.append(index_list[i].copy())

for i in range(len(index_list_sorted)):
    if index_list_sorted[i][0] in [1, 4]:
        index_list_sorted[i][1], index_list_sorted[i][2] = index_list_sorted[i][2], index_list_sorted[i][1]

for i in range(len(index_list)):
    if guide_move.index(index_list[-1][0]) - guide_move.index(index_list[i][0]) in [2, -2]:
        if index_list[-1][0] in [1, 2]:
            sum_min += min(len_block[1] + index_list[-1][1] + index_list[i][1],\
                           len_block[1] + index_list[-1][2] + index_list[i][2])

        else:
            sum_min += min(len_block[0] + index_list[-1][1] + index_list[i][1],\
                           len_block[0] + index_list[-1][2] + index_list[i][2])

    elif guide_move.index(index_list[-1][0]) - guide_move.index(index_list[i][0]) in [-1, 3]:
        sum_min += index_list_sorted[-1][2] + index_list_sorted[i][1]

    elif guide_move.index(index_list[-1][0]) - guide_move.index(index_list[i][0]) in [1, -3]:
        sum_min += index_list_sorted[-1][1] + index_list_sorted[i][2]

    else:
        sum_min += abs(index_list[-1][1] - index_list[i][1])

print(sum_min)