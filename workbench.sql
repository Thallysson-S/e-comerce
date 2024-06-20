
create database commerce_db;
use commerce_db;

create table produtos ( 
id int auto_increment primary key,
nome varchar(50) not null,
codigobar varchar(50) not null,
preco decimal (10,2) not null, 
descricao text
 );

create table cliente (
id_cliente int auto_increment primary key,
nome varchar(50) not null,
email varchar(50) not null,
endereco varchar(50) not null,
telefone varchar(50) not null
);

select * from cliente;

select * from produtos;