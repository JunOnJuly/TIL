def divide_sort(num_list, start, end):
    length = end - start + 1
    if length == 1:
        return [num_list[start]]
    elif length == 2:
        if num_list[start] < num_list[end]:
            return [num_list[end], num_list[start]]
        else:
            return [num_list[start], num_list[end]]

    half = (start + end)//2

    front_list = divide_sort(num_list, start, half - 1)
    back_list = divide_sort(num_list, half, end)

    length_front = len(front_list)
    length_back = len(back_list)



N = int(input())
num_list = [int(input()) for _ in range(N)]

