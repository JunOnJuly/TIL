import sys


def divide_sort(num_list, start, end):
    length = end - start + 1

    if length == 1:
        return [num_list[start]]
    elif length == 2:
        if num_list[start] > num_list[end]:
            return [num_list[end], num_list[start]]
        else:
            return [num_list[start], num_list[end]]

    half = (start + end)//2

    front_list = divide_sort(num_list, start, half - 1)
    back_list = divide_sort(num_list, half, end)

    front_length = len(front_list)
    back_length = len(back_list)

    front_idx = 0
    back_idx = 0

    return_list = []

    while True:
        if front_idx == front_length:
            return_list.extend(back_list[back_idx:])
            return return_list

        elif back_idx == back_length:
            return_list.extend(front_list[front_idx:])
            return return_list

        if front_list[front_idx] < back_list[back_idx]:
            return_list.append(front_list[front_idx])
            front_idx += 1
        else:
            return_list.append(back_list[back_idx])
            back_idx += 1


N = int(sys.stdin.readline().rstrip())
nums = divide_sort(list(map(int, sys.stdin.readline().split())), 0, N-1)

if N % 2:
    print(nums[N//2] ** 2)
else:
    print(nums[0]*nums[-1])