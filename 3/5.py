dictionary = [
    {
        'name': 'Buddy',
        'type': 'dog',
        'owner': 'Alex'
    }, 
    {
        'name': 'Mittens',
        'type': 'cat',
        'owner': 'Jordan'
    }, 
    {
        'name': 'Goldie',
        'type': 'fish',
        'owner': 'Emily'
    }, 
    {
        'name': 'Coco',
        'type': 'parrot',
        'owner': 'Sophia'
    }
]

for item in dictionary:
    print(f"{item['owner']} is the owner of a pet - a {item['type']} named {item['name']}.")
