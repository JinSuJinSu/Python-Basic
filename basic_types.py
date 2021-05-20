def bool_ex():  # bool 자료형
    print("===== bool 연습")
    # 참(True), 거짓(False)
    # 내부적으로 거짓은 0, 나머지는 모두 참으로 판단
    # bool의 판정 방법
    print(bool(0), bool(1))
    a = 1
    print(a > 10) # 논리 연산 or 비교 연산의 결과

    b = a == 1
    print(b, type(b))

    print(b + 10)

    # bool은 bool의 객체인가?
    print(isinstance(True, bool))   # True is bool?
    print(isinstance(True, int))    # True is int?

    # bool 캐스팅
    print("정수형:", bool(10), bool(0))
    print("실수형:", bool(3.14), bool(0.0))
    print("문자열:", bool("Python"), bool(""))
    print("순차형:", bool([1, 2, 3]), bool([]))
    print("Map:", bool({"a": 2}), bool({}))
    print("None:", bool(None)) # None : Java의 Null 과 비슷 -> 아무 것도 할당되지 않은 상태


if __name__ == "__main__":
    bool_ex();