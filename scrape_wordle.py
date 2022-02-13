from bs4 import BeautifulSoup
import requests

#print("working!\n");

URL = "https://www.powerlanguage.co.uk/wordle/"
page = requests.get(URL)

#print(page.text)
soup = BeautifulSoup(page.content, "lxml")

results = soup.find_all('date-key')
for result in results:
    print(result)
