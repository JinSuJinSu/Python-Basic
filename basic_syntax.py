
# 연산자 연습
def arith_oper():   # 산술 연산자 연습
    print("====== 산술연산")
    # +, -, *, /
    print(7/3)  # 정수를 정수로 나눠도 실수형태로 표현
    print(6/2)

    # // : 정수 나눗셈의 몫연산자
    print(7//3) # 정수 나눗셈의 몫
    print(7 % 3) # 정수 나눗셈의 나머지 연산자

    # divmod 함수 : 몫과 나머지 동시에 구하기
    print(divmod(7, 3)) # 7을 3으로 나눈 몫과 나머지
    print(divmod(7, 3)[0]) # 몫
    print(divmod(7, 3)[1]) # 나머지

    # 제곱 연산자 : **
    print(7**3) # 7의 3승
    print(pow(7, 3)) # 내장 수치 제곱함수


def complex_ex():
    print("===== 복소수 ")
    print(3+4j) # 실수부+허수부j
    print(3+4j.real) # 실수부 반환
    print(3+4J.imag)    # 허수부 반환
    print(3+4J.conjugate()) # 켤레복소수

    print(complex(3, 4)) # 타입 함수를 이용한 복소수 선언


def rel_oper(): #   비교 연산자 연습
    print("===== 비교 연산(관계 연산)")
    print("1 > 3 ?", 1 > 3)
    print("1 < 3 ?", 1 < 3)
    print("6 equals 9 ?", 6 == 9)
    print("6 not equals 9 ?", 6 != 9)

    s1 = "Python"
    s2 = "Python"

    print("문자열의 ==", s1 == s2)

    # 복합 관계식
    a = 6
    # a가 0보다 크고 a가 10보다 작은가?
    print(a > 0 and a < 10) #
    print(0 < a and a < 10) #
    print(0 < a < 10)   #

    # 수치형 이외 다른 타입의 객체 비교
    print("문자열의 대소:", "abcd" > "abd")
    print("튜플의 대소:", (1, 2, 4) > (1, 3, 1))
    print("리스트의 대소:", [1, 2, 4] < [1, 3, 1])

    # 동질성의 비교 ==
    # 동일성의 비교 is
    #   is는 객체 항목에서 좀더 자세하게 학습
    a = 10
    b = 20
    c = a
    print("a == b ?", a == b)
    print("a is b ?", a is b)
    print("a == c ?", a == c)
    print("a is c ?", a is c)


def variable_ex():  # 변수
    print("===== 변수")
    # 변수명은 문자, 숫자, _의 조합
    # 숫자로 시작하면 안됨
    # 예약어는 사용할 수 없다
    import keyword  # keyword 모듈 로드
    print(keyword.kwlist)
    print("키워드 갯수:", len(keyword.kwlist))

    # 유니코드 이름의 변수도 사용가능 -> 권장하지는 않음
    가격 = 12000
    print(가격 + 가격 * 0.1)


def assginment_ex(): # 치환문
    print("===== 치환문")

    # 여러 변수를 한꺼번에 할당
    a, b = 3.5, 5.3 # 좌변의 변수의 갯수와 우변의 값의 갯수 일치해야 한다
    print(a, b)

    # 값 교환
    a, b = b, a
    print(a, b)

    # 같은 값을 여러 변수에 동시 할당
    x = y = z = 2021
    print(x, y, z)

    # 중요: 동적 타이핑
    # 파이썬은 변수 선언이 없고, 값이 할당될 때 데이터 타입 결정
    a = 1
    print(a, "is", type(a)) # type함수 -> 데이터 혹은 객체의 데이터 타입을 확인
    a = "Hello Python" # 동적 타이핑
    print(a, "is", type(a))

    # isinstance(판별할 값 or 객체, 데이터타입)
    print("a는 str의 객체?", isinstance(a, str))


def logical_oper():
    print("===== 논리연산")
    # 논리곱(and : 둘 다 True일 때만 True)
    # 논리합(or : 둘 중 하나면 True면 True)
    # 논리부정(not : True <-> False)
    a, b = 20, 30
    print(not a < b) # a < b의 논리를 부정
    print(a < b and a != b) # a < b의 논리값과 a != b의 논리값의 논리곱
    print(a == b or a != b) # a == b의 논리값과 a != b의 논리값의 논리합


if __name__ == "__main__":
    # arith_oper()
    # complex_ex();
    # rel_oper()
    # variable_ex()
    # assginment_ex()
    logical_oper()