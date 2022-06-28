def solution(n, m, x, y, z):
    answer = []
    
    # n개의 도시를 연결
    # 2차원 배열 안에 [도로 번호, 도로 길이] 저장
    # 만약 도로가 없다면 [ -1, 무한대 ] 로 저장
    arr = [[[-1,float("inf")] for _ in range(n+1)] for __ in range(n+1)]

    # 플로이드 워샬을 적용할 배열 
    dist = [[float("inf") for _ in range(n+1)] for __ in range(n+1)]

    # a에서 b로 도로를 저장할 배열
    path = [[list() for _ in range(n+1)] for __ in range(n+1)]

    # m개의 도로 정보를 저장해주기
    for i in range(1, m+1):
        a = x[i-1]
        b = y[i-1]
        c = z[i-1]

        arr[a][b] = [i, c] # 도로 번호, 거리
        arr[b][a] = [i, c] # 도로 번호, 거리

        dist[a][b] = c
        dist[b][a] = c

        path[a][b].append(i) # i 번 도로를 이용해 a, b를 이동한다
        path[b][a].append(i)

    for k in range(1, n+1):
        for i in range(1, n+1):
            if i == k: continue
            for j in range(1, n+1):
                if i == j: continue
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j].clear() # 비운다음
                    path[i][j].extend(path[i][k])
                    path[i][j].extend(path[k][j])
    #print(path)

    # 개수를 세어줄 카운팅 배열
    counting = []
    for i in range(1,n+1):
        counting.append([i, 0]) # 도로번호, 중간 경로 사용 카운팅
    #print(counting)


    for i in range(1, n+1):
        for j in range(1, n+1):
            #print(path[i][j])
            for k in path[i][j]:

                counting[k-1][1] += 1
    #print(counting)
    # 사용된 양대로 정렬
    counting.sort(reverse=True, key=lambda x:x[1])

    # answer에 넣어주기
    for i in range(n):
        answer.append(counting[i][0])

    return answer


print(solution(3,3,[1,1,2],[3,2,3],[1,5,2]))

print(solution(4,4,[1,1,3,4],[3,4,2,2],[2,1,1,2]))