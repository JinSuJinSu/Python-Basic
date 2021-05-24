string = "Life is too short, You need Python"

new_string = string.lower().replace(',' , '').strip().replace(' ' , '')

lst = list(new_string)

chars = set(lst)

lst = list(chars)

lst.sort()

print(len(lst))
print(lst)