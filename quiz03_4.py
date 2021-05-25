s = """We encourage everyone to contribute to Python. 
If you still have questions after reviewing the material 
in this guide, then the Python Mentors 
group is available to help guide new contributors through the process."""

new_string = s.replace(',', '').replace('.', '').replace('\n', '').upper()

string_list = new_string.split()

string_set = set(string_list)

for string in string_set:
    print(string + ' : ' + str(string_list.count(string)))


