import gspread as gs
import pandas as pd

from links import *


gc = gs.service_account(filename='service_account.json')

sh = gc.open_by_url(table_url)

ws = sh.worksheet('page1')

df = pd.DataFrame(ws.get_all_records())
df.head()

print(df)
