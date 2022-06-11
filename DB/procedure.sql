use ssafy_web_db;

create table user (
userid varchar(20) not null primary key ,
name varchar(20) not null, 
password varchar(50) not null, 
position varchar(20),
department varchar(20));

insert into user(userid, name, password, position ,department) values('test1' , '홍길동' , '12345' , '교육생' , 'SSAFY');

select * from user