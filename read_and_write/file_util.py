def save_to_file(todos, filename="todo_list.txt"):
  with open(filename,"w",encoding="utf-8") as f:
    for task in todos:
      f.write(task+"\n")

