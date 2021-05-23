from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
wd = webdriver.Chrome(chrome_options=options)

wd.get('http://localhost:3000/login')
emailElement = wd.find_element_by_css_selector("#login_email_field")
emailElement.clear()
emailElement.send_keys('romaIv172@gmail.com')

passElement = wd.find_element_by_css_selector("#login_password_field")
passElement.clear()
passElement.send_keys('123456789')

btn_element = wd.find_element_by_css_selector("#login_button")
btn_element.click()

time.sleep(2)

assert wd.current_url == 'http://localhost:3000/room'