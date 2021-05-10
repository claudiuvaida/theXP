from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

number = input ("How many times?\n")
contract = input ("Contract address?\n")

i = 1

while i <= int(number):
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.minimize_window()
    driver.get("https://www.dextools.io/app/pancakeswap/pair-explorer/" + contract)
    print("Application url is", driver.current_url)
    time.sleep(10)
    driver.quit()
    print(i)
    i += 1

print("End")