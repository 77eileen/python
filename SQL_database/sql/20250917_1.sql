-- employees를 더블클릭하던가, 하기와같이 employees를 사용하겠다고 기재.
use employees;
-- 하기는 활성화된 모델 (SCHEMAS에서의 bold체) 타이틀 값을 불러옴. (주석달기 --, /* 글쓰고 */)
select * From titles;  
-- 하기는 활성화되지 않은 DB에서도 하기같이 db명을 같이 입력해주면 타이틀의 데이터를 불러올 수 있음.
SELECT * From employees.titles;
select title From titles;  #위에서 * 입력하면 타이틀 전부가져와라이고, 이것처럼 title 쓰면 타이틀만 가지고옴.
select title as 제목, emp_no as 사번 from titles; #as는 생략가능함 #타이틀을 불러오대 별칭으로 (제목, 사번) 표현

-- 현재서버에 있는 데이터베이스 조회
show databases;
-- 현재 데이터베이스에 있는 테이블의 정보 조회
show table status;

-- employees 테이블 열이 무엇이 있는지 확인
describe employees;
describe dept_emp;   #-- employees 의 dept_emp 테이블 열이 무엇이 있는지 확인

-- 조건문
select * from employees where hire_date >= 1985-01-01 and gender='f';  #고용일과 성별로 필터해서 볼 수 있음.
select 
	concat(last_name, ' ', first_name) as 이름   #concat CONCAT = 문자열 붙이기 함수 / 파이썬의 "문자열1" + "문자열2" 와 같은 역할
	from employees
where hire_date >= 1985-01-01
	and gender ='m';                #이렇게 여러문장으로 조건을 써도 됨. 
