import random
preset = ["가위", "바위", "보"]
guess = ""
user_try = int(input("원하는 플레이 횟수를 입력해주세요: "))

for i in range(0,user_try,1):
  computer = preset[random.randint(0,2)]
  guess = input("가위 바위 보: ")

  if computer == "가위":
    if guess == "가위":
      print("비겼습니다")
    elif guess == "바위":
      print("이겼습니다")
    elif guess == "보":
      print("졌어요")
    else:
      print("잘못된 입력입니다!")
  elif computer =="바위":
    if guess == "가위":
      print("졌습니다")
    elif guess == "바위":
      print("비겼습니다")
    elif guess == "보":
      print("이겼어요")
    else:
      print("잘못된 입력입니다!")
  else:
    if guess == "가위":
      print("이겼습니다")
    elif guess == "바위":
      print("졌습니다")
    elif guess == "보":
      print("비겼어요")
    else:
      print("잘못된 입력입니다!")