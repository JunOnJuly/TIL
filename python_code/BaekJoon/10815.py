def binary_search(list_data, list_length, find_number):
    if not list_length:
        return 0

    half_index = list_length // 2

    if list_data[half_index] == find_number:
        return 1
    else:
        return binary_search(list_data[:half_index], half_index, find_number) + \
               binary_search(list_data[half_index + 1:], half_index, find_number)


N = int(input())
num_input = list(map(int, input().split()))
M = int(input())
num_differ = list(map(int, input().split()))

for i in range(M):
    print(binary_search(num_input, N, num_differ[i]))