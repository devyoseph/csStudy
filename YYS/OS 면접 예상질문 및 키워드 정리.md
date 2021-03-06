# 운영체제 면접 예상 질문

> 2022-03-09 수요일에 최종 질문들을 분류하고 자신에게 맞는 최적 답안을 완성합니다.
>
> 또한 단원마다 필요한 키워드를 취합하여 2학기 면접에서 바로 사용할 수 있는 자료로 갈무리합니다.

​          

## < 중간 범위 >

> 중간범위의 질문들.

### 운영체제에 대해 간략하게 설명해주세요

* 양요셉: 운영체제는 하드웨어 바로 위에 설치되는 소프트웨어 계층으로 하드웨어의 자원을 효율적으로 관리하는 역할을 합니다.

​         

### 운영체제의 목적에 대해 설명하시오

* 양요셉: 운영체제의 목적은 하드웨어의 자원을 효율적으로 관리하는 것입니다. 주어진 자원을 효율적으로 관리하 자원을 프로그램들에 형평성있게 배분해야합니다.

​         

### blocked와 suspended는 어떤 점에서 다른가요?

* 양요셉: block은 CPU 사용을 효율적으로 하기 위해 프로세스가 I/O 작업을 처리해야하는 경우나 공유 자원에 접근할 때 큐 대기열에 넣어 프로세스를 대기하도록 하는 방식입니다. 반면 suspend는 메모리의 사용을 효율적으로 하기 위해 프로세스의 CPU사용 시간이 끝난 경우(타이머에 의한)나 Page fault에 의해 강제로 Swap Area로 이동시켜 프로세스의 수행 작업을 보관합니다. 

​       

### 부모 프로세스와 자식 프로세스가 실행될 때 자원은 어떻게 관리되나요?

* 양요셉: 부모 프로세스는 fork() 명령어를 통해 자기 자신을 복제하고 스스로 wait상태로 들어갑니다. 자식 프로세스의 PID값은 0으로 if문을 통해 부모 프로세스와 다른 코드를 실행하도록 하며 정상적으로 수행하는 경우 exit 명령어를 통해 부모프로세스를 깨웁니다. 자식 프로세스가 배정된 자원 이상을 요청한다면 부모 프로세스는 자식 프로세스를 종료합니다. 부모가 종료되거나 또는 사용자가 kill을 하는 경우 부모는 자식 프로세스를 차례 차례 종료하고 자기 자신을 종료합니다.

​           

### Multilevel Queue 에서 생길 수 있는 문제점, 해결방안

* 양요셉: multi level queue는 사용자 친화적인 프로세스를 foreground, 사용자와 상호작용하지 않는 프로세스를 background 큐에 넣어 CPU 제어를 관리합니다. Foreground 큐가 우선시되기 때문에 Starvation 문제가 발생할 수 있으므로 큐마다 적절한 CPU 시간을 할당해야합니다. 이를 구체적으로 사용한 예시가 Multilevel feedback queue입니다. Multilevel feedback queue는 해당 프로세스가 기준 시간 안에 작업을 완료하지 못한 경우 하위 레벨의 큐로 떨어져 우선순위를 점점 낮우는 방식을 사용합니다.

​         

### 프로세스가 생성(new)되어 종료(terminated)될때까지의 프로세스 상태 변화에 대해 설명하시오.

* 앙요셉: 메모리에 올라온 프로세스는 CPU를 사용하기 위해 Ready queue에 들어갑니다. 차례가 되면 CPU에서 실행하는데 이를 Running 상태라고 합니다. 중간에 I/O작업을 처리하는 경우 Blocked 상태가 되며 타이머에 Interrupt되는 경우 기존 수행 데이터는 Swap area에 suspend되고 프로세는 다시 Ready Queue 대기열 맨 뒤로 이동합니다. 작업을 모두 완료하는 경우 모든 자원을 반납하고 종료합니다.

​      

### RoundRobin 방식에서 할당 시간을 정하는 기준은?

* 양요셉: (SJF는 평균대기시간을 최소화할 수 있지만 Starvation 문제가 발생할 수 있다는 문제점이 있습니다.) RR방식은 프로세스마다 CPU를 형평성 있게 사용하도록 합니다. 그래서 Starvation 문제 등 기복없이 프로세스 작업을 처리할 수 있다는 장점이 있습니다. 프로세스의 작업은 I/O나 CPU 사용이 치우친 경우가 많은데 이런 상황에서 좋은 효율을 낼 수 있습니다.

​        

### 스케줄링 알고리즘 중 SJF

* Shortest Job First 작업은 CPU 이용 시간이 짧은 프로세스를 우선적으로 처리해 전체 프로세스의 평균 대기시간을 최소화할 수 있는 방식입니다. 하지만 CPU작업시간이 매우 긴 프로세스는 제어권을 받지 못하는 Starvation문제가 발생할 수 있습니다. 이에 대비하여 Aging방식을 통해 시간이 흐를수록 우선순위에 가중치를 부여하는 등 방식을 생각해볼 수 있습니다.

​       

### Modebit의 역할은 무엇인가요? 그리고 어떤 방식으로 작동하나요?

* 양요셉: Mode Bit은 이중 동작 모드(Dual-mode-Operation)에서 사용하는 방식입니다. 사용자의 프로그램이 잘못된 수행으로 (메모리 자원을 망가뜨려) 운영체제에 피해를 줄 수 있는데 이에 대한 보호 장치로 Mode bit를 사용합니다. 프로그램의 기본 모드 비트는 1이며 user 모드라고 부릅니다. 프로그램은 시스템 콜을 통해 monitor mode(모드 비트가 0)로 변경해 특권 명령을 사용할 수 있습니다.

​         

### 장기 스케줄러와, 중기 스케줄러의 차이는?

* 양요셉: 장기 스케줄러는 프로세스는 new에서 Ready 상태로 바꿔주는 역할을 합니다. 즉 메모리를 부여하는 역할을 합니다. 일반적인 운영체제에서는 사용하지 않는 방식입니다. 중기 스케줄러는 프로세스에게서 Memory를 빼앗는 방식입니다. 빼앗긴 프로세스는 Swap Area로 이동합니다.

​      

### 프로세스의 생명 주기에서 suspended의 특징

* 양요셉: 외부적인 이유로 프로세스가 정지된 상태입니다. block은 자신이 요청한 작업이 완료되면 다시 Ready 상태로 되지만 Suspend는 외부에서 resume 해주어야 Active한 상태가 될 수 있습니다.

​       

### 인터럽트란?

* 양요셉: CPU에 인터럽트가 발생하면 CPU가 관리하고 있는 프로세스의 레지스터와 program counter는 저장되고 인터럽트 처리루틴을 따릅니다. 하드웨어가 발생시킬 수도 있지만 프로그램이 OS에 요청해 인터럽트를 발생시킬 수 있는데 이를 Trap이라고 합니다. 시스템콜을 통해 커널함수를 호출하거나 예외를 발생시키는 경우 트랩이 발생했다고 합니다.

​       

### PCB 에 대해 설명하고 PCB 구성요소에 대해서 3가지 이상 예를 드시오.

* 양요셉: PCB는 프로세스 제어블록입니다. 운영체제의 입장에서 프로세스 스케줄링을 위해 프로세스의 관한 데이터를 PCB에 저장합니다. 문맥 교환이 일어나기 전 수행하던 작업들의 진행 상황을 PCB에 저장해 다음 작업을 원활히 수행하도록 할 수 있습니다. PCB에는 CPU가 관리하는 하드웨어 값인 Program counter와 register가 있고 메모리 관련한 code,data,stack 부분이 있습니다. 이 외에 다른 부분이 있지만 이름까지 자세히 기억나지는 않습니다.

​        

### fork 의 동작에 대해 설명하시오

* 양요셉: 부모프로세스가 특정 작업을 수행하기 위해 자식 프로세스를 생성할 때 fork를 사용합니다. 이 때 자식의 PID값은 0으로 부모와 다른 작업을 수행하고 부모 프로세스는 보통 wait 상태로 됩니다.

​       

### 스레드 간 통신보다 프로세스 간 통신이 어려운 이유?

* 양요셉: 스레드는 같은 프로세스 안에서 Programcounter, register, stack의 고유 공간을 제외하고 서로의 데이터를 공유하기 때문에 서로 간 통신을 원활하게 할 수 있습니다. 하지만 프로세스간 통신을 위해 Message Passing이나 프로세스 자원을 공유해야하는데 커널의 도움을 필요로 합니다. 이에 스레드 간 통신보다 프로세스 간 통신의 오버헤드가 더 커집니다.

​         

​          



## < 기말 범위 >    

> 기말 범위의 질문들

### 데드락이란 무엇인가?

* 양요셉: 프로세스들이 서로가 가진 자원을 기다리며 무한정 block 되는 상태를 말합니다. 데드락은 Mutual exclusion(상호 배제), No preemption(비선점), Hold and Wait(점유와 대기), Circular wait(환형 대기) 를 모두 만족했을 때 발생합니다.

​     

### MMU란 무엇인가?

* 양요셉: Memory Management Unit 의 약자로, 논리적 주소를 물리적 주소로 변환해주는 하드웨어 장치입니다. MMU에는 물리적 메모리 주소의 시작값을 담고 있는 Relocation register와 범위를 저장하는 Limit register가 있습니다. 범위를 벗어나면 인터럽트가 발생해 프로세스의 주소 할당을 중지합니다. MMU를 통해 Runtime Binding을 실현할 수 있습니다.

​     

### race condition 이란 무엇인가? 이로인해 생길 수 있는 문제는?

* 양요셉: 여러 프로세스들이 동시에 공유 데이터를 접근하면서 발생할 수 있는 문제들을 말합니다. Critical section에서 변수값이 달라진다면 데이터 불일치 문제로 비정상 작동할 수 있습니다.이를 해결하기 위해 동시 수행되는 프로세스 (concurrent process) 들은 모두 동기화 되어야 합니다.

​       

### clock algorithm이란?

* 양요셉: paging system이 실제로 사용하는 page replacement Algorithm으로 원형 queue를 순회하면서 어떤 프로그램을 Page fault할지 결정하는 알고리즘입니다. 포인터가 한바퀴 돌 때까지 한 번이라도 참조되었다면 reference bit는 1로 변환되고 포인터가 지나갈 때 1을 0으로 바꿉니다. 포인터가 지나갈 때 bit값이 0인 상태라면 그 페이지를 swap area로 이동하고 CPU가 요청한 페이지를 메모리에 올립니다.

​       

### 내부조각과 외부조각

* 양요셉: 내부 조각은 프로그램에 메모리가 배정되었을 때 프로그램이 사용하지 않는 공간을 뜻합니다. 반면 외부조각은 메모리에 배정된 프로그램 사이 다른 프로그램이 들어갈 수 없는 공간을 말합니다. 외부조각 문제를 해결하기 위해 Paging기법과 Segmentation 기법을 사용합니다.

​         

### Processor-Consumer Problem

- 앙요셉: 버퍼에 있는 공유 자원을 사용할 때 생산자 프로세스나 소비자 프로세스가 동시에 도착하면 같은 공유데이터를 참조하면서 문제가 발생합니다. 이를 방지하기 위해 접근 시 미리 lock을 걸고 자원을 획득하거나 저장하는 방식을 사용할 수 있고 Semaphor와 큐를 활용한 Monitor 구조를 사용할 수도 있습니다.

​             

###  TLB의 핵심 기능과 보완할 부분

* 양요셉: TLB는 캐싱 기법을 사용해 메모리에 직접 접근하지 않고 자주 사용하는 페이지를 탐색할 수 있도록 합니다. 하지만 index가 없기 때문에 하나씩 탐색해야하는 단점이 존재하며 associative register을 사용해 병렬적인 탐색을 통해 극복할 수 있습니다.

  ​     

### 주소바인딩 방식들은 어떻게 분류되고 차이점은 무엇인가?

* 양요셉: complie time binding은 absolute 한 주소로 새로 로드되도 주소는 여전히 그대로입니다. Load time binding: Loader 책임 하에 로드할 때마다 주소 변경가능하고 Runtime binding은 MMU의 도움으로 프로그램 실행 중에도 주소를 변경할 수 있습니다.

​      

### Segmentation의 Paging 기법과 비교한 장점과 단점은?

* 양요셉: 일정 크기로 자르는 Paging기법과는 달리 Segmentation은 문맥 단위로 잘라서 메모리에 배분합니다. 내부조각은 생기지 않지만 외부조각이 생길 수 있으며 구현이 복잡하다는 단점이 있습니다.

​          

| 키워드              | 단원                           | 설명                                                 | 관련키워드                                       |
| ------------------- | ------------------------------ | ---------------------------------------------------- | ------------------------------------------------ |
| preemptive          | 04 CPU 스케줄링<br />07 데드락 | 프로세스 강제종료<br />프로세스의 자원을 강제로 반환 | SJF<br />No preemption(비선점)                   |
| clock algorithm     | 08 메모리 관리                 | page replacement Algorithm                           | Page fault<br />LRU, LFU(heap)                   |
| 내부조각과 외부조각 | 08 메모리 관리                 | 메모리 할당 시 생길 수 있는 조각                     | Contigouous Allocation<br />Paging, Segmentation |
| Processor-Consumer  | 10 파일시스템                  | 동기화 문제 중 한가지                                | Buffer                                           |
| RAID                | 11 입출력시스템                | 디스크 사용법 중 한가지                              | Parity                                           |
| SCAN                | 11 입출력시스템                | 디스크 head의 탐색방법                               | FCFS<br />SSRF<br />C/N-SCAN<br />LOOK/C-LOOK    |
| Page fault          | 08 메모리 관리                 | 페이지를 교체하는 방법                               | Interrupt<br />clock algorithm<br />swap         |
| RR                  | 04 CPU 스케줄링                | CPU 스케줄링 방식 중 하나                            | Timer<br />LRU / LFU                             |
| Seek time           | 11 입출력 시스템               | 디스크 접근 시간 중 대부분의 시간                    | SCAN<br />Rotational latency<br />Transfer time  |
| suspend             | 프로세스                       | 프로세스의 상태                                      | blocked<br />swap<br />active                    |
| critical section    | 병행 제어                      | 공유 데이터의 변수가 존재하는 곳                     | lock<br />semaphor<br />synchronization          |
| Banker's Algorithm  | 데드락                         | 데드락의 파악 방법                                   | Safe                                             |
| TLB                 | 메모리 관리                    | 페이지 기법에서 사용: 캐싱기법                       | Associative                                      |
| MMU                 | 메모리 관리                    | 논리 주소에서 물리주소 변환                          | Limit/relocation register<br />Runtime binding   |
| FAT                 | 파일시스템                     | Linked Allocation의 방식                             | Linked Allocation                                |
| VFS                 | 파일 시스템                    | 동일한 시스템콜 인터페이스로 파일접근                | System call<br />NFS                             |
| Paging              | 가상 메모리                    | 가상 메모리를 관리하는 방법                          | 내부조각<br />Multilevel<br />                   |

