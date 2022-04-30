"""
BOJ
집합의 표현
골드4
1시간
https://www.acmicpc.net/problem/1717
"""
import sys
sys.setrecursionlimit(10**6)

def find(x):
    # (RecursionError)
    if x == P[x]:
        return x
    else:
        P[x] = find(P[x])
        return P[x]

    # # 시간 초과
    # while x != P[x]:
    #     x = P[x]
    # return x

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        P[y] = x
    else:
        P[x] = y

n, m = map(int, sys.stdin.readline().split())
P = [i for i in range(n+1)] # 자기 자신을 부모로 하는 부모 테이블 생성

for _ in range(m):
    flag, a, b = map(int, sys.stdin.readline().split())
    if flag == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')