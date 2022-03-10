def merge_sort(data_list):
    global cnt

    start = 0
    end = len(data_list)
    half_idx = (end - start) // 2

    if len(data_list) == 1:
        return data_list
    elif len(data_list) == 2:
        if data_list[0] > data_list[1]:
            cnt += 1
            data_list[0], data_list[1] = data_list[1], data_list[0]
        return data_list

    data_left = merge_sort(data_list[:half_idx])
    data_right = merge_sort(data_list[half_idx:])

    if data_left[-1] > data_right[-1]:
        cnt += 1

    return_list = []

    l = 0
    r = 0

    while True:
        if l >= len(data_left):
            return_list.extend(data_right[r:])
            break
        if r >= len(data_right):
            return_list.extend(data_left[l:])
            break

        if data_left[l] >= data_right[r]:
            return_list.append(data_right[r])
            r += 1
        else:
            return_list.append(data_left[l])
            l += 1

    return return_list


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data_input = list(map(int, input().split()))
    cnt = 0

    print(f'#{tc} {merge_sort(data_input)[N // 2]} {cnt}')