`from selenium import webdriver
from bs4 import BeautifulSoup as b4

browser = webdriver.Chrome()
browser.get('https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/login?o=dwebmge')

# 搜尋"陳舜德"
browser.find_element_by_id("ysearchinput0").send_keys("葉慶隆")

# 勾選"指導教授"
## 方法一
browser.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/div[1]/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/input[3]').click()
## 方法二
browser.find_element_by_xpath('//input[@value="ad"]').click()

# 點擊搜尋按鈕
browser.find_element_by_id("gs32search").click()

# 網頁原始碼
html = browser.page_source

# BeautifulSoup4 解析
soup = b4(html, 'html.parser')
paper_title = soup.select('#tablefmt1 span')
for i in paper_title:
    print(i.text)`