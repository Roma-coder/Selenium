from selenium import webdriver
import time
import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
    

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
wd = webdriver.Chrome(chrome_options=options)

wd.get('http://localhost:3000/register')
emailElement = wd.find_element_by_css_selector("#register_username_field")
emailElement.clear()
emailElement.send_keys(get_random_string(7))

passElement = wd.find_element_by_css_selector("#register_email_field")
passElement.clear()
passElement.send_keys(get_random_string(6) + '@gmail.com')

passElement = wd.find_element_by_css_selector("#register_password_field")
passElement.clear()
passElement.send_keys('123456')

passElement = wd.find_element_by_css_selector("#register_re_password_field")
passElement.clear()
passElement.send_keys('123456789')

btn_element = wd.find_element_by_css_selector("#register_button")
btn_element.click()

time.sleep(5)

message_element = wd.find_element_by_css_selector(".alert-success")


assert message_element != None
