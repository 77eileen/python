-- shopdb 삭제
drop database shopdb;
drop database if exists shopdb;  #존재시 삭제해줘.


/*
요구사항 분석
쇼핑몰 database shopdb
고객정보 (고객id, 이름)
상품정보 (상품id, 이름, 단가, 수량)
주문정보(고객id, 상품id, 구매가격)

액션: 회원가입
상품정보 출력
상품구입
상품정보 입력
대쉬보드: 고객별 상품별 구매회수, 평균구매액
*/

use shopdb;
select * from customer;


insert into customer values (null, '홍길동');

update customer
set name = '강감찬'
where customer_id = 3;

DELETE FROM customer
WHERE name = '강감찬';

 