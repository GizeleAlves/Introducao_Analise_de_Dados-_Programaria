SELECT Municipios_Brasileiros.Cidade, Municipio_Status.populacao_residente FROM  Municipios_Brasileiros 
INNER JOIN Municipio_Status ON Municipios_Brasileiros.municipio_ID = Municipio_Status.municipio_ID

 SELECT Estado, COUNT(Cidade) FROM Municipios_Brasileiros GROUP BY Estado ORDER BY 2 DESC;  

 SELECT SUM(pessoas_brancas), SUM(pessoas_pretas_pardas) FROM  Gerencia_Regiao ;

 SELECT Regiao, MIN(pessoas_pretas_pardas) FROM Gerencia_Regiao ;

SELECT Regiao FROM Gerencia_Regiao WHERE gerencia_branca >gerencia_preta_parda ;