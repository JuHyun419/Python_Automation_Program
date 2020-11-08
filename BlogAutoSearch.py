from selenium import webdriver
import time

# ----- m-link 체험단 자동 검색 ----- #
keyword = ["구로", "관악", "신림", "봉천"]

# Step 1. 크롬 드라이버를 사용해서 웹 브라우저를 실행합니다.
path = "c:/Temp/chromedriver.exe"
url = "http://m-link.shop/"

# 구로 검색
driver1 = webdriver.Chrome(path)
driver1.get(url)
time.sleep(2)  # 위 페이지가 모두 열릴 때 까지 2초 기다립니다.
element1 = driver1.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/input')
element1.send_keys(keyword[0])
driver1.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/button').click()
time.sleep(1)


# 관악 검색
driver2 = webdriver.Chrome(path)
driver2.get(url)
time.sleep(2)
element2 = driver2.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/input')
element2.send_keys(keyword[1])
driver2.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/button').click()
time.sleep(1)

# 신림 검색
driver3 = webdriver.Chrome(path)
driver3.get(url)
time.sleep(2)  # 위 페이지가 모두 열릴 때 까지 2초 기다립니다.
element3 = driver3.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/input')
element3.send_keys(keyword[2])
driver3.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/button').click()
time.sleep(1)

# 봉천 검색
driver4 = webdriver.Chrome(path)
driver4.get(url)
time.sleep(2)  # 위 페이지가 모두 열릴 때 까지 2초 기다립니다.
element4 = driver4.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/input')
element4.send_keys(keyword[3])
driver4.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/button').click()
time.sleep(1)


