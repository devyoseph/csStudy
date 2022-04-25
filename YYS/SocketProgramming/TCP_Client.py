#TCP Client

from socket import *

IP = '127.0.0.1'
PORT = 7777 # 연결을 원하는 호스트 주소와 포트 번호

client_socket = socket(AF_INET, SOCK_STREAM) # 서버와 같은 형식으로 생성
client_socket.connect((IP, PORT)) # server는 bind / client는 connect
print(f'{IP} 서버에 연결되었습니다.') # 연결 확인

client_socket.send("클라이언트 메시지".encode("utf-8")) # 연결 후 메시지 보내기
print("메시지 전송 완료")

data = client_socket.recv(1024) # 데이터 수신
print(f'서버로부터 수신한 내용: {data.decode("utf-8")}') # 받은 데이터 확인

client_socket.close() # 소켓 닫아주기
