# 피보나치 함수 정의
def fibonacci(num: int):
    if num == 0:
        global call_0
        call_0 += 1
        return 0
    elif num == 1:
        global call_1
        call_1 += 1
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


# 데이터 입력
test_time = int(input())

for i in range(test_time):
    global call_0
    call_0 = 0
    global call_1
    call_1 = 0
    fibonacci(int(input()))
    print("{0} {1}".format(call_0, call_1))