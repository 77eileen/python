-- -------------<<<<<<< join >>>>>>>>>>>--------------- 
-- inner join (교집합/가장많이 사용됨/그냥 join 써도 inner join)
use sqldb;
    
select *
	from buytbl
		where userid = 'jyp';
-- 상기만 실행하면 jpy가 산 목록만 나옴. 

select *
	from buytbl
		inner join usertbl  -- 그냥 join 써도 inner join
			on buytbl.userID = usertbl.userID   -- 기준에 on사용? / 서로다른 칼럼끼리 조인해도 되긴하나, relationship관계가 있는 것끼리 찾는게 빠름.좋음. (여긴 같은 pk로 연결되어 있음)
	where buytbl.userID = 'jyp';
-- 이건 바이테이블의 jpy가 산 목록과 유저테이블로부터 jyp의 정보까지 추출함.

-- outer join (외부조인)
-- left outer join : left join 으로 outer 생략가능 / 실무에서 이것만씀!!
   -- 왼쪽테이블이 마스터테이블이 되어서 왼쪽테이블의 것은 모두 출력되어야 한다로 이해
   -- 왼쪽테이블은 다 나오고 오른쪽은 왼쪽과 매칭되는 것만 나옴!!! 
	-- select <열 목록>
    -- from <첫 번째 테이블(left 테이블)>
    -- <left | right | full> outer join <두번째 테이블(right 테이블)>
    --    on <조인될 조건>
    -- [where 검색조건] ;
-- right outer join : right join으로 outer 생략가능 / 실무에서 거의 안씀!!!
use sqldb;
select u.userid, u.name, b.prodname, u.addr, concat(u.mobile1, u.mobile2) as '연락처'
	from usertbl u
		left outer join buytbl b
			on u.userid = b.userid
	order by u.userid;

-- cross join (상호조인) ==> 실무에서 거의 사용안함.
  -- 한쪽 테이블의 모든 행들과 다른 쪽 테이블의 모든 행을 조인시키는 기능
  -- cross join 결과 개수 = 두 테이블 개수를 곱한 개수
  -- 테스트로 사용할 많은 용량의 데이터를 생성할 때 주로 사용 (현업에서는 테스트용 따로 있음)
  -- on 구문을 사용할 수 없음
  -- 대량 데이터 생성하면 시스템 다운 될수 잇으니 count(*) 사용


-- union / union all / not in / in
  -- union : 파이썬의 set과 동일, 중복 열 제거
  -- union all : 중복제거 안하고 그냥 합쳐줌. 

select * from code_master;
select * from code_master where use_yn = 'Y';
select * from usertbl;

-- 서울 대신에 코드에 있는 값을 불러와서 서울특별시 .. 이런형태로 고객정보 조회
-- join 사용 : 매칭되는 기준 컬럼 code_value 와 addr의 키 값을 조인
use sqldb;
select u.userid, u.name, u.addr, cm.code_name
	from usertbl as u
		left join code_master as cm 
			on u.addr = cm.code_value
            and cm.code_type = 'addr' #addr 코드타입인, code_value를 사용하겠다. and로 묶어줌.
		where cm.use_yn = 'Y';

-- 구매정보와 상품 분류를 연결
-- 전자대신에 전자제품처럼 보기좋게 코드마스터에서 조인해서 출력
-- buytbl, code_master
select * from buytbl;
select * from code_master;
use sqldb;
select b.userID, b.prodName, cm.code_name as '분류', b.price, b.amount
	from buytbl as b
		left join code_master as cm 
			on b.groupName = cm.code_value
            and cm.code_type = 'grpn' #addr 코드타입인, code_value를 사용하겠다. and로 묶어줌.
		where cm.use_yn = 'Y'
        order by cm.display_order;    #분류 (code_name)에 따라서 display_order가 매겨져있어서 분류기준으로 정렬됨.
			-- 상기 on 이렇게 기재해도 됨. 
            -- on cm.code_type = 'grpn'
		    -- and b.groupName = cm.code_value


-- usertbl, buytbl 연결 회원별 구매내역
-- 두테이블을 회원정보 기준으로 회원정보가 누락없이 모두 출력
select * from usertbl;  -- 확인용
select * from buytbl;   -- 확인용
use sqldb;
select *
	from usertbl as u
		left join buytbl as b
			on u.userid = b.userid;

-- 각 회원별로 구매액 총합, 평균, 구매횟수 (inner join 사용, left조인하면 구입안한 사람내역도 나오니까)
select 
u.userID, u.name,
sum(b.price*b.amount) as 총구매액,   
round(avg(b.price*b.amount),2) as 평균,
count(*) as 구매횟수
from usertbl as u
join buytbl as b
	on u.userid = b.userid
group by u.userID
order by 총구매액 desc, 평균 desc, 구매횟수 desc;

-- 공통코드에서 주소와 맵핑  ==> 공통코드는 left join..해야..?? 
-- 공통코드에 있는 정보를 이용해서 출력 
-- step1
select
*
from usertbl u
left join buytbl b
	on u.userID = b.userID;
    
-- step2
select * from buytbl;   -- 확인용
select
u.name,
c.code_name as addr_name,
b.prodName,
b.price,
b.amount
from usertbl u
left join buytbl b
	on u.userID = b.userID
left join code_master c
	on c.code_type = 'addr'
    and c.code_value = u.addr
order by c.display_order
;
   
-- step3
-- 통신사 코드 추가
-- mobile1을 code_master 의 MOB1에 해당하는 code_name 연결해서 통신사까지 출력
select * from usertbl;   -- 확인용
select * from code_master;   -- 확인용
select
u.name,
c.code_name as 주소,
b.prodName,
b.price,
b.amount,
cm.code_name as 통신사
from usertbl u
left join buytbl b
	on u.userID = b.userID
left join code_master c
	on c.code_type = 'addr'
    and c.code_value = u.addr
left join code_master cm
	on cm.code_type = 'MOB1'
    and cm.code_value = u.mobile1
order by u.name
;

-- step4
-- 상품 분류 코드 추가
-- groupname을 code_master의 GRPN 코드와 연결하고 총 구매금액 계산
select * from usertbl;   -- 확인용
select * from buytbl;   -- 확인용
select * from code_master;   -- 확인용
select
u.userID,
u.name,
c.code_name as 주소,
b.prodName,
cm2.code_name,
b.price,
b.amount,
b.price*b.amount as 총구매액,
cm.code_name as 통신사
from usertbl u
left join buytbl b
	on u.userID = b.userID
left join code_master c
	on c.code_type = 'addr'
    and c.code_value = u.addr
left join code_master cm
	on cm.code_type = 'MOB1'
    and cm.code_value = u.mobile1
left join code_master cm2
	on cm2.code_type = 'GRPN'
    and cm2.code_value = b.groupName
where
	c.use_yn='Y' or cm.use_yn='y' or cm2.use_yn='Y'
order by u.name
;

-- 뷰 생성 방법
-- SCHEMAS > sqldb > views > 마우스 오른쪽 createviews -- query쓰고(칼럼명 중복되면 에러남) - apply 

-- 뷰 생성 이후
select * from user_buy_code_tbl;

-- stored procedures 생성
-- SCHEMAS > sqldb > stored procedures > 우클릭 create
-- GetUserList 프로시져 생성 후
call GetUserList();

-- getuserbyaddr 프로시져 생성 후
call getuserbyaddr("");  -- 전체 조회됨
call getuserbyaddr("서울"); 
call getuserbyaddr(null);
-- call call getuserbyaddr(); 이렇게 하면 조회 안됨. 오류발생. 매개변수는 반드시 값을 줘야함.

select * from code_master where code_type = 'addr';   -- 확인용
-- ManageCode 프로시져 생성후
call ManageCode ('ADDR', '대전', '대전광역시', 7, 'Y', 'delete');
	-- 'delete' 는 입력되어있지않은 액션 /  Error Code: 1644. invalide action! update or insert
-- [추가] ADDR 대전코드가 없어서 대전 추가
call ManageCode ('ADDR', '대전', '대전광역시', 11, 'Y', 'insert');

-- [수정] code_type='ADDR' AND code_value='부산'인 줄을 찾아서 수정
call ManageCode ('ADDR', '부산', '대전광역시', 2, 'Y', 'update');

-- 구매내역 집계 프로시져
-- 서울지역에서 구매건수
select
*
from usertbl u
join buytbl b
	on u.userID = b.userID
Where u.addr = '경남';


-- GetPurchaseSummaryByAddr 프로시져 생성후
-- GetPurchaseSummaryByAddr : 지역에 따라 구매내역 찾기
call GetPurchaseSummaryByAddr ('');
call GetPurchaseSummaryByAddr (null);
call GetPurchaseSummaryByAddr ('서울');

-- exception이 발생하는 것을 확인 
-- AddCodeWithTransaction 프로시져 생성후
call AddCodeWithTransaction(Null);
call AddCodeWithTransaction('ADDR', '서울', '서울특별시', 0, 'Y');
select * from code_master;   -- 확인용
-- ??????????????????????????????????????????????????????