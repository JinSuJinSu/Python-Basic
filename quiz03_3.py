def summary(*args):
     value_list = list(args)
     return sum(value_list), max(value_list), min(value_list), sum(value_list)/len(value_list)


total, maxval, minval, avg = summary(80, 75, 90, 95, 85)

print(total, maxval, minval, avg)
print(total, maxval, minval, avg)