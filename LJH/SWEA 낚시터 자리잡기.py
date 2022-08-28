import sys
sys.stdin = open("sample_input.txt", "r")

def sol(a,b,c,depth,lst,res):
    global N, solist, answer
    if depth==3:
        answer = min(answer, res)
        return
    seq = solist[depth]
    if seq[1]%2:
        # 홀수
        pos = 0
        count = 0
        while count!=seq[1]:
            if 0<=(seq[0] + pos) and (seq[0] + pos)<N and lst[seq[0]+pos]==0:
                lst[seq[0] + pos]=1
                res += pos+1
                count += 1
                continue
            elif 0<=(seq[0] - pos) and (seq[0] - pos)<N and lst[seq[0]-pos]==0:
                lst[seq[0] - pos] = 1
                res += pos+1
                count += 1
                continue
            else:
                pos += 1
        sol(a, b, c, depth + 1, lst, res)
    else:
        newlst = lst[:]
        pos = 0
        count = 0
        newres = res
        while count != seq[1]:
            if 0<=(seq[0] + pos) and (seq[0] + pos)<N and newlst[seq[0] + pos] == 0:
                newlst[seq[0] + pos] = 1
                newres += pos+1
                count += 1
                continue
            elif 0<=(seq[0] - pos) and (seq[0] - pos)<N and newlst[seq[0] - pos] == 0:
                newlst[seq[0] - pos] = 1
                newres += pos+1
                count += 1
                continue
            else:
                pos += 1
        sol(a,b,c,depth+1,newlst,newres)

        newlst = lst[:]
        pos = 0
        count = 0
        newres = res
        while count != seq[1]:
            if 0<=(seq[0] - pos) and (seq[0] - pos)<N and newlst[seq[0] - pos] == 0:
                newlst[seq[0] - pos] = 1
                newres += pos+1
                count += 1
                continue
            elif 0<=(seq[0] + pos) and (seq[0] + pos)<N and newlst[seq[0] + pos] == 0:
                newlst[seq[0] + pos] = 1
                newres += pos+1
                count += 1
                continue
            else:
                pos += 1
        sol(a, b, c, depth + 1, newlst, newres)


    return

T = int(input())
for tc in range(T):
    N = int(input())
    answer = float('inf')
    g1, f1 = map(int, input().split())
    g2, f2 = map(int, input().split())
    g3, f3 = map(int, input().split())
    for i in [[g1-1, f1],[g2-1, f2],[g3-1, f3]]:
        for k in [[g1-1, f1],[g2-1, f2],[g3-1, f3]]:
            if i==k:continue
            for h in [[g1-1, f1],[g2-1, f2],[g3-1, f3]]:
                if (i==h or k==h):continue
                lst = [0 for _ in range(N)]
                solist = [i,k,h]
                sol(i,k,h,0,lst,0)
    print(f"#{tc+1} {answer}")