N, K = map(int, input().split())

temp_list = list(map(int, input().split()))

max_sum = sum(temp_list[:K])
temp_sum = sum(temp_list[:K])

for j in range(N - K):
    temp_sum -= temp_list[j]
    temp_sum += temp_list[j+K]

    if temp_sum > max_sum:
        max_sum = temp_sum

print(max_sum)