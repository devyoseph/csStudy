'''
PGS
등산코스 정하기
lv 3
https://school.programmers.co.kr/learn/courses/30/lessons/118669
'''
# 다익스트라

def solution(n, paths, gates, summits):
    global minInt

    def dfs(now,depth,visited,load):
        global minInt
        for i in range(n+1):
            if i in gates: continue
            if visited[i]==0 and lst[now][i]!=0:
                if lst[now][i]>minInt: continue
                if load and max(load)>minInt:return
                load.append(lst[now][i])
                if i in summits:
                    if minInt > max(load):
                        minInt = max(load)
                    answerList.append([i,max(load)])
                    load.pop()
                    continue
                visited[i]=1
                dfs(i,depth+1,visited,load)
                visited[i]=0
                load.pop()

    answer = []
    lst = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for path in paths:
        lst[path[0]][path[1]]=path[2]
        lst[path[1]][path[0]]=path[2]
    visited = [0 for _ in range(n+1)]
    answerList = []
    minInt = float('inf')
    for gate in gates:
        dfs(gate,0,visited,[])


    for answers in answerList:

        if minInt == answers[1]:
            if not answer: answer=answers
            if answer[0]>answers[0]:
                answer=answers
    return answer



#
print(solution(5,[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]],
               [1,2], [5]))
print(solution(7,[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2,3,4]))
print(solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],
               [1,3], [5]))

print(solution(7,[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],
               [3,7], [1, 5]))
