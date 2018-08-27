CREATE PROCEDURE SP_ContactosBuscaXApodo
	@apodo varchar (250)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT * from Contactos
	where apodo = @apodo;
END