
# Belajar Membuka dan Membaca File
# file = open('hello.txt', 'r')
# text = file.read()
# print(text)

# Belajar Replace Isi File
# file = open('hello.txt', 'w')
# file.write('Belajar Typescript')

# Belajar Replace Isi File dan Membacanya
# file = open('hello.txt', 'r+')
# file.write('Belajar Javascript')
# file.seek(0)
# text = file.read()
# print(text)

# Belajar Menulis Isi File dan Membacanya
file = open('hello.txt', 'a+')
file.write('\n Belajar Python')
file.seek(0)
text = file.read()
print(text)
