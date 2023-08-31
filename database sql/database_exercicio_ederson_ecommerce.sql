create database ecommerce; #database escrito errado
use ecommerce;


create table  produtos(  #falta parenteses
    id_prod int(5) auto_increment not null, #Auto increment só funciona caso seja uma primary key
    nome_prod varchar(100) not null,
    descricao text,
    modelo varchar(50),
    id_categoria int(5),
    id_fabricante int(5), #tem uma virgula a mais
    primary key(id_prod)); #adicionando primary key

    
create table clientes (
    id_cli int auto_increment not null, #auto_increment não funciona com varchar ou char, e por erro de compatibilidade com uma foreign key mudei pra int
    nome varchar(100) not null,
    cpf varchar(11),
    telefone varchar(50),
    sexo enum('F','M'),
    cadastro datetime,
    constraint primary key (id_cli)); 
    

create table pedidos(
	num_pedido int(5) auto_increment not null,
	data datetime,
	status varchar(50),
    	id_cli int(5), #ambas as colunas relacionadas tem de ser do mesmo tipo, esta é int e a outra é varchar, então ambas não vão se relacionar
    	constraint primary key (num_pedido),
    	constraint foreign key (id_cli) references clientes(id_cli) 
    );

    #table escrito errado na linha abaixo
	create table pedido_item(
	idtem_pedido int(5) auto_increment not null,
	num_pedido int(5) not null,
    qtde int(5) not null,
    valor_unit decimal(10,2),
    total decimal(10,2),
    id_prod int(5),
    constraint primary key (idtem_pedido),
    constraint foreign key (num_pedido) references pedidos(num_pedido), #linha 42 e 43 foreign escrito errado
    constraint foreign key (id_prod) references produtos(id_prod)
    );

    create table estoque_produtos(
		id_estoque int(5) auto_increment, #este recebe auto_increment pois não pode ser vazio por ser uma primary key
        quantidade int(5) not null,
        quant_min int(5),
        id_prod int(5), #falta parenteses no fim do int
        constraint primary key (id_estoque),
		constraint foreign key (id_prod) references produtos(id_prod)
        );
        
	insert into clientes values (null,'João','02102202324','6799999999','M',now()); #clientes escrito errado
    insert into clientes values (null,'Tadeu','02102202366','6799999999','M',now()); #insert escrito errado
    insert into clientes values (null,'Francisco','02102202399','6799999999','M',now());
    insert into clientes values (null,'Maria','02102202377','6799999999','F',now());
    insert into clientes values (null,'Vinicius','32102202399','6799999999','M',now());
    insert into clientes values (null,'Antonia','02102202388','6799999999','F',now());
    select * from clientes;
    
	insert into produtos values (null,'Notebook Dell','Core i5,8GB,SDD 240GB','Inspirion 1500',null,null);
    insert into produtos values (null,'Notebook Acer','Core i5,8GB,SDD 240GB','Aspire T',null,null);
    insert into produtos values (null,'Notebook Asus','Core i5,8GB,SDD 240GB','A95Z',null,null);
    insert into produtos values (null,'Notebook Apple','Core i7, 16GB, SDD 512GB','BookPRo',null,null);
    insert into produtos values (null,'Notebook Positivo','Celerom,4GB,HD 1TB','POS8080',null,null);
    
    insert into produtos values (null,'Placa-Mãe ASUS','Onboard','P',null,null);
    insert into produtos values (null,'Processador AMD','4.2Ghz','Ryzen5',null,null); #faltava aspas no Processador AMD


    insert into produtos values (null,'Placa de Vídeo RADEON','8GB','RX5500',null,null);
    insert into produtos values (null,'Fonte Corsair','Selo 80plus','CX1200W',null,null); #faltava aspas no CX1200W

    
	select * from produtos;
    describe estoque_produtos; #describe escrito errado


	insert into estoque_produtos values (null,80,10,1);
    insert into estoque_produtos values (null,44,5,9);
    insert into estoque_produtos values (null,55,5,8);
    insert into estoque_produtos values (null,36,5,7);
    insert into estoque_produtos values (null,49,5,6);
    insert into estoque_produtos values (null,100,5,1);
    insert into estoque_produtos values (null,100,5,2);
    insert into estoque_produtos values (null,100,5,3);
    insert into estoque_produtos values (null,100,5,4);
    insert into estoque_produtos values (null,100,5,5); #estoque_produtos escrito errado em quase todos
