'''
PGS
순위 검색
lv 2

https://programmers.co.kr/learn/courses/30/lessons/72412?language=python3
'''

# 깔끔풀이
def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()

        # print(k, data[k])

    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
            # print(l, r, mid, answer)
        # answer.append((pool, find, mid))
        answer.append(len(pool)-l)

    return answer

# 풀이 2 해설
# https://github.com/yuneg11/Programmers-Solutions/tree/master/solutions/72412%20-%20%EC%88%9C%EC%9C%84%20%EA%B2%80%EC%83%89

# 내 풀이 2개 시간 초과
# def solution(info, query):
#     answer = []
#     lst = [[0]*5 for _ in range(len(info))]
#     for idx in range(len(info)):
#         lst[idx][0], lst[idx][1], lst[idx][2], lst[idx][3], lst[idx][4] = info[idx].split()
#     for que in query:
#         num = que.split()
#         pointlen = len(num[-1])
#         lan, end, nior, food = que[:-(pointlen+1)].split(' and ')
#         point = que[-pointlen:]
#         checklst = [lan, end, nior, food, point]
#         prevres = [i for i in range(len(info))]
#         for i in range(5):
#             tempres = []
#             res = []
#             if checklst[i] == '-':
#                 # res = [i for i in range(len(info))]
#                 continue
#             elif i==4:
#                 for j in range(len(info)):
#                     if int(checklst[i]) <= int(lst[j][i]):
#                         res.append(j)
#             else:
#                 for j in range(len(info)):
#                     if checklst[i] == lst[j][i]:
#                         res.append(j)
#             if not res:
#                 prevres = []
#                 break
#             for k in res:
#                 if k in prevres:
#                     tempres.append(k)
#             prevres = tempres
#         answer.append(len(prevres))
#
#
#
#         # print(lan, end, nior, food, point)
#
#
#     return answer


# 풀이 2
# from bisect import bisect_left
# from collections import defaultdict
# from itertools import combinations
#
#
# # 모든 경우의수를 만들어 해당 경우의 수를 키값으로 하는 딕셔너리에 score를 저장한다.
#
#
# def solution(info, query):
#     answer = []
#     dic = defaultdict()
#     comb = [0, 1, 2, 3]
#     for i in info:
#         person = i.split()
#         conditions = person[:-1]
#         score = int(person[-1])
#         for j in range(5):
#             for k in list(combinations(comb, j)):
#                 temp = conditions.copy()
#                 for idx in k:
#                     temp[idx] = '-'
#                 key = ''.join(temp)
#                 if key in dic:
#                     dic[key].append(score)
#                 else:
#                     dic[key] = [score]
#     # print(dic)
#     for value in dic.values():  # 딕셔너리 내 모든 값 정렬
#         value.sort()
#
#     for i in query:
#         q_list = []
#         for j in i.split():
#             if j == 'and':
#                 continue
#             q_list.append(j)
#
#         target = int(q_list[-1])
#         key = ''.join(q_list[:-1])
#
#         if key in dic:
#             hubo_list = dic[key]
#
#             index = bisect_left(hubo_list, target)
#             answer.append(len(hubo_list) - index)
#         else:
#             answer.append(0)
#             continue
#
#     # print(answer)
#     return answer


print(
    solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    )
)