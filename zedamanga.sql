create database produtos char set utf8mb4 collate utf8mb4_unicode_ci;
use produtos;

create table produtos(
referencia varchar(3) primary key,
descricao varchar(50) unique,
estoque int not null default 0
);

insert into produtos values ('001','Feijão',10);
insert into produtos values ('002','Arroz',5);
insert into produtos values ('003','Farinha',15); 

create table itensvenda(
venda int,
produto varchar(3),
quantidade int
);

insert into itensvenda values (1,'001',3);
insert into itensvenda values (1,'002',1);
insert into itensvenda values (1,'003',5);

delimiter $

select * from itensvenda$

#Trigger

create trigger Tgr_ItensVenda_Insert after insert
on itensvenda
for each row
begin
update produtos set estoque = estoque - new.quantidade
where referencia = new.produto;
end $

show triggers$

select * from produtos$

delimiter ;

#Retirou 5 feijão 
insert into itensvenda values (1,'001',5);

delimiter $

#trigger
create trigger Tgr_ItensVenda_Delete after delete
on itensvenda
for each row
begin
update produtos set estoque = estoque + old.quantidade
where referencia = old.produto;
end$

delimiter ;

show triggers;

set sql_safe_updates = 0;

#deletou a ultima compra, retornando o valor anterior pro banco de dados
delete from itensvenda where produto = '001' and quantidade = 5;