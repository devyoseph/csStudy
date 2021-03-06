# Network 

## OSI 7계층 & TCP/IP 5계층 (주형)

<img src="./Network 면접 준비.assets/image-20220601174037257.png" alt="image-20220601174037257"  />

통신이 일어나는 과정을 단계별로 파악하기 위해 네트워크에 통신이 일어나는 과정을 7단계로 나눈 것.

- 7 계층(응용 계층): 사용자와 직접 상호작용하는 응용 프로그램들이 포함된 계층, HTTP, FTP, SMTP, POP3, IMAP, Telnet 등과 같은 프로토콜이 있고 사용자 인터페이스, 전자우편, 데이터베이스 관리 등의 서비스를 제공한다. 데이터 전송 단위 -  메시지(message)
- 6 계층(표현 계층): 데이터의 형식(Format)을 정의하는 계층. 데이터 전송 단위 -  메시지(message)
- 5 계층(세션 계층): 컴퓨터끼리 통신을 하기 위해 세션을 만드는 계층, 데이터가 통신하기 위한 논리적인 연결. 데이터 전송 단위 -  메시지(message)
- 4 계층(전송 계층): 최종 수신 프로세스로 데이터의 전송을 담당하는 계층, TCP/UDP 프로토콜을 사용하여 통신을 활성화하는 계층,  패킷 생성 및 전송. 데이터 전송 단위 - TCP일 때 Segment  / UDP일 때 Datagram
-  3 계층(네트워크 계층): 패킷을 목적지까지 가장 빠른 길로 전송하기 위한 계층(라우팅). 데이터 전송 단위 - 패킷(packet)
- 2 계층(데이터링크 계층): 데이터의 물리적인 전송과 에러 검출, 흐름 제어를 담당하는 계층, 맥 주소로 통신을 하는 계층으로 전송되는 단위를 프레임, 장비는 브리지, 스위치가 있다. 데이터 전송 단위 - 프레임(frame)
- 1 계층(물리 계층): 데이터를 전기 신호로 바꾸어주는 계층, 케이블, 리피터, 허브를 통해 데이터 전송. 데이터 전송 단위 - 비트(bit)



## [TCP] 3 way handshake & 4 way handshake (다같이)

### TCP 3-way HandShake

> TCP/IP 프로토콜을 이용해 통신을 하는 응용프로그램이 데이터를 전송하기 전 정확한 전송을 보장하기 위해 상대방 컴퓨터와 세션을 수립하는 과정
>
> ```
> Client > Server : TCP SYN
> 
> Server > Client : TCP SYN ACK
> 
> Client > Server : TCP ACK
> ```

<img src="./Network 면접 준비.assets/image-20220601191104667.png" alt="image-20220601191104667"  />

​                   

#### - TCP의 3-way Handshaking 과정

**[STEP 1]**

클라이언트는 서버에 접속을 요청하는 **SYN 패킷**을 보낸다.

이때 클라이언트는 SYN을 보내고 SYN/ACK 응답을 기다리는 SYN_SENT **상태**가 되는 것이다.

 

**[STEP 2]** 

서버는 SYN요청을 받고 A클라이언트에게 요청을 수락한다는 **ACK와 SYN flag 가 설정된 패킷을 발송**하고,

클라이언트가 다시 ACK으로 응답하기를 기다린다. 이때 B서버는 **SYN_RECEIVED 상태**가 된다.

 

**[STEP 3]**

클라이언트는 서버에게 **ACK**을 보내고, 이후부터는 연결이 이루어지고 실제 데이터가 오가게 되는 것이다.

이때의 서버 상태가 ESTABLISHED이다.

**위와 같은 방식으로 통신하는 것이 신뢰성 있는 연결을 맺어 준다는 TCP의 3 Way handshake 방식**이다.

​                 

### TCP 4-way HandShake

> TCP/IP 프로토콜을 이용해 통신을 하는 응용프로그램이 데이터를 전송하기 전 정확한 전송을 보장하기 위해 상대방 컴퓨터와 세션을 수립하는 과정
>
> ```
> Client > Server : TCP FIN
> 
> Server > Client : TCP ACK, FIN(FIN을 보내기 전 data를 보낼 수 있다)
> 
> Client > Server : TCP ACK(마지막 ACK를 보내고 평소 2배이상 time out 시간을 설정)
> ```

<img src="./Network 면접 준비.assets/image-20220601191750670.png" alt="image-20220601191750670" style="zoom:80%;" />

1. 클라이언트는 서버에게 연결을 종료한다는 FIN 플래그를 보낸다.
2. 서버는 FIN을 받고, 확인했다는 ACK를 클라이언트에게 보낸다. (이때 모든 데이터를 보내기 위해 CLOSE_WAIT 상태가 된다)
3. 데이터를 모두 보냈다면, 연결이 종료되었다는 FIN 플래그를 클라이언트에게 보낸다.
4. 클라이언트는 FIN을 받고, 확인했다는 ACK를 서버에게 보낸다. (아직 서버로부터 받지 못한 데이터가 있을 수 있으므로 TIME_WAIT을 통해 기다린다.)

- 서버는 ACK를 받은 이후 소켓을 닫는다 (Closed)
- TIME_WAIT 시간이 끝나면 클라이언트도 닫는다 (Closed)



이렇게 4번의 통신이 완료되면 연결이 해제된다.



## TCP/IP (흐름제어/혼잡제어) (요셉)

> 흐름제어: Host to Host
> 혼잡제어: Host & Router
>
> 해결책 1은 보통 문제가 있는 방식으로 해결책 2를 위주로 공부한다.

​                     

### 1. 흐름제어(Flow Control)

> 송신 측(sender)와 수신 측(receiver)에서는 데이터를 그냥 받는게 아니라 **버퍼를 이용**해 보내고 받는다.
>
> * 데이터를 보내기 전: 버퍼에 하나씩 쌓아두고 순서대로 보낸다
> * 데이터를 받는 곳: 버퍼를 통해 차례차례 받아준다.
>
> **rwnd(receiver window)**: 데이터를 받는 쪽에서 **남은 버퍼의 공간**을 알려준다.(wnd = window)

​                 

#### - 문제점

* 수신 측의 데이터 처리 속도가 송신 측의 데이터 처리보다 빠르면 상관 없지만 송신측의 속도가 빠를 경우 문제가 생긴다.
  * 버퍼의 크기보다 쌓인 데이터가 많아질 경우 데이터 유실이 발생

​                

#### - 해결책 1: Stop and Wait

* 한 패킷마다 확인 응답을 받아야 그 다음 패킷을 전송하는 방법

  <img src="./Network 면접 준비.assets/image-20220601124919966.png" alt="image-20220601124919966" style="zoom: 67%;" />

​                 

#### 해결책 2: Sliding Window(Go Back N ARQ)

* 수신 측의 윈도우 크기를 기준으로 송신측의 윈도우 크기를 맞춘다.
* 윈도우 내부에 있는 세그먼트들을 자유롭게 보내기 시작한다.
  * 보내는 동안 윈도우의 크기는 점점 작아진다.
* Receiver 측에서 현재까지 받은 데이터 번호 + 1 을 ACK로 보내준다
* Sender 측에서 다시 윈도우의 크기를 원상복구하고 시작 위치를 (받은 데이터 번호 + 1) 로 재설정한다.

<img src="./Network 면접 준비.assets/image-20220601125923812.png" alt="image-20220601125923812"  />



### 2. 혼잡제어(Congestion Control)                 

> 송신 측의 데이터 전달과 네트워크의 데이터 처리 속도 차이를 해결하기 위한 기법
>
> Host vs Network(Router): 좀 더 넓은 관점에서의 전송 문제이다.
>
> * 만약 한 라우터에 데이터가 몰릴 경우 라우터는 자신의 데이터를 모두 처리할 수 없게 되고 호스트들은 또 다시 재전송하는 것을 반복해 악순환이 계속된다.

<img src="./Network 면접 준비.assets/image-20220601130428670.png" alt="image-20220601130428670"  />

​               

#### 해결책 1: AIMD(Additive Increase / Multiplicative Decrease)

* 패킷을 하나씩 보내고 잘 도착하면 window의 크기를 하나씩 증가시켜 전송한다.
* 만약 전송에 실패한다면 패킷의 속도를 절반으로 줄인다.
* 오랜 시간이 걸리고 네트워크가 혼잡해지는 상황을 미리 감지하지 못한다.

​               

#### 해결책 2: Slow Start / Fast Retransmit / Fast Recovery

​                

#### 1) Slow Start (느린 시작)

* AIMD와의 공통점: 패킷을 보내고 ACK를 받아 다음 윈도우 크기에 해당하는 패킷을 보낸다.
* AIMD와의 차이점: 윈도우 사이즈가 이전 크기의 두 배가 된다.
* **ssthresh(Slow Start threshold)**: 이 값에 도달하면 더 이상 2배 증가하지 않고 1씩 선형 증가한다. 

​           

#### 2) Fast Retransmit (빠른 재전송)

* 수신 측(라우터)에서 원래 받아야할 패킷이 아닌 그 다음 패킷이 도착한 경우에도 ACK 패킷을 보낸다.
  * 이 때 잘 도착한 패킷의 다음 패킷을 보내므로 불완전한 현재 패킷이 아닌 잘 처리된 이전 패킷 번호+1을 다시 보낸다.
  * **duplicate ACKs** 중복된 패킷을 3번 받으면 재전송을 진행한다. 이 때 window size가 감소한다.
    * 즉 2번의 기회를 주는 것이다(중복 3번 = loss 2번).
* **time out**: 시간이 지나도 ACK가 없을 때는 모든 패킷들이 loss 되었음을 의미하므로 cwnd를 1로, ssthresh를 절반으로 줄인다.

|                | TCP Tahoe                       | TCP Reno                        |
| -------------- | ------------------------------- | ------------------------------- |
| 방식           | Duplicate ACKs와 time out 구분X | Duplicate ACKs와 time out 구분O |
| Duplicate ACKs | cwnd = 1, ssthresh/2            | cwnd/2                          |
| time out       | cwnd = 1, ssthresh/2            | cwnd = 1, ssthresh/2            |

​              

#### 3) Fast Recovery (빠른 회복)

* 혼잡한 상태가 되면 window size를 1이 아닌 절반으로 줄이고 선형 증가시키는 방법이다.
  * 즉, 혼잡상황 이후 순수 AIMD 방식으로 동작한다.



## UDP (성우)

전송 계층 프로토콜중 하나

User Datagram Protocol 의 약자이며 

독립적인 관계를 가지는 패킷인 데이터그램을 전송단위로 쓰는 비연결 프로토콜 이다.

핸드쉐이크(연결)이 존재하지 않기때문에 속도가 빠르지만 최소한의 오류만 검출하기 때문에 신뢰성이 낮다.



TCP와 달리 신뢰성과 관련된 기능을 제공해 주지 않지만 빠르기 처리속도가 빠르기 때문에 실시간 스트리밍사이트 같은 분야에 적합한 프로토콜



## TCP와 UDP 차이 (미현)

TCP 는 연결형 서비스로 3-way handshaking을 사용하기 때문에 높은 신뢰성을 보장하지만 속도가 비교적 느리다는 단점이 있고, UDP는 비연결형 서비스로 수신 여부를 확인하지 않기 때문에 속도가 비교적 빠르지만 신뢰성이 떨어진다는 단점이 있습니다.

<img src="./Network 면접 준비.assets/image-20220601170409295.png" alt="image-20220601170409295"  />

## SYN Flooding (주형)

TCP의 3-way-handshake의 2단계인 Server가 Client에게 SYN패킷과 ACK패킷을 전달하고  메모리 공간인 백로그 큐에 이 연결을 저장하고 응답을 기다리는 과정에서 실제로 존재하지 않는 클라이언트 IP로 응답이 없는 연결을 초기화하기 전에 또 새로운 1단계 요청만을 무수히 보내어 백로그 큐를 포화 상태로 대기해서 다른 서비스를 계속할 수 없게 하는 공격



## 프로토콜 (요셉)

- 서로 다른 기기들 간의 데이터 교환을 원활하게 수행할 수 있도록 표준화시켜놓은 통신 규약

- 이메일을 보낼 수 있는 이유?

  * SMTP(Simple Mail Transfer Protocol)라는 프로토콜이 규정되어있고 전 세계 메일 서버가 이를 따르기 때문이다.

    ​                  

  * 이 외 대표적인 프로토콜들

    * HTTP / HTTPS / IPFS
    * TCP/IP



## TCP(Transmission Control Protocol) / IP(Internet Protocol) (성우)

- 컴퓨터 사이의 통신 표준, 네트워크 라우팅 및 상호연결에 대한 규칙을 지정하는 프로토콜 세트(혹은 suite)



## ARP - 네트워크 계층에서 사용하는 주소 결정 프로토콜 / RARP (미현)

* 네트워크 상에서 IP 주소를 물리적 네트워크 주소(MAC 주소) 로 대응시키기 위해 사용되는 프로토콜
* ARP request를 통해 생성한 ARP table 에서 IP에 매칭되는 MAC 주소를 찾아준다.



## 대칭키 & 공개키 (다같이)

* 대칭키 : 암호화와 복호화에 같은 암호키(대칭키)를 사용하는 알고리즘
  * 장점 : 수행 시간이 짧음
  * 단점 : 안전한 키교환 방식이 요구됨, 사람이 증가할수록 키관리가 어려워짐
  * 대표 알고리즘 : DES, 3DES, AES, SEED, ARIA
* 공개키 : 암호화와 복호화에 사용하는 암호키를 분리한 알고리즘
  * 대칭키의 키교환 문제를 해결하기 위해 등장한 것이 공개키(비대칭키) 암호화 방식
  * **공개키**는 모든 사람이 접근 가능한 키이고 **개인키**는 각 사용자만이 가지고 있는 키
  * A가 B에게 데이터를 보낸다고 할 때, **A는 B의 공개키로 암호화한 데이터**를 보내고 **B는 본인의 개인키로 해당 암호화된 데이터를 복호화**해서 보기 때문에 암호화된 데이터는 B의 공개키에 대응되는 개인키를 갖고 있는 B만이 볼 수 있게 되는 것
  * 대표 알고리즘 : RSA

<img src="./Network 면접 준비.assets/99EB76495A68F4790C.png" alt="99EB76495A68F4790C"  />

<img src="./Network 면접 준비.assets/27120A43587289B82C.jpeg" alt="27120A43587289B82C"  />





##  TLS/SSL HandShake (다같이)

> [참고] https://steady-coding.tistory.com/512

* HTTPS 에서 클라이언트와 서버간 통신 전 SSL 인증서로 신뢰성 여부를 판단하기 위해 연결하는 방식

* SSL handshake 과정

  * 서버는 CA 에 사이트 정보와 공개 키를 전달하여 인증서를 받음
    (클라이언트는 브라우저에 CA 공개키가 내장되어 있다고 가정)
  * ClientHello (암호화 알고리즘 나열 및 전달)
  * ServerHello (암호화 알고리즘 선택)
  * Server Certificate (인증서 전달)
  * Client Key Exchange (데이터를 암호화 할 대칭 키 전달)
  * Client/ServerHello done (정보 전달 완료)
  * Finished (SSL Handshake 종료)


<img src="./Network 면접 준비.assets/diagram-52@3x.png" alt="diagram-52@3x"  />



## Transport Layer Security (주형)

전송 계층 보안으로 기존의 SSL(Secure Socket Layer)가 표준화 된 용어. TCP/IP를 사용할 때 적용되며 독립적인 프로토콜 계층을 만들어 응용 계층과 전송 계층 사이에 속하게 된다. HTTP나 FTP, SMTP와 같은 프로토콜에 적용할 수 있다. 암호화를 통해 기밀성을 보장하며 인증서를 통해 무결성을 보장한다.



## SSL/TSL 과 HTTPS

```
SSL/TSL
공통점: 전송계층 상에서 클라이언트,서버에 대한 인증 및 데이터 암호화 수행
     - 클라이언트와 서버 양단 간 응용계층 및 TCP 전송계층 사이에서,
     - 안전한 보안 채널을 형성해 주는 역할을 하는, 보안용 프로토콜
차이점: SSL v3.0 을 참고로하여 RFC 2246(1999년)으로 표준화된 것이 TLS 임
```

HTTPS: TSL에 HTTP 프로토콜을 얹어서 사용



## HTTP & HTTPS (요셉)

### 1. HTTP

>애플리케이션 계층의 프로토콜이며 TCP 혹은 TLS로 전송된다.
>http:// 를 통해 이 프로토콜을 사용해 정보를 교환하겠다고 선언한다.
>80 포트번호를 사용한다.
>텍스트, 이미지, 영상, JSON 등 거의 모든 형태의 데이터를 전송 가능

​                  

#### 1. 클라이언트-서버 프로토콜

* 요청(Request)과 응답(Response)로 구성되어있다.
* 클라이언트와 서버가 HTTP 메시지를 주고 받으며 통신한다.

​               

#### 2. 구성

* HTTP 요청 메시지: GET, POST, PUT, HEAD, CONNECT, LINK, UNLINK

  * HEAD: 이 메시지에 대한 응답은 본문을 가져서는 안되며, 본문이 존재해도 무시한다.

* HTTP 응답 메시지: 1xx, 2xx, 3xx, 4xx, 5xx 등

  | 응답 메시지        | 설명                                                  | 주요 메시지 |
  | ------------------ | ----------------------------------------------------- | ----------- |
  | 1xx(Informational) | 요청을 받았으며 프로세스를 계속 진행합니다.           |             |
  | 2xx(Success)       | 요청을 성공적으로 받았으며 인식했고 수용하였습니다.   | 200         |
  | 3xx(Redirection)   | 요청 완료를 위해 추가 작업 조치가 필요합니다.         |             |
  | 4xx(Client Error)  | 요청의 문법이 잘못되었거나 요청을 처리할 수 없습니다. | 404, 405    |
  | 5xx(Server Error)  | 서버가 명백히 유효한 요청에 대한 충족을 실패했습니다. | 503(준비X)  |

​           

#### 3. 비연결성 프로토콜

* 종단간 연결 없음: Connectionless
* 이전 상태를 유지하지 않음: **Stateless**

​               

### 2. HTTPS

> HTTP는 전송계층 TCP위에서 동작하는데 별다른 보안 조치가 없다.
> HTTPS 는 **SSL(Secure Sockets Layer)** 라는 보안계층 위에 HTTP를 얹어서 보안을 보장한다.
> 이 방식을 SSL 암호화 통신이라고 한다.
> 443번 포트를 사용한다
>
> **HTTPS**는 대칭키 암호화 방식과 비대칭키 암호화 방식을 둘 다 사용한다.

<img src="./Network 면접 준비.assets/image-20220601140143109.png" alt="image-20220601140143109" style="zoom:67%;" />

#### 1) 대칭키 암호화

* 클라이언와 서버가 동일한 키를 사용해 암호화/복호화 진행
* 키가 노출되면 매우 위험하지만 연산 속도가 빠름

​                 

#### 2) 비대칭키 암호화

* 1개의 쌍으로 구성된 공개키와 개인키를 암호화/복호화 하는데 사용
* 키가 노출되어도 비교적 안전하지만 연산속도가 느림

​                   

#### [ 동작 과정 ] 

1. 클라이언트가 서버에 연결을 시도
2. 서버는 공개키(public key)를 브라우저(클라이언트)에게 넘겨줌
3. 브라우저(클라이언트)는 공개키의 유효성 검사를 진행하고 세션키 발급
4. 서버에서 받은 공개키로 암호화한 뒤 서버로 암호화된 세션키를 보내줌
5. 서버는 개인키로 암호화된 세션키를 복호화해 세션키를 얻어낸다.
6. 이로써 양쪽 모두에게 세션키가 배분되며 세션키(대칭키)를 이용해 HTTP를 암호화한다.

<img src="./Network 면접 준비.assets/image-20220601140920166.png" alt="image-20220601140920166" style="zoom: 33%;" />



## 로드 밸런싱(Load Balancing) (성우)

서버가 처리해야할 업무(load)를 여러대의 서버로 나누어서 처리(balancing)하는것을 의미,

한대의 서버에 부하가 집중되지 않토록 트래픽 관리를 해서 서버의 퍼포먼스 상승이 목적

기존서버의 성능을 증가시키는 scale-up 방식과 동일 혹 이하의 성능을 증설하는 scale-out 방식이 존재



계층에 따른 로드 밸런스는 고려x



##  [Network] Blocking/Non-blocking & Synchronous/Asynchronous (미현)

* Blocking / Non-blocking
  * 호출된 함수가 호출한 함수에게 제어권을 건네주는 유무의 차이. 호출된 함수에서 일을 시작할 때 바로 제어권을 리턴해주느냐(non-blocking), 할일을 마치고 리턴해주느냐(blocking)에 따라 블럭과 논블럭으로 나누어진다.
* Synchronous / Asynchronous
  * 호출된 함수를 호출한 함수가 신경 쓰는지(Synchronous), 호출된 함수가 스스로 신경쓰는지 (Asynchronous) 
  * 비동기는 호출 시 callback 을 전달하여 작업의 완료 여부를 호출한 함수에게 답하게 된다.

<img src="./Network 면접 준비.assets/img2.png" alt="img2" />

## Blocking I/O & Non-Blocking I/O (주형)

Blocking I/O

동기식 입출력(synchronous I/O)

- I/O 요청 후 입출력 작업이 완료된 후에야 제어가 사용자 프로그램에 넘어감
- 구현 방법 1 -> I/O도 낭비
  - I/O가 끝날 때까지 CPU를 낭비시킴
  - 매시점 하나의 I/O만 일어날 수 있음
- 구현 방법 2 -> 효율적
  - I/O가 완료될 때까지 해당 프로그램에게서 CPU를 뺴앗음
  - I/O 처리를 기다리는 줄에 그 프로그램을 줄 세움
  - 다른 프로그램에게 CPU를 줌

Non-Blocking I/O

비동기식 입출력(asynchronous I/O)

- I/O가 시작된 후 입출력 작업이 끝나기를 기다리지 않고 제어가 사용자 프로그램에 즉시 넘어감(I/O 사용 정보랑 무관한 작업을 바로 진행)

- 진행 순서

  1. User Process가 recvfrom 함수 호출 (커널에게 해당 Socket으로부터 data를 받고 싶다고 요청함)

  2. Kernel은 이 요청에 대해서, 곧바로 recvBuffer를 채워서 보내지 못하므로, "EWOULDBLOCK"을 return함.

  3. Blocking 방식과 달리, User Process는 다른 작업을 진행할 수 있음.

  4. recvBuffer에 user가 받을 수 있는 데이터가 있는 경우, Buffer로부터 데이터를 복사하여 받아옴.

     > 이때, recvBuffer는 Kernel이 가지고 있는 메모리에 적재되어 있으므로, Memory간 복사로 인해, I/O보다 훨씬 빠른 속도로 data를 받아올 수 있음.

  5. recvfrom 함수는 빠른 속도로 data를 복사한 후, 복사한 data의 길이와 함께 반환함.



## WEB (요셉)

WEB은 World Wide Web의 약자로 **인터넷이라는 서비스 체계 위에서 동작하는 서비스 중에 하나**입니다.

***\*인터넷에 연결된 컴퓨터를 이용해 사람들과 정보를 공유할 수 있는 거미줄(Web)처럼 얼기설기 엮인 공간을 뜻하는 용어다.\****

 

![img](https://blog.kakaocdn.net/dn/3XPOs/btq5pC7QQpG/gDjDcIGobtilnM7Oulhgp0/img.png)

 

WEB라는 서비스는 어떻게 보면 인터넷에서 동작하는 다른 전체를 합한 것보다 훨씬 더 많이 사용되고 가장 성공적인 서비스이기도 합니다. 그래서 대게 인터넷은 웹으로 보는 경향이 많다고 생각됩니다 하지만 WEB과 인터넷은 서로 다른 것입니다

**인터넷이라는 것은 컴퓨터와 컴퓨터가 연결해주는 네트워크 체계입니다** 이러한 네트워크 체계 위에서 동작하는 서비스가 **WEB, FTP, EMAIL, 스트리밍, 웹캠, 온라인 게임** 등등이며, 이러한 것들이 서로 같은 체계에서 돌아가는 서비스라고 할 수 있습니다.

```
FTP: 파일 전송 프로토콜(File Transfer Protocol)의 약자. FTP란 파일을 이동할 때 사용하는 프로토콜
Email: SMTP와 POP3를 이용한 하나의 서비스
```

​                

#### 서버와 클라이언트 관계

<img src="https://blog.kakaocdn.net/dn/c7VAJM/btq5ngkpY9k/o2YqOVOEGToiSuYK6bEkdK/img.png" alt="img" style="zoom:50%;" />

 

**서버**는 "서브" 정보를 제공한다는 의미로 서버이며, 정보를 제공하는 사업자가 사용하는 컴퓨터 또는 컴퓨터 위에 설치되어 있는 소프트웨어들을 서버라고 부릅니다.

​              

**클라이언트는** 무언가를 **요청**하는 사람을 클라이언트라고 합니다.

즉 서비스 및 데이터를 요청하는 쪽이 클라이언트입니다. 

표면적으로 웹브라우저인 크롬, 파이어폭스, 익스플로러를 **웹 클라이언트**라고 합니다



## HTTP (성우)

Hyper Text Transfer Protocol 

문서를 전송하기 위한 프로토콜

서버와 클라이언트간 메시지를 교환하는 규칙을 정의해둔것 이며 요청과 응답으로 구성되어 있다 

포트는 주로 80을 사용한다.

HTTP는 요청(Request)과 응답(Response)으로 구성되어 있고, 클라이언트가 요청을 하면 서버가 응답을 하는 구조로 되어 있다.

HTTP는 FTP나 텔넷과는 다르게 비연 결식이다. FTP나 Telnet은 클라이언트가 서버에 정보를 요청해도 서버가 클라이언트와 연결을 끊지 않지만, HTTP는 클라이언트가 서버에 정보를 요청하면 응답 코드와 내용을 전송하고 클라이언트와 연결을 종료한다.

우리가 나무 위키에 접속을 했다고 가정하자. 접속하면 클라이언트는 GET명령을 나무 위키 서버에 전송한다. GET 요청을 받은 나무 위키는 응답 코드와 메시지를 전송하고 그것을 브라우저가 뿌려주는 것이다.

 

**HTTP에서 지원하는 요청 메시지**는 다음과 같다.

- **GET**: 클라이언트가 서버에게 **URL에 해당하는** **자료의 전송을 요청**한다.
- HEAD: GET 요청으로 반환될 데이터 중 헤더 부분에 해당하는 데이터만 요청한다.
- **POST**: 클라이언트가 **서버에서 처리할 수 있는** **자료를 보낸다.** 예를 들어, 게시판에 글을 쓸 때 클라이언트의 문서가 서버로 전송되어야 한다.
- PATCH: 클라이언트가 서버에게 지정한 URL의 데이터를 부분적으로 수정할 것을 요청한다.
- **PUT**: 클라이언트가 서버에게 **지정한 URL에 지정한 데이터를 저장할 것**을 요청한다.
- **DELETE**: 클라이언트가 서버에게 **지정한 URL의 정보를 제거할 것을 요청**한다.
- TRACE: 클라이언트가 서버에게 송신한 요청의 내용을 반환해 줄 것을 요청한다.
- CONNECT: 클라이언트가 특정 종류의 프록시 서버에게 연결을 요청한다.
- OPTIONS: 해당 URL에서 지원하는 요청 메시지의 목록을 요청한다.



## HTTPS (미현)

* TLS를 통해 암호화된 연결을 하는 HTTP를 HTTPS(HTTP Secure)라고 하며, 기본 포트로 443번을 사용한다.
* TLS : 다양한 종류의 보안 통신을 하기 위한 프로토콜, HTTP 뿐만 아니라 FTP, SMTP 와 같은 프로토콜에도 적용한 수 있다. HTTPS는 TLS와 HTTP가 조합된 프로토콜만을 가리킨다.
* HTTP vs HTTPS
  * HTTP는 평문 데이터를 전송하는 프로토콜이기 때문에, HTTP로 비밀번호나 주민번호 등을 주고받으면 제 3자에 의해 조회될 수 있습니다. 
  * HTTPS 는 자신의 공개키를 갖는 인증서를 발급하여 보내는 메세지는 공개키로 암호화 하도록 하여, 공개키로 암호화 된 메시지는 개인키를 가지고 있어야만 복호화가 가능하기 때문에 기업을 제외한 누구도 원본 데이터를 얻을 수 없습니다.
  * TLS는 데이터 무결성을 제공하기 때문에 데이터가 전송 중에 수정되거나 손상되는 것을 방지하고, 사용자가 자신이 의도하는 웹사이트와 통신하고 있음을 입증하는 인증기능도 제공하고 있습니다.



## WEB Server (주형)

웹 서버란 HTTP 프로토콜을 이용하여 클라이언트의 GET, POST 등의 메소드를 활용한 요청을 서버에 전달하고 이를 서버라는 또 다른 컴퓨터가 그 요청을 처리하여 다시 클라이언트에게 전달해주는 작업



## Web Browser (요셉)

> **HTML 문서와** **그림, 멀티미디어 파일 등** **WWW**을 기반으로 한 인터넷의 콘텐츠를 검색 및 열람하기 위한 응용프로그램의 총칭

#### 핵심기능

```
브라우저의 핵심 기능은 사용자가 참조하고자 하는 웹페이지를 서버에 요청(Request)하고 서버의 응답(Response)을 받아 브라우저에 표시하는 것이다. 브라우저는 서버로부터 HTML, CSS, Javascript, 이미지 파일 등을 응답받는다. HTML, CSS 파일은 렌더링 엔진의 HTML 파서와 CSS 파서에 의해 파싱(Parsing)되어 DOM, CSSOM 트리로 변환되고 렌더 트리로 결합된다. 이렇게 생성된 렌더 트리를 기반으로 브라우저는 웹페이지를 표시한다.

자바스크립트는 렌더링 엔진이 아닌 자바스크립트 엔진이 처리한다. HTML 파서는 script 태그를 만나면 자바스크립트 코드를 실행하기 위해 DOM 생성 프로세스를 중지하고 자바스크립트 엔진으로 제어 권한을 넘긴다. 제어 권한을 넘겨 받은 자바스크립트 엔진은 script 태그 내의 자바스크립트 코드 또는 script 태그의 src 어트리뷰트에 정의된 자바스크립트 파일을 로드하고 파싱하여 실행한다. 자바스크립트의 실행이 완료되면 다시 HTML 파서로 제어 권한을 넘겨서 브라우저가 중지했던 시점부터 DOM 생성을 재개한다.

이처럼 브라우저는 동기(Synchronous)적으로 HTML, CSS, Javascript을 처리한다. 이것은 script 태그의 위치에 따라 블로킹이 발생하여 DOM의 생성이 지연될 수 있다는 것을 의미한다. 따라서 script 태그의 위치는 중요한 의미를 갖는다.
```

<img src="./Network 면접 준비.assets/image-20220601142051121.png" alt="image-20220601142051121"  />



## HTML HyperText Mark-up Language (성우)

문서의 형식(형태, 모양)을 정의하는 언어



## 마크업 언어(Markup Language) (미현)

* 문서가 화면에 표시되는 형식을 나타내거나 데이터의 논리적인 구조를 명시하기 위한 규칙들을 정의한 언어의 일종
* 데이터를 기술한 언어라는 점에서 프로그래밍 언어와는 분명한 차이가 있다. 본래는 교정 부호 등을 표기하는데에 사용했지만, 점차 용도가 확장되어 문서의 구조를 표현하도록 발전하였다.



## 월드 와이드 웹(World Wide Web, WWW, W3) (주형)

글로벌 네트워크를 의미하는 월드 와이드 웹 (World Wide Web) 의 약자 . 또한 단순히 "웹"이라고도 하며 데이터 전송을 위해 인터넷 또는 네트워크를 사용하는 분산 정보 관리 시스템 중 하나. HTTP 프로토콜을 기반으로 HTML로 작성된 하이퍼텍스트 페이지를 웹 브라우저라는 특정한 프로그램으로 읽을 수 있게 하도록 구성되어 있다.



## 프로그램 (요셉)

소프트웨어의 한 가지로, **어떤 문제를 해결하기 위하여 그 처리 방법과 순서를 기술하여 컴퓨터에 주어지는 일련의 명령문 집합체**를 뜻한다. 쉽게 말해, **사용자의 명령에 반응하는 소프트웨어를 프로그램**이라 한다.

일반적으론, 프로그램은 소프트웨어의 동의어로 취급되는데, 엄밀히 말해, 프로그램은 소프트웨어의 하위 집합이다.

최근에는 애플리케이션 또는 앱이라고 불리기도 한다.

 

입력 물(Input)에 대한 사용자의 명령(Instruction)에 따라 일련의 산출물(Output)을 제공하는 소프트웨어를 말한다.

통상적으로 프로그램은 소프트웨어의 동의어로 사용되나, 소프트웨어가 보다 큰 개념으로 프로그램을 포함하고 있다.

옛날에는 프로그램을 시스템 소프트웨어, 응용 소프트웨어, 유틸리티의 세 가지로 분류했다.

하지만 오늘날엔 유틸리티라는 개념이 점차 사라지며, 프로그램을 주로 시스템 소프트웨어, 응용 소프트웨어, 악성코드(멀웨어)로 분류한다.



## 애플리케이션 (성우)

OS를 제외한 나머지 소프트웨어

펌웨어는 (OS에 가깝다고 생각됨.)



 ## Software - 소프트웨어 (미현)

* 컴퓨터의 하드웨어 상에서 구동되거나 처리되는 무형물을 뭉뚱그려 지칭하는 말
* 사용자의 시각에서 플랫폼 소프트웨어(운영체제, 장치 드라이버), 응용 소프트웨어(오피스 제품군, 비디오 게임), 사용자 작성 소프트웨어(워드 프로세서 매크로, 스프레드시트 템플릿) 등으로 나눌 수 있다.



## Hardware - 하드웨어 (주형)

컴퓨터를 구성하는 기계적 장치, 중앙처리장치(CPU), 기억장치(RAM, HDD), 입출력 장치(마우스, 프린터) 등



## Port - 포트 (요셉)

**각 프로토콜의 데이터가 통하는 논리적 통로**이다.

컴퓨터의 물리적 포트(랜선)에서 데이터가 통해오는 것처럼, **컴퓨터 안에서 각 프로토콜의 데이터가 컴퓨터 내부의 논리적 포트에 따라 흐른다.**



## GET / POST (성우)

- get은 클라이언트가 서버에 url 에 해당하는 자료의 전송을 요청하는 메시지(메서드 라고도 하는듯?)이다. 즉 조회 요청

- post는 클라이언트가 해당 url에 해당하는 자료의 생성 및 변경을 요청하는것이고 body에 정보가 담겨 있어야 한다.



## 쿼리 스트링(Query String) (미현)

* 사용자가 입력 데이터를 전달하는 방법 중의 하나로, url 주소에 미리 협의된 데이터를 파라미터를 통해 넘기는 것을 말한다.
* Query parameters (?key=value) 를 url 뒤에 덧붙여서 추가적인 정보를 서버측에 전달한다. 파라미터가 여러개인 경우 & 를 붙여 여러개의 파라미터를 넘길 수 있다.



## JSON(JavaScript Object Notation) (주형)

- 데이터를 저장하거나 전송할 때 많이 사용되는 경량의 DATA 교환 형식, 자바스크립트 언어에서 객체 속성을 표현하기 위한 방법으로 사용하기 시작한 데이터 구조. 간결하고 쉽게 데이터를 나타내는 방법 중 하나



## JSON 객체 / JSON 배열 (요셉)

>원래는 자바스크립트 언어에서 **객체 속성**을 표현하기 위한 방법으로 사용하기 시작한 **데이터 구조.**
>**간결하고 쉽게 데이터를 나타내는 방법 중 하나(텍스트 형태로 데이터를 쉽고 간편하게 만들 수 있음)**

​               

### JSON 객체

**{ "Key" : Value }**

중괄호로 시작해서 중괄호로 끝나고 그 안에 키와 벨류가 콜론으로 나뉘어 쌍을 이루어 들어간다.

추가하고 싶다면 , 컴마를 붙이고 추가하면 된다.

키 값은 문자열만 가능하고 벨류 값은 문자열, 숫자, 배열 등등 다양한 타입이 가능하다.

Dictionary와 비슷 

​                

### JSON 배열

**대괄호 [ 로 시작**해서, **대괄호 ]로 끝나고**, 사이에 원하는 json객체를 넣어주면 된다.



## RESTful API (성우)

Representational State Transfer

REST 아키텍처의 제약조건을 준수하는 API를 의미



혹은 http 통신에서 어떤 자원에 대한 crud요청을 리소스와 메서드로 표현하여 특정한 형태로 전달하는 방식을 사용하는 api



## RESTful API의 구성요소 (미현)

* REST : 웹에 존재하는 모든 자원 (이미지, 동영상) 에 고유한 URI 를 부여해 활용하는 것으로, 자원에 대한 주소를 지정하는 방법을 의미합니다.
* 즉 REST 는 URI를 통해 자원을 표시하고, HTTP method를 이용하여 해당 자원의 행위를 정해주며 그 결과를 받는 것을 말합니다. RESTful API는 REST 기반의 규칙들을 지켜서 설계된 API를 말합니다.
* REST의 구성요소
  * 자원 (resource) : URI
  * 행위 (Verb) : HTTP method (GET, POST, PUT, DELETE)
  * 표현 (Representations)
  * Restful API 의 장점
    * 그 자체만으로도 API의 목적이 쉽게 이해가 간다.
    * 예로, **HTTP GET https://api.trueshort.com/stock/005930** 요청의 경우, 문서나 주식이 없어도 "[https://api.trueshort.com](https://api.trueshort.com/) 라는 API에서 "주식에 관한 정보를 HTTP 요청을 통해 받아오는 구나" 라는 해석이 쉽게 가능
* RESTful API 유의점
  * `/`는 계층 관계를 나타낼 때 사용
  * URI 마지막 문자로 슬래시를 포함하지 않는다.
  * 하이픈(-) 은 URI 가독성을 높이는데 사용한다.
  * 밑줄(_)은 URI에 사용하지 않는다.
  * 경로에는 소문자가 적합하다.



## URI과 URL의 차이점은? (주형)

URL(Uniform Resource Locator)은 자원이 실제로 존재하는 위치를 가리키며, URI(Uniform Resource Identifier)는 자원의 위치뿐만 아니라 자원에 대한 고유 식별자로서 URL을 의미를 포함한다.

http://torang.co.kr/user?id=107

->  http://torang.co.kr/user 까지는 자원의 실제 위치를 나타내기 때문에 URL이라고 할 수 있으며, 뒤의 쿼리스트링 식별자(?id=107)를 포함하여 URI



## REST의 특징 (요셉)

### 1. Uniform Interface(일관된 인터페이스)

Uniform Interface란, Resource(URI)에 대한 요청을 통일되고, 한정적으로 수행하는 아키텍처 스타일을 의미합니다. 이것은 요청을 하는 Client가 플랫폼(Android, Ios, Jsp 등)에 무관하며, 특정 언어나 기술에 종속받지 않는 특징을 의미합니다. 이러한 특징 덕분에 Rest API는 HTTP를 사용하는 모든 플랫폼에서 요청 가능하며, Loosely Coupling(느슨한 결함) 형태를 갖게 되었습니다.

 

### 2. Stateless(무상태성)

서버는 각각의 요청을 별개의 것으로 인식하고 처리해야 하며, 이전 요청이 다음 요청에 연관되어서는 안 됩니다. 그래서 Rest API는 세션정보나 쿠키 정보를 활용하여 작업을 위한 상태 정보를 저장 및 관리하지 않습니다. 이러한 무상태성 때문에 Rest API는 서비스의 자유도가 높으며, 서버에서 불필요한 정보를 관리하지 않으므로 구현이 단순합니다. 이러한 무상태성은 서버의 처리방식에 일관성을 부여하고, 서버의 부담을 줄이기 위함입니다.

 

### 3. Cacheable(캐시 가능)

Rest API는 결국 HTTP라는 기존의 웹 표준을 그대로 사용하기 때문에, 웹의 기존 인프라를 그대로 활용할 수 있습니다. 그러므로 Rest API에서도 캐싱 기능을 적용할 수 있는데, HTTP 프로토콜 표준에서 사용하는 Last-Modified Tag 또는 E-Tag를 이용하여 캐싱을 구현할 수 있고, 이것은 대량의 요청을 효율적으로 처리할 수 있게 도와줍니다.

 

### 4. Client-Server Architecture (서버-클라이언트 구조)

Rest API에서 자원을 가지고 있는 쪽이 서버, 자원을 요청하는 쪽이 클라이언트에 해당합니다. 서버는 API를 제공하며, 클라이언트는 사용자 인증, Context(세션, 로그인 정보) 등을 직접 관리하는 등 역할을 확실히 구분시킴으로써 서로 간의 의존성을 줄입니다.

 

### 5 . Self-Descriptiveness(자체 표현)

Rest API는 요청 메시지만 보고도 이를 쉽게 이해할 수 있는 자체 표현 구조로 되어있습니다. 아래와 같은 JSON 형태의 Rest 메시지는 http://localhost:8080/board로 게시글의 제목, 내용을 전달하고 있음을 손쉽게 이해할 수 있습니다. 또한 board라는 데이터를 추가(POST)하는 요청임을 파악할 수 있습니다.

 

```
HTTP POST , http://localhost:8080/board

{
	"board": {
		"title":"제목",
		"content":"내용"
	}
}
```

 

### 6. Layered System(계층 구조)

Rest API의 서버는 다중 계층으로 구성될 수 있으며 보안, 로드 밸런싱, 암호화 등을 위한 계층을 추가하여 구조를 변경할 수 있습니다. 또한 Proxy, Gateway와 같은 네트워크 기반의 중간 매체를 사용할 수 있게 해 줍니다. 하지만 클라이언트는 서버와 직접 통신하는지, 중간 서버와 통신하는지 알 수 없습니다.



## 안드로이드의 서버 통신 (성우)



## 응답 코드 (미현)

* 클라이언트가 보낸 HTTP 요청에 대한 서버의 응답 코드로, 상태 코드에 따라 요청의 성공/실패 여부를 판단합니다.

* 1XX : [정보 전달] 요청을 받았고, 작업을 진행 중
* 2XX : [성공] 작업을 성공적으로 받았고, 이해했으며, 받아들여졌다.
  * 200 : OK. 성공적으로 처리했을 때 쓰인다. 가장 일반적으로 볼 수 있는 HTTP 상태.
  * 204 : No Content. 성공적으로 처리했지만 컨텐츠를 제공하지는 않는다. 일반 사용자가 볼 일은 거의 드물며 처리 결과만 중요한 API 요청 등에서 주로 사용한다.
  * 206 : Partial Content. 컨텐츠의 일부 부분만 제공한다. 보통 클라이언트에서 시작 범위나 다운로드할 범위를 지정한 경우 자동으로 해당 부분만 제공할 때 사용하는 코드이다.
* 3XX : [리다이렉션] 이 요청을 완료하기 위해서는 리다이렉션이 이루어져야 한다는 의미
* 4XX : [클라이언트 오류] 이 요청은 올바르지 않다는 의미. 여기서부터 브라우저에 직접 표현된다.
  * **400 Bad Request**(잘못된 요청): 요청 자체가 잘못되었을 때 사용하는 코드이다.
  * **401 Unauthorized**(권한 없음): 인증이 필요한 리소스에 인증 없이 접근할 경우 발생한다.
  * **408 Request Timeout**(요청 시간 초과) : 요청 중 시간이 초과되었을때 사용하는 코드이다.
* 5XX : [서버 오류] 서버가 응답할 수 없다는 의미이며, 요청이 올바른지의 여부는 알 수 없다.



## DNS(Domain Name System) (주형)

호스트의 도메인 이름을 호스트의 네트워크 주소로 바꾸거나 그 반대의 변환을 수행할 수 있도록 하기 위해 개발된 분산형(중앙 집중이면 그 주변으로 트래픽 과부하가 일어난다) 데이터베이스 시스템. 도메인 이름을 IP 주소로 변환하고 라우팅 정보를 제공한다. 한 서버가 모든 IP에 대해 DNS 서비스를 제공할 수 없으므로 계층적으로 구현되어 있다.



## IP 주소와 Hosts의 개념 (요셉)

> IP와 IP 주소는 다름 개념이다.
>
> IP: 송신 호스트와 수신 호스트가 패킷 교환 네트워크(패킷 스위칭 네트워크, Packet Switching Network)에서 정보를 주고받는 데 사용하는 정보 위주의 규약(프로토콜, Protocol)
>
> **MTU(Maximum Transmission Unit)**
> TCP/IP 네트웍 등과 같이 패킷 또는 프레임 기반의 네트웍에서 전송될 수 있는 최대크기의 패킷 또는 프레임을 가리키며, 대개 옥텟을 단위로 사용한다.       

​              

### 1. IP 주소 (Internet Protocol address, IP address)

* 컴퓨터 네트워크에서 장치들이 서로를 인식하고 통신을 하기 위해서 사용하는 특수한 번호
  네트워크에 연결된 장치가 라우터이든 일반 서버이든, 모든 기계는 이 특수한 번호를 가지고 있어야 한다.
* IP 와 IP 주소는 다른 개념이다.

​              

#### IP version 4 주소

>IPv4 주소는 오늘날 일반적으로 사용하는 IP 주소이다.
>이 주소의 범위는 32비트로 보통 0~255 사이의 십진수 넷을 쓰고 **.**으로 구분하여 나타낸다.
>따라서 0.0.0.0부터 255.255.255.255까지가 된다. 이론적으로 42억9496만7296개의 IP가 존재한다.
>중간의 일부 번호들은 특별한 용도를 위해 예약되어 있다.(ex. 127.0.0.1 = localhost )

#### IP version 6 주소

```
2001:0DB8:1000:0000:0000:0000:1111:2222
```

> 모든 단말에 주소를 부여하기에 32비트로는 부족해짐에 따라 IP의 새로운 버전인 버전 6에서는 주소 길이를 128비트로 늘렸다. 
> IPv6 주소는 보통 두 자리 16진수 여덟 개를 쓰고 각각을 **:** 기호로 구분한다.

​                 

### 2. Host

```
인터넷이 연결된 장치를 Host라고 한다
```

> 인터넷에서 호스트는, 인터넷을 통해 다른 컴퓨터들과 쌍방향 통신이 가능한 컴퓨터를 말한다.
> 호스트는 특정한 호스트번호를 갖는데, 이는 네트워크 번호와 합해져서, 고유의 IP 주소를 이룬다.
> 인터넷 서비스 제공업체를 통한 PPP 사용자의 경우에는, **접속되어있는 동안에만** 고유한 IP 주소를 갖게되며, 그 시간동안은 해당 사용자의 컴퓨터도 하나의 호스트가 되는 것이다.
> 이러한 맥락에서 보면, 호스트란 네트워크를 구성하는 하나의 노드라고 볼 수도 있다.



## DNS Server (성우)

DNS 를 이용할 수 있도록 주소와 이름을 저장한 서버



## 쿠키(cookie) (미현)

* 브라우저를 사용하는 환경 (로컬 컴퓨터) 에 서버에서 받은 데이터를 저장한 파일
* 로그인 정보같이 유저가 굳이 서버에 재요청하기에 비효율적인 정보를 로컬에 저장해둠으로써 생산성을 높이는 것이 목적
* ex) 자동 로그인, 오늘 그만보기 팝업창 등



## 세션(session) (주형)

서버에서 유저의 인증 상태 (로그인 여부 등)을 임시로 저장한 파일, 방문자가 웹 서버에 접속해 있는 상태를 하나의 단위로 보고 그것을 세션이라고 한다

- 웹 서버에 웹 컨테이너의 상태를 유지하기 위한 정보를 저장한다.

- 브라우저를 닫거나, 서버에서 세션을 삭제했을때만 삭제가 되므로, 쿠키보다 비교적 보안이 좋다.

- 서버에 저장되어있어서 쿠키보다 다소 느리고 유저 정보가 많으면 메모리 과부하가 생길 수 있음.

- 서버에서 관리하기 때문에 로그관리 용이함.

- 사용 예 : 로그인 한 정보들



## 쿠키와 세션 (요셉)

- 공통점 : **데이터를 임시로 계속 저장해두는 역할.**
- 차이점 : **쿠키는 사용자에게 저장되고 세션은 서버에 저장됨.**

웹 개발 시 어떤 정보를 쿠키로 저장할지, 세션으로 저장할지 적절히 판단하는 것이 중요하다.



#### 쿠키와 세션의 사용 이유

```
stateless한 HTTP 통신의 단점을 보완하기 위해 사용한다.
client 단위로 상태 정보를 유지해야 하는 경우 Cookie와 Session이 사용된다.
```

​                  

## Session & Cookie 정리

|           | Session                                                      | Cookie                                                       |
| --------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Type      | javax.servlet.http.HttpSession(interface)                    | javax.servlet.http.Cookie(Class)                             |
| 저장 위치 | Server의 memory에 Object로 저장                              | Client 컴퓨터에 file로 저장                                  |
| 저장 형식 | Object는 모두 가능 (Dto, List 등)                            | file에 저장되기 때문에 String 형태                           |
| 사용 예   | 로그인 시 사용자 정보, 장바구니 등                           | 최근 본 상품 목록, 아이디 저장(자동 로그인),<br />오늘은 그만 열기 등 |
| 용량 제한 | 제한 없음                                                    | 도메인당 20개, 1쿠키당 4KB                                   |
| 만료시점  | 알 수 없음(Client가 로그아웃 하거나 일정 시간 session에 접근하지 않을 경우): 만료시간은 web.xml에 설정 | 쿠키 저장 시 설정(설정이 없는 경우 Browser 종료 시 만료)     |
| 공통      | 전역에 저장하기 때문에 project내의 모든 JSP에서 사용 가능<br />Map 형식으로 관리하기 때문에 key 값의 중복을 허락하지 않는다. |                                                              |



## 캐시(cache) (성우)

웹페이지들의 리소스(이미지나 비디오 같은)것들을 사용자pc에 임시 저장하는 임시 저장소

목적은 해당 웹페이지의 재접속시 사용자의 저장소에서 로드 하므로 서버를 거치지 않아 빠르게 

페이지를 로딩하는것에 있음.



## 공인 IP와 사설 IP 차이 (미현)

* 공인 IP
  * 전 세계에서 유일한 IP로 ISP(인터넷 서비스 공급자) 가 제공하는 IP 주소
  * 외부에 공개되어 있기 때문에 인터넷에 연결된 다른 장비로부터 접근이 가능하다.
* 사설 IP
  * 어떤 네트워크 안에서 사용되는 IP 주소
  * 네트워크 안에서 라우터를 통해 할당받는 가상의 주소로서, 별도의 설정 없이는 외부에서 접근이 불가능하다.



## IP 주소 클래스 (주형)

클래스란 IP주소에서 네트워크 주소 영역(서브넷 영역)과 호스트 주소 영역을 나누는 방법

A, B, C, D, E 5가지 클래스가 있는데 D, E는 멀티캐스트용, 연구용으로만 사용



A클래스

- 0xxx xxxx. | xxxx xxxx. xxxx xxxx. xxxx xxxx , 앞 부분이 네트워크 부분이고 나머지가 호스트 영역
- 하나의 네트워크가 가질 수 있는 호스트 수가 가장 많은 클래스
- 맨 앞자리 수가 0이여야 하므로 십진수로는 0.0.0.0 ~ 127.255.255.255
- 네트워크 주소 0과 127은 제외(약속)
- IP주소 중에서 1부터 126으로 시작하는 네트워크는 A클래스
- 호스트 주소는 갯수는 2^24 - 2 -> 모두 0인 경우는 네트워크 주소로 모두가 1인 경우는 브로드캐스트 주소로 사용해서 2개 제외



B클래스

- 10xx xxxx. xxxx xxxx. | xxxx xxxx. xxxx xxxx
- 128.0.0.0 ~ 191.255.255.255, 네트워크 주소 범위는 2^14 개, 호스트 주소범위는 2^16-2개



C클래스

- 110x xxxx. xxxx xxxx. xxxx xxxx. | xxxx xxxx
- 128.0.0.0 ~ 191.255.255.255, 네트워크 주소 범위는 2^21 개, 호스트 주소범위는 2^8-2개



## 서브넷, 서브넷팅 (요셉)

### IPv4 클래스      

* 관련 용어: CIDR(Classless Inter-Domain Routing)

> IP 주소는 대역에 따라 A,B,C,D,E 클래스로 나뉜다.
> 이 클래스들을 구분함으로써 클래스 내에서 Network ID와 Host ID를 구분하게 된다. 각 클래스의 간략한 설명은 다음과 같다
>
> A Class : 대규모 네트워크 환경에 쓰이며, 첫번째 마디의 숫자가 0~127까지 사용된다. (ex : 12.123.123.123)
> B Class : 중규모 네트워크 환경에 쓰이며, 첫번째 마디의 숫자가 128~191까지 사용된다. (ex : 128.123.123.123)
> C Class : 소규모 네트워크 환경에 쓰이며, 첫번째 마디의 숫자가 192~223까지 사용된다. (ex : 192.168.0.1)
> D Class : 멀티캐스팅용으로 쓰인다. 잘 쓰이지 않는다.
> E Class : 연구/개발용 혹은 미래에 사용하기 위해 남겨놓은 클래스로 일반적인 용도로 사용되지 않는다.

​                 

### 서브넷의 등장 배경

> 흔히 사용되는 IPv4 주소 체계는 클래스 방식은 매우 비효율적이다. 예를 들어 어떤 기관에 A 클래스를 할당한다고 하면 16,777,214개의 호스트를 할당할 수 있게 되는데, 이 기관이 100개의 호스트를 할당한다고 하더라도 16,777,114개의 호스트가 낭비되게 된다. 이러한 비효율성을 해결하기 위해 네트워크 장치들의 수에 따라 효율적으로 사용할 수 있는 서브넷(subnet)이 등장하게 되었다

​            

### 서브넷 & 서브넷 마스크

> **서브넷**은 IP 주소에서 네트워크 영역을 부분적으로 나눈 부분 네트워크를 뜻한다.
> **서브넷 마스크**는 IP 주소 체계의 Network ID와 Host ID를 분리하는 역할을 한다. 

* 기본 서브넷 마스크(D, E 클래스를 사용하지 않음

  * IP 주소의 Network ID와 Host ID를 구분할 수 있다.

  <img src="./Network 면접 준비.assets/image-20220601151707734.png" alt="image-20220601151707734" style="zoom:67%;" />

* Network ID: IP주소와 서브넷 마스크를 AND 연산해 얻어낸다.

  <img src="./Network 면접 준비.assets/image-20220601152326602.png" alt="image-20220601152326602" style="zoom:67%;" />

  ```
  예시의 IP주소를 보면 192.168.32.0/24 처럼 /24 같은 표시가 붙어있는 것을 확인할 수 있다. 이것은 서브넷 마스크의 bit 수(왼쪽에서부터 1의 개수)를 나타낸다. 즉 /24는 해당 IP의 서브넷 마스크의 왼쪽에서부터 24개가 1이라는 것을 의미한다. 
  ```

  ​                  

### 서브네팅

> 서브넷팅은 IP 주소 낭비를 방지하기 위해 **원본 네트워크를 여러개의 서브넷으로 분리하는 과정**을 뜻한다.
> 서브넷팅은 **서브넷 마스크의 bit 수를 증가**시키는 것이라고 생각하면 이해가 편하다.
> 서브넷마스크의 bit수를 1씩 증가시키면 할당할 수 있는 네트워크가 2배수로 증가하고 호스트 수는 2배수로 감소한다.

* 서브넷 마스크 bit 수를 24 -> 25로 증가

  <img src="./Network 면접 준비.assets/image-20220601152621368.png" alt="image-20220601152621368" style="zoom:67%;" />



## longest prefix matching (성우)

라우터에서 패킷을 포워딩 해줄때 패킷의 목적지 주소와 라우팅 테이블의 엔트리에 저장된 것을 비교하여 가장 많이 매칭되는 엔트리를 선택하여 라우팅을 해주는 개념



## 블록체인 (미현)

* P2P 방식을 기반으로하여 소규모 데이터들이 체인 형태로 무수히 연결되어 형성된 '블록'이라는 분산데이터 저장 환경에 관리 대상 데이터를 저장함으로써 누구도 임의로 수정할 수 없고, 누구나 변경의 결과를 열람할 수 있게끔 만드는 기술이다.
* 블록체인과 암호화폐 사이에는 밀접한 관계가 있지만, 블록체인이 암호화폐에만 사용될 수 있는 기술은 아니고 암오화혜가 블록체인에 종속적인 것이라고 보면 된다.