# JAVA 면접 대비

  

# JAVA 1

​              

### 1. Java 언어

* 객체 지향 프로그래밍언어
  * Abstraction, Polymorphism, Inheritance, Encapsulation
* JVM
  * 어떤 OS에서도 동작
  * 조금 느리다
* GC
  * 메모리 효율적 사용
* 타입 안정성이 뛰어나다.
  * 정적 타이핑 언어므로 타입 안정성이 뛰어나다.
  * 동적 타이핑 언어

​                       

### 2. JVM의 역할

> 가비지 콜렉터는 4부분으로 나뉩니다.

1. 클래스 로더(class loader)
2. 자바 인터프리터(interpreter)
   * 바이트 코드를 기계어로 변환
3. JIT 컴파일러(Just-In Time compiler)
   * 자주 사용하는 기계어를 캐싱해서 저장하고 일정 횟수 이상 기계어가 사용되면 트리거를 이용해서 그 값을 사용
4. 가비지 컬렉터(garbage collector)

​               

### 3. 컴파일 과정

1. Java 파일 빌드(build)
2. 자바 컴파일러: 바이트 코드로 변환(javac)
   * IDE를 사용하는 경우 저장할 때마다 이것이 자동으로 이루어집니다.
3. JVM 내부에 있는 클래스로더
   * 동적으로 끌어와서, 필요한 순간에 클래스 파일을 하나씩 로드해서
4. JVM 내부 인터프리터
5. JIT 컴파일러
6. OS로 기계어 번역

​               

### 4. Java에서 제공하는 기본형 타입

> 1비트가 아닌 1바이트?
> CPU가 인식할 수 있는 최소 단위
> 주소를 붙일 수 있는 최소 단위

* 정수형 byte, short, int, long
* 실수형 int
* 논리형 boolean
* 문자형 char

​                

### 5. 오버라이딩(Overriding) 오버로딩(Overloading)

* Overriding
  * Comparator 예시
    * Class의 경우 implements Comparable
      * toCompare
    * o1, o2 Lamda 식을 이용해서
      * compare
* Overloading
  * 메서드의 이름을 동일하게 해서 매개변수를, 타입을 다르게 해서 받아주는 방식
  * 생성자 단계에서 많이 써보았습니다.

​                

### 6. 객체 지향 프로그래밍

* 추상화: 부모 클래스가 자식에게 요구
  * 오류 발생을 줄이는
* 다형성: Object 라는 최상위 개념에 다른 객체들을 묶어서 집어넣을 수 있다는 것이었는데요
  * 결합도를 떨어뜨린다.
  * DI에 필수적인 요건
  * OCP
    * 팩토리 패턴
      * 서비스의 형태가 조금씩 다를 수 있는데 그것들을 하나의 종류로 정의할 수 있지만 세분화해서 나눠질 수 있도록 하는 것
* 상속
  * 부모의 클래스의 원본을 지키면서
  * 자식클래스에서 새로운 내용을 정의하거나 부모 메서드의 재정의 함으로
* 캡슐화
  * 객체의 속성과 행위를 하나로 묶어주고
  * 실제 구현 내용 일부를 외부에 감추어 은닉한다.
    * 패키지 내에 그 로직을 수행하는 클래스를 만들어놓으면 한줄로 표현할 수 있다.
      * 보여지는 코드가 매우 간결해진다.

​                               

### 1) Thread-safe

> 공유 자원(객체, 클래스 등) 여러 스레드로부터 동시에 접근이 이루어져도 프로그램 실행에서 문제가 없는 상황.
> 다른 스레드가 그 함수를 호출해서 동시해 실행되더라도 

* Re-entrancy
  * A, B, C 쓰레드가 공유자원에 접근해 값을 바꾸더라도 서로에게 주어지는 자원의 값이 같아야한다.
* Thread-local storage
  * 공유데이터 사용을 피할 수 없는 경우 각각의 스레드에서만 접근 가능한 저장소들을 사용
  * 동기화를 피할 수 없을 때 사용
* Mutual Exclusion
  * 공유자원을 꼭 사용해야 한다면 mutex, semaphore
    * Mutex: 들어올 때 값을 변경해 문을 닫고, 나갈 때 값을 변경해 문을 연다.
    * Semaphore
      * P(s): 공유데이터 획득 과정, -1
      * V(s): 공유데이터를 반납하는 과정, +1
      * Monitor: critical section을 모아놓은 곳
        * Queue를 이용해 모니터 내부로 들어오기 위해 프로세스들이 대기하는 상태

​                  

### 2) 싱글톤 디자인 패턴

```java
public class Class{
 private static Class instance; // Lazy Initialization
 private static Class instance = new Class instance(); // Eager Initialization: 사용X 가능성
 private static volatile Class instance; // DCL(Double Checked Locking)
  
 private Class() {}; // 인스턴스 생성 방지(new 키워드 방지) = 모든 싱글톤 방식
  
 public static Class getInstance(){
   
   /* Lazy Initialization 
   		null값 인식 때 2 개 이상 생성 가능
   */
   if(instance == null){
     instance = new Class();
   }
   
   /* DCL
   	null 값일 때 synchronized로 닫기
		하나의 스레드만 read&write
   */
   if(instance == null){
     synchronized(Class.class){
       if(instance == null){
         instance = new Class();
       }
     }
   }
   return instance;
 }
  
/* Lazy Holder 방식: 인스턴스 틀을 아예 만들지 않음 */
 private static class LazyHolder {
   private static final Class INSTANCE = new Class();
 }
 
 public static Class getInstance(){
   return LazyHolder.INSTANCE;
 } 
}
```

​                

### 3. Garbage Collection

* JVM이 메모리를 관리하는 기법
* 시스템에서 동적으로 할당됐던 메모리 영역 중 필요없어진 메모리 영역을 회수
* JVM이 작업을 중단, GC 쓰레드를 제외한 모든 쓰레드가 중단 후 GC가 사용하지 않는 메모리를 제거합니다.
* GC의 종류
  * Young 영역: Minor GC
  * Old 영역: Major GC



### 4. JVM 메모리 영역(Runtime Data Area)

> MSH(M, S, H)

* 메소드 영역(Runtime Constant Pool) / Stack 영역 / Heap 영역
  * 메소드 영역: 전역변수, static 변수 저장, JVM 로딩부터 종료까지 메모리 유지
  * Stack 영역(LIFO): 런타임시 할당(실행 버튼)
    * 전역변수, 매개변수 데이터 저장
    * 메서드 호출시 메모리에 할당
  * Heap 영역: new 키워드로 생성되는 instance 객체, 배열 등(가비지 컬렉터가 관여하는 영역)
    * 컴파일 타임 시 할당
* Heap Area
  * Eden, Survivor = Young -> Minor GC
  * Old -> Major GC
  * Permanent -> Full GC
* Parallel GC
  * GC가 single thread 에서 작동했는데 멀티스레드로 동작
  * Minor GC에 적용
* Parallel Old GC
  * Parallel GC에서 Old GC 알고리즘을 개선
  * Old GC 또한 멀티스레드로 동작

​                

### 5. 객체지향의 설계 원칙

> SOLID 원칙: 소프트웨어를 설계함에 있어 이해하기 쉽고, 유연, 유지보수 및 확장이 편하다는 장점이 있다.

1. SRP(Single responsibility principle): 단일 책임 원칙
   * 모든 원칙은 하나의 책임만 가져야 한다. 수정할 이유가 한가지여야한다.
   * 클래스는 책임을 완전히 캡슐화해야한다.
2. OCP(Open-closed principle): 개방 폐쇄 원칙
   * 기존 코드는 변경하지 않으면서 기능을 추가할 수 있도록 설계한다.
   * 추상화 다형성을 활용
3. LSP(Liskov substitution principle): 리스코프 치환 원칙
   * 상위 타입은 하위타입으로 대체할 수 있어야 한다.
   * 부모클래스 자리에 자식 클래스가 들어가도 문제가 발생하지 않는다.
4. ISP(Interface segregation principle): 인터페이스 분리 원칙
   * 각 역할에 맞게 인터페이스를 분리한다.
   * 인터페이스 내의 메서드를 최소화해서 만든다.(기능별 분리)
   * ISP < SRP
5. DIP(Dependency inversion principle): 의존관계 역전 원칙
   * 의존관계를 맺을 때 변화하기 쉬운 것보다 변화하기 어려운 것, 거의 변화가 없는 것에 의존한다.

​               

### 6. 객체와 클래스

* 객체는 보다 넓은 개념
* 그것을 구체화한 것이 클래스, 객체를 구체화한 틀
* 인스턴스: 객체에 메모리가 할당된 실체

​                 

### 7. 생성자

* 클래스와 같은 이름으로 정의한 메서드
* 클래스 내부값을 초기화할 때 사용
  * 생성하지 않아도 default 로 생성자 생성

​          

### 8. 접근 제어자

* private < default < protected < public
  * protected: 동일 패키지 클래스 또는 해당 클래스를 상속 받은 다른 패키지 클래스
  * default: 해당 패키지 내에서만 접근 가능

​               

### 9. Wrapper class / Boxing & UnBoxing

* 기본형을 객체로 표현한 것
* Wrapper Class에는 다양한 기능들이 내부에 존재
  * Integer.MAX_VALUE

​                  

### 10. Synchroized

* 성능 저하를 유발할 수 있다.

​            

### 11. new String()과 리터럴("")의 차이

* New String{}은 객체 생성이니까 Heap 메모리 저장
* ""은 Heap 영역 내부의 String Constant Pool
* `==`으로 비교하면 둘의 값이 다르다.
* 리터럴 방식으로 둘을 비교하면 저장 공간이 같고 new면 새롭게 힙 공간에 생기기에 서로 다른 주소
* **String 데이터가 불변인 이유**
  * Thread-safe, Caching을 위함

​                

### 12. String vs StringBuilder vs StringBuilder

* 쓰레드 환경
* String 은 값이 변하지 않는다. 불변객체
* StringBuilder/Buffer 는 가변적
* Buffer는 멀티스레드 환경
* Builder는 싱글스레드 환경

​               

### 13. 클래스 멤버 변수 초기화 순서

1. static 변수 선언: 클래스가 로드될 때 변수가 제일 먼저 초기화
2. 필드 변수 선언부: 생성자보다 먼저 초기화
3. 생성자 block: 객체가 생성될 때 JVM이 내부적으로 locking

​                 

### 14. 이너 클래스(Inner Class, 내부 클래스)

1. 내부 클래스에서만큼은 외부 클래스 멤버에 접근 가능
2. 캡슐화: 서로 관련있는 클래스 묶어 표현
3. 외부에서는 내부 클래스 접근 불가, 코드 복잡성 감소

​              

### 15. 리플렉션(Reflection)

구체적인 클래스를 알지 못해서 그 클래스의 메서드, 타입, 변수들에 접근할 수 있도록 하는 자바 API

​              

### 16. CheckedException과 UnCheckedException의 차이를 설명해주세요

* CheckedException은 실행하기 전에 예측 가능한 예외를 말하고, 반드시 예외 처리를 해야 합니다.
  - 대표적인 Exception - IOException, ClassNotFoundException 등

- UncheckedException은 실행하고 난 후에 알 수 있는 예외를 말하고, 따로 예외처리를 하지 않아도 됩니다.
  - 대표적인 Exception - NullPointerException, ArrayIndexOutOfBoundException 등
- RuntimeException은 UncheckedException을 상속한 클래스이고, RuntimeException이 아닌 것은 CheckedException을 상속한 클래스 입니다.

​             

### 17. List, Set, Map, Stack, Queue의 특징에 대해 설명해주세요

* 순회 가능한지
* 순서의 존재
* 중복 가능 여부: Set Map

​               

### 18. 중복이 불가능한 Set과 Map의 검사 방식

* HashCode 메서드 오버라이딩

​                

### 19. 직렬화(Serialize)

* extends Serializable
* 외부의 자바시스템에서도 사용할 수 있도록 바이트 코드로 변환
* JVM 수행

​               

### 20. SerialVersionUID 선언 이유

1. JVM이 클래스에 대한 버전 부여
2. 직렬화 할때 버전 명시 역직렬화 할때의 클래스의 형태(버전) 온전히 같게 하기 위함

​                  

