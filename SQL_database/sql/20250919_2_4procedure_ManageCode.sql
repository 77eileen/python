-- CREATE PROCEDURE `ManageCode` (IN p_code_type Char(4)) p_code_type 변수 / Char(4) 속성?도 기재해야함.
CREATE PROCEDURE `ManageCode` (
	IN p_code_type Char(4),
    IN p_code_value Char(10),
	IN p_code_name varchar(50),
    IN p_display_order int,
    IN p_use_yn char(1),
    IN p_action varchar(10)  -- insert,update  
)
BEGIN
	IF p_action = 'insert' THEN
		-- 데이터 추가
		INSERT Into code_master
        values(p_code_type, p_code_value, p_code_name, p_display_order, p_use_yn);
    ELSEIF p_action = 'update' THEN
		-- 데이터 수정
		update code_master 
        set code_name = p_code_type,
			display_order = p_display_order,
            use_yn = p_use_yn
        where code_type = p_code_type and code_value = p_code_value;
    ELSE
		-- 데이터 발생
        signal sqlstate '45000'
        Set message_text = 'invalide action! update or insert';
    END IF;
END
