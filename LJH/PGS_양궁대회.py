maxscore = 0
maxinfo = []

def solution(n, info):
    def dfs(nn,k,tempinfo):
        global maxinfo, maxscore

        if nn==n:
            scorelion = 0
            scoreapitch = 0
            while len(tempinfo)<11:
                tempinfo.append(0)
            for i in range(11):
                if tempinfo[i]!=0 or info[i]!=0:
                    if tempinfo[i]>info[i]:
                        scorelion += 10-i
                    else:
                        scoreapitch += 10-i
            resscore = scorelion-scoreapitch
            if resscore==0:
                return
            if maxscore>resscore:
                return
            elif maxscore<resscore:
                maxscore=resscore
                maxinfo = tempinfo[:]
            elif maxscore==resscore:
                # if maxinfo==[]:
                #     maxinfo = tempinfo[:]
                # # pass#tempinfo랑 maxinfo 비교 후 갱신
                # else:
                for j in range(10,-1,-1):
                    if tempinfo[j]>maxinfo[j]:
                        maxinfo = tempinfo[:]
                        break
                    elif tempinfo[j]<maxinfo[j]:
                        break
            return

        if k==10 and nn<n:
            dfs(n, k+1, tempinfo+[n-nn])
        # elif info[k]==0:      # 혹시나 해서 지워봤는데 얘가 원인이었다
        #     dfs(nn+1,k+1,tempinfo +[1])
        elif info[k]+1<=n-nn:
            dfs(nn+info[k]+1,k+1,tempinfo+[info[k]+1])
            dfs(nn, k + 1, tempinfo + [0])
        elif info[k]+1>n-nn:
            dfs(nn, k+1, tempinfo+[0])



    dfs(0,0,[])

    if maxinfo:
        answer = maxinfo
    else:
        answer = [-1]
    if maxscore==0:
        answer = [-1]
    return answer


print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))