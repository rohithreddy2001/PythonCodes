# List Comprehension
numbers = [i for i in range(1, 21)]
even = [i for i in numbers if i % 2 == 0]
odd = [i for i in numbers if i % 2 != 0]
squares = [i**2 for i in numbers]
print(f"Even numbers:", even)
print(f"Odd numbers:", odd)
print(f"Square of numbers:", squares)

# Set Comprehensions
repeated_numbers = [1, 2, 3, 2, 4, 6, 8, 6]
even_set = {i for i in repeated_numbers if i % 2 == 0}
print(f"Even set:", even_set)

# Dictionary Comprehensions
countries = ['India', 'USA', 'Canada']
cities = ['Hyderabad', 'New York', 'Toronto']

key_val_dict = {key:val for key, val in zip(countries, cities)}
print(key_val_dict)

for k, v in key_val_dict.items():
    print(f"{k} : {v}")

print(key_val_dict['India'])



