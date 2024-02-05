from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon import TelegramClient
from time import sleep
import music, json

try:
	with open('config.json', 'r') as file:
		conf = file.read()
		conf = json.loads(conf)
		api_id, api_hash = conf[0], conf[1]
except FileNotFoundError:
	print('Файл конфига (config.json) не найден!')
	exit()
except json.decoder.JSONDecodeError:
	print('Заполните config.json в формате ["api_id", "api_hash"]')
	exit()


client = TelegramClient('session_name', api_id, api_hash)

async def main():
	try:
		await client.start()
	except:
		print('Указанны неправильные токены!')
		exit()
	try:
		print('Скрипт запущен..')
		full = await client(GetFullUserRequest('me'))
		default = full.full_user.about
		change = False
		old_rez = ''
		old_url = ''
		while True:
			url = music.get_url()
			if url and old_url != str(url):
				rez = music.get_name(url)
				if rez:
					rez = '🤖Скрипт показывает какую музыку я сейчас слушаю! 🎵Сейчас слушаю: ' + rez
					if old_rez != rez:
						await client(UpdateProfileRequest(about=rez))
						print('change')
						change = True
						old_rez = rez
				else:
					if change:
						await client(UpdateProfileRequest(about=default))
						change = False
						old_rez = ''
				old_url = url
			sleep(10)
	except KeyboardInterrupt:
		await client(UpdateProfileRequest(about=default))
		await client.disconnect()
client.loop.run_until_complete(main())