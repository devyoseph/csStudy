"""
PGS
다단계 칫솔 판매
level3
1시간
https://programmers.co.kr/learn/courses/30/lessons/77486
"""

def find(parents, money, number, answer):
    # 부모의 id가 내 id와 같거나, 더이상 줄 돈이 없는 경우 종료
    if parents[number] == number or money//10 == 0:
        answer[number] += money
        return
    send = money // 10
    mine = money - send
    answer[number] += mine

    # 부모의 id 값으로 재귀호출
    find(parents, send, parents[number], answer)

def solution(enroll, referral, seller, amount):
    N = len(enroll)
    answer = [0] * (N+1)

    # 이름-번호
    d = {}
    for i in range(N):
        d[enroll[i]] = i + 1

    # 추천인 입력
    parents = [i for i in range(N + 1)]
    for i in range(N):
        if referral[i] == '-':
            parents[i+1] = 0
        else:
            parents[i+1] = d[referral[i]]

    # 칫솔 정산
    for i in range(len(seller)):
        find(parents, amount[i]*100, d[seller[i]], answer)
    return answer[1:]

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],\
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],\
               ["young", "john", "tod", "emily", "mary"],\
               [12, 4, 2, 5, 10]))