create database prueba; -- crear base de datos
-- drop database test; borra base de datos

use prueba; -- indica la base de datos que quiero utilizar

create table Usuario(id int, email varchar(255), username varchar(50));
-- drop table Usuario;

-- PARA MODIFICAR TABLA, AGREGAR/ELIMINAR/MODIFICAR CAMPOS/AGREGAR PK Y HACERLA AUTO INCREMENTAL
-- alter table Usuario add edad int; -- ALTER TABLE [Tabla] ADD [campo] [type]
-- alter table Usuario drop column edad; -- ALTER TABLE [Tabla] DROP COLUMN [campo]
-- alter table Usuario modify column email varchar(50); -- ALTER TABLE [Tabla] MODIFY COLUMN [campo] [type]
-- alter table Usuario add primary key (id); -- ALTER TABLE [Tabla] ADD PRIMARY KEY ([campo]) "suele ser id la PK"
-- alter table Usuario modify column id int AUTO_INCREMENT;  -- ALTER TABLE [Tabla] MODIFY COLUMN [campo] [type] AUTO_INCREMENT; "el valor del id incrementa con cada registro agregado"

-- AGREGAR/ELIMINAR REGISTROS A LA TABLA
-- insert into Usuario (email, username) values ("bruno@a.com", "brunoleonpuca") -- INSERT INTO [Tabla] [campo/s] values [valores]
insert into Usuario (email, username, edad) values ("chanchito@c.com", "chanchito feliz", 86);
-- delete from Usuario where email = "bruno@a.com" limit 1; -- DELETE FROM Usuario WHERE [campo] = [valor] limit 1

-- ACTUALIZAR VALOR DE REGISTRO
update Usuario set edad = 32 where id = "1"; -- UPDATE [Tabla] SET [campo] = [valorNuevo] WHERE [PK] = "[valorPK]";

-- ELIMINAR REGISTROS USANDO PK
delete from Usuario where id = "3"; -- DELETE FROM [Tabla] WHERE [PK] = "[valorPK]"
