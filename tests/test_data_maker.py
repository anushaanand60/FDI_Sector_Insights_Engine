import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from data_maker import make_clean_data


def test_make_clean_data_valid():
    data = {
        'Sector': ['A', 'B', 'Grand Total', 'Sumcheck'],
        '2000-01': [1, 2, 3, 4],
        '2001-02': [5, 6, 7, 8]
    }
    df = pd.DataFrame(data)
    df.to_excel("mock_data.xlsx", index=False)
    cleaned_df = make_clean_data("mock_data.xlsx")
    assert not cleaned_df['sector'].str.contains("Total|Sumcheck").any()
    assert 'inflow_mn_usd' in cleaned_df.columns
