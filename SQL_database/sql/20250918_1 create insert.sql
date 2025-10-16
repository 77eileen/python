use Newuserdb;
select * from usertbl where birthyear = 1972;

-- LIMIT 출력하는 개수 제한 LIMIT N : N개만 출력 
select * from usertbl where birthyear = 1972 limit 1;
-- DISTINCT
select distinct birthyear from usertbl where birthyear = 1972;

-- CREATE (테이블 생성 예시 ex. userbtl 파일)
-- CREATE TABLE usertbl (
--     userid     INT AUTO_INCREMENT PRIMARY KEY, -- 사용자 고유번호
--     name       VARCHAR(20) NOT NULL,           -- 한글 이름
--     birthyear  INT NOT NULL,                   -- 출생년도
--     height     INT,                            -- 키
--     addr       CHAR(2)                         -- 지역 (예: '서울', '경남')
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;








-- CREATE (구조+데이터 복사)
CREATE table copy_usertbl (select name from usertbl) ;  #테이블 복사
select * from copy_usertbl;
-- CREATE ... Like 구조만 복사
create table copy2_usertbl like usertbl;
-- 기존 테이블에 다른 테이블의 데이터를 가져와서 추가
insert into copy2_usertbl(name, birthyear) select name, birthyear from usertbl;
select * from copy2_usertbl;
-- 상기 userid는 autoincrement? 로 되어 있어서 자동으로 들어옴.
-- 상기 height, addr 이 Non null 이 체크되어 있으면 오류 생김. non null이 안되어 있어서 하기 null로 출력가능.