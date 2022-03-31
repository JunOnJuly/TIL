T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    data_container = sorted(list(map(int, input().split())), reverse=True)
    data_truck = sorted(list(map(int, input().split())), reverse=True)
    sum_weight = 0

    while True:
        if not data_truck or not data_container:
            break
        truck_selected = data_truck.pop(0)

        i = 0
        while True:
            if i == len(data_container) or not data_container:
                break

            if truck_selected >= data_container[i]:
                sum_weight += data_container.pop(i)
                break
            i += 1

    print(f'#{tc} {sum_weight}')