class TodoManager:
  def __init__(self):
    self.todos = []

  def add(self,task):
    self.todos.append(task)

  def list(self):
    return self.todos