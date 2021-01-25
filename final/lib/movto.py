import pandas as pd

from lib.comum import le_arquivo, LE_ARQUIVO_LOCAL, DEBUG_TRUE, DEBUG_FALSE
from lib.linha import cria_linha
from lib.saldo import saldo_df, obtem_saldos_iniciais

MOVTO_SHEET_ID = '../MovtoITEM.xlsx' if LE_ARQUIVO_LOCAL else '112XZL4n09YQk3skjYVLe_xLAlNuEVrxs'


def movto_df():
    return le_arquivo(MOVTO_SHEET_ID)


def calcula_entradas_e_saidas(item, data_lancamento, grupo_item_data_lancamento):
    entradas_e_saidas = []
    for tipo_movimento, grupo in grupo_item_data_lancamento.groupby('tipo_movimento'):
        somatorio_quantidade_valor = grupo.sum()
        quantidade = round(somatorio_quantidade_valor.loc['quantidade'], 4)
        valor = round(somatorio_quantidade_valor.loc['valor'], 2)
        entradas_e_saidas.append({'item': item,
                                  'data_lancamento': data_lancamento,
                                  'tipo_movimento': tipo_movimento,
                                  'quantidade': quantidade,
                                  'valor': valor})
    if DEBUG_FALSE:
        print(f"len(entradas_e_saidas): {len(entradas_e_saidas)}")
    if len(entradas_e_saidas) == 1:
        return cria_linha(entradas_e_saidas[0])
    return cria_linha(entradas_e_saidas[0], entradas_e_saidas[1])


def calcula(inicializa, acumula):
    def print_saldos_finais(item_atual):
        if DEBUG_TRUE and item_atual != None:
            print(f"Saldos finais para o item {item_atual}: {saldos}\n\n")

    df = inicializa()
    df_saldo = saldo_df()

    df_movto = movto_df()
    df_movto['data_lancamento'] = pd.to_datetime(df_movto['data_lancamento'], format='%m/%d/%Y')
    df_movto = df_movto.sort_values(['item', 'data_lancamento'], ascending=False)

    item_atual = None
    for item_data_lancamento, grupo in df_movto.groupby(['item', 'data_lancamento']):
        item = grupo['item'].unique()[0]
        data_lancamento = grupo['data_lancamento'].unique()[0]
        if item != item_atual:
            print_saldos_finais(item_atual)
            item_atual = item
            if DEBUG_TRUE:
                print(f"Item atual alterado para {item}")
            saldos = obtem_saldos_iniciais(df_saldo, item)
            if DEBUG_TRUE:
                print(f"Saldos iniciais para o item {item_atual}: {saldos}")
        entradas_e_saidas = calcula_entradas_e_saidas(item, data_lancamento, grupo)
        if DEBUG_FALSE:
            print(f"""
                item: {item}
                data_lancamento: {data_lancamento}
                saldos_iniciais: {saldos}
                entradas_e_saidas: {entradas_e_saidas}
                """)
        df, saldos = acumula(df, entradas_e_saidas, saldos)
    print_saldos_finais(item_atual)
    return df
