# def bfs(dict, start):
#     result = []
#     # for key in dict:
#     #     if not(key in result):
#     #         result += [key]
#     #     for val in dict[key]:
#     #         if not(val in result):
#     #             result += [val]
#     result += [start]
#     while True:
#         for val in dict[start]:
#             pass
#
#     print(result)
#     pass
def bfs(dict, start, node):
    res = [start]
    visited = [0] * (node+1)
    queue = []
    queue += [start]
    head = 0
    rare = 1
    while queue:
        t = queue[head]
        if rare == 1:
            queue = []
            rare = 0
        else:
            queue[head:] = queue[head+1:]
            rare -= 1

        if not visited[t]:
            visited[t] = 1

        for i in dict[t]:
            if not(i in res):
                res += [i]
            if not visited[i]:
                queue += [i]
    #print(res)
    for i in res:
        print(i, end=' ')
    print()
    return


def dfs(dict, start, node):
    # temp_dict = dict
    #
    # for i in temp_dict:
    #     temp_dict[i].reverse()

    res = [start]
    visited = [0] * (node+1)
    visited[start] = 1
    stack = [start]
    top = 0
    while stack:
        t = stack[top]
        if top == 0:
            stack = []
            top -= 1
        else:
            stack = stack[:top]
            top -= 1

        if not visited[t]:
#            visited[t] = 1
            if not (t in res):
                res += [t]
                visited[t] = 1

        for i in dict[t][::-1]:

            if not visited[i]:
                stack += [i]
                top += 1



    for i in res:
        print(i, end=' ')
    print()
    return

def sol(nls):
    # 0번 인덱스 : 유효한지, 1번 인덱스 : 방문여부
    graph = {}
    for i in range(1, 1+nls[0]):
        graph[i] = []

    for _ in range(nls[1]):
        input_data = list(map(int, input().split()))
        #if
        graph[input_data[0]] = graph[input_data[0]] + [input_data[1]]
        graph[input_data[1]] = graph[input_data[1]] + [input_data[0]]
    for i in graph:
        graph[i].sort()

    dfs(graph, nls[2], nls[0])
    bfs(graph, nls[2], nls[0])
    # for i in graph:
    #     print(graph[i])
    #     for j in graph[i]:
    #         print(j)
    #print(graph)

    # for row in range(nls[0]):
    #     print(graph[row])
    # pass

input_data = list(map(int, input().split()))
sol(input_data)