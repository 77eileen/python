use newuerdb;
select * from usertbl;
select * from usertbl Where name = '아이유'; #
select userid, name from usertbl where birthyear >= 1970 and height >=182;
-- between ... and 와 in () 그리고 like
-- 데이터가 숫자로 구성되어 있으며 연속적인 값 between ... and
select name, height from usertbl where height between 180 and 183;
-- 이산적인(discrete) 값의 조건 : IN ()
select name, addr from usertbl where addr in ('경남', '전남', '경북');
-- 문자열 내용 검색 : like 사용 (문자뒤에 % - 무엇이든 허용, 한극자와 매치 _ 사용)
select name, height from usertbl where name like '김%';
select name, height from usertbl where name like '%수';

-- 서브쿼리
-- 쿼리문 안에 또 쿼리문이 들어 있는 것
-- 서브쿼리의 결과가 둘 이상이 되면 에러 발생!!!!! (하기 예시도 박보검 이름 동명이인이 될 수 있으므로 오류 발생될 수 있음)
-- ex. step1. 박보검의 키를 확인
select height from usertbl where name = '박보검';  #select 는 무조건 조회
-- ex. step2 . 박보검의 키보다 더 큰 사람 (182가 박보검 키)
select * from usertbl where height > 182 ;
-- ===========> 저러면 박보검 키 변경에 따라 적용 안되므로 하기와 같이 서브쿼리 적용!!
select *
from usertbl 
where
     height > (select height
           from usertbl 
           where name = '박보검') ;
           
-- 박보검보다 나이가 많은 사람
select * from usertbl where birthyear < (select birthyear from usertbl where name = '박보검') ;

-- 박보검보다 나이가 많으면서도 키가 185 이상인 사람
select * 
from usertbl 
where birthyear < (select birthyear 
           from usertbl 
           where name = '박보검') 
	  and height >= 185 ;

-- <<<<<<< 연습 >>>>>>>>
-- 1. usertbl 의 모든 데이터를 조회
select * from usertbl;
-- 2. 성이 김씨성을 가지는 사람을 모두 출력
select * from usertbl where name like '김%';
-- 3. 박씨성을 가진 사람중에서 서울에 사는 사람
select * from usertbl where name like '박%' and addr in ('서울');
-- 4. 이씨성을 가진 사람들 중에서 지역이 서울이 아닌 사람들
select * from usertbl where name like '이%' and addr <> '서울';
select * from usertbl where name like '이%' and addr != '서울';
select * from usertbl where name like '이%' and addr not in ('서울');
-- 5. 1980년 이후 출생자이면서 키가 170이상이고 성씨가 박씨인 사람들
select * from usertbl where birthyear > 1980 and name like '박%';

-- (서브쿼리 두개이상 나오면 오류되므로 ... any all 사용.
-- any : 서브쿼리의 결과중에 하나라도 만족 
-- all : 서브쿼리의 결과중에 모두만족 

-- 하기 오류 발생 : Error Code: 1242. Subquery returns more than 1 row
/*
select *
from usertbl
where height >
(select height from usertbl where addr = '서울');
*/

-- any 사용 해석: 서울에 사는 사람들의 키보다 큰 사람들을 찾음.
-- 서울에사는 사람들의 키중에 가장 작은 키보다 큰 사람들만 추출한 것이 됨.
-- any 잘못쓰면 뜻이 와전될 수 있음. 유의!
select *
from usertbl
where height >
any(select height from usertbl where addr = '서울'); 

select min(height) from usertbl where addr = '서울' ;

select count(*)
from usertbl
where height >
any(select height from usertbl where addr = '서울'); 

-- all 사용 해석: 사람들의 키의 값들을 모두 만족하는..
-- 결국, 경남에서 가장 큰 키보다 큰 사람들을 추출하는 것
select *
from usertbl
where height >
all(select height from usertbl where addr = '경남'); 

select height from usertbl where addr = '경남' order by height desc;

-- 경남지역의 사람들의 키와 같은 값을 가지는 모든 지역의 사람들
select *
from usertbl
where height =
any(select height from usertbl where addr = '경남'); 

select height from usertbl where addr = '경남' order by height desc;


-- limit1 뭐지??????

