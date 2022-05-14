'''
PGS
신규 아이디 추천
lv 1
30분
https://programmers.co.kr/learn/courses/30/lessons/72410
'''

def solution(new_id):
    new_id = list(new_id)
    # badword = ['~''!''@''#''$''%''^''&''*''('')''=''+''[''{'']''}'':''?'',''<''>''/']
    goodword = list(map(chr, range(97, 123))) + list(map(str, range(0,10)))+ ['-', '_', '.']
    badwordidx = []
    for i in range(len(new_id)):
        if 'A'<=new_id[i]<='Z':
            new_id[i] = chr(ord(new_id[i])+32)  # 1단계 대->소
        elif new_id[i] not in goodword:
            badwordidx.append(i)
    if new_id:
        for i in range(len(badwordidx)-1,-1,-1):
            new_id.pop(badwordidx[i])   # 2단계 특수문자 제거
    killdotlst = []
    if new_id:
        for i in range(1,len(new_id)):
            if new_id[i-1]==new_id[i]=='.':
                killdotlst.append(i)
        for i in range(len(killdotlst)-1,-1,-1):
            new_id.pop(killdotlst[i])   # 3단계 겹. 제거
    if new_id:
        if new_id[-1]=='.': # 4
            new_id.pop()
    if new_id:
        if new_id[0]=='.':
            new_id.pop(0)
    if not new_id:  # 5
        new_id = ['a']
    if len(new_id)>=16: # 6
        new_id = new_id[:15]
    if new_id[-1]=='.':
        new_id.pop()
    while len(new_id)<=2:   # 7
        new_id.append(new_id[-1])

    answer = ''.join(new_id)
    return answer



print(solution("=.="))
