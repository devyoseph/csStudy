from pprint import pprint

def solution(info, query):
    answer = []
    ansewr_index = 0
    resume = [inf.split(' ') for inf in info]
    my_query = [query_set.replace(' and ', ' ').split(' ') for query_set in query]

    for forth in my_query:
        forth[4] = int(forth[4])

    for forth in resume:
        forth[4] = int(forth[4])

    resume = sorted(resume, key=lambda resume: resume[4])
    #pprint(resume)
    # pprint(my_query)

    for query_set in my_query:
        answer.append(0)
        temp_result = 0

        temp_resume = []
        temp_idx = 0
        for resume_person in resume:
            #print(resume_person[4], query_set[4])
            if int(resume_person[4]) >= query_set[4]:
                temp_resume = resume[temp_idx:]
                break
            temp_idx += 1

        for resume_person in temp_resume:

            is_ok = 0
            for idx in range(5):
                if idx == 4:
                    is_ok = 1
                elif query_set[idx] == '-' or type(query_set[idx]) == str and query_set[idx] == resume_person[idx]:
                    continue
                # elif type(query_set[idx]) == int:
                #     if query_set[idx] <= int(resume_person[idx]):
                #         is_ok = 1
                #     else:
                #         break
                else:
                    break

            if is_ok:
                temp_result += 1

        answer[ansewr_index] = temp_result
        ansewr_index += 1

    return answer

# def solution(info, query):
#     data = dict()
#     for a in ['cpp', 'java', 'python', '-']:
#         for b in ['backend', 'frontend', '-']:
#             for c in ['junior', 'senior', '-']:
#                 for d in ['chicken', 'pizza', '-']:
#                     data.setdefault((a, b, c, d), list())
#     for i in info:
#         i = i.split()
#         for a in [i[0], '-']:
#             for b in [i[1], '-']:
#                 for c in [i[2], '-']:
#                     for d in [i[3], '-']:
#                         data[(a, b, c, d)].append(int(i[4]))
#
#     pprint(data)
#
#     for k in data:
#         data[k].sort()
#
#         # print(k, data[k])
#
#     answer = list()
#     for q in query:
#         q = q.split()
#
#         pool = data[(q[0], q[2], q[4], q[6])]
#         find = int(q[7])
#         l = 0
#         r = len(pool)
#         mid = 0
#         while l < r:
#             mid = (r+l)//2
#             if pool[mid] >= find:
#                 r = mid
#             else:
#                 l = mid+1
#             # print(l, r, mid, answer)
#         # answer.append((pool, find, mid))
#         answer.append(len(pool)-l)
#
#     return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))