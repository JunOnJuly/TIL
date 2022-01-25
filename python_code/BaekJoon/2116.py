def road_dice(status: list, num_dice: int) -> int:
    list_manual_move = [5, 3, 4, 1, 2, 0]
    test_num = [1, 2, 3, 4, 5, 6]
    sums_nums = []
    for idx in range(6):
        start = test_num[idx]
        tik = 0
        sum_nums = 0
        while True:
            if tik == num_dice:
                break
            nums_temp = [1, 2, 3, 4, 5, 6]
            nums_temp.remove(start)
            nums_temp.remove(status[tik][list_manual_move[status[tik].index(start)]])
            sum_nums += max(nums_temp)
            start = status[tik][list_manual_move[status[tik].index(start)]]
            tik += 1
        sums_nums.append(sum_nums)

    return max(sums_nums)


num_dice = int(input())

stat_dices = []

for i in range(num_dice):
    stat_dices.append(list(map(int, input().split())))

print(road_dice(stat_dices, num_dice))