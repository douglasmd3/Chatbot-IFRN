drop database if exists dblocal;
create database dblocal;
use dblocal;

create table register(
	quantidade_de_usuario int not null

	);

create table interacao (
	quantidade_de_interacao int not null
	
	);
    
create table sugestao (
	nome varchar(250) not null,
	mensagem varchar (2000) /*será que é not null [entra em conversation e na hora de mandar texto, o cujo mandar mídia?] */
	
	);

create table satisfacao (
	_bom_ int not null,
	normal int not null,
	_ruim_ int not null
	
	);


/*alter table sugestao add column data_hora;*/


select * from sugestao;
select quantidade_de_usuario from register;
select quantidade_de_interacao from interacao;
select *from satisfacao;
select * from sugestao, register, interacao, satisfacao;

insert into sugestao(nome,mensagem) values ('oi', '');
insert into register (quantidade_de_usuario) values (0);
insert into interacao (quantidade_de_interacao) values (0);
insert into satisfacao (_bom_,normal,_ruim_) values (0,0,0);

update register set quantidade_de_usuario = 11;
update satisfacao set _bom_=1, _ruim_ = 3, normal = 10;
update interacao set quantidade_de_interacao = 87;
/*
truncate table satisfacao;
truncate table sugestao;
truncate table register;
truncate table interacao;

*/
/*depois do truncate tem que rodar o insert 0;*/
