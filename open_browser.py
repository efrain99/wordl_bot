from lib2to3.pgen2 import driver
from ssl import Options
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By


#options = FirefoxOptions()
#driver = webdriver.Firefox(options=options)

#driver.quit()

def first_test():
    #options = FirefoxOptions()
    driver = webdriver.Firefox()

    driver.get("https://www.nytimes.com/games/wordle/index.html")

    #assert driver.title # => "Google"

    driver.implicitly_wait(1.5)

    search_box = driver.find_element(by=By.NAME, value="q")
    search_button = driver.find_element(by=By.NAME, value="btnK")

    search_box.send_keys("query")
    search_button.click()

    search_box = driver.find_element(by=By.NAME, value="q")
    assert search_box.get_attribute("value") == "query"

    #driver.quit()

first_test()