import sys
sys.path.insert(0, './pydantic')

from pydantic import BaseModel

class A(BaseModel):
    a: int
    b: float
    c: str = 'test'

print(A(10, 20))

try:
    A()
except Exception as e:
    print(e)

type.__new__()