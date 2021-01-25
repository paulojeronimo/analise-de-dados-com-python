import pandas as pd


def df_resultado():
    return pd.DataFrame({k: [] for k in (
        'item',
        'data_lancamento',
        'qtd_entrada',
        'vlr_entrada',
        'qtd_saida',
        'vlr_saida',
        'qtd_saldo_inicial',
        'vlr_saldo_inicial',
        'qtd_saldo_final',
        'vlr_saldo_final'
    )})


def salva_em_excel(df, nome_arquivo='resultado.xlsx'):
    writer = pd.ExcelWriter(nome_arquivo, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()
    print(f'Arquivo {nome_arquivo} gerado!')
