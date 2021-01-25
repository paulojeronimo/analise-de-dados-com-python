from lib.comum import NUMERO_DE_ITENS, le_arquivo
from lib.movto import MOVTO_SHEET_ID
from lib.saldo import SALDO_SHEET_ID


def with_sheet_id(sheet_id):
    def inner_function(func):
        def wrapper():
            df = le_arquivo(sheet_id)
            assert df is not None
            return func(df)

        return wrapper

    return inner_function


@with_sheet_id(SALDO_SHEET_ID)
def test_item_count_on_balance(df):
    assert len(df.index) == NUMERO_DE_ITENS


@with_sheet_id(MOVTO_SHEET_ID)
def test_item_count_on_movement(df):
    assert df['item'].nunique() == NUMERO_DE_ITENS
