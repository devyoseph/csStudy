import copy
from pprint import pprint
from queue import PriorityQueue

# ?? 
def dfs(info, visit, arr , end, sheep, wolf, MAX):
    M = max(sheep, MAX)

    for k in range(len(end)): # 끝점들을 기준으로 백트래킹
        e = end[k]
        print(end)
        for idx in range(len(arr[e])):
            i = arr[e][idx]
            print(idx, i, arr[e]) ## 아니 연결점이 어디서 사라지는거지...??
            if visit[i] == False: # 끝점에 연결된 점 중 연결되지 않음

                if info[i] == 0: # 만약 양이라면?
                    visit[i] = True
                    end2 = copy.copy(end)
                    end2.pop(k)
                    for j in arr[i]:
                        if not visit[j]:
                            end2.append(j)

                    M = max(MAX+1, dfs(info, visit, arr, end2, sheep+1, wolf, MAX+1))
                    visit[i] = False

                elif info[i] == 1 and sheep > wolf + 1: # 만약 늑대라면?
                    visit[i] = True
                    end2 = copy.copy(end)
                    end2.pop(k)
                    for j in arr[i]:
                        if not visit[j]:
                            end2.append(j)

                    M = max(MAX,dfs(info, visit, arr, end2, sheep, wolf+1, MAX))
                    visit[i] = False


    return M

def solution(info, edges):
    N = len(info)
    arr = [list() for __ in range(N)]
    # 연결관계 정리: 그냥 배열로 최적화 가능하지만 그냥 리스트 사용
    for e in edges:
        arr[e[0]].append(e[1])
        arr[e[1]].append(e[0])
    #pprint(arr)
    # 방문체크 배열
    visit = [False]*N

    # 0을 후보에 넣어주기
    visit[0] = True

    end = [] # 끝점들만 관리
    for i in arr[0]:
        end.append(i)

    MAX = dfs(info, visit, arr, end, 1, 0, 1)
    return MAX

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])
      )






