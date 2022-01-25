def warp(num_input: int) -> int:
    n = 1
    while True:
        if (n-1) ** 2 <= num_input <= n ** 2:
            if num_input <= n * (n - 1):
                return 2*(n - 1)
            return 2*n - 1
        n += 1
    return

# 데이터 입력
test_num = int(input().strip())
for i in range(test_num):
    num1, num2 = map(int, input().split())
    num = num2 - num1
    print(warp(num))