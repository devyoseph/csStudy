N = int(input())
lst = []
def hanoi(x,y,z,depth): # x: 출발, y: 경유, z: 도착
    if depth == 1:
        return [[x,z]]
    return hanoi(x,z,y,depth - 1) + [[x,z]] + hanoi(y,x,z,depth - 1)
print(2**N-1)
for i in hanoi(1,2,3,N):
    print(*i)