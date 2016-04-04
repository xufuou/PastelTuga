/*==============================================================*/
/* DBMS name:      PostgreSQL 7.3                               */
/* Created on:     16-12-2013 20:39:23                          */
/*==============================================================*/


drop table CAPITAIS;

drop table CLIENTES;

drop table DISTRIBUIDORAS;

drop table ENCOMENDAS;

/*==============================================================*/
/* Table: CAPITAIS                                              */
/*==============================================================*/
create table CAPITAIS (
ID_CAPITAL           SERIAL               not null,
ID_DISTRIBUIDORA     INT4                 not null,
CAPITAL              TEXT                 not null,
DISTANCIA            NUMERIC              not null,
DURACAO              NUMERIC              not null,
PRECO                NUMERIC              not null,
constraint PK_CAPITAIS primary key (ID_CAPITAL)
);

/*==============================================================*/
/* Table: CLIENTES                                              */
/*==============================================================*/
create table CLIENTES (
ID_CLIENTE           SERIAL               not null,
NOME_CLIENTE         TEXT                 not null,
TELEFONE             NUMERIC              not null,
MORADA               TEXT                 not null,
CIDADE               TEXT                 not null,
constraint PK_CLIENTES primary key (ID_CLIENTE)
);

/*==============================================================*/
/* Table: DISTRIBUIDORAS                                        */
/*==============================================================*/
create table DISTRIBUIDORAS (
ID_DISTRIBUIDORA     SERIAL               not null,
NOME_DISTRIBUIDORA   TEXT                 not null,
constraint PK_DISTRIBUIDORAS primary key (ID_DISTRIBUIDORA)
);

/*==============================================================*/
/* Table: ENCOMENDAS                                            */
/*==============================================================*/
create table ENCOMENDAS (
ID_FATURA            SERIAL               not null,
ID_DISTRIBUIDORA     INT4                 not null,
ID_CLIENTE           INT4                 not null,
DATA                 DATE                 not null,
HORA                 TIME                 not null,
QUANTIDADE           NUMERIC              not null,
constraint PK_ENCOMENDAS primary key (ID_FATURA)
);

alter table CAPITAIS
   add constraint FK_CAPITAIS_DISTRIBUI_DISTRIBU foreign key (ID_DISTRIBUIDORA)
      references DISTRIBUIDORAS (ID_DISTRIBUIDORA)
      on delete restrict on update restrict;

alter table ENCOMENDAS
   add constraint FK_ENCOMEND_DISTRIBUI_DISTRIBU foreign key (ID_DISTRIBUIDORA)
      references DISTRIBUIDORAS (ID_DISTRIBUIDORA)
      on delete restrict on update restrict;

alter table ENCOMENDAS
   add constraint FK_ENCOMEND_ENCOMENDA_CLIENTES foreign key (ID_CLIENTE)
      references CLIENTES (ID_CLIENTE)
      on delete restrict on update restrict;

