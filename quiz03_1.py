initial_value = input('수를 입력하세요')

if initial_value.isdigit():

    result_array = [x for x in range(1,int(initial_value)+1) if x%3==0]

    result = sum(result_array)

    print('1부터 {}까지 3의 배수의 합 = {}'.format(initial_value,result))

else:
    print('정수가 아닙니다. 다시 입력하세요')


