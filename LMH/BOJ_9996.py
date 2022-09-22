# 한국이 그리울 땐 서버에 접속하지
# https://www.acmicpc.net/problem/9996

N = int(input()) # 파일 개수
pattern = input().split('*') # 알파벳 소문자 여러개와 별표(*) 하나로 이루어진 문자열
files = [input() for i in range(N)] # 파일 이름 리스트

for file in files:
    if len(''.join(pattern)) <= len(file) and file.startswith(pattern[0]) and file.endswith(pattern[1]) :
        print("DA")
    else:
        print("NE")