-- QUERIES DE MYSQL PARA EXPLORAR EN TABLAS
-- SELECT * FROM prueba.usuario; "basica"
use prueba; -- Aclaramos que bdd queremos utilizar
-- select * from Usuario; -- seleccionamos todo el contenido de la tabla
select * from Usuario limit 1; -- limita la cantidad de resultados que devuelve
-- select * from Usuario where email = "bruno@a.com" -- WHERE para filtrar la tabla [campo] = [valor]
select * from Usuario where edad < 25; -- operadores para filtrar