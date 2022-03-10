T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    data_input = [list(map(int, input().split())) for _ in range(E)]
    data_input.sort(key=lambda x: x[2], reverse=True)
    set_union = []
    weight_list = []
    for i in range(V + 1):
        set_union.append({i})

    while True:
        if not data_input:
            break
        for i in range(len(set_union)):
            if data_input[-1][0] in set_union[i]:
                node_1 = i
            if data_input[-1][1] in set_union[i]:
                node_2 = i
        if node_1 != node_2:
            set_union[node_1] = set_union[node_1] | set_union[node_2]
            del set_union[node_2]
            weight_list.append(data_input[-1][2])
            data_input.pop()
        else:
            data_input.pop()

    print(f'#{tc} {sum(weight_list)}')