
# TOTAL DE VAGAS APLICATIVO
vagasAplicativo = 'WITH total_dermato AS ( SELECT '
vagasAplicativo = vagasAplicativo + "C.NM_FANTASIA_ESTAB AS ESTABELECIMENTO, "
vagasAplicativo = vagasAplicativo + "OBTER_NOME_MEDICO(B.CD_PESSOA_FISICA,'N') AS PROFISSIONAL, "
vagasAplicativo = vagasAplicativo + "OBTER_DESC_ESPEC_MEDICA(B.CD_ESPECIALIDADE) AS ESPECIALIDADE, "
vagasAplicativo = vagasAplicativo + "COUNT(A.IE_STATUS_AGENDA) AS QUANTIDADE_DE_VAGAS "
vagasAplicativo = vagasAplicativo + "from AGENDA_CONSULTA A "
vagasAplicativo = vagasAplicativo + "INNER JOIN AGENDA B ON (A.CD_AGENDA = B.CD_AGENDA) "
vagasAplicativo = vagasAplicativo + "INNER JOIN ESTABELECIMENTO C ON (B.CD_ESTABELECIMENTO = C.CD_ESTABELECIMENTO) "
vagasAplicativo = vagasAplicativo + "WHERE "
vagasAplicativo = vagasAplicativo + "A.IE_STATUS_AGENDA = 'L' "
vagasAplicativo = vagasAplicativo + "AND B.CD_ESPECIALIDADE IN(49) "                              # A CONSULTA FOI ALTERADA AQUI. FORMA ADICIONADOS NOVOS CÓDIGOS DE ESPECIALIDADE
vagasAplicativo = vagasAplicativo + "AND C.CD_ESTABELECIMENTO <> '22' "
vagasAplicativo = vagasAplicativo + "AND A.DT_AGENDA BETWEEN SYSDATE AND (SYSDATE+10) "
vagasAplicativo = vagasAplicativo + "GROUP BY C.NM_FANTASIA_ESTAB, OBTER_NOME_MEDICO(B.CD_PESSOA_FISICA,'N'), OBTER_DESC_ESPEC_MEDICA(B.CD_ESPECIALIDADE) "
vagasAplicativo = vagasAplicativo + "ORDER BY COUNT(A.IE_STATUS_AGENDA) DESC, C.NM_FANTASIA_ESTAB, OBTER_NOME_MEDICO(B.CD_PESSOA_FISICA,'N'), OBTER_DESC_ESPEC_MEDICA(B.CD_ESPECIALIDADE) "
vagasAplicativo = vagasAplicativo + "), "
vagasAplicativo = vagasAplicativo + "total_ped AS ( "
vagasAplicativo = vagasAplicativo + "select "
vagasAplicativo = vagasAplicativo + "C.NM_FANTASIA_ESTAB AS ESTABELECIMENTO, "
vagasAplicativo = vagasAplicativo + "OBTER_NOME_MEDICO(B.CD_PESSOA_FISICA,'N') AS PROFISSIONAL, "
vagasAplicativo = vagasAplicativo + "OBTER_DESC_ESPEC_MEDICA(B.CD_ESPECIALIDADE) AS ESPECIALIDADE, "
vagasAplicativo = vagasAplicativo + "COUNT(A.IE_STATUS_AGENDA) AS QUANTIDADE_DE_VAGAS "
vagasAplicativo = vagasAplicativo + "from AGENDA_CONSULTA A "
vagasAplicativo = vagasAplicativo + "INNER JOIN AGENDA B ON (A.CD_AGENDA = B.CD_AGENDA) " 
vagasAplicativo = vagasAplicativo + "INNER JOIN ESTABELECIMENTO C ON (B.CD_ESTABELECIMENTO = C.CD_ESTABELECIMENTO) "
vagasAplicativo = vagasAplicativo + "WHERE A.IE_STATUS_AGENDA = 'L' " 
vagasAplicativo = vagasAplicativo + "AND B.CD_ESPECIALIDADE IN(3) "
vagasAplicativo = vagasAplicativo + "AND C.CD_ESTABELECIMENTO <> '22' " 
vagasAplicativo = vagasAplicativo + "AND A.DT_AGENDA BETWEEN SYSDATE AND (SYSDATE+6) "
vagasAplicativo = vagasAplicativo + "GROUP BY C.NM_FANTASIA_ESTAB, OBTER_NOME_MEDICO(B.CD_PESSOA_FISICA,'N'), OBTER_DESC_ESPEC_MEDICA(B.CD_ESPECIALIDADE) " 
vagasAplicativo = vagasAplicativo + "ORDER BY COUNT(A.IE_STATUS_AGENDA) DESC, C.NM_FANTASIA_ESTAB, OBTER_NOME_MEDICO(B.CD_PESSOA_FISICA,'N'), OBTER_DESC_ESPEC_MEDICA(B.CD_ESPECIALIDADE) )" 
vagasAplicativo = vagasAplicativo + "SELECT * FROM ("
vagasAplicativo = vagasAplicativo + "SELECT ESPECIALIDADE, SUM(QUANTIDADE_DE_VAGAS) AS QTD FROM total_dermato GROUP BY ESPECIALIDADE " 
vagasAplicativo = vagasAplicativo + "UNION SELECT ESPECIALIDADE, SUM(QUANTIDADE_DE_VAGAS) AS QTD FROM total_ped GROUP BY ESPECIALIDADE " 
vagasAplicativo = vagasAplicativo + ")ORDER BY QTD"  