# 좌표 압축
# https://www.acmicpc.net/problem/18870

N = input()
li = list(map(int,input().split())) # 공백 한 칸으로 구분된 X1, X2, ..., XN

tmp = sorted(list(set(li))) # 중복값 제거하여 정렬

# 시간 단축을 위해 딕셔너리 인덱싱 이용
dic = {tmp[i]:i for i in range(len(tmp))}
for num in li:
    print(dic[num], end=' ')

# [시간 초과한 방법]
# # input li의 요소와 tmp의 요소가 같은경우 li의 요소에 tmp의 인덱스 값을 넣음
# for num in [tmp.index(n) for i, n in enumerate(li)]:
#     print(num, end=' ')