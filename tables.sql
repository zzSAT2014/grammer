-- create table if not exists grammer_bank(serial_no int not null,
-- 										question_no int not null,
-- 										type1 int not null default 0,
-- 										type2 int not null default 0,
-- 										type3 int not null default 0,
-- 										type4 int not null default 0,
-- 										type5 int not null default 0,
-- 										type6 int not null default 0,
-- 										type7 int not null default 0,		
-- 										type8 int not null default 0,
-- primary key(serial_no,question_no));
-- drop table grammer_record; 										
-- create table if not exists
-- grammer_record(student_name char(30) not null,
-- 				record_date date not null,
-- 				serial_no int not null,
-- 				question_no int not null,
-- 				primary key(student_name, record_date, question_no, serial_no));
-- 
-- drop trigger name_input;
-- create trigger name_input before insert on grammer_record
-- for each row set New.student_name = lower(trim(New.student_name));

-- insert into grammer_record(student_name, record_date, serial_no, question_no)
-- 
-- values(' ZhHe  ', '2014-08-13', 2,3);
-- select * from grammer_record;
-- drop view zhixiangdu_grammer;
-- create view zhixiangdu_grammer as
-- select grammer_bank.*,grammer_record.record_date
-- from grammer_record, grammer_bank
-- where grammer_record.serial_no = grammer_bank.serial_no
-- 	and grammer_record.question_no = grammer_bank.question_no
-- 	and grammer_record.student_name = 'zhixiang du';


select sum(type1), sum(type2), sum(type3), sum(type4), sum(type5), sum(type6), sum(type7), sum(type8) from zhixiangdu_grammer;
