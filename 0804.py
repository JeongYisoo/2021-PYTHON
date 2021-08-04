#from 모듈 import *
"""
권장되지 않는 이유
    모듈에서 정의된 모든 이름을 네임스페이스에 추가함
    따라서
        1. 어떤 이름이 추가되었는지 확인이 어려움
        2. 이름 중복될 확률이 높아짐
"""

#함수 불러올 때 이름 바꾸기

"""
from 모듈 import 함수 as 이름변경
"""


def square(len):
    """
    사각형 둘레 구하는 함수
    """
    return len*4

print(square(4))

print(dir())