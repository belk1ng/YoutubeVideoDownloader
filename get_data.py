from pytube import YouTube
from check_url import correctUrl


def getData():
	video = correctUrl()
	if not video:
		return 'Действие было отменено'

	print('\nИнормация о видео:')
	print('-' * 50)
	print(f'Канал - {video.author}')
	print('-' * 50)
	print(f'Описание - {video.description}')
	print('-' * 50)
	print(f'Продолжительность видео - {video.length // 60}min {video.length % 60}sec')
	print('-' * 50)
	print(f'Дата публикации - {video.publish_date}')
	print('-' * 50)
	print(f'Просмотры - {video.views}')
	print('-' * 50)
	print(f'Рейтинг - {video.rating}')
	print('-' * 50)
	
	return 'Информация успешно предоставлена!'