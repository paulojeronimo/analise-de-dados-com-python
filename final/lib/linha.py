def cria_linha(item, data_lancamento, qtd_entrada, vlr_entrada, qtd_saida, vlr_saida):
    return locals()


def ajusta_saldos_finais(linha):
    saldo_final = lambda t: linha[f'{t}_saldo_inicial'] + linha[f'{t}_entrada'] - linha[f'{t}_saida']
    return linha | { 'qtd_saldo_final': saldo_final('qtd'), 'vlr_saldo_final': saldo_final('vlr') }


def ajusta_saldos_iniciais(linha, qtd_saldo_inicial, vlr_saldo_inicial):
    d = locals()
    return linha | {i: d[i] for i in d if i != 'linha'}
