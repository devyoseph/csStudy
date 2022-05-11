'''
PGS
다단계 칫솔 판매
lv 3
https://programmers.co.kr/learn/challenges
'''

def solution(enroll, referral, seller, amount):
    def sell(money, me):
        me = num[me]
        while money:
            if money<10:
                result[me] += money
                break
            a = int(money / 10)
            result[me] += money-a
            money = a
            dad = parent[me]
            me = dad
            if not dad:
                break

    n = len(enroll)
    result = [0] * (n + 1)
    num = dict()
    parent = [0]
    for i in range(n):
        num[enroll[i]] = i+1
    for i in range(n):
        if referral[i]=='-':
            parent += [0]
        else:
            parent += [num[referral[i]]]
    for i in range(len(amount)):
        sell(amount[i]*100, seller[i])
    # print(parent)
    answer = result[1:]
    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))