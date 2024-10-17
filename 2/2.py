input_string = input("Enter a series of integers separated by spaces: ")

numbers = input_string.split()
numbers = [int(num) for num in numbers]
total_sum = sum(numbers)

print(f"The sum of the numbers is: {total_sum}")