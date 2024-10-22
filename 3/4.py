e2g = {
    'stork': 'storch',
    'hawk': 'falke',
    'woodpecker': 'specht',
    'owl': 'eule'
}

print("English-German Dictionary (e2g):")
print(e2g)

print("\nThe German word for 'owl' is:", e2g['owl'])

e2g['sparrow'] = 'spatz'
e2g['eagle'] = 'adler'

print("\nUpdated English-German Dictionary (e2g):")
print(e2g)

keys_list = list(e2g.keys())
values_list = list(e2g.values())

print("\nKeys (English words):", keys_list)
print("Values (German translations):", values_list)