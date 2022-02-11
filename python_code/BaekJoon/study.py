T = 10


for tc in range(1, T + 1):
    dump_num = int(input())
    box_height = list(map(int, input().split()))  # 박스의 높이들

    cnt = 0
    while True:
        max_num = box_height[0]
        min_num = box_height[0]

        # 높은 박스,낮은 박스 위치 찾기
        for i in range(len(box_height)):
            if box_height[i] > max_num:
                max_num = box_height[i]
                max_idx = i  # 높은 박스의 위치(idx)

        for j in range(len(box_height)):
            if box_height[j] < min_num:
                min_num = box_height[j]
                min_idx = j  # 낮은 박스의 위치(idx)

        if cnt == dump_num:
            break

        box_height[i] -= 1
        box_height[j] += 1

        cnt += 1

    print(f'#{tc} {max_num - min_num}')