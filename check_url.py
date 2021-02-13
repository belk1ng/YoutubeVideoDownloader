from pytube import YouTube
from pytube.exceptions import *


def correctUrl():
	while 1:
		try:
			url = input('\nВведите url-адрсес видео (Q - Отмена): ')
			if url.lower() == 'q':
				return False
			video = YouTube(url)
		
		except (RegexMatchError, VideoUnavailable, VideoRegionBlocked, VideoPrivate) as error:
			print(f'{error}\nВозникла ошибка... Проверьте url-адрес или доступость видео!')
		
		else:  # Если url проходит проверку
			break
	
	return video