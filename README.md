# README for Telegram Music Status Updater (Ниже на русском языке)

## Overview
This Python project consists of a script that automatically updates your Telegram profile status with the music you are currently listening to on YouTube Music. The script `main.py` uses the Telethon library to interact with the Telegram API and a custom module `music.py` to fetch the currently playing music from YouTube Music in a Chrome browser session.

## Requirements
- Python 3.x
- Telethon
- Pytube
- Pycaw
- Comtypes

Install the required libraries using:
```bash
pip install -r requirements.txt
```

## Configuration
Before running the script, you need to set up the following:

1. **Telegram API credentials**: 
   - Obtain your `api_id` and `api_hash` from [Telegram API](https://my.telegram.org).
   - Create a `config.json` file in the same directory as your script with the format `["api_id", "api_hash"]`.

2. **Chrome History Access**: 
   - The script accesses the Chrome browser history to detect the currently playing YouTube Music track. Make sure Google Chrome is installed and you are using it to play music from YouTube Music.

## Usage
To run the script, simply execute `main.py`:
```bash
python main.py
```

## Functionality
- The script monitors the music you are currently playing on YouTube Music through Chrome.
- It updates your Telegram profile status with the title and artist of the currently playing track.
- If the music stops or changes, the script updates the status accordingly.
- The script resets your profile status to its original state upon termination.

## Notes
- The script only works with Google Chrome and YouTube Music.
- Ensure that Python, along with all required libraries, is correctly installed and configured on your system.
- Handle your Telegram API credentials securely and do not share your `config.json` file.

## Disclaimer
This project is intended for personal use and educational purposes only. Please respect privacy and use responsibly. The developer is not responsible for any misuse or damage caused by this script.


# README для обновления статуса Telegram музыкой

## Обзор
Этот проект на Python состоит из скрипта, который автоматически обновляет статус вашего профиля в Telegram информацией о музыке, которую вы в данный момент слушаете на YouTube Music. Скрипт `main.py` использует библиотеку Telethon для взаимодействия с API Telegram и пользовательский модуль `music.py` для извлечения информации о воспроизводимой музыке на YouTube Music в сессии браузера Chrome.


Установите необходимые библиотеки с помощью:
```bash
pip install -r requirements.txt
```

## Конфигурация
Перед запуском скрипта вам нужно настроить следующее:

1. **Учетные данные API Telegram**: 
   - Получите `api_id` и `api_hash` на [Telegram API](https://my.telegram.org).
   - Создайте файл `config.json` в той же директории, что и ваш скрипт, с форматом `["api_id", "api_hash"]`.

2. **Доступ к истории Chrome**: 
   - Скрипт получает доступ к истории браузера Chrome для определения текущего воспроизводимого трека на YouTube Music. Убедитесь, что Google Chrome установлен и вы используете его для прослушивания музыки на YouTube Music.

## Использование
Для запуска скрипта просто выполните `main.py`:
```bash
python main.py
```

## Функциональность
- Скрипт отслеживает музыку, которую вы в данный момент слушаете на YouTube Music через Chrome.
- Он обновляет ваш статус в профиле Telegram названием и исполнителем текущего трека.
- Если музыка останавливается или меняется, скрипт соответственно обновляет статус.
- При завершении работы скрипт возвращает ваш профиль в исходное состояние.

## Примечания
- Скрипт работает только с Google Chrome и YouTube Music.
- Убедитесь, что Python и все необходимые библиотеки установлены и правильно настроены на вашей системе.
- Бережно обращайтесь с вашими учетными данными API Telegram и не делитесь файлом `config.json`.

## Отказ от ответственности
Этот проект предназначен только для личного использования и образовательных целей. Пожалуйста, относитесь к приватности с уважением и используйте ответственно. Разработчик не несет ответственности за любое неправомерное использование или ущерб, вызванный этим скриптом.