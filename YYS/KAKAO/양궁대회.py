import copy


class Container:
    MAX = -1
    ANS = [-1]

def cal(info, record):
    start = 10
    a = 0
    b = 0
    for i in range(11):
        if info[i] == record[i] == 0:
            pass
        elif info[i] >= record[i]:
            a += start
        else:
            b += start
        start -= 1
    if b - a <= 0: return -2  # 어차피 0차이나면 의미 없으므로 -2를 리턴한다.
    return b - a

def cal2(record, record2):
    # 만약 점수가 같다면 대체가 가능한지
    for i in range(10, -1, -1):
        if record[i]==record2[i]:
            pass
        elif record[i] > record2[i]:
            return True
        else: return False
    return False

def dfs(n, info, record, depth, idx):
    # global MAX, ANS : 글로벌의 한계
    if depth >= n:

        #print(record)
        score = cal(info, record)
        if Container.MAX < score:
            #print(score, info, record)
            Container.MAX = score
            # print("기록하기 전: ",Container.ANS)
            # print("이후 덮어씌워질 값", record)
            Container.ANS = copy.deepcopy(record)
            #print(answer)
        elif Container.MAX == score and score > 0 and cal2(record, Container.ANS):
            #print(score, info, record)
            Container.ANS = copy.deepcopy(record)
        return
    if idx == 10: # 남았을 때를 고려했어야함
        record[idx] = n - depth
        dfs(n, info, record, n, idx)
        record[idx] = 0
        return

    dfs(n, info, record, depth, idx + 1)
    if n - depth >= info[idx] + 1:
        record[idx] = info[idx] + 1
        dfs(n, info, record, depth + info[idx] + 1, idx + 1)
        record[idx] = 0

def solution(n, info):
    record = [0] * 11
    dfs(n, info, record, 0, 0)
    return Container.ANS

#print(solution(5, 	[2,1,1,1,0,0,0,0,0,0,0]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
