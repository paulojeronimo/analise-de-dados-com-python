#!/usr/bin/env python
from lib.movto import calcula
from lib.resultado import salva_em_excel, df_resultado
from lib.comum import DEBUG_FALSE, DEBUG_TRUE
from lib.linha import *


def acumula(df, linha, saldos_iniciais):
    if DEBUG_FALSE:
        print("linha 0: ", linha)
    linha = ajusta_saldos_finais(ajusta_saldos_iniciais(linha, saldos_iniciais))
    if DEBUG_FALSE:
        print("linha 1: ", linha)
    saldos_finais = linha['qtd_saldo_final'], linha['vlr_saldo_final']
    return df.append(linha, ignore_index=True), saldos_finais


salva_em_excel(calcula(df_resultado, acumula))
