CREATE PROCEDURE SP_ContactosInsertar
	@id int OUTPUT,
	@nombre varchar (250),
	@apodo varchar (100),
	@numero varchar (10),
	@cumpleanhos varchar(5)
AS
BEGIN
    SET NOCOUNT ON;
    INSERT INTO Contactos 
	values(
		@nombre,
		@apodo,
		@numero,
		@cumpleanhos
	)

	SELECT @id = @@IDENTITY;
END