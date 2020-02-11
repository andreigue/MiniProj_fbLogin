from selenium import webdriver

usrEmail = raw_input("Enter your email : \n")

driver = webdriver.Chrome()
driver.get('http://www.facebook.com')
email_text_area = driver.find_element_by_id('email')



https://pythonspot.com/selenium-textbox/
