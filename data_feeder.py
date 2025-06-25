import sqlite3
import logging

logging.basicConfig(level=logging.INFO)

def feed_to_sqlite(df, db_path: str, table_name: str):
    logging.info(f"Writing to SQLite DB: {db_path} → Table: {table_name}")
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, con=conn, if_exists='replace', index=False)
    conn.close()
    logging.info("Data successfully written to DB.")
