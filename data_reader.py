from data_maker import make_clean_data
from data_feeder import feed_to_sqlite

def read_and_store(input_path: str, db_path: str, table_name: str = "fdi_sector"):
    df = make_clean_data(input_path)
    feed_to_sqlite(df, db_path, table_name)
    return df
