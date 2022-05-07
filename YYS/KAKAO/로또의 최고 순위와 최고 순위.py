def solution(lottos, win_nums):
    # 동일 수는 두 개 이상 담겨있지 않음
    rank = [6, 6, 5, 4, 3, 2, 1]
    record = [0] * 46

    for w in win_nums:
        record[w] += 1

    zero = 0
    correct = 0  # 맞춘 수
    for l in lottos:
        if not l:
            zero += 1
        elif record[l] > 0:
            record[l] -= 1
            correct += 1
    MIN = rank[correct]
    MAX = rank[correct + zero]

    return [MAX, MIN]