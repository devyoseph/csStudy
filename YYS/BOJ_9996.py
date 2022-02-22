N = int(input())
p = input().split('*')
l = len(p[0])+len(p[1])
while N > 0:
    N -= 1
    s = input()
    if len(s) < l:
        print('NE')
    elif s.startswith(p[0]) and s.endswith(p[1]):
        print('DA')
    else:
        print('NE')