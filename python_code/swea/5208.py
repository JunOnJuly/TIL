def find_route(battery_data, cnt):
    global min_cnt, move_length
    if move_length >= N:
        if cnt - 1 < min_cnt:
            min_cnt = cnt - 1
        return

    battery = battery_data[0]

    for i in range(battery, 0, -1):
        move_length += i
        find_route(battery_data[i:], cnt + 1)
        move_length -= i


T = int(input())

for tc in range(1, T + 1):
    data_input = list(map(int, input().split()))
    N = data_input[0]
    data_battery = data_input[1:]
    min_cnt = N
    move_length = 1

    find_route(data_battery, 0)

    print(f'#{tc} {min_cnt}')