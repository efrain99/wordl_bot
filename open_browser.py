from lib2to3.pgen2 import driver
from ssl import Options
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#options = FirefoxOptions()
#driver = webdriver.Firefox(options=options)

#driver.quit()

def first_test():
    #options = FirefoxOptions()
    driver = webdriver.Firefox()

    driver.get("https://www.nytimes.com/games/wordle/index.html")

    assert "Wordle" in driver.title
    ##div class="instructions" is the pop up instructions use .click() method to get rid
    driver.implicitly_wait(1.5)

    search_box = driver.find_element(by=By.ID, value="keyboard")
    #search_button = driver.find_element(by=By.NAME, value="btnK")
    search_box.clear()
    search_box.send_keys("query")
    search_box.send_keys(Keys.RETURN)
    #search_button.click()

    #search_box = driver.find_element(by=By.NAME, value="q")
    #assert search_box.get_attribute("value") == "query"

    #driver.quit()
    driver.close()


def another_test():
    driver=webdriver.Firefox()
    driver.get("http://www.python.org")

    assert "Python" in driver.title

    elem = driver.find_element(By.ID, "id-search-field")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()

#another_test()
first_test()


