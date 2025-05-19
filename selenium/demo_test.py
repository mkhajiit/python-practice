from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. 웹드라이버로 브라우저 열기
driver = webdriver.Chrome()  # ChromeDriver가 설치된 경로에 있어야 함

# 2. 로그인 페이지 열기
driver.get("https://practicetestautomation.com/practice-test-login/")

time.sleep(2)

driver.quit()