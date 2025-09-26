select * from prj1.main_tbl_rawdata;
select count(*) from prj1.main_tbl_rawdata;

select count(*) from vehicle_data;

insert into  prj1.main_tbl_rawdata(year,amount,fuel_tbl_fuel_id,cartype_tbl_cartype_id)
select vd.year, vd.amount,
ft.fuel_id fuel_tbl_fuel_id,
ct.cartype_id cartype_tbl_cartype_id
from vehicle_data vd
left join prj1.cartype_tbl ct
	on trim( vd.vehicle_type) = trim( ct.cartype_name)
left join prj1.fuel_tbl ft
	on ft.fuel_name = vd.fuel
;

commit;

select * from vehicle_data where year = 2020 and amount=81554;

select LENGTH(TRIM(ct.cartype_name)) from prj1.cartype_tbl ct;
select LENGTH(TRIM(vehicle_type)) from vehicle_data;


SELECT vehicle_type, HEX(vehicle_type) 
FROM vehicle_data
WHERE vehicle_type LIKE '%승용%';


-- vehicle_type 컬럼에서 \r과 \n 모두 제거
UPDATE project1.vehicle_data
SET vehicle_type = REPLACE(REPLACE(vehicle_type, '\r', ''), '\n', '');

-- 공백까지 제거하고 싶으면
UPDATE project1.vehicle_data
SET vehicle_type = TRIM(REPLACE(REPLACE(vehicle_type, '\r', ''), '\n', ''));



