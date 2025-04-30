# *args: 여러 개의 "위치 인자"를 튜플로 받는다

def my_func(*args):
  print(args)

# **kwargs: 여러 개의 "키워드 인자"를 딕셔너리로 받음
def my_another_func(**kwargs):
  print(kwargs)
my_func(1,2,3)
my_another_func(name="Alice",age=12)