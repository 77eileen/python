inner join
use sqldb ;
SELECT *
	FROM buytbl
	INNER JOIN usertbl
	ON buytbl.userID = usertbl.userID
    WHERE buytbl.userID = 'JYP';
    
USE sqldb;
SELECT U.userID, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2) AS '연락처'
from usertbl U
LEFT OUTER JOIN buytbl B
on U.userID = B.userID
ORDER BY U.userID;