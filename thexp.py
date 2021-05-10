from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

i = 1

while i < 6:
    contract = "0x1c12a5538173f4ef4f8d965e6189ee60d7f93a4f"
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://www.dextools.io/app/pancakeswap/pair-explorer/" + contract)
    print("Application title is ", driver.title)
    print("Application url is", driver.current_url)
    time.sleep(3)
    driver.quit()
    print(i)
    i += 1

print("End")