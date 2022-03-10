def make_map(map_data):
    for i in range(N):
        for j in range(N):
            if j + M - 1 < N:
                idx_i_1 = i
                idx_j_1 = j

        first_hive = map_data[i][j:j + M]
        if sum(first_hive) <= C:
            rev = sum([x ** 2 for x in range(len(first_hive))])
        else:

        for j in range(M):
            map_data[idx_i_1][idx_j_1 + i] = 0

        for j in range(N):
            for k in range(N):
                if k + M - 1 < N and 0 not in map_data[i][k:k+M]:
                    idx_i_2 = j
                    idx_j_2 = k
            second_hive = map_data[j][k:k+M]


def find_max_sum(num_list, limit, list_bin, idx):
    if sum([num_list[i]*list_bin[i] for i in range(M)]) > limit:
        return
    if idx == M:
        return [num_list[i]*list_bin[i] for i in range(M)]
    list_bin[idx] = 0
    find_max_sum(num_list, limit, list_bin, idx + 1)
    list_bin[idx] = 1
    find_max_sum(num_list, limit, list_bin, idx + 1)


T = int(input())

for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    data_input = [list(map(int, input().split())) for _ in range(N)]
    bin_list = [0] * M
