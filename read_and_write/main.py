from manager import TodoManager
from file_util import save_to_file, load_from_file

def main():
  manager = TodoManager()
  saved = load_from_file()
  # 이미 저장되어 있는 텍스트를 읽어온다.
  for task in saved:
    manager.add(task)

  while True:
        cmd = input("명령어 (add/list/save/exit): ").strip()
        if cmd == "add":
            task = input("할 일 입력: ")
            manager.add(task)
        elif cmd == "list":
            for i, task in enumerate(manager.list(), 1):
                print(f"{i}. {task}")
        elif cmd == "save":
            save_to_file(manager.list())
            print("저장 완료!")
        elif cmd == "exit":
            print("종료합니다.")
            break
        else:
            print("알 수 없는 명령어입니다.")

if __name__ == "__main__":
  main()