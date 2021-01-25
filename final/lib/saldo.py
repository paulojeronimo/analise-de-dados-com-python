from lib.comum import le_arquivo, LE_ARQUIVO_LOCAL

SALDO_SHEET_ID = '../SaldoITEM.xlsx' if LE_ARQUIVO_LOCAL else '1kQp2gf0OT4NFoi_UFSCSMWqQcMOdEJ6Q'


def saldo_df():
    return le_arquivo(SALDO_SHEET_ID)


def obtem_saldos_iniciais(df_saldo, item):
    item_df = df_saldo.loc[df_saldo['item'] == item]
    return item_df['qtd_inicio'].values[0], item_df['valor_inicio'].values[0]
