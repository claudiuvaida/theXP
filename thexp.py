from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

number = input ("How many times?\n")
contract = input ("Contract address?\n")

i = 1
while i <= int(number):

    #Defining and installing drivers using webdriver manager dependency

    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver2=webdriver.Edge(EdgeChromiumDriverManager().install())
    
    #Opening dextools using the defined drivers

    driver.get("https://www.dextools.io/app/pancakeswap/pair-explorer/" + contract)
    driver2.get("https://www.dextools.io/app/pancakeswap/pair-explorer/" + contract)

    ##Minimize windows for both drivers

    driver.minimize_window()
    driver2.minimize_window()

    #Wait 13 seconds to bypass protection

    time.sleep(13)

    #Quit/Close driver
    
    driver.quit()
    driver2.quit()

    print("Execution ID: " + str(i))
    i += 1

print("-- End --")