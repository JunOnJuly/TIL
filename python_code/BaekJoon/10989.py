N = int(input())

num_list = []

for i in range(N):
    num = int(input())

    idx_new = 0
    if num_list:
        for j in range(num_list - 1):
            if num_list[j] < num:
                idx_new += 1
            else:
                num_list.insert(idx_new, num)
                break

    else:
        num_list.append(num)

print(num_list)