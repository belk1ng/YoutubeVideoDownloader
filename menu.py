from pytube import YouTube
from get_data import getData
from download_video import videoDownloader

# Добавить возможность выбрать путь, куда грузить видео
# Улучшить оформление (сделать поаакуратнее)
# Почистить код

print('Привет! Я - загрузчик видео с платформы YouTube.')
print('-' * 50)
print('Выбери действие: ')
print('I - Получить информацию о видео')
print('D - Скачать видео')
print('Q - Выход')
print('-' * 50)

actions = {
	'i': getData,
	'd': videoDownloader
}

while 1:
	action = input(': ')

	if action.lower() == 'q':
		print('Был рад с тобой поработать!')
		break

	elif action in 'id':
		print(actions[action]())

	else:
		print('\nВыбери верный пункт из меню!')
