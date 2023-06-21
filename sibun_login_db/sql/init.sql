create table USUARIO
(
   E_MAIL               varchar(60) not null,
   NOMBRE       		varchar(60) not null,
   APELLIDO       		varchar(60) not null,
   USUARIO               varchar(60) not null,
   CONTRASENA           varchar(60) not null,
   DIRECCION            varchar(60) not null,
   primary key (E_MAIL)
);


create table SESION
(
   E_MAIL_USUARIO           varchar(60) not null,
   TOKEN             varchar(30) not null,
   FECHA_INICIO           timestamp default current_timestamp on update current_timestamp,

   primary key (TOKEN)
);

create table ADMINISTRADOR
(
   E_MAIL               varchar(60) not null,
   NOMBRE       		varchar(60) not null,
   CONTRASENA           varchar(60) not null,
   primary key (E_MAIL)
);


ALTER TABLE `sibunlogin`.`SESION` 
ADD INDEX `EMAIL_USUARIO_idx` (`E_MAIL_USUARIO` ASC) VISIBLE;
;
ALTER TABLE `sibunlogin`.`SESION` 
ADD CONSTRAINT `EMAIL_USUARIO`
  FOREIGN KEY (`E_MAIL_USUARIO`)
  REFERENCES `sibunlogin`.`USUARIO` (`E_MAIL`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
