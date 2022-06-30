def binary_search(data_list, find_num, start, end):

    if end == start:
        if data_list[end] == find_num:
            return 1
    if end < start:
        return 0
    length = end - start + 1
    half = start + length//2

    if data_list[half] == find_num:
        return 1

    else:
        return binary_search(data_list, find_num, start, half - 1) + binary_search(data_list, find_num, half + 1, end)


N = int(input())
num_input = list(map(int, input().split()))
M = int(input())
num_differ = list(map(int, input().split()))

for num in num_differ:
    print(binary_search(num_input, num, 0, len(num_input) - 1), end=' ')