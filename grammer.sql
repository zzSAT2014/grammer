use test;
drop table if exists grammer_bank;
create table grammer_bank (
    question_id varchar(30) not null,
    type1 int not null default 0,
    type2 int not null default 0,
    type3 int not null default 0,
    type4 int not null default 0,
    type5 int not null default 0,
    type6 int not null default 0,
    type7 int not null default 0,
    type8 int not null default 0,
    primary key (question_id)
)  engine=InnoDB;

	
