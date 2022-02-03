N = int(input().strip())

max_len = 0

for i in range(round(N * (8/13)), round(N * (13/21)) + 1):
    N_temp_0 = N - 0
    N_temp_1 = i - 0
    num_list = [N_temp_0, N_temp_1]
    while True:
        if N_temp_0 - N_temp_1 < 0:
            break
        num_list.append(N_temp_0 - N_temp_1)
        N_temp_0, N_temp_1 = N_temp_1, N_temp_0 - N_temp_1
    if max_len < len(num_list):
        max_len = len(num_list)
        return_list = num_list[:]

print(max_len)
for num in return_list:
    print(num, end=' ')