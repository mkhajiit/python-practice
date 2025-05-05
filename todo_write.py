todos = []

print("할 일을 입력하세요. 끝내려면 'exit' 입력")

while True:
  task = input("할일: ")
  if task == "exit":
    break
  todos.append(task)

# 파일에 저장 (쓰기 모드)
with open("todos.txt","w",encoding="utf-8") as file:
  for item in todos:
    file.write(item+"\n")

print("할 일 목록이 저장되었습니다.")