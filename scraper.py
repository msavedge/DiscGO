import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://discgolfdata.com/pages/yadd.html'

driver = webdriver.Safari()
# driver = webdriver.Chrome('./chromedriver')
driver.get(url)

driver.implicitly_wait(10)

title = driver.title

tableElem = driver.find_element(By.ID, value='DataTables_Table_0')

print(f'TABLE: \n{tableElem.text}')

nextButtonElem = driver.find_element(By.LINK_TEXT, value='Next')

print(f'NEXT BUTTON: \n{nextButtonElem.text}')

nextButtonElem.click()

tableElem = driver.find_element(By.ID, value='DataTables_Table_0')

print(f'TABLE 2: \n{tableElem.text}')
