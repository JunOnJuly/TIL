-- CREATE DATABASE ssafy_user;

USE ssafy_user;

/*CREATE TABLE ssafy_user (
	id varchar(20),
    name varchar(20),
    campus varchar(20),
    class varchar(20),
    gi INT
);
*/

/* 사용자등록 프로시저 서울6반 성지훈*/
DELIMITER // ;
/*
CREATE PROCEDURE `proc_user_insert`
(
	IN s_id VARCHAR(10),
    IN s_name VARCHAR(10),
    IN s_campus VARCHAR(10),
    IN s_class VARCHAR(10),
    IN s_gi INTEGER
)
BEGIN
	INSERT INTO ssafy_user (id, name, campus, class, gi)
    VALUES (s_id, s_name, s_campus, s_class, s_gi);
END
*/
DELIMITER ; //

CALL proc_user_insert('wlgnstjd', '성지훈', '서울', '6반', 7);
SELECT * FROM ssafy_user;