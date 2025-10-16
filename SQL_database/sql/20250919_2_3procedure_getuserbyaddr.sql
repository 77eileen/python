CREATE DEFINER=`root`@`localhost` PROCEDURE `GetUserByaddr`(IN p_addr char(2))
BEGIN
	if p_addr is null or p_addr = '' Then  -- Then 필수!!
        -- 지역이 없거나 빈 문자열이면 전체 회원 조회
		select 
			userid,
            name,
            addr,
            c.code_name as addr_name
        from usertbl u
        left join code_master c
			on c.code_type = 'addr' and c.code_value = u.addr
        order by name;                -- if, else 구문 끝날때 마다 ; 기재하기
    else 
		-- 특정 지역의 회원만 조회
		select 
			userid,
            name,
            addr,
            c.code_name as addr_name
        from usertbl u
        left join code_master c
			on c.code_type = 'addr' and c.code_value = u.addr
		where u.addr = p_addr
        order by name;
	end if;
END