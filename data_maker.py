import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def make_clean_data(file_path: str) -> pd.DataFrame:
    logging.info(f"Loading Excel: {file_path}")
    df = pd.read_excel(file_path)
    original_rows = len(df)
    df = df[~df['Sector'].astype(str).str.contains("Total|Sumcheck", na=False)]
    cleaned_rows = len(df)
    logging.info(f"Filtered rows: {original_rows} → {cleaned_rows}")
    df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]
    df = df.melt(id_vars='sector', var_name='year', value_name='inflow_mn_usd')
    df['year'] = df['year'].astype(str)
    df['inflow_mn_usd'] = pd.to_numeric(df['inflow_mn_usd'], errors='coerce')
    df = df.dropna(subset=['inflow_mn_usd'])
    logging.info(f"Final rows after melt and cleaning: {len(df)}")
    return df
