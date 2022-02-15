T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    switch1 = 0
    switch2 = 0

    list_input = []
    for _ in range(N):
        list_input.append(list(map(int, input().split())))

    sum_list = []
    for i in range(len(list_input)):
        sum_list.append(sum(list_input[i]))

    for i in range(N):
        if sum(sum_list[:i]) == sum(sum_list[i:]):
            switch1 = 1
    if switch1 == 0:
        print(f'#{tc} {0}')
        continue
    else:
