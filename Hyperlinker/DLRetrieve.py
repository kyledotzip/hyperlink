from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


def DLStore(InputArray):
    global driver
    dictionary = {}
    download_link = 'Nil'
    options = Options()
    options.headless = True
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),

                            options=options)
    driver.get("https://www.ahridirectory.org/Search/SearchHome")
    driver.maximize_window()
    wait = WebDriverWait(driver, 3)

    for id in InputArray:
        download_link = 'Nil'
        if id == 0:
            dictionary[id] = '0'
        else:
            args = "OnSelect({}, 68, '3500')".format(id)
            driver.execute_script(args)
            time.sleep(0.3)
            try:
                download_link = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div[3]/div/div[2]/div[2]/table/tbody/tr/td[1]/a")))
                link = download_link.get_attribute("href")
                dictionary[id] = link
                print("Assigning {} to the value of {} in the array".format(link, id))
                time.sleep(1)
            except TimeoutException:
                dictionary[id] = '0'
    return dictionary

                
def DriverQuit():
    driver.quit()

