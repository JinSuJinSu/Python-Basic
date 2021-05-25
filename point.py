class Point:
    # 인스턴스 메서드의 첫 번째 인자는 항상 self이다

    # 클래스 멤버

    instace_count = 0

    # 생성자
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.instace_count += 1

    # 소멸자
    def __del__(self):
        Point.instace_count -= 1

    # 문자열 출력 포멧1
    def __str__(self):
        return "Point x={}, y={}".format(self.x, self.y)

    # 문자열 출력 포멧2
    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __add__(self, other):
        # Point + other
        if isinstance(other, Point):    # + Point
            return Point(self.x + other.x,
                         self.y + other.y)

        elif isinstance(other, int):    # + int
            return Point(self.x + other,
                         self.y + other)

        return self + other

    # 역이행 연산자 +
    def __radd__(self, other):  # other + Point
        if isinstance(other, int):
            return Point(self.x + other,
                         self.y + other)

        return other + self

    # - 연산자 오버로딩
    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x,
                         self.y - other.y)

        elif isinstance(other, int):
            return Point(self.x - other,
                         self.y - other)

        return self - other

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y
