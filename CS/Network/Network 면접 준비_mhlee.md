# Network 

## OSI 7계층 & TCP/IP 5계층 (주형)

## [TCP] 3 way handshake & 4 way handshake (다같이)

* TCP 프로토콜을 이용하여 통신하는 응용프로그램이 데이터를 전송하기 전에 먼저 정확한 전송을 보장하기 위해 상대방 컴퓨터와 사전에 세션을 수립하는 과정을 의미한다.
* 클라이언트에서 서버로 SYN 패킷을 보내면, 서버가 SYN + ACK 패킷으로 응답하고, 클라이언트가 ACK 패킷으로 응답함으로써 세션 수립과정이 끝난다.
* 세션 수립이 끝난 후 클라이언트와 서버는 모두 ESTABLISHED 상태가 된다.

![img](/Users/mhlee/workspace/csStudy/CS/Network/Network 면접 준비/img.png)



## TCP/IP (흐름제어/혼잡제어) (요셉)

## UDP (성우)

## TCP와 UDP 차이 (미현)

* TCP 는 연결형 서비스로 3-way handshaking을 사용하기 때문에 높은 신뢰성을 보장하지만 속도가 비교적 느리다는 단점이 있고, UDP는 비연결형 서비스로 수신 여부를 확인하지 않기 때문에 속도가 비교적 빠르지만 신뢰성이 떨어진다는 단점이 있습니다.

![image-20220601170409295](/Users/mhlee/workspace/csStudy/CS/Network/Network 면접 준비/image-20220601170409295.png)

## SYN Flooding (주형)

## 프로토콜 (요셉)

## TCP(Transmission Control Protocol) / IP(Internet Protocol) (성우)

## ARP - 네트워크 계층에서 사용하는 주소 결정 프로토콜 / RARP (미현)

* 네트워크 상에서 IP 주소를 물리적 네트워크 주소(MAC 주소) 로 대응시키기 위해 사용되는 프로토콜
* ARP request를 통해 생성한 ARP table 에서 IP에 매칭되는 MAC 주소를 찾아준다.

## 대칭키 & 공개키 (다같이)

* 대칭키 : 암호화와 복호화에 같은 암호키(대칭키)를 사용하는 알고리즘
  * DES, 3DES, AES, SEED, ARIA
* 공개키 : 암호화와 복호화에 사용하는 암호키를 분리한 알고리즘
  * RSA

![img](/Users/mhlee/workspace/csStudy/CS/Network/Network 면접 준비/99EB76495A68F4790C.png)

![공개키알고리즘 Part.1](Network 면접 준비/27120A43587289B82C.jpeg)

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

  ![TLS / SSL](Network 면접 준비/diagram-52@3x.png)

## Transport Layer Security (주형)

HTTPS/SSL/TLS 특징 정리

## HTTP & HTTPS (요셉)

## 로드 밸런싱(Load Balancing) (성우)

##  [Network] Blocking/Non-blocking & Synchronous/Asynchronous (미현)

* Blocking / Non-blocking
  * 호출된 함수가 호출한 함수에게 제어권을 건네주는 유무의 차이. 호출된 함수에서 일을 시작할 때 바로 제어권을 리턴해주느냐(non-blocking), 할일을 마치고 리턴해주느냐(blocking)에 따라 블럭과 논블럭으로 나누어진다.
* Synchronous / Asynchronous
  * 호출된 함수를 호출한 함수가 신경 쓰는지(Synchronous), 호출된 함수가 스스로 신경쓰는지 (Asynchronous) 
  * 비동기는 호출 시 callback 을 전달하여 작업의 완료 여부를 호출한 함수에게 답하게 된다.

![image](Network 면접 준비/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fda50Yz%2Fbtq0Dsje4ZV%2FlGe8H8nZgdBdgFvo7IczS0%2Fimg-20220601190525426.png)

## Blocking I/O & Non-Blocking I/O (주형)

## WEB (요셉)

## HTTP (성우)

## HTTPS (미현)

* TLS를 통해 암호화된 연결을 하는 HTTP를 HTTPS(HTTP Secure)라고 하며, 기본 포트로 443번을 사용한다.
* TLS : 다양한 종류의 보안 통신을 하기 위한 프로토콜, HTTP 뿐만 아니라 FTP, SMTP 와 같은 프로토콜에도 적용한 수 있다. HTTPS는 TLS와 HTTP가 조합된 프로토콜만을 가리킨다.
* HTTP vs HTTPS
  * HTTP는 평문 데이터를 전송하는 프로토콜이기 때문에, HTTP로 비밀번호나 주민번호 등을 주고받으면 제 3자에 의해 조회될 수 있습니다. 
  * HTTPS 는 자신의 공개키를 갖는 인증서를 발급하여 보내는 메세지는 공개키로 암호화 하도록 하여, 공개키로 암호화 된 메시지는 개인키를 가지고 있어야만 복호화가 가능하기 때문에 기업을 제외한 누구도 원본 데이터를 얻을 수 없습니다.
  * TLS는 데이터 무결성을 제공하기 때문에 데이터가 전송 중에 수정되거나 손상되는 것을 방지하고, 사용자가 자신이 의도하는 웹사이트와 통신하고 있음을 입증하는 인증기능도 제공하고 있습니다.

## WEB Server (주형)

## Web Browser (요셉)

## HTML HyperText Mark-up Language (성우)

## 마크업 언어(Markup Language) (미현)

* 문서가 화면에 표시되는 형식을 나타내거나 데이터의 논리적인 구조를 명시하기 위한 규칙들을 정의한 언어의 일종
* 데이터를 기술한 언어라는 점에서 프로그래밍 언어와는 분명한 차이가 있다. 본래는 교정 부호 등을 표기하는데에 사용했지만, 점차 용도가 확장되어 문서의 구조를 표현하도록 발전하였다.

## 월드 와이드 웹(World Wide Web, WWW, W3) (주형)

## 프로그램 (요셉)

## 애플리케이션 (성우)

 ## Software - 소프트웨어 (미현)

* 컴퓨터의 하드웨어 상에서 구동되거나 처리되는 무형물을 뭉뚱그려 지칭하는 말
* 사용자의 시각에서 플랫폼 소프트웨어(운영체제, 장치 드라이버), 응용 소프트웨어(오피스 제품군, 비디오 게임), 사용자 작성 소프트웨어(워드 프로세서 매크로, 스프레드시트 템플릿) 등으로 나눌 수 있다.

## Hardware - 하드웨어 (주형)

## Port - 포트 (요셉)

## GET / POST (성우)

## 쿼리 스트링(Query String) (미현)

* 사용자가 입력 데이터를 전달하는 방법 중의 하나로, url 주소에 미리 협의된 데이터를 파라미터를 통해 넘기는 것을 말한다.
* Query parameters (?key=value) 를 url 뒤에 덧붙여서 추가적인 정보를 서버측에 전달한다. 파라미터가 여러개인 경우 & 를 붙여 여러개의 파라미터를 넘길 수 있다.

## JSON(JavaScript Object Notation) (주형)

## JSON 객체 / JSON 배열 (요셉)

## RESTful API (성우)

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

## REST의 특징 (요셉)

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

## IP 주소와 Hosts의 개념 (요셉)

## DNS Server (성우)

## 쿠키(cookie) (미현)

* 브라우저를 사용하는 환경 (로컬 컴퓨터) 에 서버에서 받은 데이터를 저장한 파일
* 로그인 정보같이 유저가 굳이 서버에 재요청하기에 비효율적인 정보를 로컬에 저장해둠으로써 생산성을 높이는 것이 목적
* ex) 자동 로그인, 오늘 그만보기 팝업창 등

## 세션(session) (주형)

## 쿠키와 세션 (요셉)

## 캐시(cache) (성우)

## 공인 IP와 사설 IP 차이 (미현)

* 공인 IP
  * 전 세계에서 유일한 IP로 ISP(인터넷 서비스 공급자) 가 제공하는 IP 주소
  * 외부에 공개되어 있기 때문에 인터넷에 연결된 다른 장비로부터 접근이 가능하다.
* 사설 IP
  * 어떤 네트워크 안에서 사용되는 IP 주소
  * 네트워크 안에서 라우터를 통해 할당받는 가상의 주소로서, 별도의 설정 없이는 외부에서 접근이 불가능하다.

## IP 주소 클래스 (주형)

## 서브넷, 서브넷팅 (요셉)

## longest prefix matching (성우)

## 블록체인 (미현)

* P2P 방식을 기반으로하여 소규모 데이터들이 체인 형태로 무수히 연결되어 형성된 '블록'이라는 분산데이터 저장 환경에 관리 대상 데이터를 저장함으로써 누구도 임의로 수정할 수 없고, 누구나 변경의 결과를 열람할 수 있게끔 만드는 기술이다.
* 블록체인과 암호화폐 사이에는 밀접한 관계가 있지만, 블록체인이 암호화폐에만 사용될 수 있는 기술은 아니고 암오화혜가 블록체인에 종속적인 것이라고 보면 된다.