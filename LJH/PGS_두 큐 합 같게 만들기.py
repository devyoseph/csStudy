'''
PGS
두 큐 합 같게 만들기
lv 2
https://school.programmers.co.kr/learn/courses/30/lessons/118667
'''

from collections import deque


def solution(queue1, queue2):
    queue11 = deque(queue1)
    queue22 = deque(queue2)
    answer = -2
    num = len(queue11)+len(queue22)
    cnt=0
    sum1 = sum(queue11)
    sum2 = sum(queue22)
    goal = (sum1+sum2) / 2
    while(sum1!=sum2):
        if sum1>goal:
            temp = queue11.popleft()
            queue22.append(temp)
            sum1 -= temp
            sum2 += temp
        else:
            temp = queue22.popleft()
            queue11.append(temp)
            sum2 -= temp
            sum1 += temp
        cnt += 1
        if cnt >= num*2:
            return -1
    answer = cnt
    return answer

print(solution([3, 2, 7, 2],[4, 6, 5, 1]))
print(solution([1, 2, 1, 2],[1, 10, 1, 2]))
print(solution([1, 1],[1, 5]))