def factorial(num: int) -> int:
    mul_num = 1
    for i in range(1, num+1):
        mul_num *= i
    return mul_num


test_num = int(input())

for i in range(test_num):
    N, M = map(int, input().split())
    print(int(factorial(M)/(factorial(M-N)*factorial(N))))