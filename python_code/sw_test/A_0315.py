T = int(input())

for t in range(1, T + 1):
    N = int(input())

    fisher_input = []
    for _ in range(3):
        fisher_input.append(list(map(int, input().split())))

    formation = [[0, 1, 2], [0, 2, 1], [1, 2, 0], [1, 0, 2], [2, 0, 1], [2, 1, 0]]
    cnt_list = []

    for k in range(len(formation)):
        fisher_input_temp = [fisher_input[formation[k][0]], fisher_input[formation[k][1]], fisher_input[formation[k][2]]]

        for l in range(2):
            sit_fishing = [0] * N
            cnt = 0
            for i in range(len(fisher_input_temp)):
                can_sit = list(range(1, N + 1))
                if l == 0 or fisher_input_temp[i][1] % 2:
                    can_sit.sort(key=lambda x: abs(x-fisher_input_temp[i][0]))
                else:
                    can_sit.sort(key=lambda x: abs(x - fisher_input_temp[i][0]))
                    for m in range(len(can_sit)):
                        if m % 2 and m + 1 < len(can_sit):
                            if can_sit[0] == len(can_sit) or can_sit[0] == 0 or can_sit[m] == 0 or \
                                    can_sit[m] == len(can_sit) or can_sit[m + 1] == 0 or can_sit[m + 1] == len(can_sit):
                                break
                            can_sit[m], can_sit[m + 1] = can_sit[m + 1], can_sit[m]
                j = 0
                tic = 0
                while True:
                    if tic == fisher_input_temp[i][1]:
                        break

                    if sit_fishing[can_sit[j] - 1] == 0:
                        sit_fishing[can_sit[j] - 1] = 1
                        cnt += abs(can_sit[j] - fisher_input_temp[i][0]) + 1
                        j += 1
                        tic += 1
                    else:
                        j += 1
                        continue

            cnt_list.append(cnt)
    print(f'#{t} {min(cnt_list)}')