dictionary = {
    'Kyiv': {
        'country': 'Ukraine',
        'population': 2962180,
        'fact': 'Kyiv is one of the oldest cities in Eastern Europe, founded in the 5th century.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'Tokyo is the most populous city in the world and is known for its skyscrapers and cherry blossoms.'
    },
    'New York': {
        'country': 'USA',
        'population': 8419600,
        'fact': 'New York City is home to the Statue of Liberty, a symbol of freedom and democracy.'
    }
}

for key, value in dictionary.items():
    print(f"{key}:")
    print(f"  Country: {value['country']}")
    print(f"  Population: {value['population']}")
    print(f"  Fact: {value['fact']}\n")
