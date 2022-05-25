import csv 

rows = [
	{ 'nama': 'Mathius', 'usia': 21 },
	{ 'nama': 'Yerin', 'usia': 26  }
]

with open('family.csv', 'a') as csvfile :
	fields = ['nama', 'usia']
	writer = csv.DictWriter(csvfile, fieldnames = fields)
	writer.writeheader()
	writer.writerows(rows)