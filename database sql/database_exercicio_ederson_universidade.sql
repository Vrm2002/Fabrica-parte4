create database universidade charset utf8mb4 collate utf8mb4_unicode_ci;
use universidade;

create table DEPARTAMENTO (
cod_depart int auto_increment,
nome varchar(100) not null,
fone int not null,
centro varchar(100) not null, 
primary key (cod_depart)
);

create table CURSO (
nome varchar(100) not null,
tipo enum('Técnico', 'Graduação', 'Mestrado', 'Doutorado'),
cod_depart int,
constraint foreign key (cod_depart) references DEPARTAMENTO (cod_depart),
primary key (nome)
);


create table ALUNO (
nome varchar(100) not null,
num_matricula int auto_increment,
CPF varchar(14) not null,
endereco varchar(300) not null,
fone int not null,
datanasci date not null,
sexo enum('M','F'),
cod_depart int,
curso varchar(100),
constraint foreign key (cod_depart) references DEPARTAMENTO (cod_depart),
constraint foreign key (curso) references CURSO (nome),
primary key (num_matricula)
);

create table PROFESSOR (
nome varchar(100) not null,
CPF varchar(14) not null,
cod_depart int,
constraint foreign key (cod_depart) references DEPARTAMENTO (cod_depart),
fone int not null,
primary key (CPF)
);

