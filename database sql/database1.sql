create database estrutura character set utf8mb4 collate utf8mb4_unicode_ci;
use estrutura;

create table Cliente (
codcliente int auto_increment,
nome varchar(100) not null,
datanasc date not null,
cpf int not null, 
primary key(codcliente)
);

create table Pedido (
codpedido int auto_increment,
codcliente int,
constraint clientePedido foreign key (codcliente) references Cliente (codcliente),
datapedido date not null,
nf int not null,
valortotal float not null,
primary key(codpedido)
);

create table Produto (
codproduto int not null,
descri varchar(300) not null,
quantidade int not null,
primary key(codproduto)
);

create table ItemPerdido (
numeroitem int not null,
codpedido int,
constraint ItemPerdidoPedido foreign key (codpedido) references Pedido (codpedido),
valorunitario float not null,
quantidade int not null,
codproduto int,
constraint ItemPerdidoProduto foreign key (codproduto) references Produto (codproduto),
primary key (numeroitem)
);

create table LOG (
codlog int auto_increment,
datas date not null,
descri varchar(300) not null,
primary key(codlog)
);

create table Requisicao_Compra (
cod_req_compra int auto_increment,
codproduto int,
constraint RequisicaoProduto foreign key (codproduto) references Produto (codproduto),
datas date not null,
quantidade int not null,
primary key(cod_req_compra)
);

show tables;