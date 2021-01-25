def cria_linha(entradas_e_saidas_0, entradas_e_saidas_1=None):
    def transforma(entradas_e_saidas):
        return {'item': entradas_e_saidas['item'],
                'data_lancamento': entradas_e_saidas['data_lancamento'],
                'qtd_entrada': entradas_e_saidas['quantidade'] if entradas_e_saidas['tipo_movimento'] == 'Ent' else 0,
                'vlr_entrada': entradas_e_saidas['valor'] if entradas_e_saidas['tipo_movimento'] == 'Ent' else 0,
                'qtd_saida': entradas_e_saidas['quantidade'] if entradas_e_saidas['tipo_movimento'] == 'Sai' else 0,
                'vlr_saida': entradas_e_saidas['valor'] if entradas_e_saidas['tipo_movimento'] == 'Sai' else 0
                }

    if entradas_e_saidas_1 is not None:
        es0 = transforma(entradas_e_saidas_0)
        es1 = transforma(entradas_e_saidas_1)
        return {'item': es0['item'], 'data_lancamento': es0['data_lancamento']} | \
               {k: es0[k] + es1[k] for k in ('qtd_entrada', 'vlr_entrada', 'qtd_saida', 'vlr_saida')}
    return transforma(entradas_e_saidas_0)


def ajusta_saldos_iniciais(linha, saldos_iniciais):
    qtd_saldo_inicial, vlr_saldo_inicial = saldos_iniciais
    return linha | {'qtd_saldo_inicial': qtd_saldo_inicial, 'vlr_saldo_inicial': vlr_saldo_inicial}


def ajusta_saldos_finais(linha):
    saldo_final = lambda t: linha[f'{t}_saldo_inicial'] + linha[f'{t}_entrada'] - linha[f'{t}_saida']
    return linha | {'qtd_saldo_final': round(saldo_final('qtd'), 4), 'vlr_saldo_final': round(saldo_final('vlr'), 2)}
