def find_min(N, num_five_fct):
    if num_five_fct == -1:
        return -1
    elif (N - num_five_fct * 5) % 3 == 0:
        return num_five_fct + ((N - num_five_fct * 5) // 3)
    else:
        return find_min(N, num_five_fct - 1)


N = int(input())

num_five = N // 5
print(find_min(N, num_five))