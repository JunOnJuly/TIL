T = int(input())

for i in range(T):
    N, M = map(int, input().split())

    list_input = list(map(int, input().split()))

    sum_start = 0
    for j in range(M):
        sum_start += list_input[j]

    max_sum = sum_start
    min_sum = sum_start

    for j in range(M - 1, N - 1):
        sum_start = sum_start + list_input[j+1] - list_input[j - M + 1]

        if sum_start > max_sum:
            max_sum = sum_start
        if sum_start < min_sum:
            min_sum = sum_start

    print(f'#{i + 1} {max_sum - min_sum}')