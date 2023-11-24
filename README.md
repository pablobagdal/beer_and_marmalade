# beer_and_marmalade
For my bro
We will use
- Python
- venv

Для работы необходимо:
- Установить Python (обязательно ставить галочку на первой станице установки Add python to PATH)

Устанавливаем библиотеку venv через модуль загрузки пакетов pip / pip3
pip install venv

Далее

1. Скачиваем репозиторий
Заходим в его папку через терминал
cd /...///.../ или dir \..\...\..\..\.
2. Создаём виртуальное окружение
Windows
python -m venv venv
Linux / MacOS
python3 -m venv venv

Далее вход в вирт.окружение
wind
source venv/Scripts/activate
Linux/ MacOS
source venv/bin/activate

На будущее, для отключения venv понадобится 
deactivate

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

включить 
https://console.cloud.google.com/apis/library/sheets.googleapis.com?project=test123-406111

в помощь
https://practicaldatascience.co.uk/data-engineering/how-to-create-a-google-service-account-client-secrets-json-key
