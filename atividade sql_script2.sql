create database BIKEDATA character set utf8mb4 collate utf8mb4_unicode_ci;

use BIKEDATA;

create table Acct_Typ_Cd_LU_Tab (Acct_Code int not null, Account_Type varchar(30) not null, primary key (Acct_Code));

create table Customer
(Customer_ID int not null,
Customer_Lname varchar(100) not null,
Customer_Fname varchar(100) not null,
Cust_street varchar(50) not null,
Cust_city varchar(50) not null,
Cust_zip varchar(9) not null,
Cust_phone int not null,
Fax_phone int not null,
primary key (Customer_ID));

create table Customer_Account
(Customer_ID int not null,
Last_purch_dte date not null,
Last_pymt_dte date not null,
Last_acct_trans_dte date not null,
Acct_balance float not null,
primary key(Customer_ID));

create table Transaction_code (Trans_code int not null, Transaction_descript varchar(200) not null, primary key (Trans_code));

create table  Customer_Acct_Hist1
(Customer_ID int not null,
Trans_dte date not null,
Old_acct_balance float not null,
New_acct_balance float not null,
primary key (Customer_ID));

create table State_Ikup (St_code int not null, State_name varchar(50) not null, primary key (St_code));

create table Supplier
(Supplier_ID int not null,
Sup_street varchar(50) not null,
Sup_city varchar(50) not null,
Sup_zip varchar(9) not null,
Sup_phone int not null,
Sup_fax int not null,
primary key (Supplier_ID));

create table Parts_Inventory
(Bar_Code varchar(13) not null,
Part_name varchar(100) not null,
Prt_Description varchar(200) not null,
Prt_cost varchar(50) not null,
Prt_price float not null,
Quantity int not null,
primary key (Bar_Code));

create table Bike_Inventory
(Seq_ID int not null,
Serial_Number int not null,
Inventory_dte date not null,
primary key (Seq_ID));

create table Bike_Description
(Model_ID int not null,
Model_name varchar(100) not null,
Sale_price float not null,
Descript varchar(200) not null,
primary key (Model_ID));

create table Purchase_Order
(Seq_ID int not null,
Purch_dte date not null,
Serial_num int not null,
Quantity int not null,
Price float not null,
primary key (Seq_ID));