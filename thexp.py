from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

number = input ("How many times?\n")
contract = input ("Contract address?\n")

i = 1
while i <= int(number):

    #Defining and installing drivers using webdriver manager dependency

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    #Opening dextools using the defined drivers

    driver.get("https://www.dextools.io/app/pancakeswap/pair-explorer/" + contract)

    ##Minimize windows for both drivers

    driver.minimize_window()

    #Wait 13 seconds to bypa

    time.sleep(13)

    #Quit/Close driver
    
    driver.quit()

    print("Execution ID: " + str(i))
    i += 1

print("-- End --")