def solution(id_list, report, k):
    dic = dict()
    L = len(id_list) #유저수
    record = [ [False for _ in range(L)] for __ in range(L)] # L*L 행렬
    for i in range(len(id_list)):
        dic[id_list[i]] = i
        # 매핑

    for r in report:
        a, b = str(r).split()
        record[dic[a]][dic[b]] = True

    res = [0]*L
    for c in range(L):
        cnt = 0
        for r in range(L):
            if record[r][c]:
                cnt += 1
        if cnt >= k:
            for r in range(L):
                if record[r][c]:
                    res[r] += 1


    return res

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2 ))