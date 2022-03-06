# 운영체제 면접 예상 질문

### 데드락이란 무엇인가?

교착상태. 프로세스들이 서로가 가진 자원을 기다리며 block 되어있는 상태를 말한다.

데드락은 Mutual exclusion(상호 배제), No preemption(비선점), Hold and Wait(점유와 대기), Circular wait(환형 대기) 를 모두 만족해야 발생한다.

### MMU란 무엇인가?

Memory Management Unit 의 약자로, 논리적 주소를 물리적 주소로 매핑해주는 Hardware device 이다.

MMU에는 접근할 수 있는 물리적 메모리 주소의 최소값(시작값) 을 저장하는 Relocation register와 논리적 주소의 범위를 저장하는 Limit register가 있다.

### race condition 이란 무엇인가? 이로인해 생길 수 있는 문제는?

여러 프로세스들이 동시에 공유 데이터를 접근하는 상황.

데이터의 불일치 문제를 발생시킬 수 있다.

데이터의 일관성 유지를 위해서 동시 수행되는 프로세스 (concurrent process) 들은 동기화 되어야 한다.



### clock algorithm이란?

paging system이 실제로 사용하는 page replacement Algorithm으로 원형 queue와 reference bit을 사용하여 교체 대상 페이지를 선정하는 알고리즘이다. 포인터가 이동하는 중 reference bit 1은 모두 0으로 바꾸고 한 바퀴를 돌때까지 페이지가 참조되지 않으면 0 그래도인 상태로 그 페이지를 교체한다.

### 내부조각과 외부조각

Internal fragmentation(내부 조각) : 

- 프로그램 크기보다 분할의 크기가 큰 경우
- 하나의 분할 내부에서 발생하는 사용되지 않는 메모리 조각
- 특정 프로그램에 배정되었지만 사용되지 않는 공간

External fragmentation(외부 조각) : 분할 2 낭비되는 공간

- 프로그램 크기보다 분할의 크기가 작은 경우
- 아무 프로그램에도 배정되지 않은 빈 곳인데도 프로그램이 올라갈 수 없는 작은 분할



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
|                     |      |                                  |            |

