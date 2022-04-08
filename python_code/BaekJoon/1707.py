K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    data_input = [list(map(int, input().split())) for _ in range(E)]

    set_list = []