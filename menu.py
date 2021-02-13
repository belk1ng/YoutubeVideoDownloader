from pytube import YouTube
from get_data import getData
from download_video import videoDownloader


print('Привет! Я - загрузчик видео с платформы YouTube.')

actions = {
	'i': getData,
	'd': videoDownloader
}

while 1:
	print()
	print('-' * 50)
	print('Выбери действие: ')
	print('I - Получить информацию о видео')
	print('D - Скачать видео')
	print('Q - Выход')
	print('-' * 50)
	action = input(': ').lower()

	if action == 'q':
		print('\nБыл рад с тобой поработать!')
		break

	elif action in set('id'):
		print(actions[action]())

	else:
		print('\nВыбери верный пункт из меню!\n')
