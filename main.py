import gspread as gs
import pandas as pd

from links import *
from functions import *

filename = 'service_account.json'

if __name__ == '__main__':
    # page_num = int(input('Введите номер страницы: '))
    item_num = int(input('Введите номер предмета: ')) - 1

    gc = gs.service_account(filename='service_account.json')

    sh = gc.open_by_url(table_url)

    ws = sh.worksheet('пиво')

    df = pd.DataFrame(ws.get_all_records())
    df.head()

    # Пример использования
    result_text = generate_text(df.iloc[item_num])
    print()
    print()
    print()
    print(result_text)
    print()
    print()
