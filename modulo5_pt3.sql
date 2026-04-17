CREATE TABLE Municipios_Brasileiros (
Cidade NVARCHAR(50) NOT NULL,
Estado NVARCHAR(2) NOT NULL,
Regiao NVARCHAR(20) NOT NULL,
municipio_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
)

CREATE TABLE Municipio_Status (
status_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
populacao_redidente INTEGER NOT NULL,
IDH_rank INTEGER NOT NULL,
educacao INTEGER NOT NULL,
renda INTEGER NOT NULL,
municipio_ID INTEGER NOT NULL,
CONSTRAINT fk_municipio FOREIGN KEY (municipio_ID) REFERENCES Municipios_Brasileiros (municipio_ID)
)

CREATE TABLE Gerencia_Regiao(
gerencia_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
Regiao TEXT(20) NOT NULL,
pessoas_brancas INTEGER NOT NULL,
pessoas_pretas_pardas INTEGER NOT NULL,
gerencia_branca INTEGER NOT NULL,
gerencia_preta_parda INTEGER NOT NULL,
CONSTRAINT fk_regiao FOREIGN KEY (Regiao) REFERENCES Municipios_Brasileiros(Regiao)
)