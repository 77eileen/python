select * from customer;
-- JSON : 객체 자체를 저장할 수 있음. 딕셔너리를 문자열로 만들수 있음. 
   -- 문자열로 저장 ==> "{'name':'홍길동', 'score':{'kor':100, 'eng':80}, 'hobby':{}}"
   -- JSON ??????????????????????
   
-- IF, ifnull
select if (100>200, '참', '거짓');
SELECT ifnull (null, 100);
-- concat_ws 
-- left, right
-- upper,lower
-- left, rtrim
-- repeat, replace
-- substring

-- sql 은 파이썬 인덱스(0부터시작)와 달리 1부터 시작함.

-- <<<<<<JOIN>>>>>>>>>>>>  구글 검색해서 이미지 확인해보기
-- INNER join 가장 많이 사용함 (일반적인 join이라하면 이너조인을 얘기함/ join만 써도 inner join으로 인식함)
   -- 