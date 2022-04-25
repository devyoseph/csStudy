#TCP Server

from socket import *

HOST = '127.0.0.1'
PORT = 7777     # 임의의 포트 번호

# 소켓 생성: 주소체계(AF_INET), 통로(Stream)
server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind((HOST, PORT))  # 생성한 소켓에 HOST, PORT를 바인드(매핑)

server_socket.listen(0)  # 매핑한 소켓을 연결 대기
print("요청을 대기 중")

connected_socket, address = server_socket.accept() # 연결될 때 반환되는 실제 통신 소켓과 클라이언트의 주소 할당
print(f'{address} 에서 서버로 접속합니다.') # 연결 완료 알림

data = connected_socket.recv(1024) # 데이터 수신 최대 1024
print(f'클라이언트로부터 수신한 내용: {data.decode("utf-8")}') # 받은 데이터를 utf-8으로 디코드

connected_socket.send("[ Your request treated ]".encode("utf-8")) # 데이터를 인코딩해서 보냄
print("클라이언트에 메시지 전송 완료") # 클라이언트에 메시지 전송 알림

server_socket.close() # 서버 닫기

