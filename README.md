# beer_and_marmalade

## Инструкция по настройке для Windows

Для работы потребуются установка:
1. Python
2. venv 

### Установка Python
* Зайти на оф.сайт [Python](https://python.org/download/)
* Скачать последнюю версию
* Установить Python (обязательно поставить галочку на первой станице установки **Add python to PATH**)
* Следовать всем дальнейшим указаниям установщика по умолчанию
***
### Установка venv
venv нужен для того, чтобы у вас были установлены правильные версии всех необходимых библиотек. Вдобавок, это упростит процесс установки библиотек в принципе.

Этапы установки:
* Открыть терминал\командную строку\консоль (всё одно и то же)
* Прописать команду:

```bash
pip install venv
```

На этом установка завершена. 
***
### Скачивание репозитория

Теперь вам необходимо загрузить файлы с данного репозитория. Самый простой способ сделать это - нажать на зелёную кнопку выше и выбрать кнопку **Download ZIP**.

Выберите некоторое место для разархивирования. Для определённости рассмотрим, что он будем находиться в папке repo в папке Documents:

```cmd
C:\Users\user\Documents\repo\bear_and_marmalate
```
Далее:

1. Открываем консоль по адресу нашей разархивированной папки с помощью команды:
```cmd
dir C:\Users\user\Documents\repo\bear_and_marmalate
```

2. Создаём виртуальное окружение с помощью venv:
```cmd
python -m venv venv
```
В результате в папке bear_and_marmalade мы обнаружим появление новой папки под названием venv. Она нам сейчас пригодится.

Открываем виртуальное окружение (venv):
```cmd
source venv/Scripts/activate
```

На будущее, для отключения venv понадобится короткая команда

```cmd
deactivate
```

С этого этапа можно сделовать инструкции с [данной статьи](https://practicaldatascience.co.uk/data-engineering/how-to-create-a-google-service-account-client-secrets-json-key). Приведу её на русском и чуть более детально.
<!-- 
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib -->

* Зайти в браузер в подключённым гугл аккаунтом
* Открыть ссылку [Google Sheets API](https://console.cloud.google.com/apis/library/sheets.googleapis.com?project=test123-406111)
* Активировать данный модуль для своего пользователя
* Открыть [Google Developer Console](https://console.cloud.google.com/cloud-resource-manager)
* Нажать CREATE PROJECT
* Придумать любое название и создать
* Нажать слева сбоку три полоски Navigation Menu -> APIs & Services
* Выбрать нужный проект
* Слева сбоку выбрать пункт Credentials
* Нажать Create credentials -> Service account
* Придумать любое имя и создать
* В нижнем списке Service accounts выбрать созданный аккаунт
* Открыть в верхней части раздел Keys
* Add key
* Выбрать JSON
* Подождать, начнётся скачивание
* Дать файлу имя service_key.json
* Разместитькачанный файл




`Выделенные слова`

    выделенный блок
    текста
    dir/fonts



Блок текста с подсветкой синтаксиса кода
указаываем тройной апостраф и после него указываем
язык синтаксиса подсветки

```python
print('hello world')
```

> Текст
>
> Продолжение текста в выделенном блоке


Нумерованный список

1. Пункт 1
2. Пункт 2
3. Пункт 3

_Наклонный_ _шрифт_

![pic_of_nature](https://upload.wikimedia.org/wikipedia/commons/8/80/140-P1020281_-_Flickr_-_Laurie_Nature_Bee.jpg)
![pic_of_nature](https://upload.wikimedia.org/wikipedia/commons/8/80/140-P1020281_-_Flickr_-_Laurie_Nature_Bee.jpg)