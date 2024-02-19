import os
from dotenv import load_dotenv
import polars as pl

load_dotenv()

db = os.getenv('db')

# df_csv = pl.read_csv('healthkit_heartrate.csv')
# print(df_csv)

# out = dataframe.select([
#     "startDate",
#     "value",
# ])
# # out.write_csv('healthkit_heartrate.csv')
# out.write_json('healthkit_heartrate.json')

# READ FROM DATABASE
# query = "SELECT * FROM healthkit_heartrate"
# print(pl.read_database_uri(query=query, uri=db, engine='adbc'))

# Expanded Print
# with pl.Config(tbl_cols=-1):
#     print(out)

# WRITE TO DATABASE
# df = pl.read_json('healthkit_workouts.json').unnest('metadata')
# out = df.select(pl.col('*').exclude(pl.Null)).sort('start')
# out.write_database(table_name='healthkit_workouts', connection=db, engine='adbc')