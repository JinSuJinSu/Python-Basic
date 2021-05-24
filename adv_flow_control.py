def if_statement():
    """
    if문 연습
    """
    # 금액을 입력 받고
    # 10000원 이상이면 by taxi
    #   1000원 이상이면 by bus
    #   그 미만이면 on foot을 출력
    money = int(input("얼마 가지고 있어?"))

    message = ""
    if money >= 10000:
        message = "by taxi"
    elif money >= 1000:
        message = "by bus"
    else:
        message = "on foot"

    print(message)


def cond_expr():    # 조건 표현식
    # C, Java의 3항 연산자와 비슷한 역할
    money = int(input("얼마 가지고 있어?"))

    message = "by taxi" if money >= 10000 else "by bus" if money >= 1000 else "on foot"
    print(message)


def for_ex():
    """
    for 반복문
    """
    # Syntax: for 변수 in 순차형:
    a = ["cat", "cow", "tiger"]
    for animal in a:
        print(animal, end=" ")
    else:   # 반복문이 break되지 않고 정상 종료시 마지막에 수행
        print()

    # 반복시 요소와 함께 인덱스도 함께 필요할 때 -> enumerate 함수 -> (인덱스, 요소) 튜플
    for index, color in enumerate(['red', 'blue', 'green', 'black', 'whie']):   # (인덱스, 요소) 튜플
        print(index, color)

    # range 객체 (범위객체)
    # 1 ~ 10까지 합 구하기
    total = 0
    for i in range(1, 11):  # 1 ~ 10까지
        total += i

    print("total:", total)

    # break : 남은 루프를 진행하지 않고 루프를 탈출
    r1 = list(range(1, 12, 2)) + [12, 13, 15]
    print("r1:", r1)
    # 첫 번째 짝수를 출력 -> 종료
    for i in r1:
        if i % 2 == 0:
            print("첫번째 짝수를 찾았습니다:", i)
            break   # 루프 탈출
    else:
        print("짝수는 없습니다.")  # break로 탈출하면 실행되지 않는다

    # continue : 남은 실행문 실행하지 않고 다음번 루프
    # 0 ~ 10까지 범위 중에서 짝수는 제외하고 출력
    for i in range(11):
        if i % 2 == 0:  # 짝수면
            continue
        print(i, end=" ")
    else:
        print()

    # 연습문제 1. 2단 ~ 9단까지 구구표 출력
    # 연습문제 2. 삼각형 그리기
    """
    *
    **
    ***
    ****
    *****
    """


def while_ex():
    """
    while 문 연습
    """
    # While문 버전 연습문제
    # 연습문제 1. 2단 ~ 9단까지 구구표 출력
    # 연습문제 2. 삼각형 그리기
    """
    *
    **
    ***
    ****
    *****
    """


def mulmul():
    for i in range(2,10):
        for j in range(1,10):
            print('{}X{}={}'.format(i,j,i*j),end=' ')
        print()

def make():
    for i in range(5):
        print('*' * (i + 1))


if __name__ == "__main__":
    # if_statement()
    # cond_expr()
    for_ex()