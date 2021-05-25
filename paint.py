from point import Point


def bound_class_method():
    # 직접 인스턴스 명시 -> 멤버에 접근
    p = Point()  # 생성
    p.setX(10)
    p.setY(20)
    print(p.getX(), p.getY(), sep=",")
    print(p.getX, p.getY)
    # getX, getY가 bound method로 실행됨을 확인


def unbound_class_method():
    # 클래스에 인스턴스를 전달해서 인스턴스 내부의 메서드 호출
    p = Point()
    Point.setX(p, 10)
    Point.setY(p, 20)
    print(Point.getX(p), Point.getY(p))
    print(Point.getX, Point.getY)
    # Point class 내의 함수


def class_member_test():
    p1 = Point()
    p1.setX(10)
    p1.setY(20)

    print("p1: {}, {}".format(p1.getX(), p1.getY()))
    print("instance_count:",
          p1.instance_count,  # 인스턴스에서 접근 가능
          Point.instance_count)  # 인스턴스 없이도 접근 가능


def test_lifecycle():
    p1 = Point(10, 20)
    print('instance_count:', Point.instace_count)

    p2 = Point()
    print('instance_count:', Point.instace_count)

    del p2
    print('instance_count:', Point.instace_count)


def test_print():
    p1 = Point(10, 10)
    print("p1:", p1)

    # __str__ : 일반 사용자가 보기 쉽게 출력(비공식적 문자열)
    # __rep__ : 개발자가 겍체 복원하기 위해 출력(공식적 문자열)

    print(repr(p1)) # __repr__ 호출
    p2 = eval(repr(p1)) # __repr__ 출력 포맷으로 객체 복원
    print("p2:", p2, type(p2))


def arith_oper_overriding():
    p1 = Point(10, 20)
    p2 = Point(30, 40)

    #Point + Point
    print(p1 + p2)
    # Point + int
    p1 = Point(10, 20)
    print(p1 + 10)

    # int + Point
    p1 = Point(10, 20)
    print(10 + p1)

    # 연습문제1
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    print(p1-p2)

    # 연습문제2
    p1 = Point(10, 20)
    print(p1-10)

    p1 = Point(10, 20)
    p2 = Point(10, 20)

    print("p1==p2?", p1==p2)




if __name__ == "__main__":
    # bound_class_method()
    # unbound_class_method()
    # class_member_test()
    # test_lifecycle()
    # test_print()
    arith_oper_overriding()
