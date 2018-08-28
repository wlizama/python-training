CREATE PROCEDURE `SP_ContactosBuscaXApodo`(
	apodo varchar(250)
)
BEGIN
	SELECT * from Contactos
	where Contactos.apodo = apodo;
END