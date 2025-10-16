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
    order by 최대 desc, 평균 desc     #위에서 별칭을 줬기 때문에 여기도 별칭 사용!
    ;
