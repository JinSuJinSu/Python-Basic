students = [
    {
        "name": "Kim",
        "kor": 80,
        "eng": 90,
        "math": 80
    },
    {
        "name": "Lee",
        "kor": 90,
        "eng": 85,
        "math": 85
    }
]


for dict in students:
    sum_value = 0
    avg_count = 0

    for key in dict:
        if key!='name':
            sum_value+=dict[key]
            avg_count+=1
        else:
            pass

    dict['total'] = sum_value
    dict['average'] = round((sum_value/avg_count),2)

print(students)





