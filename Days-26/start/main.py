
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "julia"
new_list = [letter for letter in name]
print(new_list)

range_list = [num * 2 for num in range(1, 5)]
print(range_list)

names = ["axel", "marie", "john", "elan", "julie"]
short_names = [name.upper() for name in names if len(name) >= 5]

print(short_names)