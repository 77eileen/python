select * from prj1.cartype_tbl;
select `차종별` from main_tbl_rawdata
 group by `차종별`
 ;

insert into prj1.cartype_tbl(cartype_name)
select `차종별` as cartype_name from main_tbl_rawdata
 group by `차종별`
 ;
 

select * from prj1.main_tbl_rawdata;


insert into prj1.main_tbl_rawdata(year,amount,fuel_tbl_fuel_id,cartype_tbl_cartype_id)
select 
`연도` as year,
`수량` as amount,
pft.fuel_id as fuel_tbl_fuel_id,
pct.cartype_id as cartype_tbl_cartype_id

from main_tbl_rawdata mtr
left join prj1.fuel_tbl pft
	on mtr.`연료` = pft.fuel_name
left join prj1.cartype_tbl as pct
	on pct.cartype_name = mtr.`차종별`
;

commit;

select * from prj1.main_tbl_rawdata;


