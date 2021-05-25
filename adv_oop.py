class MyString(str):  # str 클래스를 상속받는 MyString
    pass  # MyString은 str 클래스에서 모든 멤버들을 물려받는다


s = MyString()
print(type(s))
print(MyString.__bases__)  # 기반 클래스 확인
print(str.__bases__)


# 파이썬은 다중 상속이 가능
class myobj:
    pass


class Chimera(str, myobj):
    pass


print(type(Chimera))
print(Chimera.__bases__)

# 하위 클래스 or 파생 클래스
print('chimera는 str의 서브클래스?', issubclass(Chimera, str))
print('chimera는 myobj의 서브클래스?', issubclass(Chimera, myobj))

# 상위 클래스 or 기반 클래스 : __base__ 활용

ms = MyString("Python")
print(ms)
print(dir(ms))

# str의 모든 메서드를 그대로 활용(상속을 받았기 때문)
print(ms.upper())
