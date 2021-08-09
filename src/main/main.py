from selenium import webdriver
from process_csv import MOJANG_API_URL

PATH = "./geckodriver"
driver = webdriver.Firefox(executable_path=PATH)

print(driver.title)
driver.get(MOJANG_API_URL + "test")
