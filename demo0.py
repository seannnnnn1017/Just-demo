from ssl import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

options = Options()                             #取消網頁中的彈出視窗
options.add_argument("--disable-notifications") #避免妨礙網路爬蟲的執行

PATH ="C:/Users/fishd/Desktop/python/chromedriver/chromedriver.exe"  #Chromedriver 位置
driver = webdriver.Chrome(PATH) #選擇瀏覽器
Web = "https://www.google.com/" #網址

driver.get(Web)    #打開網址
print(driver.title)
search = driver.find_element_by_name("q") #找標籤
search.send_keys("人工智慧")   #輸入文字
search.send_keys(Keys.RETURN)  #ENTER


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID,"pnnext"))
)
num=0
while num <5:   
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID,"pnnext"))
    )
    titles = driver.find_elements_by_class_name("LC20lb") #找標題標籤
    for title in titles: #列印所有標題
        print(title.text)
    
    link = driver.find_element_by_id("pnnext")
    link.click()
    
    num +=1

titles = driver.find_elements_by_class_name("LC20lb") #找標題標籤
for title in titles: #列印所有標題
    print(title.text)
    

time.sleep(5)

driver.quit() #關閉瀏覽器