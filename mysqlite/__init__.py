from .database import *
# __init__.py
# 패키지 임포할 때 초기화 작업을 수행하는 파일
#   없어도 패키지로 인식

# from 패키지 import * : 내부에 있는 모든 객체를 import
__all__ = ["Database"] # 명시된 심볼만 export된다
# __all__ = []    # *로 임포트시 아무 것도 export 안함