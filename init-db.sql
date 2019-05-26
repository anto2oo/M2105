DROP TABLE IF EXISTS CONTACT CASCADE;
DROP TABLE IF EXISTS UTIL CASCADE;

CREATE TABLE UTIL (
	id_util serial primary key,
	login varchar(20) not null,
	mdp varchar(20) not null
);

CREATE TABLE CONTACT (
	id_contact serial primary key,
	nom varchar(100) not null,
	email varchar(100) not null,
	tel varchar(10) not null,
	adresse varchar(100) not null,
	latitude real,
	longitude real,
	id_util int references UTIL
);

insert into UTIL(login, mdp) values ('root', 'root');
insert into UTIL(login, mdp) values ('user', 'user');