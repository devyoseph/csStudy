n, m = list(map(int, input().split()))
p = [0]*(n+1)

def find(a):
    if p[a] == a:
        return a
    p[a] = find(p[a])
    return p[a]

def union(a, b):
    aRoot = find(a)
    bRoot = find(b)

    if aRoot != bRoot:
        p[aRoot] = bRoot

def check(a, b):
    if find(a) == find(b):
        print("YES")
    else:
        print("NO")

for i in range(n+1):
    p[i] = i

for i in range(m):
    type, a, b = list(map(int, input().split()))

    if type:
        check(a, b)
    else:
        union(a, b)