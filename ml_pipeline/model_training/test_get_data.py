
import pandas as pd

from get_data import load_and_sort_data


def test_load_and_sort_data():
    result = load_and_sort_data(2)
    assert len(result) == 2

    df1, df2 = result
    assert type(df1) == pd.DataFrame
    assert type(df2) == pd.DataFrame

    assert df1.shape[0] > 0
    assert df1.shape[1] > 0
    assert df2.shape[0] > 0
    assert df2.shape[1] > 0
