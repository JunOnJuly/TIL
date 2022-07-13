def binary_search(find_num, num_list, start, end):
    if end < start:
        return 0

    length = end - start + 1
    half = start + length//2

    if num_list[half] == find_num:
        return 1
    elif find_num > num_list[half]:
        return binary_search(find_num, num_list, half + 1, end)
    else:
        return binary_search(find_num, num_list, start, half - 1)


def divide_sort(num_list, start, end):
    length = end - start + 1

    if length == 1:
        return [num_list[start]]
    elif length == 2:
        if num_list[start] > num_list[end]:
            return [num_list[end], num_list[start]]
        else:
            return [num_list[start], num_list[end]]

    half = start + length//2

    front_list = divide_sort(num_list, start, half-1)
    back_list = divide_sort(num_list, half, end)

    length_front = len(front_list)
    length_back = len(back_list)
    return_list = []

    idx_front = 0
    idx_back = 0

    while True:
        if idx_front == length_front:
            return_list.extend(back_list[idx_back:])
            return return_list

        elif idx_back == length_back:
            return_list.extend(front_list[idx_front:])
            return return_list

        if front_list[idx_front] > back_list[idx_back]:
            return_list.append(back_list[idx_back])
            idx_back += 1
        else:
            return_list.append(front_list[idx_front])
            idx_front += 1


N = int(input())
num_list = divide_sort(list(map(int, input().split())), 0, N-1)

M = int(input())
find_list = list(map(int, input().split()))

for i in range(M):
    print(binary_search(find_list[i], num_list, 0, N-1))