import random
preset = ["가위", "바위", "보"]
# 숫자 입력 받을 시 예외 처리를 추가합니다.
while True:
  try:
    user_try = int(input("원하는 플레이 횟수를 입력해주세요: "))
    if user_try <= 0:
      print("1이상의 숫자를 입력해주세요!")
      continue
    break # 올바른 입력은 루프를 종료
  except ValueError:
    print("숫자만 입력해야 해요!")
    continue

for _ in range(user_try):
  computer = random.choice(preset)
  guess = input("가위 바위 보: ")
  # 이기는 경우, 지는 경우, 비기는 경우로 리펙토링
  print(computer)
  # 가위, 바위, 보 가 아닌 입력에 대한 예외 처리
  if guess not in preset:
    print("잘못된 입력입니다!")
    continue
  elif computer == guess:
    print("비겼습니다")
  elif computer =="바위" and guess == "보" or \
  computer == "보" and guess == "가위" or \
  computer == "가위" and guess == "바위":
    print("당신이 이겼습니다.")
  else:
    print("당신이 졌습니다.")
    