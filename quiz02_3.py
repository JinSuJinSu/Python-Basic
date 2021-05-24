total_money = 0

running = True

while running:
    condition = input('method:')

    if condition=='d':
        deposited_money = int(input('Amount:'))
        total_money += deposited_money
        print('Balance:' + str(total_money))

    elif condition=='w':
        withdrawed_money = int(input('Amount:'))

        if total_money - withdrawed_money >=0:
            total_money -= withdrawed_money

        else:
            print('잔액이 부족합니다!!!')

        print('Balance:' + str(total_money))


    elif condition=='q':
        print('종료 종료 종료')
        running = False

    else:
        print('?????')


