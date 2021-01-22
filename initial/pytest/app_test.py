import pandas as pd

def test_item_count_on_balance():
    sheet_id = '1kQp2gf0OT4NFoi_UFSCSMWqQcMOdEJ6Q'
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
    assert df is not None
    assert len(df.index) == 29
