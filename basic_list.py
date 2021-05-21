def define_list():
    """
    리스트 정의 연습
    """
    lst1 = list()   # 빈 리스트
    print(lst1, type(lst1))
    lst2 = []   # []
    lst3 = [1, 2, "python"]
    print(lst2, lst3)
    lst4 = list("Python")   # 다른 시퀀스 객체를 리스트로 반환
    print(lst4)


def list_oper():
    """
    리스트의 연산
        순차형의 모든 기능을 수행
        immutable -> 내부 데이터 변경될 수 있다
    """
    lst = [1, 2, "Python"]

    # 길이의 확인
    print(lst, "length:", len(lst))
    # 인덱싱
    print(lst[0], lst[1], lst[2])   #   정인덱싱
    print(lst[-3], lst[-2], lst[-1])    # 역인덱싱

    # Slicing
    print(lst[1:3]) # 항상 경계에 유의
    print(lst[1:])  # 끝 경계 생략 -> 끝까지
    print(lst[:3])  # 시작 경계 생략 -> 처음부터
    print(lst[:])   # 시작 경계, 끝 경계 생략 -> 전체

    copy = lst[:]   # 슬라이싱을 이용한 리스트 전체의 복사
    print(copy)
    print(copy is lst)  # 슬라이싱 -> 새 객체가 생성

    # 연결(+) : 원본 변경하지 않고 단순히 두 list를 연결한 새 리스트를 반환
    #   vs extend : 원본 뒤에 다른 리스트를 연장 -> 내부 데이터 변경
    print(lst + ["Java", True, 3.14159])
    print("원본:", lst)

    # append vs extend
    copy.append(["Java", True, 3.14159])    # 개별 요소의 추가
    print(copy)
    copy.extend(["Java", True, 3.14159])    # 다른 리스트를 연결하여 확장
    print("Extend:", copy)

    # insert
    copy.insert(2, [1, 2, 3])   # 인덱스에 요소 추가
    print("INSERT:", copy)

    # 반복 (*)
    print("원본:", lst)
    print("반복:", lst * 3)

    # 포함여부 확인 : in, not in
    print("Python" in lst)  # lst에 "Python"포함?
    # 인덱스의 확인
    print("INDEX:", lst.index("Python"))

    if "Java" in lst:
        print("INDEX:", lst.index("Java"))  # 없는 객체 검색시 ValueError

    print("COPY:", copy)

    # 항목의 갯수
    print("COUNT:", copy.count("Python"))

    # 삭제 : del
    del copy[0] # copy의 0번 인덱스 요소 삭제
    print("COPY:", copy)
    # 삭제 : remove
    copy.remove(3.14159)
    print("REMOVE:", copy)

    # 슬라이싱 이용 치환
    # 메서드 이용보다 슬라이싱 이용 치환 방법 먼저 이용하시기를 권장
    lst = [1, 12, 123, 1234, 12345]
    print("원본:", lst)
    lst[0:2] = [10, 20]
    print(lst)
    # 슬라이싱을 이용한 삭제
    lst[0:2] = []   # 슬라이싱 범위에 빈 리스트를 할당
    print(lst)
    # 슬라이싱을 이용한 삽입
    lst[1:1] = ['inserted'] # 중간에 삽입
    print(lst)
    # 맨 마지막에 삽입
    lst[4:] = ["appended"]  # 맨 뒤에 삽입
    print(lst)
    # 맨 앞에 삽입
    lst[:0] = ["prepended"] # 맨 앞에 삽입
    print(lst)

    # 다양한 기초 산술 함수 제공
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("SUM:", sum(lst)) # 모든 요소의 합
    print("MIN:", min(lst)) # 최솟값
    print("MAX:", max(lst)) # 최댓값
    print("AVERAGE:", sum(lst) / len(lst)) # 평균


def list_methods():
    """
    리스트 메서드들
    """
    lst = [10, 2, 22, 9, 8, 33, 4, 12]
    print("원본:", lst)
    copy = lst.copy()   # 복제 메서드
    # Reverse : 리스트의 반전
    copy.reverse()
    print("REVERSE:", copy)

    copy = lst.copy()
    print("원본:", copy)

    # 정렬: sort
    # 메서드로서의 sort -> 내부 데이터를 실제 소트
    # 문법으로서의 sorted -> 정렬된 새 리스트를 반환

    result = sorted(copy)   # copy를 정렬 -> 새 리스트로 반환
    print("SORTED ASC:", result)    # 오름차순 정렬
    result = sorted(copy, reverse=True) # 내림차순 정렬
    print("SORTED DESC:", result)
    # 정렬 키 함수 정의
    # 정렬 키 함수를 전달 -> 정렬 기준을 변경
    print("원본:", copy)
    result = sorted(copy, key=str)  # 키 함수를 str로 변경
    print("SORTED key=str:", result)
    # 정렬 기준의 사용자 정의
    # 리스트의 요소를 5로 나눈 나머지의 역순으로 정렬

    def key_func(val):  # 사용자 정의 키 함수
        return val % 5
    result = sorted(copy, key=key_func, reverse=True)

    print("SORTED key=custom, DESC:", result)

    # sorted 함수 -> 원본을 변경시키지 않음
    # sort 메서드 -> 원본 내부 데이터를 변경
    copy.sort(key=key_func, reverse=True)
    print("SORT METHOD:", copy)


def stack_ex():
    """
    리스트를 활용한 스택의 구현
        append, pop 메서드를 이용 구현
    """
    stack = []
    # 입력
    stack.append(10)
    stack.append(20)    # 리스트의 맨 뒤에 요소 입력
    stack.append(30)
    print("STACK:", stack)

    # 인출
    print("POP:", stack.pop())
    print("POP:", stack.pop())
    print("POP:", stack.pop())
    if len(stack):  # 스택이 비어있지 않으면
        print("POP:", stack.pop())
    else:
        print("스택이 비어있습니다.")


def queue_ex():
    """
    리스트를 활용한 QUEUE의 구현
        append, pop(0) 를 활용 구현
        First Input First Output(FIFO) 자료형
    """
    queue = []
    queue.append(10)
    queue.append(20)
    queue.append(30)

    print("QUEUE:", queue)

    # 인출: pop(0)
    print(queue.pop(0)) # 맨 앞에서부터 인출
    print(queue.pop(0))
    print(queue.pop(0))


def loop():
    """
    리스트 순회
    """
    words = "Life is too short, you need Python".replace(",", "").upper().split()
    print("LIST:", words)

    # 순차자료형은 for ~ in 문으로 차례대로 요소를 전달 받을 수 있다(별도 인덱스 변수는 없다)
    for word in words:
        print("WORD:", word)


if __name__ == "__main__":
    # define_list()
    # list_oper();
    # list_methods()
    # stack_ex()
    # queue_ex()
    loop()