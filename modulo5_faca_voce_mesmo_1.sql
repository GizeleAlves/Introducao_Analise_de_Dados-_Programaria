-- Como seria a query para somar a população total de um estado e ordenar pelo estado com menor população?


SELECT Municipios_Brasileiros.Estado, Municipio_Status.populacao_residente FROM Municipios_Brasileiros 
INNER JOIN Municipio_Status WHERE Municipios_Brasileiros.municipio_ID = Municipio_Status.municipio_ID 
GROUP BY Estado ORDER BY 2 ASC;