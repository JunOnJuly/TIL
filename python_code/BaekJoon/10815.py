def sort_list(data_list, start, end):

    length = end - start + 1
    half = start + length//2

    if length == 1:
        return [data_list[start]]

    if length == 2:
        if data_list[start] > data_list[end]:
            data_list[start], data_list[end] = data_list[end], data_list[start]

        return data_list[start:end + 1]

    sorted_list = []

    front_list = sort_list(data_list, start, half)
    back_list = sort_list(data_list, half + 1, end)

    i = 0
    j = 0

    while True:
        if i == len(front_list):
            sorted_list.extend(back_list[j:end + 1])
            break

        elif j == len(back_list):
            sorted_list.extend(front_list[i:half + 1])
            break

        if front_list[i] < back_list[j]:
            sorted_list.append(front_list[i])
            i += 1
        else:
            sorted_list.append(back_list[j])
            j += 1

    return sorted_list


def binary_search(sorted_list, start, end, num_find):
    if end < start:
        return 0

    length = end - start + 1
    half = start + length // 2

    if sorted_list[half] == num_find:
        return 1
    else:
        if num_find > sorted_list[half]:
            return binary_search(sorted_list, half + 1, end, num_find)
        else:
            return binary_search(sorted_list, start, half - 1, num_find)


N = int(input())
num_input = list(map(int, input().split()))
sorted_list = sort_list(num_input, 0, N - 1)

M = int(input())
num_differ = list(map(int, input().split()))

for num in num_differ:
    print(binary_search(sorted_list, 0, N - 1, num), end=' ')
