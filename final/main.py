#!/usr/bin/env python

import pandas as pd

from lib.linha import *
from lib.movto import movto_df
from lib.resultado import *

# Código INCOMPLETO: ainda em desenvolvimento!
def calcula_entradas_e_saidas_por_item_e_data():
    grupo_item_data = movto_df().groupby(['item', 'data_lancamento'])
    for k, i in grupo_item_data:
        grupo1 = grupo_item_data.get_group(k)
        print(grupo1)
        grupo_df = pd.DataFrame(grupo1)
        grupo_entrada_saida = grupo_df.groupby(['tipo_movimento']).sum()
        print(grupo_entrada_saida)

# Código apenas para testes ...
df = resultado_df()
linha = ajusta_saldos_finais(
    ajusta_saldos_iniciais(
        cria_linha('80.03.104-1', '8/27/2012', 34100, 70992.96, 0, 0),
        66780, 132613.28))
df = df.append(linha, ignore_index=True)

linha_anterior = linha
linha = ajusta_saldos_finais(
    ajusta_saldos_iniciais(
        cria_linha('80.03.104-1', '8/28/2012', 12090, 25170.07, 0, 0),
        linha_anterior['qtd_saldo_final'], linha_anterior['vlr_saldo_final']))
df = df.append(linha, ignore_index=True)

salva_em_excel(df)

calcula_entradas_e_saidas_por_item_e_data()