import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('C:/Users/2000b/Desktop/chromedriver_win32/chromedriver.exe')
# tự động điền các thông tin
driver.get('https://www.facebook.com/r.php?locale=vi_VN&display=page')
time.sleep(2) 
driver.find_element_by_name('lastname').send_keys('manh')
time.sleep(1)
driver.find_element_by_name('firstname').send_keys('bui')
time.sleep(2)
driver.find_element_by_name('reg_email__').send_keys('buivanmanh@gmail.com')
time.sleep(1)
driver.find_element_by_name('reg_email_confirmation__').send_keys('buivanmanh@gmail.com')
driver.find_element_by_name('reg_passwd__').send_keys('4125142srsAAa')
time.sleep(2)
#chọn ngày
day = driver.find_element(By.ID,"day")
dayDD = Select(day)
#cách 1: chọn theo số mục lục 
dayDD.select_by_index(6)
#cách 2: chọn theo giá trị option
# dayDD.select_by_value(7)
# cách 3: chọn theo Text của option
# dayDD.select_by_visible_text('7')
time.sleep(1)

#chọn tháng
month = driver.find_element(By.ID,"month")
monthDD = Select(month)
monthDD.select_by_value('3')
time.sleep(2)
#chọn năm
year = driver.find_element(By.ID,"year")
yearDD = Select(year)
yearDD.select_by_value('2000')

sex = driver.document.querySelector("#u_0_5_dR").click()
# driver.find_element_by_name('websubmit').click()