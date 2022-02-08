T = 10

for i in range(T):
    N = int(input())
    list_apart = list(map(int, input().split()))
    num_sum = 0

    for j in range(2, len(list_apart) - 2):
        s, e = j - 2, j + 2

        if (list_apart[s] < list_apart[j]) and (list_apart[e] < list_apart[j]) and \
                (list_apart[s + 1] < list_apart[j]) and (list_apart[e - 1] < list_apart[j]):
            num_sum += min(list_apart[j] - list_apart[s], list_apart[j] - list_apart[s + 1],
                           list_apart[j] - list_apart[e], list_apart[j] - list_apart[e - 1])

    print(f'#{i+1} {num_sum}')
