USE project1;

DROP TABLE IF EXISTS vehicle_data;

CREATE TABLE vehicle_data (
    year INT,
    amount BIGINT,
    fuel VARCHAR(20),
    vehicle_type VARCHAR(20)
);



LOAD DATA LOCAL INFILE 'D:/0python_SNC/project1/main_tbl_rawdata_csv2.csv'
INTO TABLE vehicle_data
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@year, @amount, @fuel, @vehicle_type)
SET 
    year = NULLIF(@year,'-'),
    amount = NULLIF(REPLACE(@amount, ',', ''), '-'),
    fuel = @fuel,
    vehicle_type = @vehicle_type;
    
select * from vehicle_data;
