# 운영체제 면접 예상 질문

## 2장 컴퓨터 시스템의 구조

### cpu가 입출력 기기에 접속하는 방식 중 하나인 memory mapped I/O란

- 메모리와 I/O가 하나의 연속된 주소영역에 할당, I/O가 차지하는 만큼 메모리 용량은 감소하나 CPU입장에서는 메모리와 I/O가 동일한 외부기기로 간주되어 액세스하는 데 같은 신호를 사용, 메모리 명령어로 I/O까지 한번에 사용

### DMA란 무엇인가

- 빠른 입출력 장치를 메모리에 가까운 속도로 처리하기 위해 사용
- CPU의 중재 없이 device contrioller가 device의 buffer storage의 내용을 **메모리에 block 단위로 직접 전송**
- 바이트 단위가 아니라 block 단위로 인터럽트를 발생시킴 -> 효율적

### OS의 분류

- 동시 작업 가능 여부
  - 단일 작업(single tasking): 한 번에 하나의 작업만 정리
  - 다중 작업(multi tasking): 동시에 두 개 이상의 작업 정리
- 사용자의 수
  - 단일 사용자: MS-DOS, MS Windows
  - 다중 사용자: UNIX, NT server
- 처리 방식
  - 일괄 처리(batch processing): 작업 요청의 일정량을 모아 한꺼번에 정리
  - 시분할(time sharing): 컴퓨터 처리 능력을 일정한 시간 단위로 분할해 사용
    - 짧은 응답 시간, interactive한 방식
  - 실시간(Realtime): 정해진 시간 안에 어떤 일이 반드시 종료가 보장되어야 함
    - Hard realtime system(경성 실시간 시스템)
    - Soft realtime system(연성 실시간 시스템)

## 3장 프로세스 관리

### 프로세서가 cpu에서 기계어 실행을 하다가 cpu를 내놓는 경우 3가지

- timer interrupt : 할당 시간 만료
- I/O or event wait : I/O나 오래 걸리는 작업 때문에 blocked로 가서 작업이 끝나면 interrupt로 다시 ready que로
- exit : 프로세스 종료

### 사용자 프로그램이 사용하는 함수 3가지

- 사용자 정의 함수
- 라이브러리 함수
  - 자신의 프로그램에서 정의하지 않고 갖다 쓴 함수
  - 자신의 프로그램 실행 파일에 포함되어 있다
- 커널 함수
  - 운영체제 프로그램의 함수
  - 커널 함수의 호출 = 시스템
  - 커널의 코드에 포함

### 프로세스가 종료되는 경우에 대해

- 자발적 종료
  - 마지막 statement 수행 후 exit() 시스템 콜을 통해
  - 자식이 부모에게 output data를 보냄 (via wait)
  - 프로세스의 각종 자원들이 운영체제에게 반납됨
  - 프로그램에 명시적으로 적어주지 않아도 main함수가 리턴되는 위치에 컴파일러가 넣어줌
- 비자발적 종료
  - 부모 프로세스가 자식 프로세스를 강제 종료시킴 (abort)
    - 자식 프로세스가 한계치를 넘어서는 자원 요청
    - 자식에게 할당된 태스크가 더 이상 필요하지 않은 경우
  - 키보드로 kill, break를 친 경우
  - 부모가 종료하는 경우 자식들이 먼저 종료

## 4장 CPU 스케줄링

### 스케줄링 알고리즘 중 SJF의 두가지 방법에 대해 설명하고 장점

- Nonpreemptive : 일단 프로세스가 진행되면 남은 시간보다 더 짧은 CPU burst time을 가진 프로세스가 들어와도 실행 중이던 프로세스를 종료 후 다음 프로세스를 진행
- Preemptive : 남은 시간보다 짧은 CPU burst time을 가진 프로세스가 들어오면 바로 context switch(SRTF- Shortest Remaining Time First)
- 평균 waiting time이 가장 적다

### RoundRobin 방식에서 할당 시간을 정하는 기준

- I/O bound job은 바로 처리되서 나가고 CPU bound job은 적절히 처리되고 나갈 정도의 시간으로 정해야 한다
- 너무 짧으면 overhead가 커진다

### 스케줄링의 성능척도 5가지를 말해보세요

- CPU utilization(이용률)
- Throughput(처리량)
- Turnaround time(소요시간)
- Waiting time(대기시간)
- Response time(응답시간)

## 5장 병행제어 

## 6장 데드락

### 데드락이란 무엇인가?

교착상태. 프로세스들이 서로가 가진 자원을 기다리며 block 되어있는 상태를 말한다.

데드락은 Mutual exclusion(상호 배제), No preemption(비선점), Hold and Wait(점유와 대기), Circular wait(환형 대기) 를 모두 만족해야 발생한다.

## 7장 메모리 관리

## 8장 가상 메모리

### 내부조각과 외부조각

Internal fragmentation(내부 조각) : 

- 프로그램 크기보다 분할의 크기가 큰 경우
- 하나의 분할 내부에서 발생하는 사용되지 않는 메모리 조각
- 특정 프로그램에 배정되었지만 사용되지 않는 공간

External fragmentation(외부 조각) :

- 프로그램 크기보다 분할의 크기가 작은 경우
- 아무 프로그램에도 배정되지 않은 빈 곳인데도 프로그램이 올라갈 수 없는 작은 분할

## 9장 파일시스템

### clock algorithm이란?

paging system이 실제로 사용하는 page replacement Algorithm으로 원형 queue와 reference bit을 사용하여 교체 대상 페이지를 선정하는 알고리즘이다. 포인터가 이동하는 중 reference bit 1은 모두 0으로 바꾸고 한 바퀴를 돌때까지 페이지가 참조되지 않으면 0 그래도인 상태로 그 페이지를 교체한다.

## 10장 입출력 시스템







### MMU란 무엇인가?

Memory Management Unit 의 약자로, 논리적 주소를 물리적 주소로 매핑해주는 Hardware device 이다.

MMU에는 접근할 수 있는 물리적 메모리 주소의 최소값(시작값) 을 저장하는 Relocation register와 논리적 주소의 범위를 저장하는 Limit register가 있다.

### race condition 이란 무엇인가? 이로인해 생길 수 있는 문제는?

여러 프로세스들이 동시에 공유 데이터를 접근하는 상황.

데이터의 불일치 문제를 발생시킬 수 있다.

데이터의 일관성 유지를 위해서 동시 수행되는 프로세스 (concurrent process) 들은 동기화 되어야 한다.



### Processor-Consumer Problem

- Producer생산자 프로세스와 Consumer소비자 프로세스가 존재. 
- Producer 프로세스가 여러 개 있고, Consumer 프로세스가 여러 개 존재.
- 발생할 수 있는 문제: 두 개의 생산자 프로세스가 동시에 도착하면 하나의 비어있는 버퍼에 동시에 두 개의 데이터를 집어 넣으면 문제 발생. 때문에 빈 버퍼에 데이터를 넣는 작업을 그냥 하지 않고 공유 데이터에 lock을 걸어서 다른 프로세스들의 접근을 막은 다음 비어있는 버퍼에 데이터를 집어넣고, 데이터를 집어넣는 작업이 끝나면 lock을 풀어서 다른 생산자 프로세스 혹은 소비자 프로세스가 공유 버퍼에 접근할 수 있게 해줌.



| 키워드              | 단원 | 설명                             | 관련키워드 |
| ------------------- | ---- | -------------------------------- | ---------- |
| preemptive          |      |                                  |            |
| clock algorithm     |      | page replacement Algorithm       |            |
| 내부조각과 외부조각 |      | 메모리 할당 시 생길 수 있는 조각 |            |
| Processor-Consumer  |      | 동기화 문제 중 한가지            |            |
|                     | 5    |                                  |            |
|                     |      |                                  |            |

키워드 

2장

Time sharing : 여러 작업을 수행할 때 컴퓨터 처리 능력을 일정한 시간 단위로 분할하여 사용

Mode bit : 사용자가 프로그램의 잘못된 수행으로 다른 프로그램 및 운영체제에 피해가 가지 않도록 하기 위한 보호 장치, 0 모니터 모드 : OS 코드 수행, 1 사용자 모드 : 사용자 프로그램 수행

Interrupt

동기식 입출력과 비동기식 입출력 : 

DMA(Direct Memory Access) : CPU의 중재 없이 device contrioller가 device의 buffer storage의 내용을 메모리에 block 단위로 직접 전송

3장

Process Control Block (PCB) : 운영체제가 각 프로세스를 관리하기 위해 프로세스당 유지하는 정보

context switch : CPU를 한 프로세스에서 다른 프로세스로 넘겨주는 과정

Scheduler : Long-term scheduler, short-term scheduler, medium-term scheduler

Suspended : 외부적인 이유로 프로세스의 수행이 정지된 상태

프로세스 상태도

스레드(Thred) : 프로세스 내에서 실행되는 흐름의 단위

4장

CPU Scheduler : ready 상태의 프로세스 중에서 이번에 CPU를 줄 프로세스를 고른다

Dispatcher : CPU의 제어권을 CPU scheduler에 의해 선택된 프로세스에게 넘기는 과정이 dispatching이고 디스패처가 이 일을 수행

Round Robin scheduling : 각 프로세스 당 동일한 할당 시간을 가지고 시간이 지나면 다른 프로세스가 CPU를 선점한다

5장

race condition : 하나의 공유 데이터에 동시에 접근하게 되었을 때 생기는 문제

critical section : 공유 데이터를 접근하는 코드

Mutual Exclusion(상호배제) : 공유 불가능한 자원의 동시 사용을 피하기

Semaphore : 두 개의 원자적 함수로 조작되는 정수 변수로서 멀티프로그래밍 환경에서 공유 자원에 대한 접근을 제한하는 방법 - Counting semaphore, Binary semaphore

6장

deadlock  : 둘 이상의 프로세스가 서로 상대방에게 충족될 수 있는 exent를 무한히 기다리는 현상

Bounded-Buffer Problem (Processor-Consumer Problem)

Readers and Writers Problem

Dining-Philocophers Problem

Moniter : 하나의 객체마다 하나의 모니터를 결합하여 모니터는 그것이 결합된 객체가 동시에 두개 이상의 스레드에 의 해 접근할 수 없도록 막는 lock기능을 제공하는 동기화를 수행하는 동기화 도구

7장

deadlock  : 교착상태. 프로세스들이 서로가 가진 자원을 기다리며 block 되어있는 상태를 말한다

Circular wait(환형 대기) : 내가 필요한 조건을 다른 프로세스가 가지는 것의 사이클이 형성

Deadlock Ignorance : 시스템에 deadlock이 발생한 경우 시스템에 비정상적으로 작동하는 것을 사람이 느낀 후 직접 process를 죽이는 등의 방법으로 대처

8장

Address Binding : Compile time binding, Load time binding, Execution time binding(=Run time binding)

MMU(Memory Management Unit) : logical address를 physical address로 매핑해 주는 하드웨어 디바이스. base register(= relocation register : 접근할 수 있는 물리적 메모리 주소의 최솟값)와 limit register(논리적 주소의 범위)를 가진다

Dynamic Loading : 프로세스 전체를 메모리에 미리 다 올리는 것이 아니라 해당 루틴이 불려질 때 메모리에 load하는 것

Dynamic Linking : Linking(소스코드와 라이브러리가 연결되는)을 실행 시간(execution time)까지 미루는 기법

Contiguous allocation : 

Noncontiguous allocation : 

TLB(translation look-aside buffer) : 주소 전환을 빨리하기 위한 캐시 메모리, associative register로 병렬적으로 한번에 있는지를 파악

Segmentation : 프로그램을 의미 단위로 할당

Paged Segmentation : segment가 여러개의 page로 구성

9장

Page replacement : page fault 시 디스크에서 요청한 page를 어떤 frame을 빼앗아와 교체하는 과정

Clock Algorithm : paging system이 실제로 사용하는 page replacement Algorithm으로 원형 queue와 reference bit을 사용하여 교체 대상 페이지를 선정하는 알고리즘

Thrashing : 메모리에 너무 많은 프로그램이 동시에 올라가서 프로그램을 실행하는데 필요한 최소한의 메모리도 없는 상황, page fault를 다루는데 바쁜 상황

10장

directory : 파일의 메타데이터 중 일부를 보관하고 있는 일종의 특별한 파일

Mounting : 루트 파일 디렉토리 특정 디렉토리 이름에다가 다른 파티션에 있는 루트 디렉토리를 마운트 해 주면 usr(마운트 된 디렉토리)에 접근하게 되면 다른 파일의 루트 디렉토리에 접근하는 꼴

11장

Disk Scheduling : seek time(헤드를 해당 실린더로 움직이는데 걸리는 시간)을 최소화하는 것이 목표

SCAN : 요청에 상관없이 일정하게 끝에서 끝으로 이동하면서 처리할 수 있는 요청을 처리

LOOK : SCAN과 유사하나 양끝에 요청이 없으면 헤드가 되돌아간다

RAID : 여러 개의 디스크를 묶어서 사용, 신뢰성 향상 시 동일 정보를 중복 저장, parity(축약)해서 저장

저널링 : 5~30초 단위로 버퍼캐시에서 수정된 내용을 저널영역에 기록하여 파일시스템의 훼손을 방지

Ext4 파일시스템 : Ext2 +저널링, 

LRFU 알고리즘 : LRU와 LFU의 성질을 모두 가진 버퍼캐시 알고리즘
