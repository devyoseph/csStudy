# 2. Application layer

## HTTP

* HTTP (Hypertext transfer protocol)
* TCP : port 80
* Stateless : 서버는 과거 클라이언트 요청에 대한 정보를 보관하지 않는다.

### Non-persistent HTTP

* HTTP 1.0
* 하나의 GET 요청에 대한 해결을 한뒤, 접속을 끊어버림
* 각각의 객체마다 하나의 TCP connection을 사용하기 때문에 대기 시간이 없어 속도가 빠르다.
* 각각의 객체마다 socket을 해당 수만큼 생성하여 메모리의 사용률을 높인다.

### Persistent HTTP

* HTTP 1.1
* 추가적으로 요청할 오브젝트가 있을 수 있기 때문에 소켓 연결을 끊지 않는다.
* 오브젝트(객체) 요청부터는 병렬로 요청한다. 

### RTT

* Round Trip Time

* 작은 패킷이 클라이언트에서 서버로 갔다가, 서버에서 다시 클라이언트로 돌아오는데 걸린 시간