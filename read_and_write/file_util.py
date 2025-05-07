def save_to_file(todos, filename="todo_list.txt"):
  with open(filename,"w",encoding="utf-8") as f:
    for task in todos:
      f.write(task+"\n")

# 따로 입력을 안받으면 todo_list.txt를 기본값으로함
def load_from_file(filename="todo_list.txt"):
  try:
    with open(filename,"r",encoding="utf-8") as f:
      return [line.strip() for line in f.readlines()]
  except FileNotFoundError:
    return []