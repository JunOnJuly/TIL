def binary_search(data_list, target_data, start, end):
    global state
    if len(data_list) == 1:
        if data_list[0] != target_data:
            state = None
            return -1

    if len(data_list) == 0:
        state = None
        return -1

    center = (end - start) // 2
    center_idx = (start + end) // 2

    if data_list[center] == target_data:
        state = None
        return center_idx

    elif data_list[center] < target_data:
        if not state or state == 'left':
            state = 'right'
            return binary_search(data_list[center + 1:], target_data, center_idx + 1, end)
        else:
            return -1

    else:
        if not state or state == 'right':
            state = 'left'
            return binary_search(data_list[:center], target_data, start, center_idx - 1)
        else:
            return -1


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    state = None

    cnt = 0
    for i in range(len(B)):
        if binary_search(A, B[i], 0, len(A) - 1) != -1:
            cnt += 1

    print(f'#{tc} {cnt}')