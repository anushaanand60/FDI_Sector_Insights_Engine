import argparse
import logging
from data_maker import make_clean_data
from data_feeder import feed_to_sqlite

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, required=True)
parser.add_argument('--db', type=str, required=True)
parser.add_argument('--table', type=str, default='fdi_sector')
args = parser.parse_args()

logging.info("Starting FDI Pipeline...")
df = make_clean_data(args.input)
feed_to_sqlite(df, args.db, args.table)
logging.info("Pipeline completed.")
