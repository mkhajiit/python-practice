# 딕셔너리 써보기
settings = {
  "theme": "dark",
  "language": "ko",
  "browser": "chrome",
  "owner" : "JH",
}
# 안쪽 따옴표를 작은따옴표로 사용해서 오류를 피한다
print(f"언어:{settings['language']}")
for key, value in settings.items():
  print(f"{key} : {value}")