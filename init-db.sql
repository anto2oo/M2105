DROP TABLE IF EXISTS CONTACT CASCADE;
DROP TABLE IF EXISTS UTIL CASCADE;

CREATE TABLE UTIL (
	id_util serial PRIMARY KEY,
	login varchar(20) NOT NULL,
	mdp varchar(20) NOT NULL
);

CREATE TABLE CONTACT (
	id_contact serial PRIMARY KEY,
	nom varchar(100) NOT NULL,
	email varchar(100) NOT NULL,
	tel varchar(10) NOT NULL,
	adresse varchar(100) NOT NULL,
	latitude real,
	longitude real,
	id_util int REFERENCES UTIL
);

INSERT INTO UTIL(login, mdp) VALUES ('root', 'root');
INSERT INTO UTIL(login, mdp) VALUES ('user', 'user');