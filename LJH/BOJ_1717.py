import sys
input = sys.stdin.readline

def find_set(x):
    while x != P[x]:
        x = P[x]
    return x

n, m = map(int, input().split())
P = [i for i in range(n+1)]
for _ in range(m):
    num, a, b = map(int, input().split())
    roota = find_set(a)
    P[a] = roota
    rootb = find_set(b)
    P[b] = rootb
    if num==0:
        P[roota] = rootb
    else:
        if roota==rootb:
            print('YES')
        else:
            print('NO')
