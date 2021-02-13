from pytube import YouTube
from check_url import correctUrl



def videoDownloader():
	video = correctUrl()
	if not video:
		return 'Действие было отменено'
	path = input(r'Введите путь, по которому нужно сохранить видео: ')
	
	print()
	print('-' * 50)
	
	samples = video.streams.all()
	for i in range(len(samples)):
	    print(f'{i + 1}) {samples[i]}')  # Начало с 1
	
	print('-' * 50)

	while True:
		downloadNum = int(input('\nВведите номер видео, которое хотите скачать: ')) - 1
		if downloadNum in range(len(samples)):  # Проверка введенного числа
			print('Произвожу скачивание...')
			break
		else:
			print('Введите существующий номер видео из списка!')

	samples[downloadNum].download(path)  # Качаем видео в введённый каталог

	return 'Видео успешно скачано!'
