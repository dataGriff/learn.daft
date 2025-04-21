import daft
from daft.io import IOConfig, AzureConfig
import os
from dotenv import load_dotenv

load_dotenv()

storage_account_key=os.environ.get('STORAGE_ACCOUNT_KEY')
storage_account_name=os.environ.get('STORAGE_ACCOUNT_NAME')

io_config = IOConfig(azure=AzureConfig(storage_account=storage_account_name, access_key=storage_account_key))
daft.set_planning_config(default_io_config=io_config)

df_csv = daft.read_csv("az://test/cheeses.csv")
df_csv.write_deltalake("az://test/delta/cheeses", mode="overwrite")
df_delta = daft.read_deltalake("az://test/delta/cheeses")
df_delta.show()

df_cheese_countries = daft.sql("SELECT  country, count(1) AS Cheeses FROM df_delta GROUP BY country ORDER BY Cheeses DESC")
df_cheese_countries.show(n=20)