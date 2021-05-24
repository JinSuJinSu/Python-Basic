def handling_exception():
    """
    예외 처리하기
    """
    lst = []

    # 1번째 예외 처리
    try:
        lst[3] = 1
        4 / 0
        int("String")
    except Exception:
        print("Error")
    # 예외 회피 가능... 실제 무슨 오류인지 확인이 불가
    try:
        # lst[3] = 1
        # 4 / 0
        # int("String")
        print(int("1234567890"))
    except ValueError as e:
        print("정수로 변환 불가!")
        print(e, type(e))
    except ZeroDivisionError as e:
        print("0으로는 나눌 수 없습니다.")
        print(e, type(e))
    except IndexError as e: # 구체적인 예외 처리가 가능
        print("인덱스에 접근 불가!")
        print(e, type(e))
    except Exception as e:  # 예외 객체의 심볼을 붙이면 어떤 예외인지 확인 가능
        print("Error")
        print(e, type(e))
    else:   # try 블록에서 예외 없을 때 한 번 실행
        print("예외 없음!")
    finally:    # 예외 유무 관계 없이 항상 마지막에 -> 주로 자원 정리에 사용
        print("예외처리 종료!")

    # 예외 있을 때: try -> except -> finally
    # 예외 없을 때: try -> else -> finally


def raise_exception():
    """
    예외의 위임
    """
    def beware_dog(animal): # animal == "dog" -> 예외 발생, 다른 동물이면 -> 어서오세요!
        if animal == "dog": # 예외를 외부로 위임
            raise RuntimeError("강아지는 출입을 제한합니다!")
        else:
            print(animal, "어서오세요!")

    try:
        beware_dog("cat")
        beware_dog("cow")
        beware_dog("dog")
    except Exception as e:
        print(e, type(e))

    print("End of code")

if __name__ == "__main__":
    # handling_exception()
    raise_exception()