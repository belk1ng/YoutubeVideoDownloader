from pytube import YouTube


def getData():
	url = input('\nВведите url-адрес видео, информацию о котором хотите получить: ')
	video = YouTube(url)
	
	return f'\nИнормация о видео:\nАвтор - {video.author}\n\
Описание - {video.description}\nПродолжительность видео - {video.length} секунды\n\
Дата публикации - {video.publish_date}\nПросмотры - {video.views}\nРейтинг - {video.rating}'