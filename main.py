import os
from dotenv import load_dotenv
import polars as pl

load_dotenv()

# from datetime import datetime

# df_csv = pl.read_csv('healthkit_heartrate.csv')
# print(df_csv)

# out = dataframe.select([
#     "startDate",
#     "value",
# ])
# # out.write_csv('healthkit_heartrate.csv')
# out.write_json('healthkit_heartrate.json')

db = os.getenv('db')
query = "SELECT * FROM competitions"

print(pl.read_database_uri(query=query, uri=db, engine='adbc'))