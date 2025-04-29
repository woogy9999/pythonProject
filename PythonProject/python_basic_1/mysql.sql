show databases;
create database mydb character
set utf8 collate utf8_general_ci;

use mydb;
/*
  NUMBER = int,double
  VARCHAR2 = VARCHAR
  CLOB = text
  Date = DateTimegenie_music
*/
create table member(
	no int,
    name varchar(50),
    sex varchar(6),
    content text
);
insert into member values(1,'홍길동','남자','홍길동입니다');
commit;
select * from member;
select * from genie_music;
select * from GENIE_MUSIC;
