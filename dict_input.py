paper ={}

for _ in range(3):
  key = input("제목을 입력하세요: ")
  value= input("줄거리를 간단하게 입력하세요: ")
  
  if key and value:
    paper[key] = value
  else:
    print("제대로 된 값을 입력해주세요!")

print(paper)