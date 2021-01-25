import pandas as pd

NUMERO_DE_ITENS = 29
DEBUG_TRUE = True
DEBUG_FALSE = False
LE_ARQUIVO_LOCAL = False

def le_arquivo(sheet_id):
    if LE_ARQUIVO_LOCAL:
        print(f"Lendo arquivo {sheet_id} localmente ...")
        return pd.read_excel(sheet_id, sheet_name=0)
    print(f"Lendo arquivo {sheet_id} a partir do Google Sheets ...")
    return pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
