# 함수 스코핑 룰
x = 1   # Global
def scope_func(a):
    return a + x    # Local 스코프에 x가 없음 -> 글로벌 x를 참조
def scope_func2(a):
    x = 2   # 치환 -> 로컬 스코프에 x 심볼이 생성 -> 글로벌 x가 아니다
    return a + x    # Local 스코프 a, Local Scope x 합산 리턴

print(scope_func(10))
print(scope_func2(10))
print("global x:", x)   # scope_func2에서 x가 치환되었지만 global x는 변경되지 않음
print("global x:", x)   # scope_func2에서 x가 치환되었지만 global x는 변경되지 않음

g = 1   # 글로벌 변수

def scope_func3(a):
    # 함수 내부에서 전역 객체를 사용해야 한다 -> global 키워드를 사용
    global g
    g = 3
    return a + g

print(scope_func3(10))
print("global g:", g)

# 글로벌 영역의 확인
print(dir())    # globals
# 내장 영역의 확인
print("내장영역:", dir('__builtins__'))