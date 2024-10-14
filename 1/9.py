number = 2659

thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10

sum_of_digits = thousands + hundreds + tens + units

print(f"{thousands} + {hundreds} + {tens} + {units} = {sum_of_digits}")
