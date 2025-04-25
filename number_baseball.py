import random

answer = random.randint(1,10);
guess = 0

while guess != answer:
  guess = int(input("숫자를 입력하세요: "))
  if guess < answer:
    print("정답은 더 큰 숫자입니다.")
  elif guess > answer:
    print("정답은 더 작은 숫자입니다.")
  elif guess == "":
    print("정답을 입력해주세요!")
  else:
    print("정답입니다.")