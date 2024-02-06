import subprocess, os, sqlite3, shutil, ctypes
from pytube import YouTube
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioSessionManager2

def playing():
	sessions = AudioUtilities.GetAllSessions()
	for session in sessions:
		if session.Process and session.State == 1 and session.Process.name() == 'chrome.exe':
			return True

def get_url():
	if playing():
		path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\History'
		temp = os.path.expanduser('~') + r'\AppData\Local\Temp\ChromeHistoryTemp'
		shutil.copyfile(path, temp)
		conn = sqlite3.connect(temp)
		cursor = conn.cursor()
		cursor.execute("SELECT url FROM urls ORDER BY last_visit_time DESC LIMIT 45")
		for url in cursor.fetchall():
			if 'https://music.youtube.com/watch?' in url[0]:
				c_url = url[0]
				break
		conn.close()
		os.remove(temp)
		return c_url
	else:
		return False

def get_name(c_url):
	if playing():
		video = YouTube(c_url)
		rez = video.title + ' / ' + video.author
		return rez
	else:
		return False

if __name__ == '__main__':
	while True:
		print(get_name())
		input()