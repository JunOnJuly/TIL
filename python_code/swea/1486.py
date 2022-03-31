def make_tower(data_height, sum_of_height):
    global min_sum_of_height

    if sum_of_height >= min_sum_of_height:
        return

    if B <= sum_of_height < min_sum_of_height:
        min_sum_of_height = sum_of_height
        return

    for i in range(len(data_height)):
        del_data = data_height[i]
        del data_height[i]
        make_tower(data_height, sum_of_height + del_data)
        data_height.insert(i, del_data)


T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())

    data_input = list(map(int, input().split()))
    min_sum_of_height = 200000

    make_tower(data_input, 0)

    print(f'#{tc} {min_sum_of_height - B}')
