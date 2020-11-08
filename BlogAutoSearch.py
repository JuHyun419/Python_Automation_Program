from bs4 import BeautifulSoup
from selenium import webdriver
import time

### m-link 체험단모집링크 크롤링
keyword = ["구로", "관악", "신림", "가산"]

# Step 1. 크롬 드라이버를 사용해서 웹 브라우저를 실행합니다.
path = "c:/Temp/chromedriver.exe"

# 구로 검색
driver1 = webdriver.Chrome(path)
driver1.get("http://m-link.shop/")
time.sleep(2)  # 위 페이지가 모두 열릴 때 까지 2초 기다립니다.
element1 = driver1.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/input')
element1.send_keys("구로")
driver1.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/button').click()
time.sleep(1)


# 관악 검색
driver2 = webdriver.Chrome(path)
driver2.get("http://m-link.shop/")
time.sleep(2)
element2 = driver2.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/input')
element2.send_keys("관악")
driver2.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/button').click()
time.sleep(1)

# 신림 검색
driver3 = webdriver.Chrome(path)
driver3.get("http://m-link.shop/")
time.sleep(2)  # 위 페이지가 모두 열릴 때 까지 2초 기다립니다.
element3 = driver3.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/input')
element3.send_keys("신림")
driver3.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/button').click()
time.sleep(1)

# 가산 검색
driver3 = webdriver.Chrome(path)
driver3.get("http://m-link.shop/")
time.sleep(2)  # 위 페이지가 모두 열릴 때 까지 2초 기다립니다.
element3 = driver3.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/input')
element3.send_keys("가산")
driver3.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/button').click()
time.sleep(1)


