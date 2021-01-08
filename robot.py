from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

print('Llega inicial')

driver = webdriver.Chrome(executable_path='./chromedriver')

driver.get('https://www.netpolizas.com/admin/login')

print('Llega final')