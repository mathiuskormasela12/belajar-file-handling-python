import json

with open('family.json', 'r') as jsonfile :
	data = json.load(jsonfile)
	for row in data :
		print(row)