T = int(input())


for tc in range(T):
    N = int(input())
    list_nums = list(map(int, input().split()))

    # 정렬
    for i in range(len(list_nums)):
        for j in range(len(list_nums) - 1):
            if list_nums[j] > list_nums[j + 1]:
                list_nums[j], list_nums[j + 1] = list_nums[j + 1], list_nums[j]

    # 맨 뒤에서 맨 앞 빼기
    print(f'#{tc + 1} {list_nums[-1] - list_nums[0]}')
