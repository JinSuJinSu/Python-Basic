# 함수 인수는 필요한 개수만큼 선언
def sum_val(a, b):
    return a + b

def incr(a, step=1):    # 두번째 인자는 기본값이 있다
    return a + step

print(sum_val(2, 3))    # 고정 인수를 전달할 때는 순서대로
print(incr(10)) # 기본 값이 있는 인수는 전달하지 않으면 기본값이 선택
print(incr(10, 2))  # 두 번째 인수의 기본값 무시, 전달한 값을 할당

# 키워드 인수
# 인수의 값을 인수의 이름으로 전달 -> 인수의 순서는 바뀌어도 무관
def area(width, height):
    print("width:", width)
    print("height:", height)
    return width * height

print(area(10, 12)) # 인수 이름 명시 안함 -> 선언 순서대로 전달
print(area(height=12, width=10)) # 인수 이름 명시 -> 인수의 순서와는 관계 없음

# 가변인수
# 정해지지 않은 개수의 인수를 받을 때
# 인수명 앞에 *를 붙여 선언
def get_total(*args):   # 여러 개의 인수를 전달 -> 합산 후 반환
    total = 0
    print("인수:", args, type(args))
    for x in args:
        total += x
    return total

print(get_total(1, 3, 5, 7, 9))

# 응용 문제
# 1. 가변인수로 값을 넘긴다
# 2. int, float일 경우, 합산
# 3. list, tuple일 경우, 내부 루프 돌면서 합산
# 4. 나머지는 합산하지 않음
# 5. 재귀 하지 않음

def get_total2(*args):
    total = 0
    for x in args:
        if isinstance(x, (int, float)): # 인수값이 int or float
            total += x
        elif isinstance(x, (list, tuple)):   # 인수가 list or tuple
            for item in x:
                if isinstance(item, (int, float)):
                    total += item
    return total

print(get_total2(1, 2, 3, 4, 5))
print(get_total2(1, 2, "3", 4, 5))
print(get_total2(1, 2, [3, 4, 5]))

# 사전 키워드
# 지정되지 않은 키워드들 -> dict로 변환되서 사전 키워드로 전달
# 사전 키워드 인수 앞에 ** 를 붙인다.
def args_test(a, b, *args, **kwd):
    # a, b -> 고정 인수
    # args -> 가변 인수
    # kwd -> 사전 키워드 인수
    print("고정인수:", a, b)
    print("가변인수:", args)
    print("사전 키워드 인수:", kwd)


# 순서 중요: 고정인수들 -> 가변인수 -> 사전 키워드 인수 순
args_test(10, 20, 30, 40, 50, option1="value1", option2="value2")

# 함수도 객체다
# 함수도 변수에 참조 할당 되거나, 다른 함수의 인수로 전달 될 수 있음
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def calculator(a, b, func): # a, b -> 숫자, func -> 함수 전달
    if (callable(func)):    # 넘어온 인수 func가 실행 가능 객체인가?
        return func(a, b)

print(calculator(1, 2, plus))   # 합산 함수를 외부에서 전달

dirty_strings = "python pRogRamming, jaVa pRoGRAMMING, LINUX , WinDoWs".split(",")
print(dirty_strings)

def clean_string(strings, *funcs):
    results = []
    for string in strings:
        # print(string)
        for func in funcs:
            if callable(func):  # 넘어온 인자가 실행 가능 객체임을 확인
                string = func(string)
        results.append(string)
    return results

cleaned = clean_string(dirty_strings, str.strip, str.title)
print("CLEANED:", cleaned)