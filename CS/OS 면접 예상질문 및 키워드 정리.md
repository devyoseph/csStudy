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



| 키워드     | 단원 | 설명 | 관련키워드 |
| ---------- | ---- | ---- | ---------- |
| preemptive |      |      |            |
|            |      |      |            |
|            |      |      |            |
|            |      |      |            |
|            |      |      |            |

