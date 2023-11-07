create database titanic_base char set utf8mb4 collate utf8mb4_unicode_ci;
use titanic_base;

create table Passenger(
Passanger_id int primary key not null,
Survived varchar (2) not null,
PClass int not null,
Passanger_Name varchar(100) not null,
Sex varchar(20) not null,
Age varchar (5),
SibSP varchar (2) not null,
Parch varchar (2) not null,
Ticket varchar (50) not null,
Fare varchar (100) not null,
Cabin varchar(100),
Embarked varchar(1) not null
);

select * from Passenger;

#quantos passageiros sobreviveram? 152
select count(*) from Passenger where Survived = 1;

#quantas crianças abaixo de 12 anos sobreviveram? 109
select sum(Survived) from Passenger where Age < 12;
select count(Survived) from Passenger where Age < 12 and Survived = 1;

#quantas mulheres sobreviveram?
select count(Survived) from Passenger where Sex = 'female' and Survived = 1;

#quantos homens sobreviveram?
select count(Survived) from Passenger where Sex = 'male' and Survived = 1;




