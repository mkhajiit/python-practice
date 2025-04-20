class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def hello(self):
    print(f"안녕, 내 이름은 {self.name} 이고 나이는 {self.age}살이야!!!")


p1 = Person("철수",25)
p1.hello();