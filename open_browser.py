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

    exit_inst = driver.find_element(by=By.XPATH, value="/html/body") ##this gets rid of the pop up menu, need to check what
    #happens when browser is in night mode
    exit_inst.click()
    exit_inst.clear
    driver.implicitly_wait(1.0)
    
    ##this does not work cannot find keyboard, try xpath seems to work better
    #keyboard elemnts are shadow root, special way to interact with them
    #<game-app>
    root = driver.find_element(by=By.TAG_NAME, value="game-app") #shadow-host
    #shadow_dom1 = driver.execute_script('return arguments[0].shadowRoot', root)
    shadow_dom1 = driver.execute_script(root)
    shadow_dom1.find_element(by = By.TAG_NAME, value="game-theme-manager")
    shadow_dom2 = shadow_dom1.find_element(by=By.ID, value="game")
    shadow_dom3 = shadow_dom2.find_element(by=By.TAG_NAME, value="game-keyboard")
    shadow_dom4 = shadow_dom3.find_element(by=By.ID, value="keyboard")
    shadow_dom4.find_element(by=By.XPATH, value="/div/div[1]/button[1]").click()
    
    #search_box.click()
    #search_box.clear()
    #search_box.send_keys(Keys.ENTER)
    #search_box.send_keys(Keys.RETURN)
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


