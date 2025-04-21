import daft
from daft.io import IOConfig, AzureConfig
import os
from dotenv import load_dotenv
import json

load_dotenv()

storage_account_key=os.environ.get('STORAGE_ACCOUNT_KEY')
storage_account_name=os.environ.get('STORAGE_ACCOUNT_NAME')

io_config = IOConfig(azure=AzureConfig(storage_account=storage_account_name, access_key=storage_account_key))
daft.set_planning_config(default_io_config=io_config)

# new line delimited json so all has to be on one line
df_dogs_json = daft.read_json("az://test/dogs/*.json")
df_dogs_json.column_names
df_dogs_json.write_deltalake("az://delta/dogs", mode="overwrite")
df_dogs_delta = daft.read_deltalake("az://delta/dogs")
print("Show sample 5 rows of wine")
df_dogs_delta.show(n=5)

# df_cheese_countries = daft.sql("SELECT  country, count(1) AS Cheeses FROM df_cheeses_delta GROUP BY country ORDER BY Cheeses DESC")
# df_cheese_countries.write_deltalake("az://event/delta/cheeses_by_country", mode="overwrite")
# df_cheese_countries_delta = daft.read_deltalake("az://event/delta/cheeses_by_country")
# print("Show top 10 countries with most cheeses")
# df_cheese_countries_delta.show(n=10)

# daft.read_json("az://events/cheeses.json").write_deltalake("az://events/delta/cheeses_json", mode="overwrite")