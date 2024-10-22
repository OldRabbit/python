dictionary = {
    'NEW YORK KNICKS': [22, 7, 6, 9, 45],
    'LOS ANGELES LAKERS': [20, 10, 5, 5, 55],
    'BOSTON CELTICS': [24, 12, 6, 6, 60],
    'MIAMI HEAT': [25, 15, 3, 7, 51],
    'GOLDEN STATE WARRIORS': [21, 11, 8, 2, 63]
}

for key, value in dictionary.items():
    print(f"{key} {value[0]} {value[1]} {value[2]} {value[3]} {value[4]}")
