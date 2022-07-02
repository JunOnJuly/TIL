S = input()
q = int(input())

alpha_list = {}

for i in range(q):

    a, l, r = input().split()
    l, r = map(int, [l, r])

    if a not in alpha_list.keys():
        for idx in range(len(S)):
            if S[idx] == a:
                if a in alpha_list.keys():
                    alpha_list[a].append(idx)
                else:
                    alpha_list[a] = [idx]

    if a in alpha_list.keys():
        length = len(alpha_list[a])

        start = length
        end = 0

        for idx_start in range(length):
            if alpha_list[a][idx_start] >= l:
                start = idx_start
                break

        if start == length:
            print(0)
            continue

        else:
            for idx_end in range(-1, -length - 1, -1):
                if alpha_list[a][idx_end] <= r:
                    end = length + idx_end + 1
                    break

        print(end - start)

    else:
        print(0)