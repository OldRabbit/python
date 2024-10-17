input_string = input("Enter 5 digits separated by spaces: ")

digits_list = input_string.split()
reversed_list = digits_list[::-1]
reversed_number = ''.join(reversed_list)

print(f"The number formed by the reversed list is: {reversed_number}")