import pandas as pd

NUMBER_OF_ITEMS = 29
BALANCE_SHEET_ID = '1kQp2gf0OT4NFoi_UFSCSMWqQcMOdEJ6Q'
STOCK_MOVEMENT_SHEET_ID = '112XZL4n09YQk3skjYVLe_xLAlNuEVrxs'


def with_sheet_id(sheet_id):
    def inner_function(func):
        def wrapper():
            df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
            assert df is not None
            return func(df)
        return wrapper
    return inner_function


@with_sheet_id(BALANCE_SHEET_ID)
def test_item_count_on_balance(df):
    assert len(df.index) == NUMBER_OF_ITEMS


@with_sheet_id(STOCK_MOVEMENT_SHEET_ID)
def test_item_count_on_movement(df):
    assert df['item'].nunique() == NUMBER_OF_ITEMS
