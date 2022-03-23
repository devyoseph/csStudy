import sys
#sys.stdin = open('[BOJ]14503_input.txt', 'r')

def sol():
    NM = list(map(int, input().split()))
    rc_d = list(map(int, input().split()))
    mat = []
    for _ in range(NM[0]):
        temp = []
        for val in list(map(int, input().split())):
            temp += [val]
        mat += [temp]
    print(mat)
    #dir = [[, ], [, ], [, ], [, ]]
    pass

sol()