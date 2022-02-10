T = 10

for i in range(10):
    N = int(input())
    list_box = list(map(int, input().split()))

    cnt = 0

    while True:
        min_hei = [100, None]
        max_hei = [1, None]
        if cnt == N:

            break

        for j in range(len(list_box)):
            if list_box[j] <= min_hei[0]:
                min_hei = [list_box[j], j]
            if list_box[j] >= max_hei[0]:
                max_hei = [list_box[j], j]

        if max_hei[0] - min_hei[0] == 0:
            break

        list_box[max_hei[1]] -= 1
        list_box[min_hei[1]] += 1
        cnt += 1

    for j in range(len(list_box)):
        if list_box[j] <= min_hei[0]:
            min_hei = [list_box[j], j]
        if list_box[j] >= max_hei[0]:
            max_hei = [list_box[j], j]

    print(f'#{i + 1} {max_hei[0] - min_hei[0]}')