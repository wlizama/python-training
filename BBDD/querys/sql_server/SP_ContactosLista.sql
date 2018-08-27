CREATE PROCEDURE SP_ContactosLista
AS
BEGIN
    SET NOCOUNT ON;
    SELECT * from Contactos;
END