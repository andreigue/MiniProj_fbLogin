from selenium import webdriver

driver = webdriver.Firefox(executable_path=r"C:\Users\Abha_Rathour\Downloads\geckodriver\geckodriver.exe")
driver.implicitly_wait(2)
driver.maximize_window()

driver.get("http://youtube.com/")
driver.find_element_by_id('search-input').click()
print("search box clicked")

#Send keyboard input to the search box
driver.find_element_by_class_name('ytd-searchbox').send_keys('Selenium-Python Tutorial')
driver.find_element_by_id('search-icon-legacy').click()
