from collections import deque
import sys
sys.stdin = open('swea1949_input.txt', 'r')

def height(mat, N):
    tops = []
    l = 0

    for row in range(N):
        for col in range(N):
            if mat[row][col] == l:
                tops.append((row, col))
            elif mat[row][col] > l:
                tops = [(row, col)]
                l = mat[row][col]
    return tops

def sol():
    def BFS(row, col):
        load = -1
        queue = deque()
        queue.append((row, col, 1, mountain[row][col]))
        while queue:
            row, col, level, before = queue.popleft()
            load = max(level, load)
            for dr, dc in delta:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < N and 0 <= nc < N and mountain[nr][nc] < before:
                    queue.append((nr, nc, level + 1, mountain[nr][nc]))
        return load

    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    delta = ((0, 1), (1, 0), (-1, 0), (0, -1))

    tops = height(mountain, N)
    #print(tops)

    how_many_load = 0
    for row in range(N):
        for col in range(N):
            down = 0
            for _ in range(1, K+1):
                mountain[row][col] -= 1
                down += 1
                for top in tops:
                    if (row, col) == top:
                        continue
                    load = BFS(*top)
                    if how_many_load < load:
                        how_many_load = load
                if mountain[row][col] == 0:
                    break
            mountain[row][col] += down

    return how_many_load

T = int(input())
for test_case in range(1, 1+T):
    print(f'#{test_case} {sol()}')