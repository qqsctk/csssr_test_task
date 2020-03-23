
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/localuser/Downloads/chromedriver.exe')
driver.implicitly_wait(10)

driver.get("https://blog.csssr.ru/qa-engineer/")
driver.find_element_by_xpath("/html/body/div[1]/section[1]/section/div[2]/a").click()
driver.find_element_by_xpath("/html/body/div[1]/section[2]/div[2]/aside/ul/li[4]/label/a").click()
driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)
link = driver.current_url
assert "http://monosnap.com/" == link
driver.quit()
