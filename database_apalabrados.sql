use apalabrados;
CREATE TABLE NUMEROS(
	ID_NUM INT IDENTITY PRIMARY KEY,
	NUMERO FLOAT NOT NULL,
	ACUMULADO FLOAT NOT NULL
);

CREATE TABLE TEXTO(
	ID_TEXT INT IDENTITY PRIMARY KEY,
	TEXTO VARCHAR(500) NOT NULL,
	INICIAL VARCHAR(1) NOT NULL,
	FINAL VARCHAR(1) NOT NULL
);

CREATE TABLE CARACTER(
	ID_CHAR INT IDENTITY PRIMARY KEY,
	CARACTER VARCHAR(1) NOT NULL
);

SELECT * FROM  SYSOBJECTS WHERE XTYPE = 'U';
