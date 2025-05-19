from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 웹드라이버로 브라우저 열기
driver = webdriver.Chrome()  # ChromeDriver가 설치된 경로에 있어야 함

# 로그인 페이지 열기
driver.get("https://practicetestautomation.com/practice-test-login/")

# 아이디 입력
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("student")

# 패스워드 입력
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("Password123")  # 비밀번호 입력

# submit 버튼 클릭
submit_btn = driver.find_element(By.ID,"submit")
submit_btn.click()

# 결과 확인 위해 2초 대기
time.sleep(2)

# 로그인 성공 메시지 확인
success_text = driver.find_element(By.TAG_NAME, "h1").text
print("로그인 후 화면 제목:", success_text)

# 브라우저 종료
driver.quit()