import gspread as gs
import pandas as pd
import threading
from links import *
from functions import *
import time

gc = None
filename = 'service_account.json'


def my_caller():
    global gc
    gc = gs.service_account(filename)


if __name__ == '__main__':
    # new_thread = threading.Thread(target=my_caller)
    # new_thread.start()

    # page_num = int(input('Введите номер страницы: '))
    # item_num = int(input('Введите номер предмета: ')) - 1
    
    time.sleep(3)
    page_num = 1
    item_num = 2

    new_thread.join()

    # gc = gs.service_account(filename='service_account.json')

    sh = gc.open_by_url(table_url)

    ws = sh.worksheet('пиво')

    df = pd.DataFrame(ws.get_all_records())
    df.head()

    # Пример использования


    result_text = generate_text(df.iloc[item_num])
    print(result_text)
