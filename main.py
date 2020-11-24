from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import os
import time

from utils import choose_browser, day, month, year, randompassword, take_email, \
    take_name, take_surname, simple_login, complex_login, bad_email, del_email, save_accounts
from email_tool import get_insta_code

chosen_browser = choose_browser()

if chosen_browser == 'Chrome':
    browser = webdriver.Chrome(executable_path=os.path.join('drivers', 'chromedriver.exe'))
elif chosen_browser == 'Firefox':
    browser = webdriver.Firefox(executable_path=os.path.join('drivers', 'geckodriver.exe'))

browser.implicitly_wait(5)

def is_ok(field):
    labels = {'email_or_phone_field' : 'emailOrPhone',
              'username_field' : 'username'
            }

    try:
        browser.find_element_by_xpath(f'//input[@name="{labels[field]}"]/following::span[starts-with(@class, "coreSpriteInputAccepted")][1]')
        return True
    except:
        browser.find_element_by_xpath(f'//input[@name="{labels[field]}"]/following::span[starts-with(@class, "coreSpriteInputError")][1]')
        return False

browser.get('https://www.instagram.com/')
time.sleep(2)

# Register button
register_button = browser.find_element_by_xpath('//a[@href="/accounts/emailsignup/"]')
register_button.click()
time.sleep(2)

# Enter user's register data
name = take_name()
surname = take_surname()
birthday_year = year
email = take_email() # returns [login, password]

username = simple_login(name, surname)
password = randompassword()

email_or_phone_field = browser.find_element_by_xpath('//input[@name="emailOrPhone"]')
def enter_email(email):
    email_or_phone_field.send_keys(email)
    email_or_phone_field.send_keys(Keys.ENTER)
    time.sleep(2)

# Check is email valid
enter_email(email[0])
while is_ok('email_or_phone_field') is not True:
    email_or_phone_field.clear()
    bad_email(email)
    del_email(email)
    email = take_email()
    enter_email(email[0])

full_name_field = browser.find_element_by_xpath('//input[@name="fullName"]')
full_name_field.send_keys(name + ' ' + surname)
full_name_field.send_keys(Keys.ENTER)
time.sleep(2)


username_field = browser.find_element_by_xpath('//input[@name="username"]')
username_field.send_keys(username)
username_field.send_keys(Keys.ENTER)
time.sleep(2)
if is_ok('username_field') is not True:
    username_field.clear()
    time.sleep(2)
    username = complex_login(name, surname, birthday_year)
    username_field.send_keys(username)
    username_field.send_keys(Keys.ENTER)
    time.sleep(2)
    if is_ok('username_field') is not True:
        username_field.clear()
        time.sleep(2)
        generate_icon = browser.find_element_by_xpath('//input[@name="username"]/following::span[starts-with(@class, "coreSpriteInputRefresh")][1]')
        generate_icon.click()
        username_field.send_keys(Keys.ENTER)
        username = browser.find_element_by_xpath('//input[@name="username"]').get_attribute('value')
        time.sleep(2)

password_field = browser.find_element_by_xpath('//input[@name="password"]')
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)
time.sleep(2)

# Enter birthday data
select_year = Select(browser.find_element_by_xpath('//select[@title="Год:"]'))
select_year.select_by_value(birthday_year)
time.sleep(2)

select_month = Select(browser.find_element_by_xpath('//select[@title="Месяц:"]'))
select_month.select_by_value(month)
time.sleep(2)

select_month = Select(browser.find_element_by_xpath('//select[@title="День:"]'))
select_month.select_by_value(day)
time.sleep(2)

next_button = browser.find_element_by_xpath('//button[text()="Далее"]')
next_button.click()

# Email code
time.sleep(3)
insta_code = get_insta_code(*email)

code_field = browser.find_element_by_xpath('//input[@name="email_confirmation_code"]')
code_field.send_keys(insta_code)

submit_button = browser.find_element_by_xpath('//button[@type="submit"]')
submit_button.click()

# Save result
del_email(email)
final_data = ':'.join([username, password, email[0], email[1]])
save_accounts(final_data)
