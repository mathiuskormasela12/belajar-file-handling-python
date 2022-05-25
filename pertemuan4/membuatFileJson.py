import json

data = [
	{
		'nama': 'Yerin',
		'usia': 26
	},
	{
		'nama': 'Mathius',
		'usia': 21
	}
]

with open('family.json', 'w') as jsonfile :
	json.dump(data, jsonfile)