# 튜플: 한 번 정하면 값을 바꿀 수 없는, "변경 불가능한 리스트"
colors = ("green","red","blue","purple")

for i in range(4):
  print(colors[i])

# 집합: 중복을 허용하지 않는, 순서 없는 자료형
# 수학의 집합처럼 합집합, 교집합, 차집합 연산이 가능
numbers = {1, 2, 3, 2, 1}
a = {1, 2, 3}
b = {3, 4, 5}

print(numbers)
print(a & b)  # 교집합: {3}
print(a | b)  # 합집합: {1, 2, 3, 4, 5}
print(a - b)  # 차집합: {1, 2}
print(type(colors))