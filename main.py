import gspread as gs
import pandas as pd

from links import *


gc = gs.service_account(filename='service_account.json')

sh = gc.open_by_url(table_url)

ws = sh.worksheet('пиво')

df = pd.DataFrame(ws.get_all_records())
df.head()


# Функция для формирования текста
def generate_text(row):
    
    template = "{рейтинг}\n{название_1} {название_2}\nстрана: {страна}\n\nстиль: {стиль}\n" \
               "ПН: {ПН}\nABV: {ABV}\nIBU: {IBU}\nplato: {plato}\nобъем: {объем}\n\n" \
               "{пена}/5 пена\n{аромат}/5 аромат\n{кислость}/5 кислотность\n" \
               "{горькость}/5 горькость\n{питкость}/5 питкость\n{вкус}/5 вкус\n\n{комментарий}"
    result_text = template.format(
        рейтинг=row['рейтинг'],
        название_1=row['название 1'],
        название_2=row['название 2'],
        страна=row['страна'],
        стиль=row['стиль'],
        ПН=row['пиво'],
        ABV=row['ABV'],
        IBU=row['IBU'],
        plato=row['plato'],
        объем=row['объем'],
        пена=row['пена'],
        аромат=row['аромат'],
        кислость=row['кислость'],
        горькость=row['горькость'],
        питкость=row['питкость'],
        вкус=row['вкус'],
        комментарий=row['комментарий']
    )
    return result_text

# Пример использования

page_num = int(input('Введите номер страницы: '))
item_num = int(input('Введите номер предмета: '))

result_text = generate_text(df.iloc[item_num])
print(result_text)
