def summary(*args):
    value_list = list(args)
    return sum(value_list), max(value_list), min(value_list), sum(value_list) / len(value_list)


total, max_val, min_val, avg = summary(80, 75, 90, 95, 85)

print(total, max_val, min_val, avg)
