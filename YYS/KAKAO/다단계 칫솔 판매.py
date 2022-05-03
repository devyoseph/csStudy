def solution(enroll, referral, seller, amount):
    parent = [0]*(len(enroll)+1)
    result = [0]*(len(enroll)+1)

    dic = dict()
    dic["-"] = 0
    for e in range(len(enroll)):
        dic[enroll[e]] = e+1
    for i in range(len(referral)):
        parent[i+1] = dic[referral[i]]
    #print(dic)
    #print(parent)

    for i in range(len(seller)):
        now = dic[seller[i]] # 최초 사람 번호
        money = 100*amount[i] # 최초 금액

        while now: # 센터가 아닐 때까지, 즉 0이 되면 종료
            #print(now)
            up = money//10 # 조공할 돈
            money -= up # 현재 소유자가 가질 돈
            result[now] += money

            if up == 0:
                break

            money = up
            now = parent[now]

    return result[1:]

print(solution(
["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
["young", "john", "tod", "emily", "mary"],
[12, 4, 2, 5, 10]
))

print()