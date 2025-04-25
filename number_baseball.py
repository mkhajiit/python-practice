import random

answer = random.randint(1,10);
guess = 0

print("1-10 사이에 있는 숫자를 맞추는 숫자야구 시작!!!")
while guess != answer:
  user_input = input("숫자를 입력하세요: ")
  
  if user_input == "":
    print("입력이 필요합니다!")
    continue # 아래의 코드를 실행시키지않고 루프를 재실행
  
  try:
    guess = int(user_input)
  except:
    print("잘못된 입력입니다 숫자를 입력하세요")
    continue
  
  if guess < answer:
    print("정답은 더 큰 숫자입니다.")
  elif guess > answer:
    print("정답은 더 작은 숫자입니다.")
  else:
    print("정답입니다.")