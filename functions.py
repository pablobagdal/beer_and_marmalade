

# Функция для формирования текста
def generate_text(row):
    template = '''
{рейтинг}
**{название_1} {название_2}**
страна: {страна}

стиль: {стиль}
ПН: {ПН}
ABV: {ABV}
IBU: {IBU}
plato: {plato}
объем: {объем}

{пена}/5 пена
{аромат}/5 аромат
{кислость}/5 кислотность
{горькость}/5 горькость
{питкость}/5 питкость
{вкус}/5 вкус

{комментарий}

(к списку)[https://t.me/ouroboris/92]
    '''

    # template = \
    #     "{рейтинг}\n{название_1} {название_2}\nстрана: {страна}\n\nстиль: {стиль}\n" \
    #     "ПН: {ПН}\nABV: {ABV}\nIBU: {IBU}\nplato: {plato}\nобъем: {объем}\n\n" \
    #     "{пена}/5 пена\n{аромат}/5 аромат\n{кислость}/5 кислотность\n" \
    #     "{горькость}/5 горькость\n{питкость}/5 питкость\n{вкус}/5 вкус\n\n{комментарий}"

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