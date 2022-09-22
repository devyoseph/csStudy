'''
PGS
두 큐 합 같게 만들기
레벨2
-
https://school.programmers.co.kr/learn/courses/30/lessons/118667
'''

def solution(queue1, queue2):
    q1 = sum(queue1)
    q2 = sum(queue2)
    idx1 = idx2 = 0
    n = len(queue1)
    answer = 0
    while q1 != q2 and idx1 < 2*n and idx2 < 2*n:
        answer += 1
        if q1 < q2:
            q1 += queue2[idx2]
            q2 -= queue2[idx2]
            queue1.append(queue2[idx2]) # pop 하지 않고 끝에 push
            idx2 += 1                   # 시작점만을 변경
        elif q1 > q2:
            q1 -= queue1[idx1]
            q2 += queue1[idx1]
            queue2.append(queue1[idx1]) # pop 하지 않고 끝에 push
            idx1 += 1                   # 시작점만을 변경
    if q1 != q2:
        answer = -1
    return answer

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))
print(solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 10],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))