select * from shop_base_tbl;

create table shop_base2_tbl 
	like shop_base_tbl;
-- 상기 base2_tbl 생성 후 table 수정에 가서 idshop 열은 삭제하고 shop_area, shop_name 2개를 PK로 지정하고 파이썬 static_04 실행

select * from shop_base2_tbl;

SELECT COUNT(*)  FROM shop_base2_tbl;