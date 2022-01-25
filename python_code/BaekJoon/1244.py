# 데이터 입력 -------------------------------------------

num_switch = int(input())

stat_switch = list(map(int, input().split()))

num_students = int(input())

# 로직 --------------------------------------------------
# 학생별로 따로 처리
for i in range(num_students):

    # 학생의 성별과 받은 숫자 입력
    stud = list(map(int, input().split()))

    # 학생이 남자일 경우
    if stud[0] == 1:

        # 배수인 스위치 판별
        for j in range(len(stat_switch)):
            if (j + 1) % stud[1] == 0:

                # 스위치의 현 상태에 따라 변화
                # ( 함수로 구현하면 편한데 처음에 짤때 이렇게 시작해서..)
                # (하다보니 귀찮아서....)
                if stat_switch[j] == 0:
                    stat_switch[j] = 1
                else:
                    stat_switch[j] = 0

            # 학생이 여자일 경우
    if stud[0] == 2:

        # 받은 숫자가 1 혹은 마지막 숫자일 때 자신만 변화
        if (stud[1] == 1) or (stud[1] == num_switch):
            if stat_switch[stud[1] - 1] == 0:
                stat_switch[stud[1] - 1] = 1
            else:
                stat_switch[stud[1] - 1] = 0

            # 받은 숫자가 그 사이 어딘가 있을 때...휴..
        else:

            # 슬라이싱할 첫 인덱스와 마지막 인덱스 지정
            a = stud[1] - 2
            b = stud[1]

            # 끝날 때 까지...
            while True:

                # 인덱싱 범위가 스위치 범위를 넘어갔을 때
                if (a < 0) or (b > num_switch - 1):

                    # 이미 인덱싱 범위가 변했으므로 지난 범위를 변화
                    for j in range(a + 1, b):
                        if stat_switch[j] == 0:
                            stat_switch[j] = 1
                        else:
                            stat_switch[j] = 0
                    break

                # 인덱싱 범위가 전체를 안넘어갔고 인덱싱 범위가 대칭일 때 인덱싱 범위 확장
                # 이걸 while문 마지막에 넣었어야 편한데... 생각의 흐름대로 코딩한 결과...
                elif stat_switch[a] == stat_switch[b]:
                    a -= 1
                    b += 1
                    continue

                # 범위는 전체를 안넘어갔는데 인덱싱 범위가 대칭이 아닐 때
                else:
                    # 이미 인덱싱 범위를 확장시켰으니까 지난 범위 변화
                    for j in range(a + 1, b):
                        if stat_switch[j] == 0:
                            stat_switch[j] = 1
                        else:
                            stat_switch[j] = 0
                    break

# 출력 --------------------------------------------------

# 스무개씩 끊어서 줄별로 출력
for i in range((num_switch // 20) + 1):
    # join 쓸거니까 인덱싱
    stat_switch_temp = stat_switch[:20]

    # 다음을 위해 앞에 잘라내기 -> 좀 재귀처럼 했네요
    stat_switch = stat_switch[20:]

    # join 으로 출력, join 하려고 str 로 타입 변환
    print(' '.join(list(map(str, stat_switch_temp))))