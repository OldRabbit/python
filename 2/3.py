cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']

if len(cities) != 6:
	print('List length is not equal to 6')
	exit()

message = ', '.join(cities[:-1]) + ' and ' + cities[-1]

print(message)