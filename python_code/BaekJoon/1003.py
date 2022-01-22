# 피보나치 함수 정의
fib_num = []
fib_num.append(0)
fib_num.append(1)
for i in range(40):
    fib_num.append(fib_num[i] + fib_num[i + 1])



# 데이터 입력
test_time = int(input())

for i in range(test_time):
    input_num = int(input())
    if input_num == 0:
        print(f'{1} {0}')
    else:
        print(f'{fibonacci(input_num - 1)} {fibonacci(input_num)}')