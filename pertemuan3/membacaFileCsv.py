import csv

rows = []

with open('family.csv', 'r') as csvfile :
	csvreader = csv.DictReader(csvfile)
	rows = list(csvreader)
	print('Total baris', csvreader.line_num)

for row in rows :
	# print(row['nama'] + ' => ' + row['usia'])
	print('Nama :', row['nama'])
	print('Usia :', row['usia'])