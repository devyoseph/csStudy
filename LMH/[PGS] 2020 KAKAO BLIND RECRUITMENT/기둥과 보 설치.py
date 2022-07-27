"""
PGS
기둥과 보 설치
level3

https://school.programmers.co.kr/learn/courses/30/lessons/60061
"""

def solution(n, build_frame):
    answer = []
    def check():
        for x,y,type in answer:
            if type == 0:
                # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
                if y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x + 1, y, 1] in answer:
                    continue
                else:
                    return False
            else:
                # 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
                if [x,y-1,0] in answer or [x+1,y-1,0] in answer or [x-1,y,1] in answer and [x+1,y,1] in answer:
                    continue
                else:
                    return False
        return True

    for x, y, a, b in build_frame:
        if b == 1:          # 설치
            if [x, y, a] not in answer:
                answer.append([x, y, a])
                if not check():
                    answer.remove([x, y, a])
        else:               # 삭제
            if [x,y,a] in answer:
                answer.remove([x, y, a])
                if not check():
                    answer.append([x, y, a])

    # return 하는 배열은 x좌표 기준으로 오름차순 정렬하며, x좌표가 같을 경우 y좌표 기준으로 오름차순 정렬해주세요.
    # x, y좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됩니다.
    answer.sort(key=lambda x:(x[0],x[1],x[2]))
    return answer

# print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
# print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
print(solution(100, [[2, 0, 0, 1], [100, 0, 0, 1], [100, 1, 1, 1], [99, 1, 1, 1], [99, 1, 0, 1], [99, 0, 0, 1]]))