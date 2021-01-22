import pandas as pd

NUMERO_DE_ITENS = 29

def le_csv(sheet_id):
    return pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")