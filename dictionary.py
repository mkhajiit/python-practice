grade = {"Yeon": 90, "Kim" : 70, "Yang": 65}

print(grade["Yeon"])
print(grade.get('Yeon'))

obj = grade.keys()
values_obj = grade.values()
# key, value 쌍을 튜플로 묶은 값을 리턴
items_obj = grade.items()

# 객체에 저장된 데이터 하나씩 불러오기
for k in obj:
  print("key:",k)

for v in values_obj:
  print("value:",v)

for i in items_obj:
  print("items:",i)