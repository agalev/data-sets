import polars as pl
# from datetime import datetime

df_csv = pl.read_csv('healthkit_heartrate.csv')
print(df_csv)

# out = dataframe.select([
#     "startDate",
#     "value",
# ])
# # out.write_csv('healthkit_heartrate.csv')
# out.write_json('healthkit_heartrate.json')