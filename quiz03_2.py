lst = [1, 3.14, 'python', 7, 89.1, 3]

result_array = []

for value in lst:
    if isinstance(value, int) or isinstance(value, float):
        result_array.append(value)

    else:
        pass

print(result_array)
