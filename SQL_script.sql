CREATE DATABASE SENAC;
CREATE DATABASE POPO;
USE SENAC;
CREATE TABLE funcionario (cod_func INT);
CREATE TABLE alunos (
id int,
nome varchar (30) not null,
fone varchar (30) not null,
email varchar(30) not null
);
show tables; #mostra tabelas
create database senac character set utf8mb4 collate utf8mb4_unicode_ci; #uft8 é o charset, unicode_ci faz não ser mais case sensitive
drop database SENAC;
drop database POPO;
use senac; #Serve para usar um banco de dados
create table alunos (id int auto_increment, nome varchar(30) not null, fone varchar(30) not null, email varchar(30) not null, primary key(id)); #Cria uma tabela com as seguintes colunas
# primary key - chave unica de uma tabela, varchar(30) o 30 em varchar singifica o limite de caracteres, not null impede de uma coluna ficar vazia, auto_increment faz com que a coluna se encha sozinha
describe alunos;
