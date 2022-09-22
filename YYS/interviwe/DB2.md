# 신입 기술 면접 DB

​                  

### 1. SQL Injection

* 공격자가 악의적인 SQL문을 삽입해 데이터베이스를 비정상적으로 조작하는 코드 인젝션 공격

  * MyBatis를 사용할 경우 SQL문에서 `#{}`와 `${}`를 통해 Dto에서 값을 집어넣을 수 있는데 `${}` 내부에서는 SQL문이 그대로 실행되기 때문에 SQL Injection에 취약합니다.

* 해결책

  1. 입력값을 검증해 이미 정해진, 의도된 값인지 유효성 검사를 진행합니다.

  2. 저장 프로시저(Stored Procedure)를 사용합니다.

     * Query에 미리 형식을 지정해 해당 형식이 아니면 Query문 자체가 실행되지 않는다.

     * Oracle, MySQL 등 대부분 DBMS에서 제공

       * Oracle과 MySQL의 차이점

         |           | Oracle                     | MySQL            |
         | --------- | -------------------------- | ---------------- |
         | 스토리지  | 통합 저장 및 공유          | 독립 저장        |
         | 조인 방식 | 중첩 루프, 해시, 머지 소트 | 중첩 루프        |
         | 확장성    | 별도의 DBMS 사용 불가      | 별도의 DBMS 사용 |
         | 메모리    | 사용율이 매우 큼(수백MB)   | 사용률 낮음      |

         * 중첩 루프: 외곽 루프에서 참인 것을 뽑아 내곽루프에서 한번 더 검증해 뽑아내는 방식

     * MySQL에서의 저장 프로시저

       * `DELIMITER [바꾸기 전 문자열]` ~ `DELIMITER [바꿀 문자열] ;`: 저장 프로시저가 완료되지 않았음에도 SQL문이 실행되는 위험을 막기 위해 구분자(;)를 다른 형식으로 표기해야하는데 일단 `$$`같은 문자열로 지정해놓고 프로시저가 끝나는 문에 `$$`를 `;`로 바꿔주는 것이다.

       ```sql
       DELIMITER $$ 
       CREATE PROCEDURE GetCustomers() 
       BEGIN 
       	SELECT customerName, city, state, postalCode, country 
           FROM customers 
           ORDER BY customerName; 
       END $$ 
       DELIMITER ;
       ```

  ​               

### 2. RDBMS와 NoSQL

|        | RDBMS                                                        | NoSQL                                                        |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 예시   | MySQL                                                        | mongoDB                                                      |
| 스키마 | 스키마에 맞춰 데이터 보관(데이터의 정합성)<br />데이터 수정시 연결된 데이터 수정 용이 | 스키마X, Key-Value 형태 저장(자유로움)<br />연결성이 없기에 모든 컬렉션에서 수정 사항 적용<br />데이터 구조 결정이 어려울 수 있다 |
| Scale  | Scale-up만 가능, 시스템이 커질수록 복잡, 성능 저하           | 데이터 분산 용이, scale-up뿐 아닌 scale-out 가능             |
| 사용처 | 스키마가 중요한 곳<br />데이터 구조가 명확한 경우<br />관계를 맺는 데이터가 자주 변경되는 경우 | 정확한 데이터 구조를 알 수 없는 경우<br />확장/변경이 될 수 있는 경우<br />Update가 많이 없는 경우 |

* Scale-Up: 장비 성능 향상
* Scale-Out: 장비를 추가, 확장

​             

### 3. 트랜잭션

* 작업의 완전성을 보장, 안전장치라고 생각합니다.
* 작업들을 모두 처리하거나 처리하지 못한 경우 이전 상태로 복구해 작업의 일부만 적용되는 현상이 발생하지 않도록 함
* 하나의 트랜잭션: Commit 또는 Rollback
* 트랜잭션의 특성(ACID)
  * A(Atomicity)-원자성: 작업이 모두 반영되든지 아니면 전혀 반영되지 않도록 합니다.
  * C(Consistency)-일관성: 실행이 완료되면 일관성 있는 상태 유지
  * I(Isolation)-독립성: 둘 이상 트랜잭션이 서로 동시에 실행될 경우 서로의 연산에 끼어들 수 없다.
  * D(Durability)-영속성: 완료된 결과는 영구적으로 반영

​                

### 4. DB락

* DB Lock은 트랜잭션 처리의 순차성을 보장하기 위한 방법
  * 공유락(LS, Shared Lock), Read Lock라고도 하는 공유락은 트랜잭션이 읽기를 할 때 사용하는 락이며, 데이터를 읽기만 하기 때문에 같은 공유락끼리는 동시 접근이 가능하다.
  * 베타락(LX, Exclusive Lock): Write Lock, 데이터 변경 시 사용하는 락, 트랜잭션이 완료될 때까지 유지, 베타락이 끝나기 전까지 어떠한 접근도 허용X
* 병행제어 비유
  * Race Condition의 Mutual Exclusion(상호 배제)
    * Peterson's Algorithm: flag와 turn을 모두 사용해 critical section
  * Reader-Writers Problem
    * Shared data: DB
      * readcount: DB로 접근 중인 Reader의 수
    * Synchronization variables
      * Mutex: 공유 변수 readcount를 접근하는 코드(critical section)의 mutual exclusion 보장을 위해 사용
        * readcount의 동시 접근을 방지
      * db: reader의 Lock을 거는 역할
  * Starvation
    * 만약 Writer가 readcount값이 0일 때만 접근 가능하면 reader가 계속 조회하는 경우 무한정 대기할 수 있다.
    * 해결: 신호등, 일정 시간 안에 도착한 reader에게 읽기를 허용하고 조회가 끝나면 writer가 수정할 수 있도록

​               

### 5. Elastic Search 키워드 검색과 RDBMS의 LIKE 검색의 차이

* RDBMS의 LIKE는 `%`나 `_`를 이용한 단순 텍스트 매칭이 가능
  * MySQL 최신 버전에서 보안했다고 하지만 한글 검색은 아직 빈약하다.
* Elastic Search는 동의어나 유의어를 활용한 검색이 가능, 비정형 데이터의 색인과 검색 가능, 역색인 지원으로 빠른 검색 가능

​                 

### 6. 옵티마이저(Optimizer)에 대해 아는대로 말해주세요

* 옵티마이저는 SQL문을 빠르고 효율적으로 수행할 최적의 처리 경오를 생성해주는 DBMS의 엔진

* 개발자가 SQL문을 작성하고 실행하면 옵티마이저가 해당문을 처리할 로직을 구현하고 최고의 효율을 내는 방법으로 해당 쿼리를 실행합니다

* MySQL의 경우 `EXPLAIN`이라는 명령으로 그것을 확인할 수 있습니다.

  ```sql
  EXPLAIN SELECT *
  FROM employees e
      INNER JOIN salaries s ON s.emp_no = e.emp_no
  WHERE first_name='ABC';
  ```

  * 8 버전 옵티마이저: 서브쿼리문 몇몇 방식에 한해 효율성이 JOIN문과 비슷해짐

​               

### 7. DB 튜닝

* DB 시스템의 전체적인 성능을 개선하는 작업
* 작업의 크기로 분류
  * DB 설계튜닝 -> DBMS 튜닝 -> SQL 튜닝
    1. DB 설계 튜닝(모델링 관점)
       * 성능을 고려한 설계
         * Ex) 역정규화/반정규화, 분산파일 배치
       * 데이터모델링, 인덱스 설계
       * 데이터베이스 용량 산정
    2. DBMS 튜닝
       * 성능을 고려하여 메모리나 블록 크기 지정
       * CPU, 메모리 I/O에 관한 관점
       * 튜닝 사례 - Buffer 크기, Cache 크기
    3. SQL 튜닝
       * SQL 작성 시 성능 고려
       * Join, Indexing, SQL Execution Plan
       * 튜닝 사례 - Hash/Join

​                

### 7-2 데이터모델링

* 식별자(실선)/비식별자(점선)
  * 식별자는 부모테이블의 Entity/Attribute를 가져와서 자식테이블의 PK로 사용하는 경우
  * 비식별자는 Entity/Attribute를 단순 값으로 사용하는 경우

​            

### 8. Inner/Outer Join

* Inner Join: 서로 연관된 내용만 검색하는 조인 방식

* Outer Join: A에는 B에는 없어도 A의 있는 데이터를 모두 출력하는 방식

  * LEFT

  * RIGHT

  * FULL

    * Oracle 존재
    * MySQL: UNION을 사용

  * CROSS JOIN

    * A의 테이블의 데이터가 N개 B 테이블의 데이터가 M개라면 CROSS JOIN의 결과값은 NM개
    * 주로 테스트 용도로 사용

  * SELF JOIN

    * 직원테이블에서 이름과 선임/사수가 적혀있다면 다른 칼럼에 두 개의 값이 존재할 수 있다.

      * 이 때 SELF JOIN을 통해 특정 직원의 선임의 데이터를 SELF JOIN으로 불러올 수 있다.

      ```sql
      SELECT A.Name AS [이름], B.Name AS [직속상관]
      FROM Employee A
              INNER JOIN Employee B
              ON A.Manager = B.Name
      WHERE A.Name = '우대리'
      ```

  * NATUAL JOIN

    * 동일한 TYPE(INT, VARCHAR 등)과 NAME(COLUMN명)을 조건으로 조인을 간단히 표현한다.
    * Alias를 붙이면 오류 발생

​               

### 9. GROUP BY

* 특정 컬럼을 기준으로 연산한 결과를 `집계 키`로 정의해 그룹을 지어줍니다.
* 집합의 결과에 집합 연산자를 사용할 수 있습니다.
  * COUNT, SUM, MIN, MAX, AVG
  * DISTINCT
* HAVING을 통해 구체화

​              

### 10. DELETE / TRUNCATE / DROP

|           | DELETE                                               | TRUNCATE<br />= DELETE FROM [테이블 명]         | DROP                           |
| --------- | ---------------------------------------------------- | ----------------------------------------------- | ------------------------------ |
| 종류      | DML                                                  | DDL > DML                                       | DDL                            |
| COMMIT    | 사용자 COMMIT                                        | AUTO COMMIT                                     | AUTO COMMIT                    |
| 로그      | O                                                    | X                                               | X                              |
| 삭제방식  | 논리삭제                                             | 물리삭제                                        | 물리삭제                       |
| 속도      | 느림                                                 | 빠름                                            | 빠름                           |
| ROLL BACK | COMMIT 이전 가능                                     | 불가능                                          | 불가능                         |
| Storage   | 데이터를 모두 DELETE한다고 해도 Storage에는 남아있음 | 최초 테이블 생성 시 할당된 Stroge만 남기고 삭제 | Storage 모두 삭제(스키마 포함) |

​               

### 11. ORM에 대해 설명하시오.

* Object Relational Mapping
* ORM은 객체 그리고 관계형 데이터베이스 매핑의 줄임말이며 클래스와 RDB에서 쓰이는 데이터 테이블이 매핑되는 것입니다.
* SQL문을 쓰지않고 DB의 CRUD를 실현할 수 있다.
* 장점
  * MyBatis를 사용하는 경우: DTO를 여러개로 만드는 경우도 있었습니다.
  * 하지만 ORM을 사용하면 하나의 객체를 재활용할 수 있는 기회가 많아집니다.
  * 코드의 길이를 줄일 수 있습니다
    * 시간 절약
  * 객체지향방식으로 접근이 가능
* 단점
  * 프로젝트가 커지면 난이도가 올라간다
    * 최적화, 속도 저하 문제 등
    * 별도의 튜닝이 필요하다.
  * (유효성 검사를 위한)프로시저가 많은 경우 ORM의 장점을 활용하기 어렵다.
    * 바꾸는 작업이 쉽지 않을 것
* JPA/Hibernate
  * JPA(JAVA Persistence API)는 자바의 ORM 기술 표준, 인터페이스 모음
  * 그것을 구현한 것이 Hibernate

​                

### 12. HAVING vs WHERE

* HAVING: GROUP BY절에서 사용
  * 집계함수와 함께 사용 가능
* WHERE 개별 행 필터링

​               

### 13. JOIN에서 ON과 WHERE 차이

* ON이 WHERE보다 먼저 실행된다.
  * FROM할 때 ON으로 조인해서 가져옴
  * ON 다음 JOIN이 실행
    * JOIN은 SET 으로 데이터를 모음, 서브쿼리도 로직에 포함되어서 임시테이블 만드는 것에 도움을 줌
  * JOIN다음 WHERE이 실행