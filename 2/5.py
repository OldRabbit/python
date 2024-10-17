professions = ['Doctor', 'Engineer', 'Teacher', 'Artist', 'Chef']

print("Original list of professions:", professions)

professions.reverse()
print("After reverse():", professions)

professions.sort()
print("After sort():", professions)

unsorted_list = ['Programmer', 'Carpenter', 'Doctor']
sorted_list = sorted(unsorted_list)
print(f"Original list: {unsorted_list}, Sorted copy: {sorted_list}")

print("Length of the professions list:", len(professions))

print(f"The first profession is: {professions[0]}")
print(f"The last profession is: {professions[-1]}")

print("A slice of the list (first 3 elements):", professions[:3])