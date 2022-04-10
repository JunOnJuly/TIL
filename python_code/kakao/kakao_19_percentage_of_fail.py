def solution(N, stages):
    percent = []

    stage = 1
    while True:
        if stage > N:
            break

        num_of_stages = len(stages)
        num_of_stage = 0

        idx = 0
        while True:
            if idx >= len(stages):
                break

            if stages[idx] == stage:
                num_of_stage += 1
                del stages[idx]
            else:
                idx += 1

        percent.append(num_of_stage / num_of_stages)
        stage += 1

    answer = []
    while True:
        if all(num < 0 for num in percent):
            return answer
        max_percent = -1
        max_idx = 0

        for i in range(len(percent)):
            if percent[i] > max_percent:
                max_percent = percent[i]
                max_idx = i
        answer.append(max_idx + 1)
        percent[max_idx] = -1