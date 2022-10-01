def solution(registered_list, new_id):
    global count1, count2
    lst = [ord(n) for n in new_id]
    NUM = []
    L = len(new_id)
    # 소문자 카운팅
    count1 = 0

    for l in lst:
        if 97 <= l <= 122:
            count1 += 1
        else:
            break

    S = new_id[0:count1]
    N = int(new_id[count1:L]) if new_id[count1:L] != "" else 0

    dictionary = dict.fromkeys(registered_list,1)
    if N == 0:
        try:
            dictionary[S]
            N += 1
        except:
            return S

    for i in range(N, 1000000):
        try:
            dictionary[S+str(i)]
        except:
            return S + str(i)



#print(solution(["ace15", "card", "ace16"], "ace15"))
#print(solution(["cow", "cow1", "cow2"], "cow"))
print(chr(65))