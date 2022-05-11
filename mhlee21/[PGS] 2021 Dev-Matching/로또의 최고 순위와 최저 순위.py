"""
PGS
로또의 최고 순위와 최저 순위
level1
10분
https://programmers.co.kr/learn/courses/30/lessons/77484
"""
def solution(lottos, win_nums):
    zero = lottos.count(0)
    win = 0
    for num in win_nums:
        if num in lottos:
            win += 1
    answer = [7-(zero+win),7-win]
    for i in range(len(answer)):
        if answer[i] == 7:
            answer[i] = 6
    return answer