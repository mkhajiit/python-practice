def save_to_file(todos, filename="todo_list.txt"):
  with open(filename,"w",encoding="utf-8") as f:
    for task in todos:
      f.write(task+"\n")

def load_from_file(filename="todo_list.txt"):
  try:
    with open(filename,"r",encoding="utf-8") as f:
      return [line.strip() for line in f.readlines()]
  except FileNotFoundError:
    return []