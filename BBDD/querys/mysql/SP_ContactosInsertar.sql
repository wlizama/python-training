CREATE PROCEDURE `SP_ContactosInsertar`(
	OUT id int,
	nombre varchar (250),
	apodo varchar (100),
	numero varchar (10),
	cumpleanhos varchar(5)
)
BEGIN
	INSERT INTO Contactos 
	values(
		0,
		nombre,
		apodo,
		numero,
		cumpleanhos
	);
    
    SET id = LAST_INSERT_ID();
END