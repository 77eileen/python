-- <<<<<< GROUP BY 및 HAVING 그리고 집계함수 >>>>>>>>
-- GROUP BY 절
-- -그룹으로 묶어주는 역할
-- -집계함수와 함께 사용
-- --효율적인 데이터 그룹화
-- --ex 각 사용자 별로 구매한 개수를 합쳐 출력
use employees;
select gender from employees Group by gender;  #group by : distint 처럼 중복제거처럼 가능함
select gender,count(*) from employees Group by gender;  #그룹핑된 것의 갯수 확인 가능 count
select gender,max(birth_date) from employees Group by gender; #그룹핑 된 것의 max, min 확인 가능

-- -읽기 좋게 하기 위해서 별칭 AS 사용
select gender,max(birth_date) as 생년월일 from employees Group by gender; 

-- GROUP BY 와 함께 자주 사용되는 집계 함수
-- AVG() 평균 / MIN() / MAX() / COUNT() 행의 갯수 / COUNT(DISTINCT) 행의 개수를 센다(중복은 1개만 인정) / STDEV() 표준편차 / VAR_SAMP() 분산

-- HAVING절
-- WHERE과 비슷한 개념으로 조건 제한하는 것이지만, 집계함수에 대해서 조건을 제한하는 것
-- GROUP BY 절 다음에 나와야 함. 순서 바뀌면 안됨.
-- ex. 구매 횟수가 3회 이상인 사람
-- select
-- userid, count(*)
-- from oder
-- group by userid
-- having count(*) <=3

use sakila;
select * from payment;
-- 고객별 결제 횟수
select customer_id, count(*) from payment group by customer_id;
-- having (조건) 30번 이상 결제한 고객
select customer_id, count(*) from payment group by customer_id having count(*) >=30 ;

-- payment테이블의 amount 금액
-- 각 고객별 총 결제 금액
select 
	customer_id, 
	sum(amount) as "총 금액", 
    avg(amount) as 평균, 
    max(amount) 최대
from payment 
	group by customer_id
    order by 최대 desc, 평균 desc     #위에서 별칭을 줬기 때문에 여기도 별칭 사용! 또는 max(amount) desc 로 표기
    ;
    
-- ROLLUP (소계를 낼 때 사용)
-- - 총합 또는 중간 합계가 필요할 경우 사용
-- - group by절과 함께 with rollup문 사용
-- - ex. 분류별로 합계 및 그 총합 구하기
-- rollup 총합과 단위합 group by 절과 함께 사용
-- 직원별 결제 금액의 총합
select 
customer_id, staff_id, sum(amount)
from payment
group by customer_id, staff_id with rollup
;

select year(payment_date), month(payment_date), sum(amount)
from payment
group by year(payment_date), month(payment_date)
with rollup
;

-- DML (DATA Manipulation Language, 데이터 조작 언어)
-- -데이터를 조작(선택,삽입, 수정, 삭제)하는데 사용되는 언어
-- -DML 구문이 사용되는 대상은 테이블의 행
-- -DML사용하기 위해서는 테이블이 정의되어 있어야함
-- -SQL문 중 select, insert, update, delete가 이 문구에 해당
-- 트랜색션(Transaction)이 발생하는 SQL도 DML에 속함
  -- 테이블의 데이터를 변경(입력/수정/삭제)할 때 실제 테이블에 완전히 적용하지 않고, 임시로 적용시키는 것
  -- 취소 가능
  
-- DDL (Data Definition Language, 데이터 정의 언어)
 -- 데이터베이스, 테이블, 뷰, 인덱스 등의 데이터베이스 개체를 생성, 삭제, 변경하는 역할
 -- CREATE, DROP, ALTER 자주사용
 -- DDL은 트랜잭션 발생시키지 않음
 -- 되돌림(롤백)이나 완전적용(commit)사용 불가
 -- 실행즉시 MySQL에 적용
 
-- DCL (데이터 제어 언어 / 권한)
  -- 사용자에게 어떤 권한을 부여하거나 빼앗을 때 주로 사용하는 구문
  -- GRANT/REVOKE/DENY 구문
  
-- INSERT
  -- 테이블 이름 다음에 나오는 열 생략 가능
    -- 생략할 경우 VALUES 다음에 나오는 값들의 순서 및 개수가 테이블이 정의된 열 순서 및 개수와 동일해야함
  -- INSERT INTO .. selct 

-- customer_backup 테이블 생성 및 데이터추가
create table customer_backup2
select * from customer where customer_id <= 10;

select * from customer_backup2;
-- customer_backup 테이블에 테이터를 추가 (insert into)
insert into customer_backup2
select * from customer where customer_id > 10 and customer_id < 20;  #11~19번 고객만 넣고 싶다면
select * from customer_backup2;
-- 상기내용확인해보기!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1111

-- update customer_id가 1인 고객의 activer 0으로 수정
select * from customer_backup2 where customer_id = 1; 

update customer_backup2 
set active = 0, address_id=4  #active와 adress_id 값 변경
where customer_id = 1;


select * from customer_backup where customer_id = 1; 
delete from customer_backup
where customer_id = 1; 
-- 상기내용확인해보기!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1111


-- 자동으로 증가하는 AUTO_INCREMENT

--
  -- drop 삭제
  -- 
  