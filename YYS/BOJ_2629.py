N = int(input())
weight = list(map(int, input().split()))
K = int(input())
problem = list(map(int, input().split()))

arr = set()
arr.add(0)
#print(arr)

for w in weight:
    tmp = set()
    tmp.add(w)
    #print(tmp)
    for s in arr:
        tmp.add(s + w)
        tmp.add(abs(s - w))
        #print("tmp", tmp)
    arr = set.union(arr, tmp)

#print(arr)
        
answer = list()
for p in problem:
    #print(p, p in arr)
    if p in arr: # 검색
        answer.append("Y")
    else:
        answer.append("N")

print(*answer)