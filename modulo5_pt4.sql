-- ALTER TABLE Municipios_Brasileiros  ADD COLUMN pais;

-- UPDATE Municipios_Brasileiros SET pais='Brasil';

-- ALTER TABLE Municipios_Brasileiros DROP COLUMN pais;

-- SELECT Regiao FROM Municipios_Brasileiros;

-- SELECT * FROM Municipios_Brasileiros WHERE Cidade = 'Itaquaquecetuba';

-- SELECT * FROM Municipios_Brasileiros WHERE Cidade LIKE 'Itaqua%';

SELECT * FROM Municipio_Status WHERE populacao_residente >50000;