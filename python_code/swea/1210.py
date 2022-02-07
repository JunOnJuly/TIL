for try_num in range(10):
    case_num = int(input())
    ladder_input = []
    guide_non_lad = []
    for i in range(100):
        temp_input = input()
        if i == 0:
            for j in range(100):
                if list(map(int, temp_input.split()))[j] == 1:
                    guide_non_lad.append(j)
                ladder_input.append(list(map(int, temp_input.split())))

        elif i == 99:
            ladder_input.append(list(map(int, temp_input.split())))

        elif '1 1' in temp_input:
            ladder_input.append(list(map(int, temp_input.split())))

    x, y = ladder_input[-1].index(2), len(ladder_input) - 1

    switch = 0

    while True:
        if switch == 1:
            break
        if x == 0:
            for i in range(y)[::-1]:
                if i == 0:
                    switch = 1
                    break

                if ladder_input[i][1] == 1:
                    y = i
                    x = guide_non_lad[1]
                    break

        elif x == 99:
            for i in range(y)[::-1]:
                if i == 0:
                    switch = 1
                    break

                if ladder_input[i][98] == 1:
                    y = i
                    x = guide_non_lad[-2]
                    break

        else:
            for i in range(y)[::-1]:
                if i == 0:
                    switch = 1
                    break

                if ladder_input[i][x - 1] == 1:
                    y = i
                    x = guide_non_lad[guide_non_lad.index(x) - 1]
                    break

                elif ladder_input[i][x + 1] == 1:
                    y = i
                    x = guide_non_lad[guide_non_lad.index(x) + 1]
                    break
    print(f'#{try_num + 1} {x}')