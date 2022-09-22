def solution(n, paths, gates, summits):

    global record

    paths.sort(key=lambda x: x[2])

    # record : 각각의 위치의 정보를 기록
    record = [0 for _ in range(n+1)]

    # 출입구는 -1
    for g in gates:
        record[g] = -1

    # 봉우리는 1
    for s in summits:
        record[s] = 1

    # union find 방식으로 연결하면서 완성
    # 부모 / 봉우리 / 출입구
    parent = [[0, 0, 0] for _ in range(n+1)]
    #print(parent)
    # 왼쪽이 부모 오른쪽이 최소 intensity
    for i in range(n+1):
        parent[i][0] = i

    # 대신 합칠 때 봉우리를 우선으로 합치기

    # 부모 찾기
    def find(a):
        if parent[a][0] != a:
            parent[a][0] = find(parent[a][0])
        return parent[a][0]


    def union(a, b):
        global record
        A = find(a)
        B = find(b)

        if record[a] == 1:
            parent[A][1] = 1

        if record[a] == -1:
            parent[A][2] = 1

        if record[b] == 1:
            parent[B][1] = 1

        if record[b] == -1:
            parent[B][2] = 1

        if A != B:
            #print(a, record[a], b, record[b])
            # a가 봉우리에 더 가깝다면
            if record[A] > record[B]:
                parent[B][0] = A
                parent[A][1] = max(parent[B][1], parent[A][1])
                parent[A][2] = max(parent[B][2], parent[A][2])

            elif record[B] > record[A]:
                parent[A][0] = B

                parent[B][1] = max(parent[B][1], parent[A][1])
                parent[B][2] = max(parent[B][2], parent[A][2])

            elif A < B: # 둘이 같은 성향일 때 더 작은 아이가 임자
                parent[B][0] = A

                parent[A][1] = max(parent[B][1], parent[A][1])
                parent[A][2] = max(parent[B][2], parent[A][2])
            else:
                parent[A][0] = B

                parent[B][1] = max(parent[B][1], parent[A][1])
                parent[B][2] = max(parent[B][2], parent[A][2])
        # 둘 중 하나는 봉우리 하나는 출입구라면
        if parent[find(A)][1]*parent[find(A)][2] == 1:
            return True, A, B
        return False, A, B

    global MIN, PEER
    MIN = float("inf")

    #INT = float("inf")
    PEER = float("inf")

    for p in paths:
        #global MIN, PEER
        print(parent)
        print(p[0], p[1], p[2])
        res = union(p[0], p[1])
        if res[0]:
            if MIN > p[2]:
                MIN = p[2]
            elif MIN < p[2]:
                return [PEER, MIN]

            if record[res[1]] == 1 and record[res[2]] == 1:
                PEER = min(PEER, res[1], res[2])
            elif record[res[1]] == 1:
                PEER = min(PEER, res[1])
            elif record[res[2]] == 1:
                PEER = min(PEER, res[2])



    return list()

#print(solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
#print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4] ))
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],[3, 7], [1, 5] ))
#print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1,2], [5]))

# 3번에서 1번을 먼저 추가한 뒤 5번을 추가하면 1번이 대장으로 인식되는 현상 발생

def solution(n, paths, gates, summits):
    # n : 노드 개수
    # paths : 경로 정보
    # gates : 출입문
    # summits : 봉우리
    # 두 사이의 길이 하나 밖에 없고 무조건 어떤 방식으로든 갈 수 있다.
    # n이 5만개라서 배열 방식은 조금 힘들 것 같다.
    # dfs / 백트래킹은 가능한가? 출입구가 많으면 많을 수록 탐색 횟수가 많아져서 매우 어려워진다.
    # bfs는 가능한가? 마킹하는 방식이라면 가능할 것 같다
    # 그러면 최소값 기록을 하면서 dfs형식으로 가본다

    # 다익스트라?

    # 전략
    # 출입문 출발, 봉우리 도착 시 중단
    # 지나왔던 길을 되돌아가거나 뱅뱅이 돌면 안된다
    # 산봉우리를 기준으로 출력하므로 산봉우리 작은 순서부터 출발해서 출입구로 들어간다
    global min_arr, MIN, edge, PEER
    MIN = float("inf")
    PEER = 0
    def dfs(now, intensity, visit, peer):
        global MIN, PEER
        visit[now] = True # 방문 체크
        #print(now, intensity, visit, peer)
        # 입출구라면 값 갱신
        if min_arr[now] == -1:
            if MIN > intensity:
                MIN = intensity
                PEER = peer
            visit[now] = False
            return
        # 입출구가 아니라면 연결된 길들을 살핀다.
        for next in edge[now]:
            if min_arr[next[0]] != 0 and not visit[next[0]]: # 한 번도 방문한적 없다면
                next_intensity = max(intensity, next[1])  # 둘 중 큰 값으로 변경

                if min_arr[next[0]] == -1 or next_intensity < min_arr[next[0]]: # 그리고 intensity가 최소라면
                    dfs(next[0], next_intensity, visit, peer)
        visit[now] = False

        return


    # 해당 노드에 도달까지 intensity 최소값
    min_arr = [float("inf") for _ in range(n+1)]

    # 편의를 위한 n+1 기록
    edge = [list() for _ in range(n + 1)]

    # 백트래킹 방문체크 배열
    visit = [False for _ in range(n + 1)]

    # 출입문은 -1 값으로 초기화
    for g in gates:
        min_arr[g] = -1

    # 봉우리는 0 값으로 초기화
    for s in summits:
        min_arr[s] = 0

    # 양 방향으로 넣어주기
    for p in paths:
        edge[p[0]].append([p[1], p[2]])
        edge[p[1]].append([p[0], p[2]])

    for s in summits:
        dfs(s, 0, visit, s) # 현재 들어갈 출입구 / intensity / 방문 체크 배열

    return [PEER, MIN]