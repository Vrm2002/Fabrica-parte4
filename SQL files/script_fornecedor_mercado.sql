create database Mercado character set utf8mb4 collate utf8mb4_unicode_ci;

use Mercado;

create table fornecedor( 
cod_fornecedor varchar(30) not null,
nome varchar(100) not null,
cidade_sede varchar(100) not null,
grupo_cod_fornecedor varchar(30),
primary key(cod_fornecedor)
);

create table material(
cod_material int not null,
cod_fornecedor varchar(30) not null,
constraint foreign key (cod_fornecedor) references fornecedor(cod_fornecedor),
nome varchar(100) not null,
descricao text not null,
primary key(cod_material)
);

insert into fornecedor(cod_fornecedor, nome, cidade_sede, grupo_cod_fornecedor) values
('ABC', 'ABC Materiais Eletricos', 'Vitoria', Null),
('XYZ', 'XYZ Materiais de Escritorio', 'Rio de Janeiro', 'HiX'),
('Hidra', 'Hidra Materiais Hidraulicos', 'Sao Paulo', 'HiX'),
('HiX', 'HidraX Materiais Eletricos e Hidraulicos', 'Sao Paulo', Null);

insert into material(cod_material, cod_fornecedor, nome, descricao) values
(123, 'ABC', 'Tomada eletrica 10A Nova', 'Tomada eletrica 10A padrao novo'),
(234, 'ABC', 'Disjuntor 25A', 'Disjuntor eletrico 25A'),
(345, 'XYZ', 'Resma Papel A4', 'Resma papel branco A4'),
(456, 'XYZ', 'Toner Imp HR5522', 'Toner impressora HR5522'),
(678, 'Hidra', 'Cano PVC 1/2', 'Cano PVC 1/2 pol'),
(679, 'Hidra', 'Cano PVC 3/4', 'Cano PVC 3/4 pol'),
(680, 'Hidra', 'Medidor hidr 1/2', 'Medidor hidraulico 1/2 pol'),
(681, 'Hidra', 'Joelho 1/2', 'Conector Joelho 1/2 pol'),
(682, 'Hidra', 'Junta 1/2', 'Cano PVC 1/2 pol'),
(1234, 'ABC', 'Tomada eletrica 20A Nova', 'Tomada eletrica 20A padrao novo'),
(2345, 'XYZ', 'Caneta Azul', 'Caneta esferografica azul'),
(4567, 'XYZ', 'Grampeador', 'Grampeador mesa pequeno'),
(4568, 'XYZ', 'Caneta Marca Texto Amarela', 'Caneta Marca Texto Amarela'),
(4569, 'XYZ', 'Lapis HB', 'Lapis Preto HB');

select * from material;
describe material;
describe fornecedor;
