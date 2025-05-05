with open("todos.txt","r", encoding="utf-8") as file:
  lines = file.readlines()

print("저장된 할 일 목록:")
for idx, line in enumerate(lines,start=1):
  print(f"{idx}.{line.strip()}")

# enumerate()는 파이썬에서 리스트나 반복 가능한 객체(iterable)를 순회할 때, 각 요소의 "인덱스"까지 함께 가져오는 함수