# Aplikasi Input Sederhana

def add_to_list(text) :
	file = open('data.txt', 'a+')
	file.write('\n' + text)
	file.seek(0)
	text2 = file.read()
	print('Anda telah membeli', text2)
	ask_user()

def ask_user() :
	add_to_list(input('Mau beli apa : '))

ask_user()