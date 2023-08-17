create database NETFLIX;
use NETFLIX;
create table USUARIO (
CPF varchar(30) not null,
EMAIL varchar(30) unique not null, #definir UNIQUE
SENHA varchar(30) not null,
NOME varchar(50) not null, #normalmente 50 char
CARTAO int not null,
FONE int not null,
ENDERES varchar(60) not null,
primary key(CPF,EMAIL)
);
create table VIDEO (
TEMP int, #TEMP E ED tem um problema
EP int,
TITULO varchar(50) not null,
ANO date default(2023) not null, #default determina um valor como padrão
DURACAO float not null,
PROD varchar(50) not null,
GENERO varchar(50) not null,
primary key(TITULO)
);
create table ATOR (
NOME varchar(50) not null, #Normalmente 50
NASCI date not null,
LUGARNASC varchar(100) not null, 
primary key(NOME)
);
create table MENSALIDADE (
MES_ANO date not null,
VALOR_PG float not null,
PAGMENT_DT date not null,
primary key (MES_ANO)
);
rename table MENSALIDADE to MENSAL; #troca o nome da tabela