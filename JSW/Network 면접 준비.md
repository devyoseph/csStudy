# Network 

## OSI 7계층 & TCP/IP 5계층 (주형)

## [TCP] 3 way handshake & 4 way handshake (다같이)

3-way 가 연결(접속)의 과정

c-s 연결해줘!

s-c ㅇㅋ 연결 해드림

c-s 확인!

4-way 가 연결 해제(접속 해제)의 과정

c-s 더 필요없으니 연결 끊을게!

s-c ㅇㅋ

s-c 연결끊음!

c-s 확인!

## TCP/IP (흐름제어/혼잡제어) (요셉)

## UDP (성우)

전송 계층 프로토콜중 하나

User Datagram Protocol 의 약자이며 

독립적인 관계를 가지는 패킷인 데이터그램을 전송단위로 쓰는 비연결 프로토콜 이다.

핸드쉐이크(연결)이 존재하지 않기때문에 속도가 빠르지만 최소한의 오류만 검출하기 때문에 신뢰성이 낮다.



TCP와 달리 신뢰성과 관련된 기능을 제공해 주지 않지만 빠르기 처리속도가 빠르기 때문에

실시간 스트리밍사이트 같은 분야에 적합한 프로토콜

## TCP와 UDP 차이 (미현)

## SYN Flooding (주형)

## 프로토콜 (요셉)

## TCP(Transmission Control Protocol) / IP(Internet Protocol) (성우)

컴퓨터 사이의 통신 표준, 네트워크 라우팅 및 상호연결에 대한 규칙을 지정하는 프로토콜 세트(혹은 suite)

## ARP - 네트워크 계층에서 사용하는 주소 결정 프로토콜 / RARP (미현)

## 대칭키 & 공개키 (다같이)

대칭키는 메시지를 전송할때 메시지 내용일 알려지면 안되니 암호화를 하고 수신측에서 복호화를 하여 메시지를 읽는데 이때 암호화 할때와 복호화 할때 같은 키를 사용하는것이 대칭키 방식이다

공개키방식은 이때 키가 다른 암호화 방식인데 비대칭키 암호화라고도 한다.

암호화 할때는 누구나 알 수 있는 공개키로 복호화 할때는 개인키로만 복호화를 할 수 있다.



##  TLS/SSL HandShake (다같이)

## Transport Layer Security (주형)

HTTPS/SSL/TLS 특징 정리

## HTTP & HTTPS (요셉)

## 로드 밸런싱(Load Balancing) (성우)

서버가 처리해야할 업무(load)를 여러대의 서버로 나누어서 처리(balancing)하는것을 의미,

한대의 서버에 부하가 집중되지 않토록 트래픽 관리를 해서 서버의 퍼포먼스 상승이 목적

기존서버의 성능을 증가시키는 scale-up 방식과 동일 혹 이하의 성능을 증설하는 scale-out 방식이 존재



계층에 따른 로드 밸런스는 고려x

##  [Network] Blocking/Non-blocking & Synchronous/Asynchronous (미현)

## Blocking I/O & Non-Blocking I/O (주형)

## WEB (요셉)

## HTTP (성우)

Hyper Text Transfer Protocol 

문서를 전송하기 위한 프로토콜

서버와 클라이언트간 메시지를 교환하는 규칙을 정의해둔것 이며 요청과 응답으로 구성되어 있다 

포트는 주로 80을 사용한다.

## HTTPS (미현)

## WEB Server (주형)

## Web Browser (요셉)

## HTML HyperText Mark-up Language (성우)

문서의 형식(형태, 모양)을 정의하는 언어

## 마크업 언어(Markup Language) (미현)

## 월드 와이드 웹(World Wide Web, WWW, W3) (주형)

## 프로그램 (요셉)

## 애플리케이션 (성우)

OS를 제외한 나머지 소프트웨어

펌웨어는 (OS에 가깝다고 생각됨.)

 ## Software - 소프트웨어 (미현)

## Hardware - 하드웨어 (주형)

## Port - 포트 (요셉)

## GET / POST (성우)

get은 클라이언트가 서버에 url 에 해당하는 자료의 전송을 요청하는 메시지(메서드 라고도 하는듯?)이다. 즉 조회 요청

post는 클라이언트가 해당 url에 해당하는 자료의 생성 및 변경을 요청하는것이고 body에 정보가 담겨 있어야 한다.

## 쿼리 스트링(Query String) (미현)

## JSON(JavaScript Object Notation) (주형)

## JSON 객체 / JSON 배열 (요셉)

## RESTful API (성우)

Representational State Transfer

REST 아키텍처의 제약조건을 준수하는 API를 의미



혹은 http 통신에서 어떤 자원에 대한 crud요청을 리소스와 메서드로 표현하여 특정한 형태로 전달하는 방식을 사용하는 api



## RESTful API의 구성요소 (미현)

## URI과 URL의 차이점은? (주형)

## REST의 특징 (요셉)

## 안드로이드의 서버 통신 (성우)



## 응답 코드 (미현)

## DNS(Domain Name System) (주형)

## IP 주소와 Hosts의 개념 (요셉)

## DNS Server (성우)

DNS 를 이용할 수 있도록 주소와 이름을 저장한 서버

## 쿠키(cookie) (미현)

## 세션(session) (주형)

## 쿠키와 세션 (요셉)

## 캐시(cache) (성우)

웹페이지들의 리소스(이미지나 비디오 같은)것들을 사용자pc에 임시 저장하는 임시 저장소

목적은 해당 웹페이지의 재접속시 사용자의 저장소에서 로드 하므로 서버를 거치지 않아 빠르게 

페이지를 로딩하는것에 있음.

## 공인 IP와 사설 IP 차이 (미현)

## IP 주소 클래스 (주형)

## 서브넷, 서브넷팅 (요셉)

## longest prefix matching (성우)

라우터에서 패킷을 포워딩 해줄때 패킷의 목적지 주소와 라우팅 테이블의 엔트리에 저장된 것을 비교하여 가장 많이 매칭되는 엔트리를 선택하여 라우팅을 해주는 개념

## 블록체인 (미현)