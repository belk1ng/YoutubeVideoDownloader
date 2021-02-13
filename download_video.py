from pytube import YouTube


def videoDownloader():
	url = input('\nВведите url-адрес видео, которое хотите скачать: ')
	video = YouTube(url)
	
	samples = video.streams.all()
	for i in range(len(samples)):
	    print(f'{i}. {samples[i]}')

	downloadNum = int(input('Введите номер видео, которое хотите скачать: '))
	samples[downloadNum].download('/home/dmitry/passwordManager')

	return
	
